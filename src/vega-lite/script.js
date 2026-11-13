
async function createVisualization() {
    // Load and parse the dataset
    const response = await fetch("../../penglings.csv");

    if (!response.ok) {
        throw new Error("Could not load penglings.csv");
    }

    const csvText = await response.text();
    const parsedRows = vega.read(csvText, { type: "csv" });

    // Convert measurement columns to numbers
    const penguinData = parsedRows.map(row => ({
        ...row,
        flipper_length_mm: Number(row.flipper_length_mm),
        body_mass_g: Number(row.body_mass_g),
        bill_length_mm: Number(row.bill_length_mm)
    }));

    // Determine actual bill length boundaries
    const validBillLengths = penguinData
        .filter(row =>
            Number.isFinite(row.bill_length_mm) &&
            Number.isFinite(row.flipper_length_mm) &&
            Number.isFinite(row.body_mass_g) &&
            row.species !== "NA"
        )
        .map(row => row.bill_length_mm);

    if (validBillLengths.length === 0) {
        throw new Error("No valid penguin measurements found.");
    }

    const minBillLength = Math.min(...validBillLengths);
    const maxBillLength = Math.max(...validBillLengths);

    // Get slider elements
    const minSlider = document.getElementById("minSlider");
    const maxSlider = document.getElementById("maxSlider");
    const minValueLabel = document.getElementById("minValue");
    const maxValueLabel = document.getElementById("maxValue");
    const sliderRange = document.getElementById("sliderRange");

    // Configure slider boundaries
    minSlider.min = minBillLength;
    minSlider.max = maxBillLength;
    minSlider.value = minBillLength;

    maxSlider.min = minBillLength;
    maxSlider.max = maxBillLength;
    maxSlider.value = maxBillLength;

    // Create the Vega-Lite specification
    const spec = {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",

        "width": 650,
        "height": 450,

        "title": {
            "text": "Penguin Measurements",
            "subtitle": "Adjust the slider to filter penguins by bill length.",
            "font": "Arial",
            "fontSize": 20,
            "fontWeight": "bold",
            "subtitleFont": "Arial",
            "subtitleFontSize": 13,
            "subtitleFontWeight": "normal",
            "color": "#222222",
            "subtitleColor": "#555555",
            "anchor": "middle"
        },

        "data": {
            "values": penguinData
        },

        "params": [
            {
                "name": "minBillLength",
                "value": minBillLength
            },
            {
                "name": "maxBillLength",
                "value": maxBillLength
            }
        ],

        "transform": [
            {
                "filter": "isValid(datum.flipper_length_mm) && isValid(datum.body_mass_g) && isValid(datum.bill_length_mm) && datum.species != 'NA'"
            },
            {
                "filter": "datum.bill_length_mm >= minBillLength && datum.bill_length_mm <= maxBillLength"
            }
        ],

        "mark": {
            "type": "circle",
            "opacity": 0.8,
            "stroke": "#333333",
            "strokeWidth": 0.5
        },

        "encoding": {
            "x": {
                "field": "flipper_length_mm",
                "type": "quantitative",
                "title": "Flipper Length (mm)",
                "scale": {
                    "zero": false
                }
            },

            "y": {
                "field": "body_mass_g",
                "type": "quantitative",
                "title": "Body Mass (g)",
                "scale": {
                    "zero": false
                }
            },

            "color": {
                "field": "species",
                "type": "nominal",
                "title": "Species",
                "scale": {
                    "domain": ["Adelie", "Chinstrap", "Gentoo"],
                    "range": ["#e11d48", "#ecb425", "#2563EB"]
                },
                "legend": {
                    "orient": "right",
                    "titleFont": "Arial",
                    "titleFontSize": 12,
                    "titleFontWeight": "bold",
                    "labelFont": "Arial",
                    "labelFontSize": 11,
                    "symbolSize": 150,
                    "symbolStrokeColor": "#333333",
                    "symbolStrokeWidth": 0.5
                }
            },

            "size": {
                "field": "bill_length_mm",
                "type": "quantitative",
                "title": "Bill Length (mm)",
                "scale": {
                    "type": "pow",
                    "exponent": 2,
                    "domain": [35, 55],
                    "range": [75, 300]
                },
                "legend": {
                    "orient": "right",
                    "values": [35, 40, 45, 50, 55],
                    "symbolFillColor": "#888888",
                    "symbolStrokeColor": "#333333",
                    "symbolStrokeWidth": 0.5,
                    "titleFont": "Arial",
                    "titleFontSize": 12,
                    "titleFontWeight": "bold",
                    "labelFont": "Arial",
                    "labelFontSize": 11
                }
            },
        },

        "config": {
            "background": "#F7F7F2",
            "font": "Arial",

            "title": {
                "font": "Arial",
                "fontSize": 20,
                "fontWeight": "bold",
                "subtitleFont": "Arial",
                "subtitleFontSize": 13,
                "anchor": "middle",
                "color": "#222222",
                "subtitleColor": "#555555"
            },

            "axis": {
                "labelFont": "Arial",
                "titleFont": "Arial",
                "labelFontSize": 11,
                "titleFontSize": 13,
                "labelColor": "#222222",
                "titleColor": "#222222",
                "gridColor": "#DDDDDD",
                "gridWidth": 0.7,
                "domainColor": "#AAAAAA",
                "tickColor": "#AAAAAA"
            },

            "legend": {
                "labelFont": "Arial",
                "titleFont": "Arial",
                "labelFontSize": 11,
                "titleFontSize": 12,
                "titleFontWeight": "bold",
                "labelColor": "#222222",
                "titleColor": "#222222",
                "padding": 8
            }
        }
    };

    // Render the chart
    const result = await vegaEmbed("#chart", spec, {
        actions: false
    });

    const view = result.view;

    // Update the slider appearance and chart filters
    function updateSlider() {
        let min = Number(minSlider.value);
        let max = Number(maxSlider.value);

        // Prevent the minimum from exceeding the maximum
        if (min > max) {
            min = max;
            minSlider.value = min;
        }

        // Prevent the maximum from falling below the minimum
        if (max < min) {
            max = min;
            maxSlider.value = max;
        }

        // Update displayed values
        minValueLabel.textContent = min.toFixed(1);
        maxValueLabel.textContent = max.toFixed(1);

        // Update highlighted portion of slider track
        const range = maxBillLength - minBillLength;

        const leftPercent = ((min - minBillLength) / range) * 100;
        const rightPercent = ((max - minBillLength) / range) * 100;

        sliderRange.style.left = `${leftPercent}%`;
        sliderRange.style.width = `${rightPercent - leftPercent}%`;

        // Update the Vega-Lite filter parameters
        view.signal("minBillLength", min);
        view.signal("maxBillLength", max);
        view.runAsync();
    }

    // Connect both handles to the update function
    minSlider.addEventListener("input", updateSlider);
    maxSlider.addEventListener("input", updateSlider);

    // Initialize slider labels and appearance
    updateSlider();
}

createVisualization().catch(console.error);
