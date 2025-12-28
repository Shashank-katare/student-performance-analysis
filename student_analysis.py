import pandas as pd


df = pd.read_csv("students.csv")

print("\nOriginal Data:")
print(df)


df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3

print("\nAfter Calculating Total & Average:")
print(df)


df_sorted = df.sort_values(by="Total", ascending=False)

print("\nSorted by Performance (Top to Bottom):")
print(df_sorted)


topper = df_sorted.head(1)
weakest = df_sorted.tail(1)

print("\nTopper:")
print(topper)

print("\nWeakest Student:")
print(weakest)

df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 40 else "Fail")

print("\nFinal Result:")
print(df)
# Save final result
df.to_csv("final_student_result.csv", index=False)

print("\nFinal result saved as final_student_result.csv")
