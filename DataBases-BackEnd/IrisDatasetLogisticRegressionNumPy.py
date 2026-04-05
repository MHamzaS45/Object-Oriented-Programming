import numpy as np
from sklearn.datasets import load_iris  # Used only for data download

# =========================
# 1. Data
# =========================
iris = load_iris()

# Original order in Iris datset:
# [Sepal Length, Sepal Width, Petal Length, Petal Width]
X = iris.data
y = iris.target

n_samples, n_features = X.shape
n_classes = len(np.unique(y))

# -------------------------
# Feature scaling (Highly recommended!)
# -------------------------
X_mean = X.mean(axis=0)
X_std = X.std(axis=0)
X = (X - X_mean) / X_std

# One-hot encoding
Y = np.zeros((n_samples, n_classes))
Y[np.arange(n_samples), y] = 1

# =========================
# 2. Settings
# =========================
np.random.seed(0)

W = np.random.randn(n_features, n_classes) * 0.01
b = np.zeros((1, n_classes))

learning_rate = 0.1
epochs = 5000

# =========================
# 3. Softmax
# =========================
def softmax(z):
    z = z - np.max(z, axis=1, keepdims=True)  # numerical stability
    exp_z = np.exp(z)
    return exp_z / np.sum(exp_z, axis=1, keepdims=True)

# =========================
# 4. Gradient Descent
# =========================
for epoch in range(epochs):

    # Forward pass
    z = X @ W + b
    y_pred = softmax(z)

    # Cross-entropy loss
    loss = -np.mean(np.sum(Y * np.log(y_pred + 1e-9), axis=1))

    # Gradients
    dz = y_pred - Y
    dW = X.T @ dz / n_samples
    db = np.sum(dz, axis=0, keepdims=True) / n_samples

    # Update
    W -= learning_rate * dW
    b -= learning_rate * db

    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, loss {loss:.4f}")

# =========================
# 5. Results
# =========================
print("\nInput order:")
print("1: Sepal Length (SL)")
print("2: Sepal Width  (SW)")
print("3: Petal Length (PL)")
print("4: Petal Width  (PW)")

# Each column corresponds to one class (Setosa, Versicolor, Virginica) and
# each row corresponds to one input feature
print("\nWeight matrix W (4 x 3):")
print(W)

# Bias values for each class (Setosa, Versicolor, Virginica)
print("\nBias vector b (1 x 3):")
print(b)

# =========================
# 6. Training accuracy
# =========================
z = X @ W + b
y_pred = np.argmax(softmax(z), axis=1)
accuracy = np.mean(y_pred == y)

print(f"\nTraining accuracy: {accuracy:.4f}")