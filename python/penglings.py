from matplotlib.patches import Patch
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_csv(Path(__file__).parent.parent / 'penglings.csv')

plt.scatter(df['flipper_length_mm'],
            df['body_mass_g'],
            s=(df['bill_length_mm']**3) / 1000,
            c=df['species'].astype('category').cat.codes,
            alpha=0.7)
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')
plt.title('Penglings')
plt.show()