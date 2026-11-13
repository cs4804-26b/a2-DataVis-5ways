async function createScatterplot() {

    const penguinData = await d3.csv("../penglings.csv", d3.autoType);

    // Specify the chart’s dimensions.
    const width = 850;
    const height = 550;
    const marginTop = 20;
    const marginBottom = 65;
    const marginRight = 30;
    const marginLeft = 80;

    // The scales (X,Y,Color,Radius)
    const x = d3.scaleLinear()
        .domain([170, 245])
        .range([marginLeft, width - marginRight]);

    const y = d3.scaleLinear()
        .domain([2500, 6500])
        .range([height - marginBottom, marginTop]);

    const color = d3.scaleOrdinal()
        .domain(["Adelie", "Chinstrap", "Gentoo"])
        .range(["#FF7F7F", "#90EE90", "#ADD8E6"]);

    const radius = d3.scaleSqrt()
        .domain([32, 60])
        .range([3, 10]);

    // Create the container
    const svg = d3.create("svg")
        .attr("viewBox", [0, 0, width, height])
        .attr("style", "max-width: 100%; height: auto; font: 10px sans-serif;")
        .attr("aria-label", "Scatterplot of Penguin Measurements with D3");

    // Create the axes.
    svg.append("g")
        .attr("transform", `translate(0, ${height - marginBottom})`)
        .call(d3.axisBottom(x).ticks(7));

    svg.append("g")
        .attr("transform", `translate(${marginLeft},0)`)
        .call(d3.axisLeft(y))


    // Add the axis labels
    svg.append("text")
        .attr("x", (marginLeft + width - marginRight) / 2)
        .attr("y", height - 15)
        .attr("text-anchor", "middle")
        .text("Flipper Length (mm)");



    svg.append("text")
        .attr("transform", "rotate(-90)")
        .attr("x", -(marginTop + height - marginBottom) / 2)
        .attr("y", 20)
        .attr("text-anchor", "middle")
        .text("Body Mass (g)");


    // Add dots to the graph
    const circles = svg.selectAll("circle")
        .data(penguinData)
        .join("circle")
        .attr("cx", d => x(d.flipper_length_mm))
        .attr("cy", d => y(d.body_mass_g))
        .attr("r", d => radius(d.bill_length_mm))
        .attr("fill", d => color(d.species))
        .attr("opacity", 0.8);

    // Technical achievement/tooltips

    //Create tooltip container
    const tooltip = svg.append("g")
        .attr("pointer-events", "none");

    const tooltipText = tooltip.append("foreignObject")
        .attr("width", 130)
        .attr("height", 200)
        .append("xhtml:div")
        .style("background", "white")
        .style("border", "1px solid black")
        .style("border-radius", "5px")
        .style("padding", "10px")
        .style("white-space", "pre-line");

    // Hover mouse event for each circle
    // Creates a tool tip for each circle when hovered over
    circles
    .on("mouseenter", function(event, d) {
        d3.select(this).attr("stroke", "black");
        tooltip.style("display", "block")
            .attr("transform",`translate(${x(d.flipper_length_mm) + 15}, ${y(d.body_mass_g) - 15})`
        );
        tooltipText.text(
            `${d.species} Penguin
            Island: ${d.island}
            Bill Length: ${d.bill_length_mm} mm
            Flipper Length: ${d.flipper_length_mm} mm
            Body Mass: ${d.body_mass_g} g
            Sex: ${d.sex}
            Year: ${d.year}`
        );
    })
    .on("mouseleave", function() {
        d3.select(this).attr("stroke", "none");
        tooltip.style("display", "none");
        
    });


    document.querySelector("#chart").append(svg.node());
}
createScatterplot();