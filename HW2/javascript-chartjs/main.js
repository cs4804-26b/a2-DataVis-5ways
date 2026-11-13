const SPECIES = ["Adelie", "Chinstrap", "Gentoo"];
const COLORS = {
  Adelie: "rgba(251, 119, 8, 0.8)",
  Chinstrap: "rgba(131, 15, 191, 0.8)",
  Gentoo: "rgba(14, 120, 119, 0.8)",
};

function parseCsv(text) {
  const rows = [];
  let row = [];
  let cell = "";
  let inQuotes = false;
  const source = text.replace(/^\uFEFF/, "");
  for (let i = 0; i < source.length; i++) {
    const c = source[i];
    if (inQuotes) {
      if (c === '"') {
        if (source[i + 1] === '"') {
          cell += '"';
          i++;
        } else {
          inQuotes = false;
        }
      } else {
        cell += c;
      }
    } else if (c === '"') {
      inQuotes = true;
    } else if (c === ",") {
      row.push(cell);
      cell = "";
    } else if (c === "\n") {
      row.push(cell);
      rows.push(row);
      row = [];
      cell = "";
    } else if (c !== "\r") {
      cell += c;
    }
  }
  if (cell.length || row.length) {
    row.push(cell);
    rows.push(row);
  }
  const headers = rows[0];
  return rows.slice(1).filter((cells) => cells.some((value) => value !== "")).map((cells) => {
    const record = {};
    headers.forEach((header, index) => {
      record[header] = cells[index] ?? "";
    });
    return record;
  });
}

function loadPenguins(text) {
  return parseCsv(text).flatMap((row) => {
    const flipper = Number(row.flipper_length_mm);
    const mass = Number(row.body_mass_g);
    const bill = Number(row.bill_length_mm);
    if (!Number.isFinite(flipper) || !Number.isFinite(mass) || !Number.isFinite(bill)) {
      return [];
    }
    return [{
      species: row.species,
      island: row.island,
      sex: row.sex && row.sex !== "NA" ? row.sex : "unknown",
      flipper,
      mass,
      bill,
    }];
  });
}

function radius(bill, extent) {
  const [low, high] = extent;
  const t = high === low ? 0.5 : (bill - low) / (high - low);
  return 4 + t * 10;
}

fetch("../penglings.csv")
  .then((response) => response.text())
  .then((text) => {
    const penguins = loadPenguins(text);
    const bills = penguins.map((penguin) => penguin.bill);
    const extent = [Math.min(...bills), Math.max(...bills)];
    const datasets = SPECIES.map((species) => ({
      label: species,
      data: penguins
        .filter((penguin) => penguin.species === species)
        .map((penguin) => ({
          x: penguin.flipper,
          y: penguin.mass,
          r: radius(penguin.bill, extent),
          ...penguin,
        })),
      backgroundColor: COLORS[species],
      borderWidth: 0,
    }));

    const canvas = document.getElementById("chart");
    new Chart(canvas, {
      type: "bubble",
      data: { datasets },
      options: {
        responsive: false,
        plugins: {
          title: {
            display: true,
            text: "Flipper length and body mass of Palmer penguins",
            align: "start",
            color: "#222",
            font: { family: "Segoe UI", size: 16, weight: "600" },
            padding: { bottom: 16 },
          },
          legend: {
            position: "right",
            labels: {
              font: { family: "Segoe UI", size: 12 },
              usePointStyle: true,
              pointStyle: "circle",
            },
          },
          tooltip: {
            callbacks: {
              label(context) {
                const penguin = context.raw;
                return [
                  penguin.species,
                  `Flipper length: ${penguin.x} mm`,
                  `Body mass: ${penguin.y} g`,
                  `Bill length: ${penguin.bill} mm`,
                  `Island: ${penguin.island}`,
                  `Sex: ${penguin.sex}`,
                ];
              },
            },
          },
        },
        scales: {
          x: {
            min: 165,
            max: 235,
            title: {
              display: true,
              text: "Flipper Length (mm)",
              font: { family: "Segoe UI", size: 13 },
            },
            afterBuildTicks(scale) {
              scale.ticks = [170, 180, 190, 200, 210, 220, 230].map((value) => ({ value }));
            },
            ticks: {
              font: { family: "Segoe UI", size: 12 },
            },
            grid: { color: "#ececec" },
          },
          y: {
            min: 2500,
            max: 6500,
            title: {
              display: true,
              text: "Body Mass (g)",
              font: { family: "Segoe UI", size: 13 },
            },
            afterBuildTicks(scale) {
              scale.ticks = [3000, 3500, 4000, 4500, 5000, 5500, 6000].map((value) => ({ value }));
            },
            ticks: {
              font: { family: "Segoe UI", size: 12 },
            },
            grid: { color: "#ececec" },
          },
        },
      },
    });
    document.body.dataset.ready = "true";
  });
