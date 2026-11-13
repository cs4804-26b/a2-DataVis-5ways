
const svg = d3.select("#chart");

const width = 900;
const height = 600;

const margin = {
    top: 60,
    right: 180,
    bottom: 80,
    left: 90
};

const chartWidth = width - margin.left - margin.right;
const chartHeight = height - margin.top - margin.bottom;

const chart = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Create chart instructions and species filter
const chartContainer = d3.select("#chart").node().parentElement;

const filterContainer = d3.select(chartContainer)
    .insert("div", "#chart")
    .style("margin-bottom", "15px")
    .style("font-family", "Arial, sans-serif");

filterContainer.append("label")
    .attr("for", "species-filter")
    .style("font-weight", "bold")
    .style("margin-right", "10px")
    .style("font-size", "14px")
    .text("Filter by Species:");

const speciesFilter = filterContainer.append("select")
    .attr("id", "species-filter")
    .style("padding", "6px 10px")
    .style("border-radius", "5px")
    .style("border", "1px solid #ccc")
    .style("font-size", "14px");

speciesFilter.append("option")
    .attr("value", "All")
    .text("All Species");

// Create tooltip
const tooltip = d3.select("body")
    .append("div")
    .style("position", "absolute")
    .style("background", "#222222")
    .style("color", "#ffffff")
    .style("padding", "10px 14px")
    .style("border-radius", "6px")
    .style("font-size", "12px")
    .style("line-height", "1.6")
    .style("pointer-events", "none")
    .style("opacity", 0)
    .style("z-index", 1000);

d3.csv("../../penglings.csv").then(data => {

    // Remove rows with missing measurements
    data = data.filter(d =>
        d.flipper_length_mm !== "NA" &&
        d.body_mass_g !== "NA" &&
        d.bill_length_mm !== "NA" &&
        d.species !== "NA"
    );

    // Convert measurements to numbers
    data.forEach(d => {
        d.flipper_length_mm = +d.flipper_length_mm;
        d.body_mass_g = +d.body_mass_g;
        d.bill_length_mm = +d.bill_length_mm;
    });

    // X and Y scales
    const x = d3.scaleLinear()
        .domain(d3.extent(data, d => d.flipper_length_mm))
        .nice()
        .range([0, chartWidth]);

    const y = d3.scaleLinear()
        .domain(d3.extent(data, d => d.body_mass_g))
        .nice()
        .range([chartHeight, 0]);

    // Color scale based on species
    const speciesColors = {
        "Adelie": "#e11d48",
        "Chinstrap": "#ecb425",
        "Gentoo": "#2563EB"
    };

    const species = [...new Set(data.map(d => d.species))];

    const color = d3.scaleOrdinal()
        .domain(species)
        .range(species.map(s => speciesColors[s]));

    // Add species options to dropdown
    species.forEach(s => {
        speciesFilter.append("option")
            .attr("value", s)
            .text(s);
    });

    // Circle size based on bill length
    const size = d3.scaleSqrt()
        .domain(d3.extent(data, d => d.bill_length_mm))
        .range([3, 11]);

    // Track current interactions
    let selectedSpecies = "All";
    let hoveredPenguin = null;

    // Chart title
    chart.append("text")
        .attr("class", "title")
        .attr("x", chartWidth / 2)
        .attr("y", -40)
        .attr("text-anchor", "middle")
        .text("Penguin Measurements");

    // Chart subtitle
    chart.append("text")
        .attr("class", "subtitle")
        .attr("x", chartWidth / 2)
        .attr("y", -15)
        .attr("text-anchor", "middle")
        .text("Hover over penguins to view their details. Use the dropdown to filter by species.");

    // X axis
    chart.append("g")
        .attr("transform", `translate(0, ${chartHeight})`)
        .call(d3.axisBottom(x))
        .selectAll("text")
        .attr("font-size", 11)
        .attr("fill", "#222222");

    // Y axis
    chart.append("g")
        .call(d3.axisLeft(y))
        .selectAll("text")
        .attr("font-size", 11)
        .attr("fill", "#222222");

    // Axis gridlines
    chart.selectAll(".tick line")
        .attr("stroke", "#DDDDDD")
        .attr("stroke-width", 0.7);

    chart.selectAll(".domain")
        .attr("stroke", "#AAAAAA");

    // X axis label
    chart.append("text")
        .attr("class", "axis-label")
        .attr("x", chartWidth / 2)
        .attr("y", chartHeight + 55)
        .attr("text-anchor", "middle")
        .text("Flipper Length (mm)");

    // Y axis label
    chart.append("text")
        .attr("class", "axis-label")
        .attr("transform", "rotate(-90)")
        .attr("x", -chartHeight / 2)
        .attr("y", -60)
        .attr("text-anchor", "middle")
        .text("Body Mass (g)");

    // Update point appearance based on interactions
    function updatePointStyles() {
        points
            .attr("opacity", d => {
                if (selectedSpecies !== "All" && d.species !== selectedSpecies) {
                    return 0;
                }

                if (hoveredPenguin) {
                    return d === hoveredPenguin ? 1 : 0.35;
                }

                return 0.8;
            })
            .attr("stroke", d =>
                d === hoveredPenguin ? "#000000" : "#333333"
            )
            .attr("stroke-width", d =>
                d === hoveredPenguin ? 2 : 0.5
            )
            .attr("pointer-events", d =>
                selectedSpecies === "All" || d.species === selectedSpecies
                    ? "all"
                    : "none"
            );
    }

    // Plot penguins
    const points = chart.selectAll(".penguin")
        .data(data)
        .join("circle")
        .attr("class", "penguin")
        .attr("cx", d => x(d.flipper_length_mm))
        .attr("cy", d => y(d.body_mass_g))
        .attr("r", d => size(d.bill_length_mm))
        .attr("fill", d => color(d.species))
        .attr("opacity", 0.8)
        .attr("stroke", "#333333")
        .attr("stroke-width", 0.5)

        // Show tooltip when hovering over a penguin
        .on("mouseenter", function(event, d) {
            hoveredPenguin = d;
            updatePointStyles();

            tooltip
                .style("opacity", 1)
                .html(`
                    <strong>${d.species}</strong><br>
                    Flipper Length: ${d.flipper_length_mm} mm<br>
                    Body Mass: ${d.body_mass_g.toLocaleString()} g<br>
                    Bill Length: ${d.bill_length_mm} mm
                `);
        })

        // Move tooltip with cursor
        .on("mousemove", function(event) {
            tooltip
                .style("left", `${event.pageX + 15}px`)
                .style("top", `${event.pageY - 15}px`);
        })

        // Hide tooltip when cursor leaves penguin
        .on("mouseleave", function() {
            hoveredPenguin = null;
            updatePointStyles();

            tooltip.style("opacity", 0);
        });

    // Filter penguins by species
    speciesFilter.on("change", function() {
        selectedSpecies = this.value;

        hoveredPenguin = null;
        tooltip.style("opacity", 0);

        points.transition()
            .duration(300)
            .attr("opacity", d =>
                selectedSpecies === "All" || d.species === selectedSpecies
                    ? 0.8
                    : 0
            )
            .attr("pointer-events", d =>
                selectedSpecies === "All" || d.species === selectedSpecies
                    ? "all"
                    : "none"
            );
    });

    // Shared legend text styling
    const legendTitleStyle = selection => selection
        .attr("font-family", "Arial, sans-serif")
        .attr("font-size", 12)
        .attr("font-weight", "bold")
        .attr("fill", "#222222");

    const legendLabelStyle = selection => selection
        .attr("font-family", "Arial, sans-serif")
        .attr("font-size", 11)
        .attr("fill", "#222222");

    // Species color legend
    const speciesLegend = chart.append("g")
        .attr("transform", `translate(${chartWidth + 30}, 20)`);

    legendTitleStyle(
        speciesLegend.append("text")
            .attr("y", -5)
            .text("Species")
    );

    species.forEach((s, i) => {
        const item = speciesLegend.append("g")
            .attr("transform", `translate(0, ${i * 25 + 15})`);

        item.append("circle")
            .attr("r", 7)
            .attr("fill", color(s))
            .attr("stroke", "#333333")
            .attr("stroke-width", 0.5);

        legendLabelStyle(
            item.append("text")
                .attr("x", 15)
                .attr("y", 4)
                .text(s)
        );
    });

    // Bill length size legend
    const billLegend = chart.append("g")
        .attr("transform", `translate(${chartWidth + 30}, 160)`);

    legendTitleStyle(
        billLegend.append("text")
            .attr("y", -5)
            .text("Bill Length (mm)")
    );

    const billValues = [35, 40, 45, 50, 55];

    billValues.forEach((value, i) => {
        const item = billLegend.append("g")
            .attr("transform", `translate(20, ${i * 45 + 25})`);

        item.append("circle")
            .attr("r", size(value))
            .attr("fill", "#888888")
            .attr("opacity", 0.8)
            .attr("stroke", "#333333")
            .attr("stroke-width", 0.5);

        legendLabelStyle(
            item.append("text")
                .attr("x", 30)
                .attr("y", 4)
                .text(value)
        );
    });

}).catch(error => {
    console.error("Error loading penguin dataset:", error);
});
