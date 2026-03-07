# 🧮 NumPy Cheat Sheet

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-orange?logo=numpy)
![Level](https://img.shields.io/badge/Level-Beginner--Intermediate-green)

A quick reference guide for **NumPy**, the fundamental Python library used for **numerical computing, arrays, and scientific computing**.

---

# 📌 What is NumPy?

NumPy (Numerical Python) is a powerful Python library used for:

* Fast numerical computations
* Working with multi-dimensional arrays
* Mathematical operations
* Scientific computing
* Data science and machine learning workflows

---

# ⚙️ Installation

Install NumPy using pip:

```bash
pip install numpy
```

Import NumPy:

```python
import numpy as np
```

Check version:

```python
np.__version__
```

---

# 📦 Creating Arrays

### From Python List

```python
import numpy as np

arr = np.array([1,2,3,4])
```

### Zeros Array

```python
np.zeros(5)
```

### Ones Array

```python
np.ones(5)
```

### Range Array

```python
np.arange(1,10)
```

### Evenly Spaced Values

```python
np.linspace(0,10,5)
```

---

# 📊 Array Attributes

```python
arr = np.array([[1,2,3],[4,5,6]])
```

| Attribute   | Description          |
| ----------- | -------------------- |
| `arr.shape` | Dimensions of array  |
| `arr.size`  | Number of elements   |
| `arr.ndim`  | Number of dimensions |
| `arr.dtype` | Data type            |

---

# 🔢 Indexing & Slicing

### Access element

```python
arr = np.array([10,20,30,40])

arr[1]
```

### Slicing

```python
arr[1:3]
```

---

# 🔄 Reshaping Arrays

```python
arr = np.arange(1,10)

arr.reshape(3,3)
```

Output

```
[[1 2 3]
 [4 5 6]
 [7 8 9]]
```

---

# ➕ Mathematical Operations

```python
a = np.array([1,2,3])
b = np.array([4,5,6])
```

Addition

```python
a + b
```

Multiplication

```python
a * b
```

Division

```python
a / b
```

Power

```python
a ** 2
```

---

# 📊 Statistical Functions

```python
arr = np.array([10,20,30,40])
```

| Function       | Purpose            |
| -------------- | ------------------ |
| `np.mean(arr)` | Average            |
| `np.sum(arr)`  | Sum                |
| `np.max(arr)`  | Maximum            |
| `np.min(arr)`  | Minimum            |
| `np.std(arr)`  | Standard deviation |

---

# 🎲 Random Numbers

Random numbers

```python
np.random.rand(5)
```

Random integers

```python
np.random.randint(1,100,10)
```

Random normal distribution

```python
np.random.randn(5)
```

---

# 📐 Matrix Operations

```python
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
```

Matrix addition

```python
A + B
```

Matrix multiplication

```python
np.dot(A,B)
```

or

```python
A @ B
```

Transpose matrix

```python
A.T
```

---

# ⚡ NumPy vs Python Lists

Python list operation:

```python
a = [1,2,3]
b = [4,5,6]

result = []
for i in range(len(a)):
    result.append(a[i] + b[i])
```

NumPy vectorized operation:

```python
a = np.array([1,2,3])
b = np.array([4,5,6])

a + b
```

NumPy is faster because operations are **vectorized and optimized in C**.

---

# 📊 Common NumPy Functions

| Function        | Description           |
| --------------- | --------------------- |
| `np.array()`    | Create array          |
| `np.zeros()`    | Array of zeros        |
| `np.ones()`     | Array of ones         |
| `np.arange()`   | Range of numbers      |
| `np.linspace()` | Evenly spaced numbers |
| `np.mean()`     | Average value         |
| `np.sum()`      | Sum of values         |
| `np.max()`      | Maximum value         |
| `np.min()`      | Minimum value         |

---

# 🚀 Quick Reference

```python
import numpy as np

np.array([1,2,3])
np.zeros(5)
np.ones(5)
np.arange(1,10)
np.linspace(0,10,5)

np.mean(arr)
np.sum(arr)
np.max(arr)

arr.reshape(3,3)
np.random.rand(5)
```

---

# 📚 Use Cases

NumPy is widely used in:

* Data Science
* Machine Learning
* Artificial Intelligence
* Image Processing
* Scientific Computing

Many libraries are built on NumPy including:

* Pandas
* Scikit-Learn
* TensorFlow
* PyTorch

---


