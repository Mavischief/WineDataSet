from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import relationship
from typing import Union

from  model import Base

"""cria uma vinho e adiciona o item a tabela_Vinho"""

class Vinho(Base):
    __tablename__ = 'Tabela_de_vinho'

    name = Column(String(100), primary_key=True)
    fixed_acidity = Column(Float)
    volatile_acidity = Column(Float)
    citric_acid = Column(Float)
    residual_sugar = Column(Float)
    chlorides = Column(Float)
    free_sulfur_dioxide = Column(Float)
    total_sulfur_dioxide = Column(Float)
    density = Column(Float)
    pH = Column(Float)
    sulphates = Column(Float)
    alcohol = Column(Float)
    quality = Column(Integer, nullable=True)

    
    def __init__(self, name:str, fixed_acidity:float, volatile_acidity:float, citric_acid:float, residual_sugar:float, chlorides:float, free_sulfur_dioxide:float,
                 total_sulfur_dioxide:float, density:float, pH: float, sulphates:float, alcohol:float, quality:Integer):
        self.name = name
        self.fixed_acidity = fixed_acidity
        self.volatile_acidity = volatile_acidity
        self.citric_acid = citric_acid
        self.residual_sugar = residual_sugar
        self.chlorides = chlorides
        self.free_sulfur_dioxide = free_sulfur_dioxide
        self.total_sulfur_dioxide = total_sulfur_dioxide
        self.density = density
        self.pH = pH
        self.sulphates = sulphates
        self.alcohol = alcohol
        self.quality = quality

    # Verifica se o pH está dentro da faixa aceitável de 0 a 14
    def verifica_pH (self):
        if 0 <= self.pH <= 14:
            return True
        else:
            return False
    
    # Verifica se o acidez >= 0
    def verifica_acidez(self):
        if 0 <= self.fixed_acidity:
            return True
        else: 
            return False

    # Verifica se o volatilidade >= 0        
    def verifica_volatilidade(self):
        if 0 <= self.volatile_acidity:
            return True
        else:
            return False

    # Verifica se o acidez citrica >= 0    
    def verifica_citric(self):
        if 0 <= self.citric_acid:
            return True
        else:
            return False

    # Verifica se o açudar residual >= 0
    def verifica_sugar(self):
        if 0 <= self.residual_sugar:
            return True
        else:
            return False

    # Verifica se o cloridrato >= 0
    def verifica_cloridratos(self):
        if 0 <= self.chlorides:
            return True
        else:
            return False

    # Verifica se o dioxido de sulfurio livre >= 0
    def verifica_free_sulfur_dioxide(self):
        if 0 <= self.free_sulfur_dioxide:
            return True
        else:
            return False

    # Verifica se o dioxido de sulfurio toal >= 0
    def verifica_total_sulfur_dioxide(self):
        if 0 <= self.total_sulfur_dioxide:
            return True
        else:
            return False

    # Verifica se densidade > 0
    def verifica_density(self):
        if 0 < self.density:
            return True
        else:
            return False

    # Verifica se o sulfato >= 0
    def verifica_sulphates(self):
        if 0 <= self.sulphates:
            return True
        else:
            return False

    # Verifica se o alcohol >= 0       
    def verifica_alcohol(self):
        if 0 <= self.alcohol:
            return True
        else:
            return False

    # Verifica se a qualidade está dentro da faixa aceitável de 0 a 10
    def verifica_quality(self):
        if 0 <= self.quality <= 10:
            return True
        else:
            return False
    
    #método de verificação de erro global
    def verifica_tudo(self):
        resultado = (self.verifica_acidez() and self.verifica_volatilidade() and self.verifica_citric() and self.verifica_sugar() and self.verifica_cloridratos() and 
        self.verifica_free_sulfur_dioxide() and self.verifica_total_sulfur_dioxide() and self.verifica_density() and self.verifica_pH() and self.verifica_sulphates() and
        self.verifica_alcohol())
        return resultado