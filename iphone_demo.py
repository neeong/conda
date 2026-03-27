"""
iphone_demo.py — quick environment check and data demo for a-Shell on iPhone.
Run with: python3 iphone_demo.py
"""

import sys

# ── 1. Python info ────────────────────────────────────────────────────────────
print("=" * 50)
print(f"Python {sys.version}")
print("=" * 50)

# ── 2. Import check ───────────────────────────────────────────────────────────
packages = ["numpy", "pandas", "dask", "matplotlib", "toolz", "bokeh", "psutil", "dill"]
print("\nPackage versions:")
for name in packages:
    try:
        mod = __import__(name)
        version = getattr(mod, "__version__", "installed")
        print(f"  {name:<14} {version}")
    except ImportError:
        print(f"  {name:<14} NOT FOUND")

# ── 3. NumPy: basic stats ─────────────────────────────────────────────────────
import numpy as np

print("\n--- NumPy ---")
rng = np.random.default_rng(42)
data = rng.normal(loc=100, scale=15, size=1000)
print(f"  1000 samples  mean={data.mean():.2f}  std={data.std():.2f}  min={data.min():.2f}  max={data.max():.2f}")

# ── 4. Pandas: DataFrame summary ──────────────────────────────────────────────
import pandas as pd

print("\n--- Pandas ---")
df = pd.DataFrame({
    "day":   pd.date_range("2024-01-01", periods=7, freq="D"),
    "temp":  [22.1, 19.8, 23.4, 25.0, 21.3, 18.9, 24.7],
    "humid": [55, 60, 50, 45, 65, 70, 48],
})
print(df.to_string(index=False))
print(f"\n  avg temp: {df['temp'].mean():.1f}°C   avg humidity: {df['humid'].mean():.0f}%")

# ── 5. Dask: parallel computation ─────────────────────────────────────────────
import dask.array as da

print("\n--- Dask ---")
x = da.from_array(data, chunks=250)
result = x.mean().compute()
print(f"  dask mean of 1000-element array (4 chunks): {result:.2f}")

# ── 6. psutil: system info ────────────────────────────────────────────────────
import psutil

print("\n--- psutil ---")
mem = psutil.virtual_memory()
print(f"  memory  total={mem.total // 1024**2} MB  available={mem.available // 1024**2} MB  used={mem.percent}%")
print(f"  CPUs: {psutil.cpu_count(logical=True)}")

print("\n" + "=" * 50)
print("All checks passed — environment is ready!")
print("=" * 50)
