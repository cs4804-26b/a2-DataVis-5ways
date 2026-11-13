// ---------- 1. Setup ----------
const canvas = document.getElementById("plot");
const ctx = canvas.getContext("2d");

// Space around the plot area (left, right, top, bottom)
const M = { left: 70, right: 160, top: 20, bottom: 60 };
const plotW = canvas.width - M.left - M.right;
const plotH = canvas.height - M.top - M.bottom;

// Axis ranges (same as the image)
const xMin = 170, xMax = 235;
const yMin = 2500, yMax = 6500;

// Convert data values to pixel positions
const toX = v => M.left + (v - xMin) / (xMax - xMin) * plotW;
const toY = v => M.top + (1 - (v - yMin) / (yMax - yMin)) * plotH;

// Colors for each species
const colors = { Adelie: "darkorange", Chinstrap: "darkorchid", Gentoo: "teal" };
const sizeOf = bill => 2 + (bill - 30) * 0.2;

// ---------- 2. Read the CSV ----------
function parseCSV(text) {
  const lines = text.trim().split("\n");
  const headers = lines[0].split(",").map(h => h.replace(/"/g, ""));
  return lines.slice(1).map(line => {
    const cells = line.split(",").map(c => c.replace(/"/g, ""));
    const row = {};
    headers.forEach((h, i) => row[h] = cells[i]);
    return row;
  });
}

// ---------- 3. Draw everything ----------
function draw(rows) {
  // Clear canvas and draw grey background
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#ebebeb";
  ctx.fillRect(M.left, M.top, plotW, plotH);

  // White grid lines and tick labels
  ctx.strokeStyle = "white";
  ctx.lineWidth = 1.5;
  ctx.fillStyle = "#4d4d4d";
  ctx.font = "13px Arial";
  ctx.textAlign = "center";
  for (let v = 170; v <= 230; v += 10) {
    ctx.beginPath(); ctx.moveTo(toX(v), M.top); ctx.lineTo(toX(v), M.top + plotH); ctx.stroke();
    ctx.fillText(v, toX(v), M.top + plotH + 18);
  }
  ctx.textAlign = "right";
  for (let v = 3000; v <= 6000; v += 1000) {
    ctx.beginPath(); ctx.moveTo(M.left, toY(v)); ctx.lineTo(M.left + plotW, toY(v)); ctx.stroke();
    ctx.fillText(v, M.left - 8, toY(v) + 5);
  }

  // Axis titles
  ctx.fillStyle = "black";
  ctx.font = "16px Arial";
  ctx.textAlign = "center";
  ctx.fillText("Flipper Length (mm)", M.left + plotW / 2, canvas.height - 12);
  ctx.save();
  ctx.translate(18, M.top + plotH / 2);
  ctx.rotate(-Math.PI / 2);
  ctx.fillText("Body Mass (g)", 0, 0);
  ctx.restore();

  // Draw each penguin as a circle
  ctx.globalAlpha = 0.75;
  rows.forEach(r => {
    const flipper = parseFloat(r.flipper_length_mm);
    const mass = parseFloat(r.body_mass_g);
    const bill = parseFloat(r.bill_length_mm);
    if (isNaN(flipper) || isNaN(mass) || isNaN(bill)) return; // skip NA rows

    const radius = sizeOf(bill);   // bigger bill = bigger circle
    ctx.beginPath();
    ctx.arc(toX(flipper), toY(mass), radius, 0, 2 * Math.PI);
    ctx.fillStyle = colors[r.species];
    ctx.fill();
  });
  ctx.globalAlpha = 1;

  // ----- Species legend -----
  ctx.font = "16px Arial";
  ctx.textAlign = "left";
  ctx.fillStyle = "black";
  ctx.fillText("species", M.left + plotW + 25, M.top + 30);
  Object.keys(colors).forEach((name, i) => {
    const ly = M.top + 60 + i * 28;
    ctx.beginPath();
    ctx.arc(M.left + plotW + 35, ly, 6, 0, 2 * Math.PI);
    ctx.fillStyle = colors[name];
    ctx.fill();
    ctx.fillStyle = "black";
    ctx.font = "14px Arial";
    ctx.fillText(name, M.left + plotW + 50, ly + 5);
    ctx.font = "16px Arial";
  });

  // ----- Bill length size legend -----
  const sizeTop = M.top + 170;
  ctx.font = "16px Arial";
  ctx.fillStyle = "black";
  ctx.fillText("bill_length_mm", M.left + plotW + 25, sizeTop);
  [40, 50].forEach((bill, i) => {
    const cy = sizeTop + 30 + i * 40;
    ctx.beginPath();
    ctx.arc(M.left + plotW + 35, cy, sizeOf(bill), 0, 2 * Math.PI);
    ctx.fillStyle = "rgba(0, 0, 0, 0.85)";
    ctx.fill();
    ctx.fillStyle = "black";
    ctx.font = "14px Arial";
    ctx.fillText(bill, M.left + plotW + 60, cy + 5);
    ctx.font = "16px Arial";
  });
}

// ---------- 4. Load the file when chosen ----------
document.getElementById("file").addEventListener("change", e => {
  const reader = new FileReader();
  reader.onload = ev => draw(parseCSV(ev.target.result));
  reader.readAsText(e.target.files[0]);
});