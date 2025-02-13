from pathlib import Path
import pandas as pd

# Get the current working directory (i.e., the folder where this script is placed)
project_dir = Path.cwd()  # This ensures no extra nesting

# Define subdirectories
data_dir = project_dir / "data"
scripts_dir = project_dir / "scripts"
notebooks_dir = project_dir / "notebooks"

# Create directories
for directory in [data_dir, scripts_dir, notebooks_dir]:
    directory.mkdir(parents=True, exist_ok=True)

print("✅ Project folder structure created successfully in:", project_dir)

# Define the CSV file path
csv_file_path = data_dir / "movies.csv"

# Create dataset
data = {
    "Movie": ["Inception", "Titanic", "The Dark Knight", "Interstellar", "The Godfather",
              "Pulp Fiction", "The Shawshank Redemption", "The Matrix", "Forrest Gump",
              "Gladiator", "Avatar", "Avengers: Endgame", "Joker", "Parasite", "The Lion King"],
    "Genre": ["Sci-Fi", "Romance", "Action", "Sci-Fi", "Crime",
              "Crime", "Drama", "Sci-Fi", "Drama",
              "Action", "Sci-Fi", "Action", "Crime", "Thriller", "Animation"],
    "Rating": [8.8, 7.8, 9.0, 8.6, 9.2,
               8.9, 9.3, 8.7, 8.8,
               8.5, 7.9, 8.4, 8.4, 8.6, 8.5],
    "Votes": [2000000, 2200000, 2500000, 1800000, 1600000,
              1800000, 2500000, 1700000, 2000000,
              1500000, 2300000, 2100000, 1800000, 1400000, 1000000],
    "Release_Year": [2010, 1997, 2008, 2014, 1972,
                     1994, 1994, 1999, 1994,
                     2000, 2009, 2019, 2019, 2019, 1994]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save as CSV using pathlib
df.to_csv(csv_file_path, index=False)
print(f"✅ Dataset saved at: {csv_file_path}")
