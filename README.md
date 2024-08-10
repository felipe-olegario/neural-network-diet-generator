# Modelo de Previsão Nutricional

---

## Descrição do Projeto

Este projeto implementa uma rede neural utilizando TensorFlow e Keras para prever valores nutricionais, como calorias, proteínas, carboidratos e gorduras, com base em características pessoais e preferências alimentares. Além disso, a aplicação sugere um plano alimentar detalhado, comparando os dados do usuário com exemplos já existentes na base de dados.

## Arquitetura do Projeto

O projeto é construído utilizando as seguintes bibliotecas:

- **TensorFlow/Keras**: Para a construção e treinamento do modelo de rede neural.
- **Scikit-Learn**: Para o pré-processamento dos dados, incluindo normalização e codificação one-hot.
- **Pandas**: Para manipulação de dados e leitura/escrita de arquivos CSV.
- **Docker**: Para encapsular a aplicação e gerenciar o ambiente de execução.

## Funcionalidades Principais

1. **Leitura de Dados**:
   - Os dados são carregados de um arquivo CSV que contém informações sobre as características pessoais (idade, peso, altura, gênero, atividade, preferências alimentares) e saídas nutricionais desejadas (calorias, proteínas, carboidratos, gorduras, refeições).

2. **Pré-processamento dos Dados**:
   - **Codificação One-Hot**: Para transformar variáveis categóricas (gênero, atividade, preferências) em variáveis numéricas.
   - **Normalização**: Os dados numéricos de entrada e saída são normalizados usando `StandardScaler` para melhorar o desempenho do modelo.

3. **Divisão de Dados**:
   - Os dados são divididos em conjuntos de treinamento e teste usando `train_test_split`, garantindo que o modelo seja avaliado de forma justa.

4. **Construção e Treinamento do Modelo**:
   - Um modelo de rede neural simples é construído utilizando camadas densas (`Dense`). O modelo é treinado para prever valores numéricos associados a nutrientes.

5. **Avaliação do Modelo**:
   - O modelo é avaliado utilizando o conjunto de teste, e a função de perda (`mean_squared_error`) é impressa para indicar a precisão da previsão.

6. **Previsão com Novos Dados**:
   - O usuário pode fornecer novos dados (idade, peso, altura, gênero, atividade, preferências), e o modelo prevê os valores nutricionais esperados.
   - **Sugestão de Plano Alimentar**: A aplicação compara os dados do usuário com exemplos na base de dados e sugere um plano alimentar detalhado.

## Requisitos

- **Python 3.x**
- **Bibliotecas Python**:
  - `tensorflow`
  - `scikit-learn`
  - `pandas`
- **Docker** (opcional, se estiver usando contêineres)

## Instruções de Uso

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu-usuario/modelo-previsao-nutricional.git
   cd modelo-previsao-nutricional
   docker compose up
   ```

## Estrutura do Projeto
- app.py                  # Código principal da aplicação
- dataset.csv             # Base de dados de exemplo (deve ser fornecida pelo usuário)
- Dockerfile              # Dockerfile para criar a imagem do contêiner
- docker-compose.yml      # Arquivo Docker Compose para orquestrar contêineres
- requirements.txt        # Arquivo com as dependências Python
- README.md               # Este documento

