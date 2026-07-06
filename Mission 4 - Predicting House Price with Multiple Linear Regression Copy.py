#!/usr/bin/env python
# coding: utf-8

# ## Mission 4 - Predicting House Price with Multiple Linear Regression Copy
# 
# New notebook

# ## Mission 4: Predicting House Price with Multiple Linear Regression
# 
# Introduction
# In this mission, you will be working with a real estate dataset to perform Exploratory Data Analysis (EDA) and create a Multiple Linear Regression (MLR) model to predict the Price of a house based on various features such as Square Feet, Number of Bedrooms, Number of Bathrooms, and other factors.
# 
# The dataset includes the following columns:
# 
# **Square_Feet:** The total area of the house in square feet.
# 
# **Num_Bedrooms:** The number of bedrooms in the house.
# 
# **Num_Bathrooms:** The number of bathrooms in the house.
# 
# **Num_Floors:** The number of floors in the house.
# 
# **Garage_Size:** The size of the garage.
# 
# **Location_Score:** A score representing the desirability of the location.
# 
# **Distance_to_Center:** The distance (in km) to the city center.
# 
# **Price:** The price of the house (target variable).
# 

# ## Creating a Multiple Linear Regression (MLR) Model
# 
# In this step, we will use Multiple Linear Regression to predict the Price of the house based on the features. We will split the data into a training set and a testing set, fit the model, and evaluate its performance.
# 
# Task 3.1: Split the Data into Features and Target
# Split the dataset into features (X) and target variable (y).
# 
# Task 3.2: Split the Data into Training and Testing Sets
# Split the data into training (80%) and testing (20%) sets.
# 
# Task 3.3: Train the Multiple Linear Regression Model
# Train the Multiple Linear Regression (MLR) model using the training data.
# 
# Task 3.4: Visualise the Predicted vs Actual Prices
# Create a scatter plot comparing the actual prices and predicted prices for the test set.
# 
# Task 3.5: Evaluate the Model
# Evaluate the model using Root Mean Squared Error (RMSE) and interpret the results.
# 
# Task 3.6. Write 1–2 sentences explaining the insights from the visualisation.

# In[8]:


# Task 3.1 - Split the Data into Features and Target. Split the dataset into features (X) and target variable (y).

# all columns minus 'Price' (features)
x = df_house_price.drop(columns = 'Price')

# just 'Price' column (Target Variable)
y = df_house_price['Price']

# Task 3.2: Split the Data into Training and Testing Sets Split the data into training (80%) and testing (20%) sets.
from sklearn.model_selection import train_test_split

# splits the data into test data and training data. test_size=0.2 = %20 remmaining %80 is training data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42) 


# In[9]:


# Task 3.3: Train the Multiple Linear Regression (MLR) model using the training data.

# Imports Linear Regression model from Scitkitlearn library
from sklearn.linear_model import LinearRegression

# creates an blank linear regression model
lr = LinearRegression()

# trains the model using the training data
lr.fit(x_train, y_train)

# generates predictions
y_pred_test = lr.predict(x_test)

# Assigns the data a name and ensures when printed the name prints as a list
Actual_Price = list(y_train[:5])
Predicted_Price = list(y_pred_test[:5])

# rounds and prints the value with added comma seperator's and "$" for clarity
print("Actual Price")
print([f"${round(p):,}" for p in Actual_Price]) 
print ("Predicted Price")
print([f"${round(p):,}" for p in Predicted_Price])


# In[10]:


# Task 3.4: Visualise the Predicted vs Actual Prices Create a scatter plot
# comparing the actual prices and predicted prices for the test set.

# allows us to plot the scatterplot graph
import matplotlib.pyplot as plt

# This just aassigns the dimensions of the chart as 8 inches by 6 inches
plt.figure(figsize=(8, 6))

# alpha=0.6 adds a bit of opacity to the plotted marks to make it a bit easier to read
plt.scatter(y_test, y_pred_test, alpha=0.6, color="blue", label="Predictions")

# Draws a line using test data to gague the accuracy of the plotted trained data
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color="red", linestyle="-", label="Perfect Prediction")

# assigns labels and titles to the x and y axis.
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Predicting House Price with Multiple Linear Regression")

# plt.legend displays the legend to show what is plotted on the graph
plt.legend()

# plt.grid(True) determines if the graph is displayed with a grid (true) or not (False)
plt.grid(True)

# Generates the graph
plt.show()


#  #### Task 3.6
#  Write 1–2 sentences explaining the insights from the visualisation.
# 
# * X-Axis: The real house prices.
# * Y-Axis: The prices the model guessed.
# * Red Line: 100% perfect predictions.
# 
#  ###### **Takeaways from visualisation**
# * **Good Accuracy:** Most of the blue dots cluster tightly along the red line. This means for most normal houses, the model's after price is very close to the before price.
# * **Under-Guesstimate (Below the Red Line):** For the highly expensive houses on the far right (over $800,000), the blue dots sit below the red line. This means your model is under-predicting the value of luxury houses.
# * **Over-Guesstimate (Above the Red Line):** For some cheaper houses on the left (under $400,000), the dots sit above the red line. This means the model over-guessed their value.
# 
# ###### **Final Takeaway**
# The model is reliable for normal, average houses but struggles to guess extreme prices correctly.

# In[11]:


"""
"r2_score" Calculates the coefficient of determination.
A result of 0 wouldn't be favorable as it shows no significant difference to just measuring the average normally
whereas a result of 0.70 through to 1 would be most favorable with 1 being a perfect prediction without error.
"""

from sklearn.metrics import r2_score
r2_score(y_test, y_pred_test)


# In[12]:


# Task 3.5: Evaluate the model using Root Mean Squared Error (RMSE) and interpret the results.

# used to make results_y a dataframe
import pandas as pd

# used to calculate the square root
import numpy as np

# Required to calculate the Mean Squared Error metric before taking the square root.
from sklearn.metrics import mean_squared_error

# assigns names to the test and prediction data so the columns are labeled once displayed below
results_y = pd.DataFrame({'Actual House Price': y_test, 'Predicted House Price': y_pred_test})
display(results_y) # shows the results_y data neatly in a table

# Evaluate model performance via Root mean square error
rmse_mlr = np.sqrt(mean_squared_error(y_test, y_pred_test))

# prints the rmse result with added $ and comma seperators
print(f"House Price RMSE: ${rmse_mlr:,.2f}")


# #### **What does this mean?**
# The result of $63,952.38 means that the predicted result is on average off by $63,952.38
# 
# With an average house price of $582,209.62 this gives the model an average error rate of just 11%

# ## Step 4: Compare with Random Forest Regressor
# 
# Task 4.1: Train a Random Forest Model
# Train a Random Forest Regressor model and evaluate its performance.
# 
# Task 4.2: Visualise Actual vs Predicted Prices for Random Forest
# Create a scatter plot comparing the actual prices and predicted prices for the Random Forest model.
# 
# Task 4.3: Model Comparison
# Compare the RMSE values of both the MLR and Random Forest models. Which model performs better?

# In[13]:


# Used to train the model
from sklearn.ensemble import RandomForestRegressor

# Calculates the error score
from sklearn.metrics import root_mean_squared_error

# Create the model with 100 trees
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model using training data
rf_model.fit(x_train, y_train)

# Predict prices using test data
y_pred_rf = rf_model.predict(x_test)

# Calculate the error score (RMSE)
rmse_rf = root_mean_squared_error(y_test, y_pred_rf)

# Print the final error score
print(f"Random Forest RMSE: {rmse_rf:.2f}")


#  #### What does this mean?
# The result of 71733.36 means that the predicted result is on average off by 71733.36
# 
# With an average house price of 582,209.62 this gives the model an average error rate of just 12.3%

# In[14]:


import matplotlib.pyplot as plt

# Set the size of the plot
plt.figure(figsize=(8, 6))

# Plot actual prices vs predicted prices
plt.scatter(y_test, y_pred_rf, alpha=0.6, color='forestgreen', label='Predictions')

# Draw a red diagonal line for perfect accuracy
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', label='Perfect Fit')

# Add titles and labels to the chart
plt.title('Random Forest: Actual vs Predicted Prices')
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.legend()
plt.grid(True)

# Show the final plot
plt.show()


# In[15]:


"""
"r2_score" Calculates the coefficient of determination.
A result of 0 wouldn't be favorable as it shows no significant difference to just measuring the average normally
whereas a result of 0.70 through to 1 would be most favorable with 1 being a perfect prediction without error.
"""

from sklearn.metrics import r2_score
r2_score(y_test, y_pred_rf)


# ##### Random Forest Graph Performance
# 
# ###### Chart Basics
# * **X-Axis:** The real house prices.
# * **Y-Axis:** The prices the model guessed.
# * **Red Line:** 100% perfect predictions.
# 
# ###### Model Performance
# * **Good for Average Homes:** Between $500k and $700k, the green dots cluster well around the red line. This means the model is generally accurate for normal houses.
# * **Bad for Cheap Homes:** Under $400k, the green dots sit noticeably high above the red line. This means the model heavily **over-guesses** the value of cheaper homes.
# * **Bad for Luxury Homes:** Over $800k, the green dots flatten out below the red line. This means the model heavily **under-guesses** the value of expensive homes.
# 
# ###### Final Takeaway
# Just like the MLR model, the Random Forest model is reliable for normal houses but makes major errors on very cheap and very expensive properties.

# In[16]:


# Compare the two error scores
print(f"MLR RMSE: {rmse_mlr:.2f}")
print(f"Random Forest RMSE: {rmse_rf:.2f}\n")

# The model with the lower number wins!
print("--- Final Model Comparison ---")
if rmse_mlr < rmse_rf:
    print(" Multiple Linear Regression (MLR) wins! It has a lower error score.")
elif rmse_rf < rmse_mlr:
    print("Random Forest wins! It has a lower error score.")
else:
    print("Both models performed exactly the same!")


# ## Step 5: Conclusion and Insights
# 
# Task 5.1: Insights and Recommendations
# 
# Based on the RMSE and visualisations, summarise which model performs better and why.
# 
# Discuss any improvements that could be made to both models.

# ##### Conclusion and Insights
# ##### Insights and Recommendations
# 
# ###### Which Model is Better?
# * **The Winner:** The **Multiple Linear Regression (MLR)** model won.
# * **Why:** In data science, a lower score means fewer guessing mistakes. On average, the MLR model was off by **$63,952**, while the Random Forest model was off by a larger **$71,733**. This means MLR is roughly $7,781 more accurate per house.
# 
# ###### What the Graphs Showed Us
# * **Good for Normal Houses:** Both models are very good at guessing the prices of average, mid-range houses ($500,000 to $700,000). The dots pack tightly together in the middle of the charts.
# * **Bad for Expensive Houses:** Both models struggle with luxury houses over $800,000. They consistently **under-guessed** the prices, predicting them as much cheaper than they actually are.
# * **Bad for Cheap Houses:** Both models struggle with cheaper houses under $400,000. They consistently **over-guessed** their values, predicting them as more expensive than they actually are.
# 
# ###### Simple Ways to Improve Both Models
# 1. **Smooth Out the Prices:** Use a quick math formula (called a Log Transformation) to shrink the giant luxury house prices. This levels out the playing field and stops the models from getting confused by massive numbers.
# 2. **Delete Useless Information:** Our charts showed that minor features like garage size have almost zero effect on a house's value. We should remove them so the computer can focus entirely on what matters most: house size and the number of bedrooms.
# 3. **Get More Information:** Size and bedrooms do not tell the whole story. To stop the models from guessing incorrectly, we need to feed them missing real-world data like **Neighborhood Safety**, **School Quality**, and **Home Condition**.
# 

# ##### House Price Prediction Project Overview
# 
#  ###### 1. Project Goal
# The objective of this project is to build and train a machine learning model that can accurately predict house prices based on physical features like square footage and the number of bedrooms. 
# 
# ###### 2. Exploratory Data Analysis
# Before building models, we explored the dataset to find key trends and patterns:
# * **The Main Driver:** Our scatter plot showed a positive trend—bigger houses generally cost more money.
# * **The Data Curve:** Our price histogram showed that most houses cost between $500,000 and $600,000, with a few premium luxury houses stretching the right side of the graph.
# * **Feature Importance:** Our correlation matrix confirmed that house size and bedroom counts have the strongest impact on house prices.
# 
# ###### 3. & 4. Model Building and Prediction
# We trained two different machine learning algorithms using the training data and tested their performance:
# 1. **Multiple Linear Regression (MLR):** A baseline model that uses a straight line approach.
# 2. **Random Forest (RF):** A more complex tree-based model designed to capture non-linear trends.
# 
# ###### 5. Final Evaluation and Conclusion
# We compared both models side-by-side using evaluation charts and their overall error scores (**RMSE**):
# * **MLR RMSE Score:** 63,952.38
# * **Random Forest RMSE Score:** 71,733.36
# * **The Winner:** **Multiple Linear Regression (MLR)** performed better because it achieved a lower error score, making it roughly $7,781 more accurate per house.
# * **Shared Weaknesses:** Looking at both performance graphs, both models are highly accurate for normal houses ($500k to $700k), but both struggle at the extremes—over-guessing cheap homes and under-guessing luxury homes.
# * **Recommendations:** In order to more finely tune the predictions generated for house prices we would recommend
# gathering more data that would be better for gauging and predicting house price such as Neighborhood Safety, School Quality, and Home Condition. We would also recommend removing some data points with very little impact on house price such as garage size  and the distance to Center.
# 

# Good work

# In[ ]:




