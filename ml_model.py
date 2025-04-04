import xgboost as xgb
import joblib
from sklearn.metrics import accuracy_score
from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split

# Carregar o dataset de doenças cardíacas
# O dataset é retirado do UCI Machine Learning Repository através da biblioteca ucimlrepo
heart_disease = fetch_ucirepo(id=45)
dados = heart_disease.data.features
dados['doenca'] = (heart_disease.data.targets > 0) * 1

# Separando os dados em treino e teste
X = dados.drop(columns=['doenca'])
y = dados['doenca']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=432, stratify=y)

# Classificando com XGBoost
modelo = xgb.XGBClassifier(objetive='binary:logistic')
modelo.fit(X_train, y_train)
preds = modelo.predict(X_test)

# Avaliando o modelo
acuracia = accuracy_score(y_test, preds)
print(f'Acurácia do modelo: {acuracia:.2%}')

# Salvar o modelo treinado
joblib.dump(modelo, 'modelo_heart_disease.pkl')
