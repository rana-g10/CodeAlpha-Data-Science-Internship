
# CodeAlpha Internship
# Task 2: Unemployment Analysis with Python

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------
# 1. Load the Dataset
# ----------------------------------

df = pd.read_csv("Unemployment in India.csv")

print("Original Dataset Shape:")
print(df.shape)

# ----------------------------------
# 2. Clean Column Names
# ----------------------------------

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Remove extra spaces from text values
for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].str.strip()

print("\nCleaned Column Names:")
print(df.columns)

# ----------------------------------
# 3. Handle Missing Values
# ----------------------------------

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Remove rows containing missing values
df = df.dropna()

print("\nDataset Shape After Cleaning:")
print(df.shape)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# ----------------------------------
# 4. Convert Date Column
# ----------------------------------

df["Date"] = pd.to_datetime(
    df["Date"],
    dayfirst=True,
    errors="coerce"
)

# Remove rows where date conversion failed
df = df.dropna(subset=["Date"])

# Sort data by date
df = df.sort_values("Date")

# ----------------------------------
# 5. Display Cleaned Dataset
# ----------------------------------

print("\nFirst 5 Rows After Cleaning:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

# Monthly Unemployment Rate Trend

monthly_unemployment = df.groupby("Date")[
    "Estimated Unemployment Rate (%)"
].mean()

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_unemployment.index,
    monthly_unemployment.values,
    marker="o"
)

plt.title("Unemployment Rate in India Over Time")
plt.xlabel("Date")
plt.ylabel("Average Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.savefig("unemployment_trend.png")
plt.show()

# Average Unemployment Rate by Region

region_unemployment = df.groupby("Region")[
    "Estimated Unemployment Rate (%)"
].mean()

region_unemployment = region_unemployment.sort_values(ascending=False)

plt.figure(figsize=(12, 6))

region_unemployment.plot(kind="bar")

plt.title("Average Unemployment Rate by Region")
plt.xlabel("Region")
plt.ylabel("Average Unemployment Rate (%)")
plt.xticks(rotation=90)
plt.grid(axis="y")

plt.tight_layout()
plt.savefig("unemployment_by_region.png")
plt.show()

# Rural vs Urban Unemployment Rate

area_unemployment = df.groupby("Area")[
    "Estimated Unemployment Rate (%)"
].mean()

plt.figure(figsize=(8, 5))

area_unemployment.plot(kind="bar")

plt.title("Average Unemployment Rate: Rural vs Urban")
plt.xlabel("Area")
plt.ylabel("Average Unemployment Rate (%)")
plt.xticks(rotation=0)
plt.grid(axis="y")

plt.tight_layout()
plt.savefig("rural_vs_urban.png")
plt.show()

print("\nAverage Unemployment Rate by Area:")
print(area_unemployment)

# Key Insights

print("\n========== KEY INSIGHTS ==========")

# Overall average unemployment rate
overall_average = df["Estimated Unemployment Rate (%)"].mean()
print(f"Overall Average Unemployment Rate: {overall_average:.2f}%")

# Region with the highest average unemployment rate
highest_region = region_unemployment.idxmax()
highest_rate = region_unemployment.max()

print(f"Region with Highest Average Unemployment: {highest_region}")
print(f"Average Unemployment Rate: {highest_rate:.2f}%")

# Region with the lowest average unemployment rate
lowest_region = region_unemployment.idxmin()
lowest_rate = region_unemployment.min()

print(f"Region with Lowest Average Unemployment: {lowest_region}")
print(f"Average Unemployment Rate: {lowest_rate:.2f}%")

# Rural vs Urban comparison
highest_area = area_unemployment.idxmax()
highest_area_rate = area_unemployment.max()

print(f"Area with Higher Average Unemployment: {highest_area}")
print(f"Average Unemployment Rate: {highest_area_rate:.2f}%")


# Project Conclusion

print("\n========== PROJECT CONCLUSION ==========")

print(
    "The dataset shows an overall average unemployment rate "
    f"of {overall_average:.2f}%."
)

print(
    f"{highest_region} had the highest regional average "
    f"unemployment rate at {highest_rate:.2f}%."
)

print(
    f"{lowest_region} had the lowest regional average "
    f"unemployment rate at {lowest_rate:.2f}%."
)

print(
    f"The average unemployment rate was higher in {highest_area} "
    f"areas ({highest_area_rate:.2f}%) than in the other area."
)