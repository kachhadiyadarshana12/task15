import pandas as pd 
try:
    df = pd.read_csv("sample_data.csv")
    print("Data set loaded successfully!\n")
except FileNotFoundError:
    print("sample_data.csv file not found.")
    exit()

print("\nFrist 5 Rows:\n")
print(df.head())

print("\nDataset Info:\n")
print(df.info())

print("\n Statistical Summary:\n")
print(df.describe())

print("\n Missing Values:\n")
print(df.isnull())

df.fillna(df.mean(numeric_only=True), inplace=True)
print("\nMissing values handled.\n")

if "salary" in df.columns:
    filtered_df = df[df["Salary"] > 50000]
    print("Filtered data (salary > 50000): \n")
    print(filtered_df)

    sorted_df = df.sort_values(by="salary", ascending=False)
    print("\nTop 5 highest salaries:\n")
    print(sorted_df.head())

else:
    print("Salary column not found. Skipping filter & sort.")

if "salart" in df.columns:
    df["Bonus"] = df["salary"] * 0.10
    df["Total_Compensation"] = df["Salary"] + df["Bonus"]
    print("\nNew Columns Addes (bonus & total compensation):\n")
    print(df.head())
else:
    print("Salary column missing. cannotadd new columns.")

df.to_csv("cleaned_data.csv", index=False)
print("\nCleaned data explored to cleaned_data.csv")

print("\nINSIGHTS:")
if "salary" in df.columns:
    print(f"Average Salary: {df['salary'].mean():.2f}")
    print(f"maximum Salary: {df['salary'].max()}")
    print(f"Minimu  Salary: {df['salary'].min()}")

if "Department" in df.columns and "salary" in df.columns:
    highest_dept = df.groupby("Department")["salary"].mean().idxmax()
    print(f"\n- department with highest avg salary : {highest_dept}")

print("\nData analysis complated successfully!!")