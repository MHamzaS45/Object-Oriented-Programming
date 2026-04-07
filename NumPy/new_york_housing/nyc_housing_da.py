################################
# New York Housing Data Analysis
# Author: Hamza Sahqani
################################

#################################
# IMPORTING LIBRARIES
#################################

import numpy as np                             # Linear algebra
import pandas as pd                            # Data processing/manipulation, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt                # Embedded in Jupyter Notebook
import seaborn as sns                          # Statistical data visualization
import folium                                  # Interactive maps
from IPython.display import display

sns.set_style('darkgrid')                     # Improved aesthetics for plots


#################################
# DATA LOADING AND PREPROCESSING
#################################

# Load the dataset into a variable called df
df = pd.read_csv('NumPy\\new_york_housing\\NY-House-Dataset.csv')
df = df.sort_values('PRICE')

# Print column names to understand the dataset structure
print(df.columns) 
print(len(df))           # must be large
print(df.head())

# Drop missing values
df = df.dropna(subset=["LATITUDE", "LONGITUDE", "PRICE", "PROPERTYSQFT"])

# Remove invalid entries
df = df[(df["PRICE"] > 0) & (df["PROPERTYSQFT"] > 0)]


# Create a new column for price per square foot (which will be used for visualizations)
df["price_per_sqft"] = df["PRICE"] / df["PROPERTYSQFT"]
df = df[df["price_per_sqft"] < 35000]
print(df[["LATITUDE", "LONGITUDE", "PRICE", "PROPERTYSQFT", "price_per_sqft"]].head())
print("Min Price per Sqft:", df["price_per_sqft"].min())
print("Max Price per Sqft:", df["price_per_sqft"].max())

# Price Bins 
bins = [1.14, 292.55, 416.67, 583.66, 966.38, 27469.91]
df["price_bin"] = pd.cut(df["price_per_sqft"], bins=bins, labels=[0,1,2,3,4])

# Print bin ranges
for i in range(len(bins) - 1):
    print(f"Bin {i}: ${bins[i]:.2f} - ${bins[i+1]:.2f}")

# Display the structure of the dataset and the first 10 rows 
df.info()
df.head(10)


# Check the dimensions (rows, columns) of the dataset
df.shape

# Summarize the dataset using descriptive statistics
df.describe()


#################################
# DATA VISUALISATION 
#################################
fig, axes = plt.subplots(1, 2, figsize=(12,5))

# Longitude plot
sns.scatterplot(                              # Seaborn used to enhance visuals
    x="LONGITUDE",
    y="price_per_sqft",
    hue="price_bin",
    palette="crest",
    data=df,
    alpha=0.6,
    ax=axes[0]
)
axes[0].set_ylim(df["price_per_sqft"].min(), df["price_per_sqft"].max())         # Set a consistent y-axis limit for better comparison
axes[0].set_title("Longitude vs Price per SQFT")

# Latitude plot
sns.scatterplot(
    x="LATITUDE",
    y="price_per_sqft",
    hue="price_bin",
    palette="flag",
    data=df,
    alpha=0.6,
    ax=axes[1]
)
axes[1].set_ylim(df["price_per_sqft"].min(), df["price_per_sqft"].max())
axes[1].set_title("Latitude vs Price per SQFT")

plt.tight_layout()
plt.show()

# Showing relationship between longitude and latitude
sns.scatterplot(x='LONGITUDE', y='LATITUDE', data=df) 
sns.scatterplot(x='LONGITUDE', y='LATITUDE', hue='price_bin', data=df, palette='viridis') # This color is lowkirkeknu
plt.title('Longitude vs Latitude colored by Price')
plt.show()   


##############################################
# INTERACTIVE MAP VISUALIZATION USING FOLIUM
##############################################

# Create a base map centered around New York City
nyc_center = [df["LATITUDE"].mean(), df["LONGITUDE"].mean()]
m = folium.Map(location=nyc_center, zoom_start=10)

# Add markers (limit for performance)
for _, row in df.sample(min(300, len(df))).iterrows():
    folium.CircleMarker(
        location=[row["LATITUDE"], row["LONGITUDE"]],
        radius=4,
        popup=f"${row['PRICE']:.2f}/sqft",
        color="blue",   
        fill=True,
        fill_opacity=0.6
    ).add_to(m)
m

# Save map
m.save("NumPy\\new_york_housing\\images\\nyc_housing_map.html")
print("Map saved as nyc_housing_map.html")