# Autor: Jonathan Hernández
# Fecha: 02 Octubre 2024
# Descripción: Código para Regresion Lineal.
# GitHub: https://github.com/Jona163

# Importar Librerias, matplotlib, numpy, pandas, seaborn, sklearn(linear_model, model_selection, metrics)
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Semilla random || random.seed || random.uniform
np.random.seed(101)
# X y Y
# Vamos a crear 50 valores aleatorios
x = np.linspace(0,50,50)
y = np.linspace(0,50,50)

x += np.random.uniform(-4,4,50)
y += np.random.uniform(-4,4,50)

# Mostraremos la data dispersa || scatter 
plt.scatter(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data Dispersa')

# Caracteristica
x[0]

# Valor real
y[0]
