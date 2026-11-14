//setting the margins in a way that is more progomatic than changing individual values
var margin = {top: 10, right: 130, bottom: 60, left: 60},
    width = 870 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

const svg = d3.select("#main")
        .append("svg").attr("height",(height + margin.top + margin.bottom))
                        .attr("width",(width + margin.left + margin.right))
        .append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

//this is the background canvas
svg.append('rect')
    .attr("height", (height + margin.top + margin.bottom))
    .attr("width", (width + margin.left + margin.right))
    .attr("fill", '#f5f5f5');

//this is going to be the gray smaller bg
svg.append('rect')
    .attr("height", height)
    .attr("width", width)
    .attr("fill", '#dedede')
    .attr("x", margin.left)
    .attr("y", margin.top);

//here I am loading the data
d3.csv("../penglings.csv", d => {
  if (d.species=="NA" || d.flipper_length_mm=="NA" || d.body_mass_g=="NA" || d.bill_length_mm=="NA") return null;  // skip rows with empty fields
  return {species: d.species, flipper_length_mm: +d.flipper_length_mm, body_mass_g: +d.body_mass_g, bill_length_mm: +d.bill_length_mm };
}).then(data => {
    console.log(data); //checking data exists :)

// Add X axis
  var x = d3.scaleLinear()
    .domain([165, 230])
    .range([ 0, width]);

  const xGrid = svg.append("g")
  .attr("class", "grid")
  .attr("transform", "translate(" + margin.left + "," + (height + 10) + ")")
  .call(d3.axisBottom(x).tickSize(-height).tickFormat(() => ""));

  xGrid.select(".domain").remove();

  svg.append("g")
    .attr("transform", "translate(" + margin.left + "," + (height + 10) + ")")
    .call(d3.axisBottom(x));

  // Add Y axis
  var y = d3.scaleLinear()
    .domain([2650, 6500])
    .range([height, 0]);

  // Horizontal grid lines
  const yGrid = svg.append("g")
  .attr("class", "grid")
  .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
  .call(d3.axisLeft(y).tickSize(-width).tickFormat(() => ""));
  
  yGrid.select(".domain").remove();

  svg.append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
    .call(d3.axisLeft(y));

  // Style both grid groups
  svg.selectAll(".grid line")
  .attr("stroke", "#efefef")
  .attr("stroke-opacity", 0.5);
  
  // Add a scale for bubble size
  var z = d3.scaleLinear()
    .domain([1, 100])
    .range([ 1, 10]);

  // Add a scale for bubble color
  var myColor = d3.scaleOrdinal()
    .domain(["Adelie", "Chinstrap", "Gentoo"])
    .range(["#f7a518", "#a658ef", "#2bb9b7"]);

  // Add dots
  svg.append('g')
    .selectAll("dot")
    .data(data)
    .enter()
    .append("circle")
      .attr("cx", function (d) { return x(d.flipper_length_mm); } )
      .attr("cy", function (d) { return y(d.body_mass_g); } )
      .attr("r", function (d) { return z(2*d.bill_length_mm); } )
      .style("fill", function (d) { return myColor(d.species); } )
      .style("opacity", "0.8")
      .style("stroke-width", "2px")
});
