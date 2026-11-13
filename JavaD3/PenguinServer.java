import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpServer;

/**
 * A test static web server for the D3 visualization
 *
 * Also converts ../penglings.csv into /data.json on the fly so browser
 * doesnt deal with the NA values in the raw file
 * Keeping the data loading on the Java side also avoids file:// 
 * CORS problems with d3.json()
 */
public class PenguinServer {

    private static Path root;

    public static void main(String[] args) throws IOException {
        int port = args.length > 0 ? Integer.parseInt(args[0]) : 8000;

        root = locateProjectRoot();
        Path csv = root.getParent().resolve("penglings.csv");
        if (!Files.isRegularFile(csv)) {
            throw new IOException("Could not find penglings.csv next to " + root.getParent()
                    + ". Run this from the repository root or the JavaD3 folder.");
        }

        String json = buildJson(csv);
        // Keep a static copy next to index.html so GitHub Pages can serve
        // chart without running Java
        Files.writeString(root.resolve("data.json"), json, StandardCharsets.UTF_8);
        System.out.println("Loaded " + (json.split("\\{", -1).length - 1)
                + " complete penguin observations from " + csv);

        HttpServer server = HttpServer.create(new InetSocketAddress(port), 0);
        server.createContext("/data.json", exchange ->
                send(exchange, json.getBytes(StandardCharsets.UTF_8), "application/json"));
        server.createContext("/", PenguinServer::serveStatic);
        server.setExecutor(null);
        server.start();
        System.out.println("Serving http://localhost:" + port + "  (Ctrl+C to stop)");
    }

    /**
     * Finds JavaD3 folder containing index.html
     */
    private static Path locateProjectRoot() throws IOException {
        Path cwd = Paths.get("").toAbsolutePath().normalize();

        if (Files.isRegularFile(cwd.resolve("JavaD3").resolve("index.html"))) {
            return cwd.resolve("JavaD3");
        }
        if (Files.isRegularFile(cwd.resolve("index.html"))) {
            return cwd;
        }

        for (Path dir = cwd; dir != null; dir = dir.getParent()) {
            if (Files.isRegularFile(dir.resolve("JavaD3").resolve("index.html"))) {
                return dir.resolve("JavaD3");
            }
            if (Files.isRegularFile(dir.resolve("index.html"))) {
                return dir;
            }
        }

        throw new IOException("Could not find JavaD3/index.html. Run this from the "
                + "repository root or the JavaD3 folder.");
    }

    private static void serveStatic(HttpExchange exchange) throws IOException {
        String requested = exchange.getRequestURI().getPath();
        if (requested.equals("/")) {
            requested = "/index.html";
        }

        Path file = root.resolve(requested.substring(1)).normalize();
        if (!file.startsWith(root) || !Files.isRegularFile(file)) {
            send(exchange, "Not found".getBytes(StandardCharsets.UTF_8), "text/plain", 404);
            return;
        }

        send(exchange, Files.readAllBytes(file), contentType(file.toString()));
    }

    private static void send(HttpExchange exchange, byte[] body, String type) throws IOException {
        send(exchange, body, type, 200);
    }

    private static void send(HttpExchange exchange, byte[] body, String type, int status)
            throws IOException {
        exchange.getResponseHeaders().set("Content-Type", type);
        exchange.getResponseHeaders().set("Cache-Control", "no-store");
        exchange.sendResponseHeaders(status, body.length);
        try (OutputStream out = exchange.getResponseBody()) {
            out.write(body);
        }
    }

    private static String contentType(String name) {
        if (name.endsWith(".html")) return "text/html; charset=utf-8";
        if (name.endsWith(".js")) return "text/javascript; charset=utf-8";
        if (name.endsWith(".css")) return "text/css; charset=utf-8";
        if (name.endsWith(".json")) return "application/json; charset=utf-8";
        if (name.endsWith(".png")) return "image/png";
        if (name.endsWith(".svg")) return "image/svg+xml";
        return "application/octet-stream";
    }

    /**
    * Reads CSV and emits only rows that have every value
    */
    private static String buildJson(Path csvPath) throws IOException {
        List<String> lines = Files.readAllLines(csvPath, StandardCharsets.UTF_8);
        StringBuilder json = new StringBuilder("[");
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

            // Skip rows with missing measurements
            if (isMissing(bill) || isMissing(flipper) || isMissing(mass)) continue;

            if (!first) json.append(",");
            first = false;
            json.append("{\"species\":\"").append(escape(species))
                .append("\",\"island\":\"").append(escape(island))
                .append("\",\"bill_length_mm\":").append(bill)
                .append(",\"flipper_length_mm\":").append(flipper)
                .append(",\"body_mass_g\":").append(mass)
                .append(",\"sex\":\"").append(escape(sex))
                .append("\"}");
        }
        return json.append("]").toString();
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

    /**
    * Minimal CSV parser that understands quoted fields and doubled quotes
    */
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
