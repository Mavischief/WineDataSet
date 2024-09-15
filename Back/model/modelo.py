from joblib import load
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import pickle
import pandas as pd
import numpy as np
import chardet 

class Model:

    def preditor(model, x_input):
        """Realiza a predição da qualidade do vinho"""
        quality = model.predict(x_input)
        return quality


    def carrega_modelo(path):
        """Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra
        """
        
        if path.endswith('.pkl'):
            with open(path, 'rb') as file:
                model = pickle.load(file)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model

    def aplicando_scaler(x_input):
        """Ajusta a entrada para scaler na predição"""
        with open('./model/scaler.pkl', 'rb') as f:
            scaler = load(f)
        #scaler = pickle.load(open('./model/scaler.pkl', 'rb'))
        rescaledX = scaler.transform(x_input)
        return rescaledX

        
    
    
    

    

class Carregador:

    def carregar_dados(url: str, atributos: list):
        """ Carrega e retorna um DataFrame. Há diversos parâmetros 
        no read_csv que poderiam ser utilizados para dar opções 
        adicionais.
        """

        with open(url, 'rb') as f:
            result = chardet.detect(f.read(10000))  # Lê os primeiros 10.000 bytes
            print(result['encoding'])
        
        return pd.read_csv(url, names=atributos, header=0, encoding=result['encoding'],
                           skiprows=0, delimiter=',') # Esses dois parâmetros são próprios para uso deste dataset. Talvez você não precise utilizar
        

class PreProcessador:

    def preparar_form(form):
        """Prepara os dados do formulário recebido"""
        x_input = np.array([form.fixed_acidity,
                            form.volatile_acidity,
                            form.citric_acid,
                            form.residual_sugar,
                            form.chlorides, 
                            form.free_sulfur_dioxide,
                            form.total_sulfur_dioxide, 
                            form.density, 
                            form.pH, 
                            form.sulphates, 
                            form.alcohol])
        x_input = x_input.reshape(1,-1)
        return x_input

with open('./model/model.pkl', 'rb') as f:
    loaded_model = load(f)