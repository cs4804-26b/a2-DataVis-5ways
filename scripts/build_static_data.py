"""Write data.json files used by the static GitHub Pages site
"""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV = ROOT / "penglings.csv"
OUTPUTS = [ROOT / "JavaD3" / "data.json", ROOT / "JavaP5JS" / "data.json"]

NUMERIC_FIELDS = ("bill_length_mm", "flipper_length_mm", "body_mass_g")


def number(value: str):
    """Keep whole numbers as integers so the JSON matches the Java output."""
    return float(value) if "." in value else int(value)


def load_records():
    records = []
    with CSV.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if any(
                row.get(field, "").strip() in ("", "NA")
                for field in NUMERIC_FIELDS
            ):
                continue

            records.append(
                {
                    "species": row["species"],
                    "island": row["island"],
                    "bill_length_mm": number(row["bill_length_mm"]),
                    "flipper_length_mm": number(row["flipper_length_mm"]),
                    "body_mass_g": number(row["body_mass_g"]),
                    "sex": row["sex"],
                }
            )
    return records


def main() -> None:
    records = load_records()
    text = json.dumps(records, indent=2) + "\n"

    for output in OUTPUTS:
        output.write_text(text, encoding="utf-8")
        print(f"wrote {output.relative_to(ROOT)} ({len(records)} observations)")


if __name__ == "__main__":
    main()
