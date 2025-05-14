import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# -----------------------------
# 1️⃣ Load the Dataset
# -----------------------------
print("Loading data...")
df = pd.read_csv('owid-covid-data.csv')

# Optional: Display first few rows
print("\nFirst 5 rows:")
print(df.head())

# Check basic info and missing values
print("\nData Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# 2️⃣ Data Cleaning
# -----------------------------
print("\nCleaning data...")

# Convert date column to datetime
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])

# Filter for specific countries (e.g., Kenya, USA, India)
countries_of_interest = ['Kenya', 'United States', 'India', 'Brazil', 'Germany']
filtered_df = df[df['location'].isin(countries_of_interest)]

# Drop rows where key columns are missing
key_columns = ['total_cases', 'total_deaths', 'new_cases', 'new_deaths']
filtered_df = filtered_df.dropna(subset=key_columns)

# Fill missing numeric values with 0 or interpolate
numeric_cols = filtered_df.select_dtypes(include='number').columns
filtered_df[numeric_cols] = filtered_df[numeric_cols].fillna(0)

# -----------------------------
# 3️⃣ Add New Metrics
# -----------------------------
print("\nAdding derived metrics...")

# Death rate = total deaths / total cases
filtered_df['death_rate'] = filtered_df['total_deaths'] / filtered_df['total_cases']
filtered_df['death_rate'] = filtered_df['death_rate'].fillna(0)

# Vaccination coverage
if 'total_vaccinations' in filtered_df.columns and 'population' in filtered_df.columns:
    filtered_df['vaccination_rate'] = filtered_df['total_vaccinations'] / filtered_df['population']
    filtered_df['vaccination_rate'] = filtered_df['vaccination_rate'].fillna(0)

# -----------------------------
# 4️⃣ Exploratory Data Analysis (EDA)
# -----------------------------
print("\nGenerating visualizations...")

# Plot Total Cases Over Time by Country
plt.figure(figsize=(12,6))
sns.lineplot(data=filtered_df, x='date', y='total_cases', hue='location', marker='')
plt.title('Total Confirmed COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend(title='Country')
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot Total Deaths Over Time
plt.figure(figsize=(12,6))
sns.lineplot(data=filtered_df, x='date', y='total_deaths', hue='location', marker='')
plt.title('Total Confirmed COVID-19 Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend(title='Country')
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar Chart: Top Countries by Total Cases (latest date only)
latest_df = filtered_df[filtered_df['date'] == filtered_df['date'].max()]
plt.figure(figsize=(10,6))
sns.barplot(data=latest_df, x='location', y='total_cases', palette='viridis')
plt.title(f'Total Cases by Country on {latest_df["date"].iloc[0]}')
plt.xlabel('Country')
plt.ylabel('Total Cases')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# -----------------------------
# 5️⃣ Vaccination Progress
# -----------------------------
if 'total_vaccinations' in filtered_df.columns:
    plt.figure(figsize=(12,6))
    sns.lineplot(data=filtered_df, x='date', y='total_vaccinations', hue='location', marker='')
    plt.title('Cumulative Vaccinations Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Vaccinations')
    plt.legend(title='Country')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# -----------------------------
# 6️⃣ Optional: Choropleth Map (World View)
# -----------------------------
try:
    # Group by country and take latest total cases
    map_df = df.groupby('iso_code')['total_cases'].last().reset_index()
    fig = px.choropleth(
        map_df,
        locations='iso_code',
        locationmode='ISO-3',
        color='total_cases',
        color_continuous_scale='Reds',
        title='Global Total Confirmed Cases (Latest)',
        labels={'total_cases': 'Total Cases'}
    )
    fig.show()
except Exception as e:
    print("⚠️ Could not generate choropleth map:", str(e))

# -----------------------------
# 7️⃣ Generate Insights
# -----------------------------
print("\n📈 Key Insights:")

# Insight 1: Fastest Vaccine Rollout
if 'total_vaccinations' in filtered_df.columns:
    latest_vax = filtered_df.pivot(index='date', columns='location', values='total_vaccinations').diff().mean()
    fastest_vax_country = latest_vax.idxmax()
    print(f"- {fastest_vax_country} had the fastest average daily vaccination rollout.")

# Insight 2: Highest Death Rate
highest_death_rate_row = filtered_df[filtered_df['date'] == filtered_df['date'].max()].sort_values(by='death_rate', ascending=False).iloc[0]
print(f"- On {highest_death_rate_row['date'].date()}, {highest_death_rate_row['location']} had the highest death rate at {highest_death_rate_row['death_rate'] * 100:.2f}%.")

# Insight 3: Most Cases
most_cases_row = latest_df.sort_values(by='total_cases', ascending=False).iloc[0]
print(f"- On {most_cases_row['date'].date()}, {most_cases_row['location']} had the most confirmed cases: {most_cases_row['total_cases']:,}.")