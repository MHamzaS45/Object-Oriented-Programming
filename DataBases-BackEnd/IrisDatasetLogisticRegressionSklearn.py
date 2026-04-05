import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# 1. Ladataan Iris-data
iris = load_iris()
X = iris.data   # (150, 4)
y = iris.target # (150,)

# 2. Määritellään logistinen regressio
# solver + random_state takaavat deterministisen tuloksen (sama tulos joka koneella)
model = LogisticRegression(
    multi_class='ovr',
    solver='liblinear',
    penalty='l2',
    C=1.0,
    fit_intercept=True,
    max_iter=1000,
    random_state=0
)

# 3. Koulutetaan malli
model.fit(X, y)

# 4. Haetaan painot ja bias
W = model.coef_      # shape (3, 4)
b = model.intercept_ # shape (3,)

# 5. Tulostetaan
class_names = iris.target_names

for i, class_name in enumerate(class_names):
    print(f"\nClass: {class_name}")
    print("Weights:", W[i])
    print("Bias:", b[i])

# 6. Matriisimuodossa
print("\nWeight matrix W:")
print(W)

print("\nBias vector b:")
print(b)
