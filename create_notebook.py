import json

notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Matrix Operations with NumPy\n",
                "\n",
                "This notebook demonstrates various matrix operations using NumPy, including:\n",
                "- Matrix multiplication\n",
                "- Matrix addition and subtraction\n",
                "- Matrix visualization\n",
                "\n",
                "We'll use NumPy's powerful array operations to perform these calculations efficiently."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import numpy as np\n",
                "import matplotlib.pyplot as plt\n",
                "import seaborn as sns\n",
                "\n",
                "# Set style for better visualizations\n",
                "plt.style.use('seaborn')\n",
                "sns.set_palette('husl')"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 1. Matrix Multiplication\n",
                "\n",
                "Let's start with matrix multiplication using two 2x2 matrices."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Example of 2D Matrices (Matrix Multiplication)\n",
                "A = np.array([[1, 2],[3, 4]])\n",
                "B = np.array([[5, 6],[7, 8]])\n",
                "\n",
                "result = A.dot(B)\n",
                "print(\"Matrix A:\")\n",
                "print(A)\n",
                "print(\"\\nMatrix B:\")\n",
                "print(B)\n",
                "print(\"\\nResult of A.dot(B):\")\n",
                "print(result)\n",
                "\n",
                "# Explanation of the process\n",
                "# [1*5 + 2*7, 1*6 + 2*8]  => [19, 22]\n",
                "# [3*5 + 4*7, 3*6 + 4*8]  => [43, 50]"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Matrix Addition and Subtraction\n",
                "\n",
                "Let's explore matrix addition and subtraction with the same matrices."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Matrix addition\n",
                "addition_result = A + B\n",
                "print(\"Matrix Addition (A + B):\")\n",
                "print(addition_result)\n",
                "\n",
                "# Matrix subtraction\n",
                "subtraction_result = A - B\n",
                "print(\"\\nMatrix Subtraction (A - B):\")\n",
                "print(subtraction_result)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3. Matrix Visualization\n",
                "\n",
                "Let's visualize our matrices using heatmaps to better understand their structure."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "def plot_matrix(matrix, title):\n",
                "    plt.figure(figsize=(6, 4))\n",
                "    sns.heatmap(matrix, annot=True, cmap='viridis', fmt='.0f')\n",
                "    plt.title(title)\n",
                "    plt.show()\n",
                "\n",
                "# Visualize original matrices\n",
                "plot_matrix(A, 'Matrix A')\n",
                "plot_matrix(B, 'Matrix B')\n",
                "\n",
                "# Visualize results\n",
                "plot_matrix(result, 'Matrix Multiplication Result')\n",
                "plot_matrix(addition_result, 'Matrix Addition Result')\n",
                "plot_matrix(subtraction_result, 'Matrix Subtraction Result')"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 4. Larger Matrix Example\n",
                "\n",
                "Let's try with larger matrices to see how NumPy handles more complex operations."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Create larger matrices\n",
                "C = np.random.randint(1, 10, size=(3, 3))\n",
                "D = np.random.randint(1, 10, size=(3, 3))\n",
                "\n",
                "# Perform operations\n",
                "larger_result = C.dot(D)\n",
                "print(\"\\nResult of C.dot(D):\")\n",
                "print(larger_result)\n",
                "\n",
                "# Visualize larger matrices\n",
                "plot_matrix(C, 'Matrix C')\n",
                "plot_matrix(D, 'Matrix D')\n",
                "plot_matrix(larger_result, 'Larger Matrix Multiplication Result')"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.9.6"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 2
}

with open('Jupyter_Notebooks/sandBox.ipynb', 'w') as f:
    json.dump(notebook, f, indent=1) 