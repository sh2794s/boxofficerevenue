# 🎬 Movie Revenue Prediction using Linear Regression

This project builds a simple multiple linear regression model using Python to predict the **Box Office Revenue** of a movie based on three main features:
- 📊 Production Budget
- 🎭 Genre Popularity
- 🌟 Cast Star Power

---

## 📂 Files Included

- `MovieRevenue.py` – Python script that reads the dataset, builds the regression model, prints summary statistics, and predicts revenue for a sample input.
- `HW 6 Data.xlsx` – Excel dataset (not included here; expected to be in the same folder as the `.py` file).
- `HW6_Report.pdf` – Final academic report written in LaTeX format.
- `HW6_Code.txt` – Plain text version of the code for submission (if required).

---

## 📌 How It Works

1. **Load Data**  
   Reads movie data from an Excel file.

2. **Train Model**  
   Trains a Linear Regression model using:
   - `ProductionBudget`
   - `GenrePopularity`
   - `CastStarPower`

3. **Model Summary Output**
   - Displays intercept and feature coefficients.

4. **Make Prediction**
   - Predicts box office revenue for a new movie with:
     - Production Budget = \$120 million
     - Genre Popularity = 8
     - Cast Star Power = 6

---

## 📈 Sample Output

```bash
Dataset Preview:
   BoxOfficeRevenue  ProductionBudget  GenrePopularity  CastStarPower
0               500               100                8              9
...

Model Summary:
Intercept: -103.86
Coefficient for ProductionBudget: 3.60
Coefficient for GenrePopularity: 9.80
Coefficient for CastStarPower: 13.56

Predicted Box Office Revenue for input [120, 8, 6]: $487.90 million
