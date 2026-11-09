const DATA_URL = "http://localhost:8000/penglings.csv"

const loadData = async () => {
  return await d3.csv(DATA_URL, (d) => {
    if (Object.values(d).includes("NA")) return // skip rows with null values
    return {
      species: d.species,
      billLength: +d.bill_length_mm,
      flipperLength: +d.flipper_length_mm,
      bodyMass: +d.body_mass_g,
    }
  })
}

const penguinsChart = (data) => {
  const chartLen = 1000
  const margin = 80
  const labelOffset = 20

  // scales for graph visual elements
  const xPos = d3.scaleLinear(
    d3.extent(data, d => d.flipperLength),
    [margin, chartLen-margin],
  ).nice()
  const yPos = d3.scaleLinear(
    d3.extent(data, d => d.bodyMass),
    [chartLen-margin, margin],
  ).nice()
  const species = [...new Set(data.map(o => o.species))]
  const color = d3.scaleOrdinal(
    species,
    d3.schemeObservable10,
  )
  const colorMapping = Object.fromEntries(species.map((name) => [color(species), name]))

  const radius = d3.scaleLinear(
    d3.extent(data, d => d.billLength),
    [4, 13],
  ).nice()

  const legendNode = (x, y) => {
    const width = 200
    const height = 280
    const subheadingOffset = 25
    const valueOffset = subheadingOffset + 95
    const lineSpacing = 20

    const legend = d3.create("svg:g")
    .attr("transform", `translate(${x}, ${y})`)

    legend.append("svg:rect")
    .attr("class", "info-box")
    .attr("width", width)
    .attr("height", height)


    legend.append("svg:text")
      .attr("class", "label main")
      .attr("x", width/2)
      .attr("y", width/5)
      .text("Legend")

    // Species description
    legend.append("svg:text")
      .attr("x", subheadingOffset)
      .attr("y", 70)
      .attr("class", "label sub")
      .text("Species")
    species.forEach((name, i) => {
      legend.append("svg:text")
        .attr("class", "label local")
        .attr("x", subheadingOffset)
        .attr("y", 90+i*lineSpacing)
        .text(name)
      legend.append("circle")
        .attr("cx", valueOffset)
        .attr("cy", 86+i*lineSpacing)
        .attr("r", 5)
        .attr("fill", color(name))
    })

    legend.append("svg:text")
      .attr("x", subheadingOffset)
      .attr("y", 170)
      .attr("class", "label sub")
      .text("Bill Length (mm)")
    const values = Array.from({length: 4}, (_, i) => 35+i*5)
    values.forEach((rad, i) => {
      legend.append("svg:text")
        .attr("class", "label local")
        .attr("x", subheadingOffset)
        .attr("y", 190+i*lineSpacing)
        .text(String(rad))
      legend.append("circle")
        .attr("cx", valueOffset)
        .attr("cy", 186+i*lineSpacing)
        .attr("r", radius(rad))
        .attr("fill", "black")
    })

    return legend.node()
  }

  const popupNode = (() => {
    const sideLen = 207
    const offset = 15
    const popup = d3.create("svg:g")
      .attr("id", "popup")
      .style("display", "none")
      .attr("transform", `translate(700, 800)`)

      popup.append("svg:rect")
      .attr("class", "info-box")
      .attr("width", sideLen)
      .attr("height", sideLen*4/9)
    popup.append("svg:text")
      .attr("id", "hover-values")
      .attr("class", "label local")
      .attr("x", 10)
      .attr("y", 5)

    return popup.node()
  })()

  const svg = d3
    .create("svg")
    .attr("width", chartLen)
    .attr("height", chartLen)

  // x-axis
  svg.append("svg:g")
    .attr("transform", `translate(0, ${chartLen-margin})`)
    .call(d3.axisBottom(xPos).ticks(10))
    .append("svg:text")
    .attr("class", "local-transform label main")
    .attr("x", `${chartLen/2}`)
    .attr("y", `${margin-labelOffset}`)
    .text("Flipper Length (mm)")
  // y-axis
  svg.append("svg:g")
    .attr("transform", `translate(${margin}, 0)`)
    .call(d3.axisLeft(yPos).ticks(10))
    .append("svg:text")
    .attr("class", "local-transform label main")
    .attr("x", `${-margin+labelOffset}`)
    .attr("y", `${chartLen/2}`)
    .attr("transform", "rotate(270)")
    .text("Body Mass (g)")

  // points
  svg.append("svg:g")
    .selectAll("circle")
    .data(data)
    .join("svg:circle")
    .attr("class", "point")
    .attr("cx", d => xPos(d.flipperLength))
    .attr("cy", d => yPos(d.bodyMass))
    .attr("fill", d => color(d.species))
    .attr("r", d => radius(d.billLength))
    .on("mouseenter", function (event, d) {
      const textValues = d3.select("#hover-values")
      textValues.text(`
Flipper Length (mm): ${d.flipperLength} mm
Body Mass (g): ${d.bodyMass} g
Species: ${d.species}
Bill Length (mm): ${d.billLength} mm
`)
      d3.select("#popup").style("display", "block")
    }).on("mouseleave", function (event, d) {
      d3.select("#popup").style("display", "none")
    })


  svg.append(() => legendNode(100, 60))
  svg.append(() => popupNode)

  return svg.node()
}

async function main() {
  const container = document.getElementById("container")
  let data
  try {
    data = await loadData()
  } catch (error) {
    console.error(error);
    const message = document.createElement("p");
    message.textContent = "Failed to load data.";
    message.style.color = "red";
    container.append(message);
    return
  }
  const svg = penguinsChart(data)
  container.append(svg)
}

main()
