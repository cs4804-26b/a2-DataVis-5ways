
const width = 1000;
const height = 600;

const margin = {
    top: 25,
    right: 180,
    bottom: 75,
    left: 90
};

const chartWidth = width - margin.left - margin.right;
const chartHeight = height - margin.top - margin.bottom;

// Colors for the three penguin species
const colors = {
    Adelie: "#FF8C00",
    Chinstrap: "#A536D2",
    Gentoo: "#008B8B"
};

// Create the drawing area
const svg = d3.select("#chart-area")
    .append("svg")
    .attr("viewBox", `0 0 ${width} ${height}`)
    .attr("role", "img")
    .attr("aria-label", "Penguin scatterplot showing flipper length and body mass");

const plot = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Set up the scales
const xScale = d3.scaleLinear()
    .domain([169, 234])
    .range([0, chartWidth]);

const yScale = d3.scaleLinear()
    .domain([2500, 6500])
    .range([chartHeight, 0]);

const sizeScale = d3.scaleSqrt()
    .domain([30, 60])
    .range([3, 12]);

// Add a gray background
plot.append("rect")
    .attr("width", chartWidth)
    .attr("height", chartHeight)
    .attr("fill", "#EBEBEB");

// Vertical gridlines
plot.append("g")
    .selectAll("line")
    .data(d3.range(170, 231, 10))
    .join("line")
    .attr("x1", d => xScale(d))
    .attr("x2", d => xScale(d))
    .attr("y1", 0)
    .attr("y2", chartHeight)
    .attr("stroke", "white");

// Horizontal gridlines
plot.append("g")
    .selectAll("line")
    .data(d3.range(3000, 6500, 500))
    .join("line")
    .attr("x1", 0)
    .attr("x2", chartWidth)
    .attr("y1", d => yScale(d))
    .attr("y2", d => yScale(d))
    .attr("stroke", "white");

// Horizontal axis
plot.append("g")
    .attr("class", "axis")
    .attr("transform", `translate(0, ${chartHeight})`)
    .call(d3.axisBottom(xScale)
        .tickValues(d3.range(170, 231, 10))
        .tickSize(0)
        .tickPadding(10));

// Vertical axis
plot.append("g")
    .attr("class", "axis")
    .call(d3.axisLeft(yScale)
        .tickValues([3000, 4000, 5000, 6000])
        .tickSize(0)
        .tickPadding(10));

// Horizontal axis label
svg.append("text")
    .attr("class", "axis-label")
    .attr("x", margin.left + chartWidth / 2)
    .attr("y", height - 18)
    .attr("text-anchor", "middle")
    .text("Flipper Length (mm)");

// Vertical axis label
svg.append("text")
    .attr("class", "axis-label")
    .attr("transform", `translate(24, ${margin.top + chartHeight / 2}) rotate(-90)`)
    .attr("text-anchor", "middle")
    .text("Body Mass (g)");



// Create the legends
const legend = svg.append("g")
    .attr("transform", `translate(${width - 160}, 90)`);

// Bill length legend
legend.append("text")
    .attr("font-size", 16)
    .attr("font-weight", "bold")
    .text("Bill Length (mm)");

[40, 50].forEach(function(length, i) {
    const y = 38 + i * 47;

    legend.append("circle")
        .attr("cx", 13)
        .attr("cy", y)
        .attr("r", sizeScale(length))
        .attr("fill", "#555")
        .attr("opacity", 0.8);

    legend.append("text")
        .attr("class", "legend-label")
        .attr("x", 35)
        .attr("y", y + 5)
        .text(length);
});

// Species legend
legend.append("text")
    .attr("font-size", 16)
    .attr("font-weight", "bold")
    .attr("y", 148)
    .text("Species");

["Adelie", "Chinstrap", "Gentoo"].forEach(function(species, i) {
    const y = 180 + i * 32;

    legend.append("circle")
        .attr("cx", 13)
        .attr("cy", y)
        .attr("r", 6)
        .attr("fill", colors[species])
        .attr("opacity", 0.8);

    legend.append("text")
        .attr("class", "legend-label")
        .attr("x", 35)
        .attr("y", y + 5)
        .text(species);
});



// Load the penguin dataset
d3.csv("../penglings.csv").then(function(rows) {

    const penguins = rows.map(function(row) {
        return {
            species: row.species,
            island: row.island,
            year: row.year,
            flipper: +row.flipper_length_mm,
            mass: +row.body_mass_g,
            bill: +row.bill_length_mm
        };
    }).filter(function(d) {
        return Number.isFinite(d.flipper) && d.flipper > 0 &&
               Number.isFinite(d.mass) && d.mass > 0 &&
               Number.isFinite(d.bill) && d.bill > 0;
    });

    // Draw the penguins
    const dots = plot.append("g")
        .selectAll("circle")
        .data(penguins)
        .join("circle")
        .attr("class", "dot")
        .attr("cx", d => xScale(d.flipper))
        .attr("cy", d => yScale(d.mass))
        .attr("r", d => sizeScale(d.bill))
        .attr("fill", d => colors[d.species])
        .attr("opacity", 0.8);

    
// Show detailed information when hovering over a circle
const tooltip = d3.select("#tooltip");

dots.on("mouseenter", function(event, d) {
    tooltip.style("display", "block")
        .html(`<strong>${d.species} penguin</strong><br>` +
              `Flipper length: ${d.flipper} mm<br>` +
              `Body mass: ${d.mass.toLocaleString()} g<br>` +
              `Bill length: ${d.bill} mm<br>` +
              `Island: ${d.island}<br>` +
              `Year: ${d.year}`);

}).on("mousemove", function(event) {
    const bounds = document.getElementById("chart-area").getBoundingClientRect();

    const left = Math.min(event.clientX - bounds.left + 15, bounds.width - 205);
    const top = Math.max(0, event.clientY - bounds.top - 95);

    tooltip.style("left", `${Math.max(0, left)}px`)
           .style("top", `${top}px`);

}).on("mouseleave", function() {
    tooltip.style("display", "none");
});


// Filter the penguins by species
d3.selectAll("#filters button").on("click", function() {
    const chosen = this.getAttribute("data-species");

    // Highlight the selected button
    d3.selectAll("#filters button")
        .classed("selected", function() {
            return this.getAttribute("data-species") === chosen;
        });

    // Show only the selected species
    dots.style("display", function(d) {
        return chosen === "All" || d.species === chosen
            ? null
            : "none";
    });

    // Update the number of penguins being shown
    const visible = chosen === "All"
        ? penguins.length
        : penguins.filter(d => d.species === chosen).length;

    d3.select("#count")
        .text(`Showing ${visible} of ${penguins.length} penguins`);

    tooltip.style("display", "none");
});

// Display the initial count
d3.select("#count")
    .text(`Showing ${penguins.length} of ${penguins.length} penguins`);


}).catch(function(error) {
    d3.select("#count")
        .text("Could not load penglings.csv. Check the terminal folder.");
    console.error(error);
});
