
# CodeAlpha Internship
# Task 1: Iris Flower Classification

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# ----------------------------------
# 1. Load the Iris Dataset
# ----------------------------------

iris = load_iris()

X = iris.data
y = iris.target

# Convert dataset into a DataFrame
df = pd.DataFrame(
    X,
    columns=iris.feature_names
)

df["species"] = iris.target_names[y]

print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

# ----------------------------------
# 2. Data Preprocessing
# ----------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# ----------------------------------
# 3. Split Dataset
# ----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# ----------------------------------
# 4. Train Machine Learning Model
# ----------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("\nModel Training Completed!")

# ----------------------------------
# 5. Make Predictions
# ----------------------------------

y_pred = model.predict(X_test)

# ----------------------------------
# 6. Evaluate Model
# ----------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy * 100, "%")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=iris.target_names
    )
)

# ----------------------------------
# 7. Confusion Matrix
# ----------------------------------

cm = confusion_matrix(y_test, y_pred)

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=iris.target_names
)

display.plot(cmap="Blues")

plt.title("Iris Flower Confusion Matrix")

plt.savefig("iris_confusion_matrix.png")

plt.show()

# ----------------------------------
# 8. Visualize Dataset
# ----------------------------------

plt.figure(figsize=(8, 6))

plt.scatter(
    X[:, 0],
    X[:, 1],
    c=y,
    cmap="viridis"
)

plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")

plt.title("Iris Flower Dataset Visualization")

plt.savefig("iris_visualization.png")

plt.show()

# ----------------------------------
# 9. Predict a New Flower
# ----------------------------------

new_flower = [[5.1, 3.5, 1.4, 0.2]]

prediction = model.predict(new_flower)

predicted_species = iris.target_names[prediction[0]]

print("\nNew Flower Prediction:")
print("Predicted Species:", predicted_species)
