import pandas as pd                            # For reading and handling Excel data
import numpy as np                             # For numerical operations
from sklearn.linear_model import LinearRegression  # For building the regression model

# Load the movie dataset from the Excel file
movieData = pd.read_excel("HW 6 Data.xlsx")

print("Dataset Preview:")
print(movieData.head(11))  # To ensure that the data is loaded correctly.

# Separate the input (features) and the output (target)
inputFeatures = movieData[['ProductionBudget', 'GenrePopularity', 'CastStarPower']]

# This is the value we want to predict (Box Office Revenue)
targetRevenue = movieData['BoxOfficeRevenue']

# Create a linear regression model and train it using the data
regressionModel = LinearRegression()
regressionModel.fit(inputFeatures, targetRevenue)  # The model learns the relationship between inputs and revenue

# The model now has a formula: Revenue = Intercept + (coefficients * features) and Print out what the model has learned
print("\nModel Summary:")
print(f"Intercept: {regressionModel.intercept_:.2f}")  # This is the base value of the revenue
for feature, coef in zip(inputFeatures.columns, regressionModel.coef_):
    print(f"Coefficient for {feature}: {coef:.2f}")  # Tells how much each feature influences the prediction

# Use the model to make a prediction
# ProductionBudget = $120M, GenrePopularity = 8, CastStarPower = 6
newMovieData = pd.DataFrame([[120, 8, 6]], columns=['ProductionBudget', 'GenrePopularity', 'CastStarPower'])

# Use the model to predict the revenue for the new movie
predictedRevenue = regressionModel.predict(newMovieData)[0]

# Show the predicted revenue
print(f"\nPredicted Box Office Revenue for input [120, 8, 6]: ${predictedRevenue:.2f} million")
