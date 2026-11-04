# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "altair>=6.3.0",
#     "pandas>=3.1.0",
# ]
# ///
import http.server
import os
import socketserver

import altair as alt
import pandas as pd

HOST = "localhost"
PORT = 8080

def serve_html(html: string):
    class ChartRequestHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200, 'OK')
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(bytes(html, encoding="utf-8"))

    socketserver.BaseServer.allow_reuse_address = True

    try:
        with socketserver.TCPServer((HOST, PORT), ChartRequestHandler) as httpd:
            print(f"Serving altair chart at http://{HOST}:{PORT}")
            print("Press Ctrl-C to stop the server")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped and socket unbound.")

def main() -> None:
    csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "penglings.csv")

    if not (os.path.exists(csv_path) and os.path.isfile(csv_path)):
        print("penglings.csv cannot be found in the directory above the one containing this script")
        return

    print("loading the following file", "\n", csv_path)
    df = pd.read_csv(csv_path)
    print(df.head())
   
    alt.renderers.enable("browser")
    chart = alt.Chart(df).mark_point().encode(
        x="flipper_length_mm",
        y="body_mass_g",
        color="species",
        size="bill_length_mm",
    )
    serve_html(chart.to_html())

if __name__ == "__main__":
    main()
