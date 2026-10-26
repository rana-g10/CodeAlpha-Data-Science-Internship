# Iris Flower Classification

## Project Overview

This project is part of my CodeAlpha Data Science Internship.

The objective of this project is to develop a machine learning model that can classify Iris flowers into three different species:

- Iris Setosa
- Iris Versicolor
- Iris Virginica

The model uses flower measurements to predict the species.

## Dataset

The Iris dataset is obtained from Scikit-learn.

It contains 150 samples with four numerical features:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

The dataset contains three flower species.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn

## Project Workflow

1. Load the Iris dataset.
2. Explore the dataset.
3. Check for missing values.
4. Split the dataset into training and testing sets.
5. Train a Random Forest Classifier.
6. Make predictions.
7. Evaluate the model.
8. Visualize the results.

## Model

Random Forest Classifier was used for this project.

The dataset was divided into:

- 80% Training Data
- 20% Testing Data

## Results

The model achieved 90% accuracy on the test dataset.

The project also generates:

- Iris Flower Dataset Visualization
- Iris Flower Confusion Matrix

## How to Run

Install the required libraries:

```bash
python -m pip install pandas matplotlib scikit-learn
```

Run the Python file:

```bash
python iris_classification.py
```

## Conclusion

This project demonstrates the basic machine learning workflow, including data loading, preprocessing, model training, prediction, evaluation, and visualization.

It helped me understand how machine learning can be used to classify data based on numerical features.
