# Datawrapper has no way to filter rows, so this makes a clean copy of the data
# without the NA rows. Upload the output file to Datawrapper.
# Run from the repo root:  python datawrapper/clean.py
import pandas as pd

df = pd.read_csv("penglings.csv").dropna(
    subset=["flipper_length_mm", "body_mass_g", "bill_length_mm"])
df.to_csv("datawrapper/penglings_clean.csv", index=False)
print(f"Saved {len(df)} rows to datawrapper/penglings_clean.csv")
