/* Penguin scatterplot built with D3 v7.
 * The data comes from /data.json, which PenguinServer.java generates from
 * ../penglings.csv (dropping rows with missing measurements).
 */

const SPECIES_COLORS = {
  Adelie: "#F2A03D",
  Chinstrap: "#8E44AD",
  Gentoo: "#2A7F7F",
};

const WIDTH = 1000;
const HEIGHT = 600;
const MARGIN = { top: 24, right: 190, bottom: 62, left: 72 };
const INNER_W = WIDTH - MARGIN.left - MARGIN.right;
const INNER_H = HEIGHT - MARGIN.top - MARGIN.bottom;

const X_DOMAIN = [168, 234];
const Y_DOMAIN = [2700, 6300];

const tooltip = d3.select("#tooltip");

const svg = d3
  .select("#chart")
  .append("svg")
  .attr("viewBox", `0 0 ${WIDTH} ${HEIGHT}`)
  .attr("role", "img")
  .attr("aria-label", "Scatterplot of penguin body mass against flipper length");

const plot = svg
  .append("g")
  .attr("transform", `translate(${MARGIN.left},${MARGIN.top})`);

const x = d3.scaleLinear().domain(X_DOMAIN).range([0, INNER_W]);
const y = d3.scaleLinear().domain(Y_DOMAIN).range([INNER_H, 0]);

const color = d3
  .scaleOrdinal()
  .domain(["Adelie", "Chinstrap", "Gentoo"])
  .range(Object.values(SPECIES_COLORS));

const radius = d3.scaleSqrt().domain([32, 60]).range([4, 11.5]);

// White gridlines on light grey panel
plot
  .append("g")
  .attr("class", "grid")
  .selectAll("line")
  .data(y.ticks(4))
  .join("line")
  .attr("x1", 0)
  .attr("x2", INNER_W)
  .attr("y1", y)
  .attr("y2", y);

plot
  .append("g")
  .attr("class", "grid")
  .selectAll("line")
  .data(d3.range(170, 231, 10))
  .join("line")
  .attr("x1", x)
  .attr("x2", x)
  .attr("y1", 0)
  .attr("y2", INNER_H);

// Axes
const xAxis = plot
  .append("g")
  .attr("class", "axis")
  .attr("transform", `translate(0,${INNER_H})`)
  .call(
    d3
      .axisBottom(x)
      .tickValues(d3.range(170, 231, 10))
      .tickSizeOuter(0)
  );

const yAxis = plot
  .append("g")
  .attr("class", "axis")
  .call(
    d3
      .axisLeft(y)
      .tickValues(d3.range(3000, 6001, 1000))
      .tickFormat(d3.format("d"))
      .tickSizeOuter(0)
  );

plot
  .append("text")
  .attr("class", "axis-label")
  .attr("x", INNER_W / 2)
  .attr("y", INNER_H + 48)
  .attr("text-anchor", "middle")
  .text("Flipper Length (mm)");

plot
  .append("text")
  .attr("class", "axis-label")
  .attr("transform", "rotate(-90)")
  .attr("x", -INNER_H / 2)
  .attr("y", -50)
  .attr("text-anchor", "middle")
  .text("Body Mass (g)");

// Legends
const legend = svg
  .append("g")
  .attr("transform", `translate(${MARGIN.left + INNER_W + 34},${MARGIN.top + 30})`);

legend
  .append("text")
  .attr("class", "legend-title")
  .attr("x", 0)
  .attr("y", 0)
  .text("species");

const speciesOrder = ["Adelie", "Chinstrap", "Gentoo"];
legend
  .selectAll("circle.species")
  .data(speciesOrder)
  .join("circle")
  .attr("class", "species")
  .attr("cx", 8)
  .attr("cy", (_, i) => 26 + i * 24)
  .attr("r", 7)
  .attr("fill", color);

legend
  .selectAll("text.species")
  .data(speciesOrder)
  .join("text")
  .attr("class", "species")
  .attr("x", 24)
  .attr("y", (_, i) => 30 + i * 24)
  .attr("font-size", 13)
  .attr("fill", "#222")
  .text((d) => d);

legend
  .append("text")
  .attr("class", "legend-title")
  .attr("x", 0)
  .attr("y", 128)
  .text("bill_length_mm");

const sizeValues = [40, 50];
legend
  .selectAll("circle.size")
  .data(sizeValues)
  .join("circle")
  .attr("class", "size")
  .attr("cx", 8)
  .attr("cy", (d, i) => 156 + i * 32)
  .attr("r", (d) => radius(d))
  .attr("fill", "#3b3b3b");

legend
  .selectAll("text.size")
  .data(sizeValues)
  .join("text")
  .attr("class", "size")
  .attr("x", 28)
  .attr("y", (d, i) => 160 + i * 32)
  .attr("font-size", 13)
  .attr("fill", "#222")
  .text((d) => d);

// Point
function showTooltip(event, d) {
  tooltip
    .classed("visible", true)
    .html(
      `<b>${d.species}</b><br>` +
        `${d.island} &middot; ${d.sex}<br>` +
        `Flipper: ${d.flipper_length_mm} mm<br>` +
        `Body mass: ${d.body_mass_g} g<br>` +
        `Bill: ${d.bill_length_mm} mm`
    );
  moveTooltip(event);
}

function moveTooltip(event) {
  tooltip.style("left", `${event.clientX}px`).style("top", `${event.clientY}px`);
}

function hideTooltip() {
  tooltip.classed("visible", false);
}

d3.json("data.json")
  .then((data) => {
    const points = data
      .filter(
        (d) =>
          Number.isFinite(d.flipper_length_mm) &&
          Number.isFinite(d.body_mass_g) &&
          Number.isFinite(d.bill_length_mm)
      )
      .sort((a, b) => a.bill_length_mm - b.bill_length_mm);

    plot
      .append("g")
      .selectAll("circle")
      .data(points)
      .join("circle")
      .attr("class", "point")
      .attr("cx", (d) => x(d.flipper_length_mm))
      .attr("cy", (d) => y(d.body_mass_g))
      .attr("r", (d) => radius(d.bill_length_mm))
      .attr("fill", (d) => color(d.species))
      .attr("tabindex", 0)
      .on("mouseenter", function (event, d) {
        d3.select(this).classed("hovered", true);
        showTooltip(event, d);
      })
      .on("mousemove", moveTooltip)
      .on("mouseleave", function () {
        d3.select(this).classed("hovered", false);
        hideTooltip();
      })
      .on("focus", function (event, d) {
        d3.select(this).classed("hovered", true);
        const box = this.getBoundingClientRect();
        showTooltip(
          { clientX: box.left + box.width / 2, clientY: box.top },
          d
        );
      })
      .on("blur", function () {
        d3.select(this).classed("hovered", false);
        hideTooltip();
      });

    d3.select(".subtitle").text(
      `${points.length} observations · color = species · size = bill length · opacity = 0.8`
    );
  })
  .catch((error) => {
    console.error("Could not load data.json:", error);
    plot
      .append("text")
      .attr("x", INNER_W / 2)
      .attr("y", INNER_H / 2)
      .attr("text-anchor", "middle")
      .attr("fill", "#b00020")
      .text("Could not load data.json — run `java PenguinServer` and reload.");
  });
