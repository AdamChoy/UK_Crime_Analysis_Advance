import pandas as pd

# ── Read the correct sheet from the Excel file ────────────────────────────────
# Sheet: 'Mid-2024 LSOA 2021'
# Header is on row 4 (0-indexed: row 3) -- rows 1-3 are title/description text
pop = pd.read_excel(
    "sapelsoabroadage20222024.xlsx",
    sheet_name="Mid-2024 LSOA 2021",
    header=3,          # row 4 in Excel is index 3 in pandas
    thousands=","      # handles comma-formatted numbers e.g. 1,925 -> 1925
)

# ── Retain only the two required columns ─────────────────────────────────────
pop = pop[["LSOA 2021 Code", "Total"]]

# ── Rename for consistency with the pipeline naming convention ────────────────
pop.columns = ["lsoa_code", "population"]

# ── Drop any rows where lsoa_code is null (e.g. footer rows in the sheet) ────
pop = pop.dropna(subset=["lsoa_code"])

# ── Confirm output ────────────────────────────────────────────────────────────
print(f"Rows extracted : {len(pop):,}")
print(f"Null check     : {pop.isnull().sum().to_dict()}")
print(pop.head())

# ── Export to CSV for upload to Snowflake stage ───────────────────────────────
pop.to_csv("population_clean.csv", index=False)
print("\nSaved: population_clean.csv")
