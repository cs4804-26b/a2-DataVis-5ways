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

Promise.all([
  fetch("spec.json").then((response) => response.json()),
  fetch("../penglings.csv").then((response) => response.text()),
]).then(([spec, text]) => {
  spec.data.values = loadPenguins(text);
  return vegaEmbed("#chart", spec, {actions: false, renderer: "svg"});
}).then(() => {
  document.body.dataset.ready = "true";
});
