import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

/**
 * Converts ../penglings.csv into data.json for the p5.js sketch
 *
 *     javac PrepareData.java
 *     java PrepareData
 *     python3 -m http.server 8001
 *     # open http://localhost:8001
 */
public class PrepareData {

    public static void main(String[] args) throws IOException {
        Path here = locateHere();
        Path csv = here.getParent().resolve("penglings.csv");
        Path out = here.resolve("data.json");

        if (!Files.isRegularFile(csv)) {
            throw new IOException("Could not find penglings.csv next to " + here.getParent()
                    + ". Run this from the repository root or the JavaP5JS folder.");
        }

        List<String> lines = Files.readAllLines(csv, StandardCharsets.UTF_8);
        StringBuilder json = new StringBuilder("[");
        int kept = 0;
        boolean first = true;

        for (int i = 1; i < lines.size(); i++) {
            List<String> row = parseCsvLine(lines.get(i));
            if (row.size() < 9) continue;

            String species = row.get(1);
            String island = row.get(2);
            String bill = row.get(3);
            String flipper = row.get(5);
            String mass = row.get(6);
            String sex = row.get(7);

            if (isMissing(bill) || isMissing(flipper) || isMissing(mass)) continue;

            if (!first) json.append(",\n  ");
            first = false;
            kept++;
            json.append("{\"species\":\"").append(escape(species))
                .append("\",\"island\":\"").append(escape(island))
                .append("\",\"bill_length_mm\":").append(bill)
                .append(",\"flipper_length_mm\":").append(flipper)
                .append(",\"body_mass_g\":").append(mass)
                .append(",\"sex\":\"").append(escape(sex))
                .append("\"}");
        }
        json.append("\n]");

        Files.writeString(out, json.toString(), StandardCharsets.UTF_8);
        System.out.println("Wrote " + kept + " complete observations to " + out);
    }

    /**
     * Finds JavaP5JS folder containing sketch.js
     */
    private static Path locateHere() throws IOException {
        Path cwd = Paths.get("").toAbsolutePath().normalize();

        if (Files.isRegularFile(cwd.resolve("sketch.js"))) {
            return cwd;
        }
        if (Files.isRegularFile(cwd.resolve("JavaP5JS").resolve("sketch.js"))) {
            return cwd.resolve("JavaP5JS");
        }

        for (Path dir = cwd; dir != null; dir = dir.getParent()) {
            if (Files.isRegularFile(dir.resolve("JavaP5JS").resolve("sketch.js"))) {
                return dir.resolve("JavaP5JS");
            }
            if (Files.isRegularFile(dir.resolve("sketch.js"))) {
                return dir;
            }
        }

        throw new IOException("Could not find JavaP5JS/sketch.js. Run this from the "
                + "repository root or the JavaP5JS folder.");
    }

    private static boolean isMissing(String value) {
        return value == null || value.isEmpty() || value.equalsIgnoreCase("NA");
    }

    private static String escape(String value) {
        return value.replace("\\", "\\\\")
                .replace("\"", "\\\"")
                .replace("\r", "\\r")
                .replace("\n", "\\n");
    }

    private static List<String> parseCsvLine(String line) {
        List<String> fields = new ArrayList<>();
        StringBuilder field = new StringBuilder();
        boolean quoted = false;

        for (int i = 0; i < line.length(); i++) {
            char c = line.charAt(i);
            if (quoted) {
                if (c == '"') {
                    if (i + 1 < line.length() && line.charAt(i + 1) == '"') {
                        field.append('"');
                        i++;
                    } else {
                        quoted = false;
                    }
                } else {
                    field.append(c);
                }
            } else if (c == '"') {
                quoted = true;
            } else if (c == ',') {
                fields.add(field.toString());
                field.setLength(0);
            } else {
                field.append(c);
            }
        }
        fields.add(field.toString());
        return fields;
    }
}
