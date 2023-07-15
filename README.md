# House Price Prediction ML Project

This project focuses on developing a machine learning model capable of accurately estimating house prices based on various features. The goal is to provide users with a reliable and efficient solution for predicting house prices.

## Project Highlights

- Data Cleaning: The dataset is thoroughly cleaned, handling missing values, duplicates, and data inconsistencies to ensure reliable results.

- Modification to Standard Form: The dataset is standardized, renaming variables, adjusting data types, and organizing the data for efficient analysis.

- Exploratory Data Analysis (EDA) Visualization: Captivating visualizations, including histograms, scatter plots, box plots, and correlation matrices, provide insights into variable relationships and identify outliers or anomalies.

- EDA Pandas Profiling: A comprehensive report generated using pandas profiling offers detailed statistical analysis, summaries, correlation matrices, and distribution plots for a holistic view of the dataset.

- Handling Outliers: Outliers are identified and appropriately treated using various techniques such as z-score, percentiles, and box plots to ensure robust modeling.

- Model Building: Two regression models, Linear Regression and Ridge, are constructed to establish relationships between independent variables and house prices, with Ridge regularization for improved generalization.

- Dumping the Ridge Model using Pickle: The trained Ridge model is serialized and saved as a binary file for future use without retraining.

- Creating Flask Application: A user-friendly Flask application is developed to provide an intuitive interface for users to interact with the model and obtain predictions.

- Deploying the Model in the Flask Application: The trained Ridge model is integrated into the Flask application, allowing real-time predictions based on user input.

- Prediction Accuracy: The developed application achieves an impressive prediction correctness rate of 80%, providing users with reliable estimates of house prices.

- GitHub Repository: The complete project, including source code, dataset, and documentation, is shared on GitHub for collaboration, version control, and easy access for further development.

## Getting Started

To get started with the House Price Prediction ML Project, follow the steps below:

1. Clone the repository: `git clone https://github.com/your-username/house-price-prediction.git`
2. Install the necessary dependencies: `pip install -r requirements.txt`
3. Run the data cleaning and preprocessing scripts: `python data_preprocessing.py`
4. Perform EDA and generate visualizations: `python eda_visualization.py`
5. Train and evaluate the regression models: `python train_models.py`
6. Dump the Ridge model using pickle: `python dump_model.py`
7. Start the Flask application: `python app.py`
8. Access the application in your browser at `http://localhost:5000` and enter the required house features to get the predicted price.

## Conclusion

The House Price Prediction ML Project successfully develops a robust machine learning model and a user-friendly Flask application for accurate house price estimation. The project showcases thorough data cleaning, exploratory data analysis, and the construction of regression models. With an 80% prediction correctness rate, the application provides users with reliable estimates of house prices. The GitHub repository allows for collaboration and further development in the field of house price prediction.

Feel free to contribute, explore, and utilize this project to gain insights into house prices and enhance your understanding of machine learning techniques.
