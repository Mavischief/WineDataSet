# importa função do arquivo
import pytest
from model.modelo import Model
from model.modelo import Carregador
from pickle import load
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from model.vinho import Vinho

# Instanciando classes
modelo = Model()

# Parâmetros    
url_dados_x = "./model/data/X_test_dataset_vinho.csv"
url_dados_y = "./model/data/y_test_dataset_vinho.csv"
colunas = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density',
           'pH', 'sulphates', 'alcohol']
outcome = ['quality']
# Carga dos dados
dataset_x = Carregador.carregar_dados(url_dados_x, colunas)
array = dataset_x.values
X = array
dataset_y = Carregador.carregar_dados(url_dados_y, outcome)
array = dataset_y.values
y = array


# Método para testar modelo KNN a partir do arquivo correspondente
def test_modelo_knn():
    # Importando modelo de KNN
    knn_path = './model/model.pkl'
    modelo_knn = load(open(knn_path, 'rb'))

    # Aplicar o scaler
    scaled_x = Model.aplicando_scaler(X)
  
    #realiza a predição a partir do modelo e dos dados de entradas com scaler
    predicoes = modelo_knn.predict(scaled_x)
    
    #Reliza a comparação para obter a acurácia
    acuracia = accuracy_score(y, predicoes)
    
    # Testando as métricas do KNN
    assert acuracia <= 0.65





# Teste para valores de pH válidos (pH = -0.1)
def test_valor_limite_abaixo_pH():
  vinho = Vinho(name="Merlot", fixed_acidity=7.1, volatile_acidity=0.28, citric_acid=0.5, residual_sugar=2.0, chlorides=0.045, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=-0.1, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_pH() == False

# Teste para pH no limite inferior (pH = 0)
def test_valor_limite_inferior_pH():
  vinho = Vinho(name="Merlot", fixed_acidity=7.1, volatile_acidity=0.28, citric_acid=0.5, residual_sugar=2.0, chlorides=0.045, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=0, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_pH() == True

# Teste para pH no limite superior (pH = 14)
def test_valor_limite_superior_pH():
  vinho = Vinho(name="Merlot", fixed_acidity=7.1, volatile_acidity=0.28, citric_acid=0.5, residual_sugar=2.0, chlorides=0.045, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=14, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_pH() == True

# Teste para pH no limite superior (pH = 14.1)
def test_valor_superior_limite_superior_pH():
  vinho = Vinho(name="Merlot", fixed_acidity=7.1, volatile_acidity=0.28, citric_acid=0.5, residual_sugar=2.0, chlorides=0.045, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=14.1, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_pH() == False






# Teste para acidez fixa no limite inferior (fixed_acidity = 0)
def test_valor_limite_inferior_acidez():
  vinho = Vinho(name="Merlot", fixed_acidity=0, volatile_acidity=0.28, citric_acid=0.5, residual_sugar=2.0, chlorides=0.045, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=11, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_acidez() == True

# Teste para acidez fixa no limite inferior (fixed_acidity = -0.1)
def test_valor_abaixo_limite_inferior_acidez():
  vinho = Vinho(name="Merlot", fixed_acidity=-0.1, volatile_acidity=0.28, citric_acid=0.5, residual_sugar=2.0, chlorides=0.045, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=11, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_acidez() == False






# Teste para volatilidade no limite inferior (volatile_acidity = 0)
def test_valor_limite_inferior_volatilidade():
  vinho = Vinho(name="Merlot", fixed_acidity=0.1, volatile_acidity=0, citric_acid=0.5, residual_sugar=2.0, chlorides=0.045, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=11, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_volatilidade() == True

# Teste para volatilidade no limite inferior (volatile_acidity = -0.1)
def test_valor_abaixo_limite_inferior_volatilidade():
  vinho = Vinho(name="Merlot", fixed_acidity=0.1, volatile_acidity=-0.1, citric_acid=0.5, residual_sugar=2.0, chlorides=0.045, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=11, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_volatilidade() == False






# Teste para acido citrico no limite inferior (citric_acid = 0)
def test_valor_limite_inferior_citric():
  vinho = Vinho(name="Merlot", fixed_acidity=0.1, volatile_acidity=0.1, citric_acid=0, residual_sugar=2.0, chlorides=0.045, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=11, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_citric() == True

# Teste para acido citrico no limite inferior (citric_acid = -0.1)
def test_valor_abaixo_limite_inferior_citric():
  vinho = Vinho(name="Merlot", fixed_acidity=0.1, volatile_acidity=0.1, citric_acid=-0.1, residual_sugar=2.0, chlorides=0.045, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=11, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_citric() == False






# Teste para açucar residual no limite inferior (residual_sugar = 0)
def test_valor_limite_inferior_residual_sugar():
  vinho = Vinho(name="Merlot", fixed_acidity=0.1, volatile_acidity=0.1, citric_acid=0.1, residual_sugar=0, chlorides=0.045, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=11, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_sugar() == True

# Teste para açucar residual no limite inferior (residual_sugar = -0.1)
def test_valor_abaixo_limite_inferior_residual_sugar():
  vinho = Vinho(name="Merlot", fixed_acidity=0.1, volatile_acidity=0.1, citric_acid=0.1, residual_sugar=-0.1, chlorides=0.045, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=11, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_sugar() == False






# Teste para cloridratos no limite inferior (chlorides = 0)
def test_valor_limite_inferior_chlorides():
  vinho = Vinho(name="Merlot", fixed_acidity=0.1, volatile_acidity=0.1, citric_acid=0.1, residual_sugar=0.1, chlorides=0, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=11, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_cloridratos() == True

# Teste para cloridratos no limite inferior (chlorides = -0.1)
def test_valor_abaixo_limite_inferior_chlorides():
  vinho = Vinho(name="Merlot", fixed_acidity=0.1, volatile_acidity=0.1, citric_acid=0.1, residual_sugar=0.1, chlorides=-0.1, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=11, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_cloridratos() == False






# Teste para free_sulfur_dioxide no limite inferior (free_sulfur_dioxide = 0)
def test_valor_limite_inferior_free_sulfur_dioxide():
  vinho = Vinho(name="Merlot", fixed_acidity=0.1, volatile_acidity=0.1, citric_acid=0.1, residual_sugar=0.1, chlorides=0.1, 
                free_sulfur_dioxide=0, total_sulfur_dioxide=30.0, density=0.995, pH=11, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_free_sulfur_dioxide() == True

# Teste para free_sulfur_dioxide no limite inferior (free_sulfur_dioxide = -0.1)
def test_valor_abaixo_limite_inferior_free_sulfur_dioxide():
  vinho = Vinho(name="Merlot", fixed_acidity=0.1, volatile_acidity=0.1, citric_acid=0.1, residual_sugar=0.1, chlorides=0.1, 
                free_sulfur_dioxide=-0.1, total_sulfur_dioxide=30.0, density=0.995, pH=11, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_free_sulfur_dioxide() == False






# Teste para total_sulfur_dioxide no limite inferior (total_sulfur_dioxide = 0)
def test_valor_limite_inferior_total_sulfur_dioxide():
  vinho = Vinho(name="Merlot", fixed_acidity=0.1, volatile_acidity=0.1, citric_acid=0.1, residual_sugar=0.1, chlorides=0.1, 
                free_sulfur_dioxide=0.1, total_sulfur_dioxide=0, density=0.995, pH=11, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_total_sulfur_dioxide() == True

# Teste para total_sulfur_dioxide no limite inferior (total_sulfur_dioxide = -0.1)
def test_valor_abaixo_limite_inferior_total_sulfur_dioxide():
  vinho = Vinho(name="Merlot", fixed_acidity=0.1, volatile_acidity=0.1, citric_acid=0.1, residual_sugar=0.1, chlorides=0.1, 
                free_sulfur_dioxide=0.1, total_sulfur_dioxide=-0.1, density=0.995, pH=11, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_total_sulfur_dioxide() == False






# Teste para density no limite inferior (density = 0.1)
def test_valor_limite_inferior_density():
  vinho = Vinho(name="Merlot", fixed_acidity=0.1, volatile_acidity=0.1, citric_acid=0.1, residual_sugar=0.1, chlorides=0.1, 
                free_sulfur_dioxide=0.1, total_sulfur_dioxide=0.1, density=0.1, pH=11, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_density() == True

# Teste para density no limite inferior (density = 0)
def test_valor_abaixo_limite_inferior_density():
  vinho = Vinho(name="Merlot", fixed_acidity=0.1, volatile_acidity=0.1, citric_acid=0.1, residual_sugar=0.1, chlorides=0.1, 
                free_sulfur_dioxide=0.1, total_sulfur_dioxide=0.1, density=0, pH=11, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_density() == False






# Teste para sulphates no limite inferior (sulphates = 0)
def test_valor_limite_inferior_sulphates():
  vinho = Vinho(name="Merlot", fixed_acidity=0.1, volatile_acidity=0.1, citric_acid=0.1, residual_sugar=0.1, chlorides=0.1, 
                free_sulfur_dioxide=0.1, total_sulfur_dioxide=0.1, density=0.1, pH=11, sulphates=0, alcohol=12.5, quality=None)
  assert vinho.verifica_sulphates() == True

# Teste para sulphates no limite inferior (sulphates = -0.1)
def test_valor_abaixo_limite_inferior_sulphates():
  vinho = Vinho(name="Merlot", fixed_acidity=0.1, volatile_acidity=0.1, citric_acid=0.1, residual_sugar=0.1, chlorides=0.1, 
                free_sulfur_dioxide=0.1, total_sulfur_dioxide=0.1, density=0.1, pH=11, sulphates=-0.1, alcohol=12.5, quality=None)
  assert vinho.verifica_sulphates() == False






# Teste para alcohol no limite inferior (alcohol = 0)
def test_valor_limite_inferior_alcohol():
  vinho = Vinho(name="Merlot", fixed_acidity=0.1, volatile_acidity=0.1, citric_acid=0.1, residual_sugar=0.1, chlorides=0.1, 
                free_sulfur_dioxide=0.1, total_sulfur_dioxide=0.1, density=0.1, pH=11, sulphates=0.1, alcohol=0, quality=None)
  assert vinho.verifica_alcohol() == True

# Teste para alcohol no limite inferior (alcohol = -0.1)
def test_valor_abaixo_limite_inferior_alcohol():
  vinho = Vinho(name="Merlot", fixed_acidity=0.1, volatile_acidity=0.1, citric_acid=0.1, residual_sugar=0.1, chlorides=0.1, 
                free_sulfur_dioxide=0.1, total_sulfur_dioxide=0.1, density=0.1, pH=11, sulphates=0.1, alcohol=-0.1, quality=None)
  assert vinho.verifica_alcohol() == False






# Teste para quality no limite inferior (quality = -1)
def test_valor_inferior_limite_inferior_quality():
  vinho = Vinho(name="Merlot", fixed_acidity=7.1, volatile_acidity=0.28, citric_acid=0.5, residual_sugar=2.0, chlorides=0.045, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=7, sulphates=0.6, alcohol=12.5, quality=-1)
  assert vinho.verifica_quality() == False

# Teste para quality no limite inferior (quality = 0)
def test_valor_limite_inferior_quality():
  vinho = Vinho(name="Merlot", fixed_acidity=7.1, volatile_acidity=0.28, citric_acid=0.5, residual_sugar=2.0, chlorides=0.045, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=7, sulphates=0.6, alcohol=12.5, quality=0)
  assert vinho.verifica_quality() == True

# Teste para quality no limite superior (quality = 10)
def test_valor_limite_superior_quality():
  vinho = Vinho(name="Merlot", fixed_acidity=7.1, volatile_acidity=0.28, citric_acid=0.5, residual_sugar=2.0, chlorides=0.045, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=7, sulphates=0.6, alcohol=12.5, quality=10)
  assert vinho.verifica_quality() == True

# Teste para quality no limite superior (quality = 11)
def test_valor_superior_limite_superior_quality():
  vinho = Vinho(name="Merlot", fixed_acidity=7.1, volatile_acidity=0.28, citric_acid=0.5, residual_sugar=2.0, chlorides=0.045, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=7, sulphates=0.6, alcohol=12.5, quality=11)
  assert vinho.verifica_quality() == False







# Teste da verificação global
def test_verifica_tudo():
  vinho = Vinho(name="Merlot", fixed_acidity=7.1, volatile_acidity=0.28, citric_acid=0.5, residual_sugar=2.0, chlorides=0.045, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=7, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_tudo() == True

# Teste da verificação global para acidez fixa
def test_verifica_tudo_acidez():
  vinho = Vinho(name="Merlot", fixed_acidity=-1, volatile_acidity=0.28, citric_acid=0.5, residual_sugar=2.0, chlorides=0.045, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=7, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_tudo() == False

# Teste da verificação global para volatilidade
def test_verifica_tudo_volatilidade():
  vinho = Vinho(name="Merlot", fixed_acidity=7.1, volatile_acidity=-1, citric_acid=0.5, residual_sugar=2.0, chlorides=0.045, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=7, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_tudo() == False

# Teste da verificação global para acido citrico
def test_verifica_tudo_acido_citrico():
  vinho = Vinho(name="Merlot", fixed_acidity=7.1, volatile_acidity=0.28, citric_acid=-1, residual_sugar=2.0, chlorides=0.045, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=7, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_tudo() == False

# Teste da verificação global para açudar residual
def test_verifica_tudo_resdual_sugar():
  vinho = Vinho(name="Merlot", fixed_acidity=7.1, volatile_acidity=0.28, citric_acid=0.5, residual_sugar=-1, chlorides=0.045, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=7, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_tudo() == False

# Teste da verificação global para cloridratos
def test_verifica_tudo_cloridrates():
  vinho = Vinho(name="Merlot", fixed_acidity=7.1, volatile_acidity=0.28, citric_acid=0.5, residual_sugar=2.0, chlorides=-1, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=7, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_tudo() == False

# Teste da verificação global para dioxido de sulfurio livre
def test_verifica_tudo_free_sulfur_dioxide():
  vinho = Vinho(name="Merlot", fixed_acidity=7.1, volatile_acidity=0.28, citric_acid=0.5, residual_sugar=2.0, chlorides=0.045, 
                free_sulfur_dioxide=-1, total_sulfur_dioxide=30.0, density=0.995, pH=7, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_tudo() == False

# Teste da verificação global para dioxido de sulfurio total
def test_verifica_tudo_total_sulfur_dioxide():
  vinho = Vinho(name="Merlot", fixed_acidity=7.1, volatile_acidity=0.28, citric_acid=0.5, residual_sugar=2.0, chlorides=0.045, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=-1, density=0.995, pH=7, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_tudo() == False

# Teste da verificação global para densidade
def test_verifica_tudo_density():
  vinho = Vinho(name="Merlot", fixed_acidity=7.1, volatile_acidity=0.28, citric_acid=0.5, residual_sugar=2.0, chlorides=0.045, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0, pH=7, sulphates=0.6, alcohol=12.5, quality=None)
  assert vinho.verifica_tudo() == False

# Teste da verificação global para alcool
def test_verifica_tudo_alcohol():
  vinho = Vinho(name="Merlot", fixed_acidity=7.1, volatile_acidity=0.28, citric_acid=0.5, residual_sugar=2.0, chlorides=0.045, 
                free_sulfur_dioxide=15.0, total_sulfur_dioxide=30.0, density=0.995, pH=7, sulphates=0.6, alcohol=-1, quality=None)
  assert vinho.verifica_tudo() == False