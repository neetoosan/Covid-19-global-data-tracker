# Covid-19-global-data-tracker
covid 19 Global data tracker

### 🧪 Project Overview

This project performs exploratory data analysis (EDA) on a global COVID-19 dataset. It includes data loading, cleaning, visualization, and insights generation using Python libraries like pandas, matplotlib, seaborn, and plotly.

The goal is to:
- Understand trends in confirmed cases, deaths, and vaccinations.
- Compare country-level performance.
- Visualize global case distribution using interactive maps.
- Extract meaningful insights from real-world pandemic data.

---

### 📁 Project Structure

covid_analysis/
├── owid-covid-data.csv            # Raw dataset (source: e.g., Our World in Data)
├── analysis.py        # Main script for data analysis and visualization
├── README.md                 # This file
---

### 📥 Dataset Source

This project uses an open-source dataset typically sourced from [Our World in Data](https://ourworldindata.org/coronavirus) or similar repositories. The dataset contains daily records of:

| Column              | Description                          |
|---------------------|--------------------------------------|
| date              | Date of observation                  |
| location          | Country name                         |
| total_cases       | Cumulative confirmed cases           |
| new_cases         | Daily new cases                      |
| total_deaths      | Cumulative confirmed deaths          |
| new_deaths        | Daily new deaths                     |
| total_vaccinations| Cumulative number of vaccinations    |
| population        | Population of the country            |
| iso_code          | ISO 3-letter country code            |

> Note: You can replace covid_data.csv with any compatible CSV file containing these or similar columns.

---

### 🛠️ Requirements

To run this project, ensure you have the following Python libraries installed:

pip install pandas matplotlib seaborn plotly
Optional (for saving figures):
pip install pillow  # For image handling
---

### ▶️ How to Run

1. Clone or download the project directory.
2. Place your owid-covid-data.csv file in the root folder.
3. Run the analysis script:
  
   python analysis.py
   
4. Interactive visualizations will appear in your browser (for Plotly), and static plots will be shown inline or saved if configured.

---

### 📊 Features

- Filters data for specific countries (Kenya, USA, India, Brazil, Germany).
- Computes derived metrics like death rate and vaccination coverage.
- Generates line charts for time-series trends.
- Displays bar charts comparing countries.
- Produces an optional choropleth world map showing total cases per country.

---

### 💡 Key Insights Generated

At the end of the analysis, the script prints out:
- Fastest average vaccination rollout by country.
- Highest death rate observed.
- Country with the most confirmed cases.

---

### 📤 Exporting Results

You can modify the script to export visualizations as image files (e.g., PNG, PDF) or generate HTML reports using tools like Jupyter Notebook or plotly.offline.

---

### 🤝 Contributing

Contributions are welcome! If you'd like to improve this project, feel free to:
- Add support for more advanced statistical analysis.
- Include regression models or forecasting.
- Improve visualization aesthetics or interactivity.

---

### 📬 Contact

If you have questions, suggestions, or want to collaborate:
- Email: tobimolla44@gmail.com
- GitHub: [github.com/neetoosan](https://github.com/neetoosan)

---

Made with ❤️ by [neetoosan]

---

Our World in Data (https://ourworldindata.org/coronavirus)
COVID-19 Pandemic
The COVID-19 pandemic has had a profound impact on the world. Explore global data and research to understand its impact, spread, and global response.
