import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Carregar os dados de um arquivo CSV
data = pd.read_csv('dataset.csv')

# Pré-processamento dos dados
X = data[['idade', 'peso', 'altura', 'gênero', 'atividade', 'preferências']]
y = data[['calorias', 'proteínas', 'carboidratos', 'gorduras', 'refeição1', 'refeição2', 'refeição3', 'refeição4', 'refeição5']]

# Separar as partes numéricas e textuais das saídas
y_numeric = y[['calorias', 'proteínas', 'carboidratos', 'gorduras']]
y_text = y[['refeição1', 'refeição2', 'refeição3', 'refeição4', 'refeição5']]

# One-hot encoding para variáveis categóricas
X_encoded = pd.get_dummies(X, columns=['gênero', 'atividade', 'preferências'])

# Normalização das entradas
scaler_X = StandardScaler()
X_scaled = scaler_X.fit_transform(X_encoded)

# Normalização das saídas numéricas
scaler_y = StandardScaler()
y_numeric_scaled = scaler_y.fit_transform(y_numeric)

# Divisão dos dados
X_train, X_test, y_train_numeric, y_test_numeric, y_train_text, y_test_text = train_test_split(
    X_scaled, y_numeric_scaled, y_text, test_size=0.2, random_state=42)

# Construção do modelo para as saídas numéricas
model_numeric = Sequential([
    Dense(64, input_dim=X_train.shape[1], activation='relu'),
    Dense(32, activation='relu'),
    Dense(16, activation='relu'),
    Dense(y_numeric.shape[1])  # Saída com 4 valores: calorias, proteínas, carboidratos, gorduras
])

model_numeric.compile(optimizer='adam', loss='mean_squared_error')

# Treinamento do modelo para as saídas numéricas
model_numeric.fit(X_train, y_train_numeric, epochs=100, batch_size=8, validation_split=0.2)

# Avaliação do modelo numérico
loss_numeric = model_numeric.evaluate(X_test, y_test_numeric)
print(f"Loss (numérico): {loss_numeric}")

# Previsão para novos dados de anamnese
new_data = pd.DataFrame({
    'idade': [28],
    'peso': [75],
    'altura': [178],
    'gênero': ['M'],
    'atividade': ['média'],
    'preferências': ['vegano']
})

new_data_encoded = pd.get_dummies(new_data, columns=['gênero', 'atividade', 'preferências'])

# Garantir que new_data_encoded tenha as mesmas colunas que X_encoded
new_data_encoded = new_data_encoded.reindex(columns=X_encoded.columns, fill_value=0)

# Normalização dos novos dados
new_data_scaled = scaler_X.transform(new_data_encoded)  # Usando o scaler_X, que foi ajustado com X_encoded

# Previsão dos valores numéricos
predictions_numeric = model_numeric.predict(new_data_scaled)
predictions_numeric = scaler_y.inverse_transform(predictions_numeric)  # Invertendo a normalização das saídas
print(f"Previsão dos valores numéricos: {predictions_numeric}")

# Encontrar o exemplo mais próximo na base de dados
closest_example = data.iloc[(X_encoded - new_data_encoded.values).abs().sum(axis=1).argmin()]
print(f"Plano Alimentar Detalhado: {closest_example[['refeição1', 'refeição2', 'refeição3', 'refeição4', 'refeição5']]}")
