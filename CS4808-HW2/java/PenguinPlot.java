import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Map;

/**
 * Draws the Palmer penguins scatter plot as an SVG, using only the JDK.
 *
 * From this folder:
 *   javac PenguinPlot.java
 *   java PenguinPlot
 */
public class PenguinPlot {
    record Penguin(String species, String island, String sex, double flipper, double mass, double bill) {}

    static final String[] SPECIES = {"Adelie", "Chinstrap", "Gentoo"};
    static final Map<String, String> COLORS = Map.of(
            "Adelie", "#FB7708",
            "Chinstrap", "#830FBF",
            "Gentoo", "#0E7877");

    static final int WIDTH = 860;
    static final int HEIGHT = 560;
    static final int LEFT = 72;
    static final int RIGHT = 140;
    static final int TOP = 56;
    static final int BOTTOM = 56;

    public static void main(String[] args) throws IOException {
        Path csv = args.length > 0 ? Path.of(args[0]) : Path.of("..", "penglings.csv");
        Path svg = args.length > 1 ? Path.of(args[1]) : Path.of("penguins.svg");
        List<Penguin> penguins = load(csv);
        Files.writeString(svg, render(penguins), StandardCharsets.UTF_8);
        System.out.println("plotted " + penguins.size() + " penguins -> " + svg.toAbsolutePath());
    }

    static List<Penguin> load(Path csv) throws IOException {
        List<String> lines = Files.readAllLines(csv, StandardCharsets.UTF_8);
        if (lines.isEmpty()) {
            return List.of();
        }
        List<String> headers = splitCsv(lines.get(0));
        int species = headers.indexOf("species");
        int island = headers.indexOf("island");
        int sex = headers.indexOf("sex");
        int flipper = headers.indexOf("flipper_length_mm");
        int mass = headers.indexOf("body_mass_g");
        int bill = headers.indexOf("bill_length_mm");
        List<Penguin> penguins = new ArrayList<>();
        for (int i = 1; i < lines.size(); i++) {
            if (lines.get(i).isBlank()) {
                continue;
            }
            List<String> cells = splitCsv(lines.get(i));
            Double flipperValue = number(cells, flipper);
            Double massValue = number(cells, mass);
            Double billValue = number(cells, bill);
            if (flipperValue == null || massValue == null || billValue == null) {
                continue;
            }
            String sexValue = cell(cells, sex);
            if (sexValue.isEmpty() || sexValue.equals("NA")) {
                sexValue = "unknown";
            }
            penguins.add(new Penguin(
                    cell(cells, species),
                    cell(cells, island),
                    sexValue,
                    flipperValue,
                    massValue,
                    billValue));
        }
        return penguins;
    }

    static String render(List<Penguin> penguins) {
        int innerW = WIDTH - LEFT - RIGHT;
        int innerH = HEIGHT - TOP - BOTTOM;
        double billMin = penguins.stream().mapToDouble(Penguin::bill).min().orElse(32);
        double billMax = penguins.stream().mapToDouble(Penguin::bill).max().orElse(60);
        StringBuilder out = new StringBuilder();
        out.append("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n");
        out.append(String.format(Locale.US,
                "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"%d\" height=\"%d\" viewBox=\"0 0 %d %d\">\n",
                WIDTH, HEIGHT, WIDTH, HEIGHT));
        out.append("""
                <style>
                  text { font-family: "Segoe UI", Helvetica, Arial, sans-serif; fill: #222; }
                  .grid { stroke: #ececec; stroke-width: 1; }
                  .axis { stroke: #888; stroke-width: 1; }
                  .tick { stroke: #888; stroke-width: 1; }
                  circle.pt { stroke: transparent; stroke-width: 1.5; }
                  circle.pt:hover { stroke: #222; }
                </style>
                """);
        out.append("<rect width=\"100%\" height=\"100%\" fill=\"#fff\"/>\n");
        out.append("<text x=\"" + LEFT + "\" y=\"28\" font-size=\"16\" font-weight=\"600\">"
                + "Flipper length and body mass of Palmer penguins</text>\n");

        for (int mass = 3000; mass <= 6000; mass += 500) {
            double y = y(mass, innerH);
            out.append(line(LEFT, y, LEFT + innerW, y, "grid"));
            out.append(line(LEFT, y, LEFT - 6, y, "tick"));
            out.append(label(LEFT - 10, y + 4, "end", 12, String.format(Locale.US, "%,d", mass)));
        }
        for (int flipper = 170; flipper <= 230; flipper += 10) {
            double x = x(flipper, innerW);
            out.append(line(x, TOP, x, TOP + innerH, "grid"));
            out.append(line(x, TOP + innerH, x, TOP + innerH + 6, "tick"));
            out.append(label(x, TOP + innerH + 22, "middle", 12, Integer.toString(flipper)));
        }
        out.append(line(LEFT, TOP, LEFT, TOP + innerH, "axis"));
        out.append(line(LEFT, TOP + innerH, LEFT + innerW, TOP + innerH, "axis"));
        out.append(String.format(Locale.US,
                "<text text-anchor=\"middle\" font-size=\"13\" transform=\"translate(18, %.1f) rotate(-90)\">Body Mass (g)</text>\n",
                TOP + innerH / 2.0));
        out.append(label(LEFT + innerW / 2.0, HEIGHT - 12, "middle", 13, "Flipper Length (mm)"));

        for (Penguin penguin : penguins) {
            double radius = radius(penguin.bill, billMin, billMax);
            String title = penguin.species + " · " + penguin.island + " · " + penguin.sex + " · flipper " + format(penguin.flipper, 0) + " mm" + " · mass " + format(penguin.mass, 0) + " g" + " · bill " + format(penguin.bill, 1) + " mm";
            out.append(String.format(Locale.US,
                    "<circle class=\"pt\" cx=\"%.2f\" cy=\"%.2f\" r=\"%.2f\" fill=\"%s\" fill-opacity=\"0.8\"><title>%s</title></circle>\n",
                    x(penguin.flipper, innerW),
                    y(penguin.mass, innerH),
                    radius,
                    COLORS.getOrDefault(penguin.species, "#999"),
                    escape(title)));
        }

        double legendY = TOP + 12;
        for (String species : SPECIES) {
            out.append(String.format(Locale.US,
                    "<circle cx=\"%d\" cy=\"%.1f\" r=\"6\" fill=\"%s\" fill-opacity=\"0.8\"/>\n",
                    LEFT + innerW + 28, legendY, COLORS.get(species)));
            out.append(label(LEFT + innerW + 42, legendY + 4, "start", 13, species));
            legendY += 26;
        }
        out.append("</svg>\n");
        return out.toString();
    }

    static double x(double flipper, int innerW) {
        return LEFT + (flipper - 165.0) / (235.0 - 165.0) * innerW;
    }

    static double y(double mass, int innerH) {
        return TOP + (6500.0 - mass) / (6500.0 - 2500.0) * innerH;
    }

    static double radius(double bill, double billMin, double billMax) {
        double t = billMax == billMin ? 0.5 : (bill - billMin) / (billMax - billMin);
        return 4 + t * 10;
    }

    static String line(double x1, double y1, double x2, double y2, String css) {
        return String.format(Locale.US,
                "<line x1=\"%.2f\" y1=\"%.2f\" x2=\"%.2f\" y2=\"%.2f\" class=\"%s\"/>\n",
                x1, y1, x2, y2, css);
    }

    static String label(double x, double y, String anchor, int size, String text) {
        return String.format(Locale.US,
                "<text x=\"%.2f\" y=\"%.2f\" text-anchor=\"%s\" font-size=\"%d\">%s</text>\n",
                x, y, anchor, size, escape(text));
    }

    static String format(double value, int digits) {
        return String.format(Locale.US, digits == 0 ? "%.0f" : "%.1f", value);
    }

    static String cell(List<String> cells, int index) {
        return index >= 0 && index < cells.size() ? cells.get(index) : "";
    }

    static Double number(List<String> cells, int index) {
        try {
            return Double.valueOf(cell(cells, index));
        } catch (NumberFormatException ex) {
            return null;
        }
    }

    static List<String> splitCsv(String line) {
        List<String> cells = new ArrayList<>();
        StringBuilder current = new StringBuilder();
        boolean quoted = false;
        for (int i = 0; i < line.length(); i++) {
            char c = line.charAt(i);
            if (quoted) {
                if (c == '"') {
                    if (i + 1 < line.length() && line.charAt(i + 1) == '"') {
                        current.append('"');
                        i++;
                    } else {
                        quoted = false;
                    }
                } else {
                    current.append(c);
                }
            } else if (c == '"') {
                quoted = true;
            } else if (c == ',') {
                cells.add(current.toString());
                current.setLength(0);
            } else {
                current.append(c);
            }
        }
        cells.add(current.toString());
        return cells;
    }

    static String escape(String text) {
        return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;");
    }
}
