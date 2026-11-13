/* Penguin scatterplot drawn with p5.js
 */

const SPECIES_COLORS = {
  Adelie: "#F2A03D",
  Chinstrap: "#8E44AD",
  Gentoo: "#2A7F7F",
};

const MARGIN = { top: 24, right: 190, bottom: 62, left: 72 };
const PANEL = "#F5F5F5";
const GRID = "#FFFFFF";
const INK = "#1D1D1D";
const MUTED = "#444444";

const X_DOMAIN = [168, 234];
const Y_DOMAIN = [2700, 6300];

let penguins = [];
let hovered = null;
let canvasEl;
let loadError = null;

function setup() {
  canvasEl = createCanvas(1000, 600);
  canvasEl.parent("chart");
  pixelDensity(2);
  noLoop();
  canvasEl.elt.addEventListener("mouseleave", () => {
    hovered = null;
    updateTooltip();
    redraw();
  });
  loadData();
}

function loadData() {
  fetch("data.json")
    .then((response) => {
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return response.json();
    })
    .then((data) => {
      penguins = data;
      updateSubtitle();
      redraw();
    })
    .catch((error) => {
      loadError = String(error);
      console.error("Could not load data.json:", error);
      redraw();
    });
}

function updateSubtitle() {
  const p = select(".subtitle");
  if (p && penguins) {
    p.html(
      `${penguins.length} observations &middot; color = species &middot; ` +
        `size = bill length &middot; opacity = 0.8`
    );
  }
}

function innerWidth() {
  return width - MARGIN.left - MARGIN.right;
}

function innerHeight() {
  return height - MARGIN.top - MARGIN.bottom;
}

function xScale(value) {
  return MARGIN.left + ((value - X_DOMAIN[0]) / (X_DOMAIN[1] - X_DOMAIN[0])) * innerWidth();
}

function yScale(value) {
  return (
    MARGIN.top +
    innerHeight() -
    ((value - Y_DOMAIN[0]) / (Y_DOMAIN[1] - Y_DOMAIN[0])) * innerHeight()
  );
}

function radiusFor(bill) {
  // Area-proportional sizing
  const t = constrain((bill - 32) / (60 - 32), 0, 1);
  return 4 + (11.5 - 4) * Math.sqrt(t);
}

function hexToRgb(hex) {
  return [
    parseInt(hex.slice(1, 3), 16),
    parseInt(hex.slice(3, 5), 16),
    parseInt(hex.slice(5, 7), 16),
  ];
}

function draw() {
  background(251);

  if (loadError) {
    fill("#B00020");
    textAlign(CENTER, CENTER);
    textSize(14);
    text(
      "Could not load data.json — run `java PrepareData` and serve this folder.",
      width / 2,
      height / 2
    );
    return;
  }

  if (!penguins || penguins.length === 0) {
    fill("#B00020");
    textAlign(CENTER, CENTER);
    textSize(14);
    text("data.json is still loading…", width / 2, height / 2);
    return;
  }

  drawPanel();
  drawGrid();
  drawAxes();
  drawPoints();
  drawLegends();
  if (hovered) drawHoverRing(hovered);
}

function drawPanel() {
  noStroke();
  fill(PANEL);
  rect(MARGIN.left, MARGIN.top, innerWidth(), innerHeight());
}

function drawGrid() {
  stroke(GRID);
  strokeWeight(1.5);
  for (let mass = 3000; mass <= 6000; mass += 1000) {
    line(MARGIN.left, yScale(mass), MARGIN.left + innerWidth(), yScale(mass));
  }
  for (let flipper = 170; flipper <= 230; flipper += 10) {
    line(xScale(flipper), MARGIN.top, xScale(flipper), MARGIN.top + innerHeight());
  }
}

function drawAxes() {
  const baseY = MARGIN.top + innerHeight();

  stroke("#C9C9C9");
  strokeWeight(1);
  // x axis line
  line(MARGIN.left, baseY, MARGIN.left + innerWidth(), baseY);
  // y axis line
  line(MARGIN.left, MARGIN.top, MARGIN.left, baseY);

  noStroke();
  fill(MUTED);
  textSize(12);
  textStyle(NORMAL);
  textAlign(CENTER, TOP);

  for (let flipper = 170; flipper <= 230; flipper += 10) {
    const xPos = xScale(flipper);
    stroke("#C9C9C9");
    line(xPos, baseY, xPos, baseY + 5);
    noStroke();
    text(flipper, xPos, baseY + 9);
  }

  textAlign(RIGHT, CENTER);
  for (let mass = 3000; mass <= 6000; mass += 1000) {
    const yPos = yScale(mass);
    stroke("#C9C9C9");
    line(MARGIN.left - 5, yPos, MARGIN.left, yPos);
    noStroke();
    text(mass, MARGIN.left - 10, yPos);
  }

  // Axis titles
  fill(INK);
  textStyle(BOLD);
  textSize(14);
  textAlign(CENTER, TOP);
  text("Flipper Length (mm)", MARGIN.left + innerWidth() / 2, baseY + 30);

  push();
  translate(22, MARGIN.top + innerHeight() / 2);
  rotate(-HALF_PI);
  textAlign(CENTER, CENTER);
  text("Body Mass (g)", 0, 0);
  pop();
}

function drawPoints() {
  noStroke();
  for (const d of penguins) {
    const [r, g, b] = hexToRgb(SPECIES_COLORS[d.species] || "#777777");
    fill(r, g, b, 204); // 0.8 opacity
    circle(xScale(d.flipper_length_mm), yScale(d.body_mass_g), radiusFor(d.bill_length_mm) * 2);
  }
}

function drawHoverRing(d) {
  const [r, g, b] = hexToRgb(SPECIES_COLORS[d.species] || "#777777");
  noFill();
  stroke(r * 0.6, g * 0.6, b * 0.6);
  strokeWeight(1.5);
  circle(
    xScale(d.flipper_length_mm),
    yScale(d.body_mass_g),
    radiusFor(d.bill_length_mm) * 2 + 4
  );
}

function drawLegends() {
  const x0 = MARGIN.left + innerWidth() + 34;
  let y0 = MARGIN.top + 30;

  noStroke();
  fill(INK);
  textStyle(BOLD);
  textSize(13);
  textAlign(LEFT, CENTER);
  text("species", x0, y0);

  textStyle(NORMAL);
  textSize(13);
  fill("#222");
  const order = ["Adelie", "Chinstrap", "Gentoo"];
  order.forEach((species, i) => {
    const cy = y0 + 26 + i * 24;
    const [r, g, b] = hexToRgb(SPECIES_COLORS[species]);
    noStroke();
    fill(r, g, b);
    circle(x0 + 8, cy, 14);
    fill("#222");
    textAlign(LEFT, CENTER);
    text(species, x0 + 24, cy);
  });

  textStyle(BOLD);
  fill(INK);
  textAlign(LEFT, CENTER);
  text("bill_length_mm", x0, y0 + 128);

  textStyle(NORMAL);
  [40, 50].forEach((bill, i) => {
    const cy = y0 + 158 + i * 32;
    noStroke();
    fill("#3B3B3B");
    circle(x0 + 8, cy, radiusFor(bill) * 2);
    fill("#222");
    textAlign(LEFT, CENTER);
    text(bill, x0 + 28, cy);
  });
}

// Hover interaction
function mouseMoved() {
  if (!penguins || penguins.length === 0) return;

  let found = null;
  let best = Infinity;

  for (const d of penguins) {
    const dx = mouseX - xScale(d.flipper_length_mm);
    const dy = mouseY - yScale(d.body_mass_g);
    const distance = Math.sqrt(dx * dx + dy * dy);
    const hitRadius = radiusFor(d.bill_length_mm) + 4;
    if (distance <= hitRadius && distance < best) {
      found = d;
      best = distance;
    }
  }

  if (found !== hovered) {
    hovered = found;
    updateTooltip();
    redraw();
  }
}

function updateTooltip() {
  const tip = select("#tooltip");
  if (!tip) return;

  if (!hovered) {
    tip.removeClass("visible");
    return;
  }

  tip.html(
    `<b>${hovered.species}</b><br>` +
      `${hovered.island} &middot; ${hovered.sex}<br>` +
      `Flipper: ${hovered.flipper_length_mm} mm<br>` +
      `Body mass: ${hovered.body_mass_g} g<br>` +
      `Bill: ${hovered.bill_length_mm} mm`
  );
  tip.addClass("visible");

  const rect = canvasEl.elt.getBoundingClientRect();
  const scaleX = rect.width / width;
  const scaleY = rect.height / height;
  tip.style("left", `${rect.left + mouseX * scaleX}px`);
  tip.style("top", `${rect.top + mouseY * scaleY}px`);
}
