from pathlib import Path
import pandas as pd

# Define paths
csv_file_path = Path.cwd() / "data" / "movies.csv"
output_txt_path = Path.cwd() / "data" / "output.txt"
summary_csv_path = Path.cwd() / "data" / "summary.csv"

# Load dataset
df = pd.read_csv(csv_file_path)

# Open a file to save the results
with open(output_txt_path, "w", encoding="utf-8") as f:
    # First 5 rows of data
    f.write("📌 First 5 Rows of Dataset:\n")
    f.write(df.head().to_string() + "\n\n")
    
    # Dataset info
    f.write("📌 Dataset Info:\n")
    f.write(str(df.info()) + "\n\n")  # .info() prints directly, so we'll need an alternative way
    
    # Missing values
    f.write("📌 Missing Values in Dataset:\n")
    f.write(str(df.isnull().sum()) + "\n\n")
    
    # Average movie rating
    average_rating = df["Rating"].mean()
    f.write(f"📌 Average Movie Rating: {average_rating:.2f}\n\n")

    # Most common genre
    most_common_genre = df["Genre"].mode()[0]
    f.write(f"📌 Most Common Genre: {most_common_genre}\n\n")

    # Highest-rated movie
    highest_rated = df[df["Rating"] == df["Rating"].max()]
    f.write("📌 Highest-Rated Movie:\n")
    f.write(highest_rated[["Movie", "Rating"]].to_string() + "\n\n")

    # Movies per decade
    df["Decade"] = (df["Release_Year"] // 10) * 10
    f.write("📌 Movies Released Per Decade:\n")
    f.write(df["Decade"].value_counts().to_string() + "\n\n")

print(f"✅ Analysis saved to: {output_txt_path}")

# Save key stats to a summary CSV file
summary_data = {
    "Metric": ["Average Rating", "Most Common Genre", "Highest Rated Movie"],
    "Value": [f"{average_rating:.2f}", most_common_genre, highest_rated.iloc[0]["Movie"]]
}

summary_df = pd.DataFrame(summary_data)
summary_df.to_csv(summary_csv_path, index=False)

print(f"✅ Summary saved to: {summary_csv_path}")
