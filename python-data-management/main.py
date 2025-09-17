import os
import pandas as pd
import matplotlib.pyplot as plt
import requests
from io import StringIO

# ---------- Utility ----------
def ensure_folder(path: str) -> str:
    """Check if a folder exists, create it if not."""
    os.makedirs(path, exist_ok=True)
    return path

# ---------- Setup ----------
data_folder = ensure_folder("./data")
results_folder = ensure_folder("./result")

# ---------- Fetch Data ----------
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
response = requests.get(url)

if response.status_code == 200:
    data = StringIO(response.text)
    df = pd.read_csv(data)
    data_path = os.path.join(data_folder, "iris.csv")
    df.to_csv(data_path, index=False)
    print(f"Data saved to {data_path}")
else:
    raise RuntimeError("Failed to fetch data from GitHub")

# ---------- Analysis ----------
plt.figure(figsize=(8, 6))
plt.scatter(df['sepal_length'], df['sepal_width'], c=pd.Categorical(df['species']).codes)

plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Iris Sepal Dimensions by Species')

fig_path = os.path.join(results_folder, "iris_sepal_scatter.png")
plt.savefig(fig_path)
plt.show()
print(f"Figure saved to {fig_path}")

# ---------- Results ----------
summary = df.groupby('species').mean()
summary_path = os.path.join(results_folder, "iris_summary.csv")
summary.to_csv(summary_path)
print(f"Summary saved to {summary_path}")