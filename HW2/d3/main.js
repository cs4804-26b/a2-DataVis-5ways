const SPECIES = ["Adelie", "Chinstrap", "Gentoo"];
const COLORS = new Map([
  ["Adelie", "#FB7708"],
  ["Chinstrap", "#830FBF"],
  ["Gentoo", "#0E7877"],
]);

const margin = { top: 64, right: 150, bottom: 56, left: 72 };
const width = 860;
const height = 560;
const innerW = width - margin.left - margin.right;
const innerH = height - margin.top - margin.bottom;

const svg = d3.select("#chart")
  .append("svg")
  .attr("width", width)
  .attr("height", height)
  .attr("role", "img")
  .attr("aria-label", "Scatter plot of penguin flipper length and body mass");

svg.append("text")
  .attr("x", margin.left)
  .attr("y", 28)
  .attr("font-size", 16)
  .attr("font-weight", 600)
  .text("Flipper length and body mass of Palmer penguins");

const plot = svg.append("g")
  .attr("transform", `translate(${margin.left},${margin.top})`);

const tip = d3.select("#tip");

d3.csv("../penglings.csv").then((raw) => {
  const data = [];
  for (const row of raw) {
    const flipper = +row.flipper_length_mm;
    const mass = +row.body_mass_g;
    const bill = +row.bill_length_mm;
    if (!Number.isFinite(flipper) || !Number.isFinite(mass) || !Number.isFinite(bill)) {
      continue;
    }
    data.push({
      species: row.species,
      island: row.island,
      sex: row.sex && row.sex !== "NA" ? row.sex : "unknown",
      flipper,
      mass,
      bill,
    });
  }

  const x = d3.scaleLinear().domain([165, 235]).range([0, innerW]);
  const y = d3.scaleLinear().domain([2500, 6500]).range([innerH, 0]);
  const radius = d3.scaleLinear()
    .domain(d3.extent(data, (d) => d.bill))
    .range([4, 14]);

  plot.append("g")
    .attr("class", "grid")
    .call(d3.axisLeft(y).tickValues(d3.range(3000, 6001, 500)).tickSize(-innerW).tickFormat(""))
    .call((axis) => axis.select(".domain").remove());

  plot.append("g")
    .attr("class", "grid")
    .attr("transform", `translate(0,${innerH})`)
    .call(d3.axisBottom(x).tickValues(d3.range(170, 231, 10)).tickSize(-innerH).tickFormat(""))
    .call((axis) => axis.select(".domain").remove());

  plot.append("g")
    .attr("class", "axis")
    .attr("transform", `translate(0,${innerH})`)
    .call(d3.axisBottom(x).tickValues(d3.range(170, 231, 10)));

  plot.append("g")
    .attr("class", "axis")
    .call(d3.axisLeft(y).tickValues(d3.range(3000, 6001, 500)));

  plot.append("text")
    .attr("x", innerW / 2)
    .attr("y", innerH + 44)
    .attr("text-anchor", "middle")
    .attr("fill", "#222")
    .attr("font-size", 13)
    .text("Flipper Length (mm)");

  svg.append("text")
    .attr("text-anchor", "middle")
    .attr("fill", "#222")
    .attr("font-size", 13)
    .attr("transform", `translate(18, ${margin.top + innerH / 2}) rotate(-90)`)
    .text("Body Mass (g)");

  const active = new Set(SPECIES);

  const circles = plot.selectAll("circle")
    .data(data)
    .join("circle")
    .attr("class", "pt")
    .attr("cx", (d) => x(d.flipper))
    .attr("cy", (d) => y(d.mass))
    .attr("r", (d) => radius(d.bill))
    .attr("fill", (d) => COLORS.get(d.species))
    .on("mouseenter", (event, d) => {
      tip.property("hidden", false).html(
        `<strong>${d.species}</strong><br>`
        + `${d.island} · ${d.sex}<br>`
        + `Flipper length: ${d.flipper} mm<br>`
        + `Body mass: ${d.mass} g<br>`
        + `Bill length: ${d.bill} mm`
      );
    })
    .on("mousemove", (event) => {
      tip.style("left", `${event.clientX + 14}px`).style("top", `${event.clientY + 14}px`);
    })
    .on("mouseleave", () => {
      tip.property("hidden", true);
    });

  function paint() {
    circles.attr("fill-opacity", (d) => (active.has(d.species) ? 0.8 : 0.08));
    legend.classed("off", (species) => !active.has(species));
  }

  const legend = svg.selectAll(".legend")
    .data(SPECIES)
    .join("g")
    .attr("class", "legend")
    .attr("transform", (_, i) => `translate(${margin.left + innerW + 24}, ${margin.top + 8 + i * 26})`)
    .on("click", (_, species) => {
      if (active.has(species) && active.size === 1) {
        SPECIES.forEach((name) => active.add(name));
      } else if (active.has(species)) {
        active.delete(species);
      } else {
        active.add(species);
      }
      paint();
    });

  legend.append("circle")
    .attr("r", 6)
    .attr("cy", 0)
    .attr("fill", (species) => COLORS.get(species))
    .attr("fill-opacity", 0.8);

  legend.append("text")
    .attr("x", 16)
    .attr("y", 4)
    .attr("font-size", 13)
    .text((species) => species);

  paint();
  document.body.dataset.ready = "true";
});
