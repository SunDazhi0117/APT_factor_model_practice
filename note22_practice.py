from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Fixed seed for a reproducible, entirely simulated monthly sample.
rng = np.random.default_rng(22)

n_months = 120

market_excess = rng.normal(
    loc=0.005,
    scale=0.04,
    size=n_months
)

smb = rng.normal(loc=0.002, scale=0.025, size=n_months)
hml = rng.normal(loc=0.003, scale=0.03, size=n_months)

print(market_excess[:5])

# Known coefficients generate the data; OLS must estimate them from X and y.
noise = rng.normal(loc=0, scale=0.03, size=n_months)

stock_excess = (
    0.002
    + 1.2 * market_excess
    + 0.6 * smb
    - 0.4 * hml
    + noise
)

data = pd.DataFrame({
    "Market_Excess": market_excess,
    "SMB": smb,
    "HML": hml,
    "Stock_Excess": stock_excess
})

print(data.head())
print(data.shape)

X = data[["Market_Excess", "SMB", "HML"]]
y = data["Stock_Excess"]

# A constant column lets OLS estimate alpha rather than force it to zero.
X = sm.add_constant(X)

results = sm.OLS(y, X).fit()
print(results.summary())

beta_comparison = pd.DataFrame({
    "True Beta": [1.2, 0.6, -0.4],
    "Estimated Beta": results.params[
        ["Market_Excess", "SMB", "HML"]
    ]
}, index=["Market_Excess", "SMB", "HML"])

beta_comparison.plot.bar(rot=0)
plt.axhline(0, color="black", linewidth=0.8)
plt.ylabel("Factor Beta")
plt.title("True vs Estimated Factor Exposures")
plt.tight_layout()

# Save before showing the figure. Paths are relative to this script.
output_folder = Path(__file__).resolve().parent / "outputs"
output_folder.mkdir(exist_ok=True)
data.to_csv(output_folder / "simulated_data.csv", index=False)
(output_folder / "regression_summary.txt").write_text(
    results.summary().as_text() + "\n", encoding="utf-8"
)
plt.savefig(output_folder / "factor_betas.png", dpi=150)
print(f"Saved data, regression summary and chart to: {output_folder}")
plt.show()
