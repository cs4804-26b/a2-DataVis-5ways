// Set up dimensions for chart
const width = 1100;
const height = 650;
const margin = {
    top: 30,
    right: 200,
    bottom: 80,
    left: 90
};

// Calculate usable chart area
const chartWidth = width - margin.left - margin.right;
const chartHeight = height - margin.top - margin.bottom;
// Set colors for species
const colors = {
Adelie: "#E09719",Chinstrap: "#B363C7",Gentoo: "#27f5b4"
};

// Reads the file
d3.csv("../penglings.csv").then(data => {
    // Convert measurement columns text -> numbers
    data.forEach(d => {
        d.flipper_length_mm = +d.flipper_length_mm;
        d.body_mass_g = +d.body_mass_g;
        d.bill_length_mm = +d.bill_length_mm;
    });
    // Remove the missing measurements
    data = data.filter(d =>
        d.species &&
        Number.isFinite(d.flipper_length_mm) &&
        Number.isFinite(d.body_mass_g) &&
        Number.isFinite(d.bill_length_mm)
    );
    // Create the SVG area
    const svg = d3.select("#chart")
        .append("svg")
        .attr("width", width)
        .attr("height", height);
    // Create a group for the chart
    const chart = svg.append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);
    // Create x-axis scale
    const xScale = d3.scaleLinear()
        .domain([170, 235])
        .range([0, chartWidth]);
    // Create y-axis scale
    const yScale = d3.scaleLinear()
        .domain([2500, 6500])
        .range([chartHeight, 0]);
    // Create circle size scale
    const sizeScale = d3.scaleSqrt()
        .domain(d3.extent(data, d => d.bill_length_mm))
        .range([3, 9]);
    
    // Add grid lines
    chart.append("g")
        .attr("class", "grid")
        .call(
            d3.axisLeft(yScale)
                .tickSize(-chartWidth)
                .tickFormat("")
        );
    chart.append("g")
        .attr("class", "grid")
        .attr("transform", `translate(0,${chartHeight})`)
        .call(
            d3.axisBottom(xScale)
                .tickSize(-chartHeight)
                .tickFormat("")
        );

    // Draw the x-axis
    chart.append("g")
        .attr("class", "axis")
        .attr("transform", `translate(0,${chartHeight})`)
        .call(d3.axisBottom(xScale));
    // Draw the y-axis
    chart.append("g")
        .attr("class", "axis")
        .call(d3.axisLeft(yScale));
    // Add the axis labels
    svg.append("text")
        .attr("class", "axis-label")
        .attr("x", margin.left + chartWidth / 2)
        .attr("y", height - 20)
        .attr("text-anchor", "middle")
        .text("Flipper Length (mm)");
    svg.append("text")
        .attr("class", "axis-label")
        .attr("transform", "rotate(-90)")
        .attr("x", -(margin.top + chartHeight / 2))
        .attr("y", 25)
        .attr("text-anchor", "middle")
        .text("Body Mass (g)");

    // Draw the circles
    chart.selectAll("circle")
        .data(data)
        .enter()
        .append("circle")
        .attr("cx", d => xScale(d.flipper_length_mm))
        .attr("cy", d => yScale(d.body_mass_g))
        .attr("r", d => sizeScale(d.bill_length_mm))
        .attr("fill", d => colors[d.species])
        .attr("stroke", d => colors[d.species])
        .attr("stroke-width", 1)
        .attr("opacity", 0.8);

    // Create the species legend
    const speciesLegend = svg.append("g")
        .attr("transform", `translate(${margin.left + chartWidth + 35}, 150)`);
    speciesLegend.append("text")
        .attr("class", "legend-title")
        .text("Species");
    const species = ["Adelie", "Chinstrap", "Gentoo"];

    species.forEach((name, i) => {
        const item = speciesLegend.append("g")
            .attr("transform", `translate(0, ${30 + i * 30})`);
        item.append("circle")
            .attr("r", 6)
            .attr("fill", colors[name])
            .attr("opacity", 0.8);
        item.append("text")
            .attr("class", "legend-text")
            .attr("x", 15)
            .attr("y", 4)
            .text(name);
    });

    // Create bill length legend
    const sizeLegend = svg.append("g")
        .attr("transform", `translate(${margin.left + chartWidth + 35}, 300)`);
    sizeLegend.append("text")
        .attr("class", "legend-title")
        .text("Bill Length (mm)");
    [40, 50].forEach((value, i) => {
        const item = sizeLegend.append("g")
            .attr("transform", `translate(15, ${40 + i * 45})`);
        item.append("circle")
            .attr("r", sizeScale(value))
            .attr("fill", "#777777")
            .attr("opacity", 0.5);
        item.append("text")
            .attr("class", "legend-text")
            .attr("x", 25)
            .attr("y", 4)
            .text(value);
    });
}).catch(error => {
    console.error("Error loading the penguin dataset:", error);
}); 
