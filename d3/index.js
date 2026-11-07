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

  const legend = (x, y) => {
    const width = 200
    const height = 380
    const subheadingOffset = 25
    const valueOffset = subheadingOffset + 95
    const lineSpacing = 20

    const box = d3.create("svg:g")
    .attr("transform", `translate(${x}, ${y})`)

    box.append("svg:rect")
    .attr("id", "legend")
    .attr("width", width)
    .attr("height", height)


    box.append("svg:text")
      .attr("class", "label main")
      .attr("x", width/2)
      .attr("y", width/5)
      .text("Legend")

    // Species description
    box.append("svg:text")
      .attr("x", subheadingOffset)
      .attr("y", 70)
      .attr("class", "label sub")
      .text("Species")
    species.forEach((name, i) => {
      box.append("svg:text")
        .attr("class", "label local")
        .attr("x", subheadingOffset)
        .attr("y", 90+i*lineSpacing)
        .text(name)
      box.append("circle")
        .attr("cx", valueOffset)
        .attr("cy", 86+i*lineSpacing)
        .attr("r", 5)
        .attr("fill", color(name))
    })

    box.append("svg:text")
      .attr("x", subheadingOffset)
      .attr("y", 170)
      .attr("class", "label sub")
      .text("Bill Length (mm)")
    const values = Array.from({length: 4}, (_, i) => 35+i*5)
    console.log(values)
    values.forEach((rad, i) => {
      box.append("svg:text")
        .attr("class", "label local")
        .attr("x", subheadingOffset)
        .attr("y", 190+i*lineSpacing)
        .text(String(rad))
      box.append("circle")
        .attr("cx", valueOffset)
        .attr("cy", 186+i*lineSpacing)
        .attr("r", radius(rad))
        .attr("fill", "black")
    })

    box.append("svg:text")
      .attr("class", "label sub")
      .attr("x", labelOffset)
      .attr("y", 280)
      .text("Values")
    box.append("svg:text")
      .attr("id", "hover-values")
      .attr("class", "label local")
      .attr("x", labelOffset)
      .attr("y", 280)
      .text(`
Flipper Length (mm)
Body Mass (g)
Species
Bill Length (mm)
`)

    return box.node()
  }

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
    .on("mouseover", function (event, d) {
      d3.select("#hover-values")
        .text(`
Flipper Length: ${d.flipperLength} mm
Body Mass: ${d.bodyMass} g
Species: ${d.species}
Bill Length: ${d.billLength} mm
`)
    }).on("mouseleave", function (event, d) {
      d3.select("#hover-values").text(`
Flipper Length
Body Mass
Species
Bill Length
`)
    })

  svg.append(() => legend(100, 60))

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
