from pydantic import BaseModel
from typing import List
from model.vinho import Vinho


class VinhoSchema(BaseModel):
    """ Define a representação de um novo vinho a ser inserido """
    name: str = "Carbenet"
    fixed_acidity: float = 6.2
    volatile_acidity: float = 0.66
    citric_acid: float = 0.48
    residual_sugar: float = 1.2
    chlorides: float = 0.029
    free_sulfur_dioxide: float = 29
    total_sulfur_dioxide: float = 75
    density: float = 0.9892
    pH: float = 3.33
    sulphates: float = 0.39
    alcohol: float = 12.8

class VinhoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será feita apenas com base no nome do vinho. """
    name: str = "Teste"


class ListagemVinhosSchema(BaseModel):
    """ Define como uma listagem de NC será retornada."""
    vinhos:List[VinhoSchema]


def apresenta_vinhos(vinhos: List[Vinho]):
    """ Retorna uma representação de vinho seguindo o schema definido em VinhoViewSchema. """
    result = []
    for vinho in vinhos:
        result.append({
            "name": vinho.name,
            "fixed_acidity": vinho.fixed_acidity,
            "volatile_acidity": vinho.volatile_acidity,
            "citric_acid": vinho.citric_acid,
            "residual_sugar": vinho.residual_sugar,
            "chlorides": vinho.chlorides,
            "free_sulfur_dioxide": vinho.free_sulfur_dioxide,
            "total_sulfur_dioxide": vinho.total_sulfur_dioxide,
            "density": vinho.density,
            "pH": vinho.pH,
            "sulphates": vinho.sulphates,
            "alcohol": vinho.alcohol,
            "quality": vinho.quality
        })

    return {"vinhos": result}


class VinhoViewSchema(BaseModel):
    """ Define como o Vinho será retornado"""
    name: str = "Carbenet"
    fixed_acidity: float = 6.2
    volatile_acidity: float = 0.66
    citric_acid: float = 0.48
    residual_sugar: float = 1.2
    chlorides: float = 0.029
    free_sulfur_dioxide: float = 29
    total_sulfur_dioxide: float = 75
    density: float = 0.9892
    pH: float = 3.33
    sulphates: float = 0.39
    alcohol: float = 12.8
    quality: int = 8


class VinhoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição de remoção."""
    message: str
    name: str

def apresenta_vinho(vinho: Vinho):
    """ Retorna uma representação de vinho seguindo o schema definido em VinhoViewSchema."""
    return {
        "name": vinho.name,
        "fixed_acidity": vinho.fixed_acidity,
        "volatile_acidity": vinho.volatile_acidity,
        "citric_acid": vinho.citric_acid,
        "residual_sugar": vinho.residual_sugar,
        "chlorides": vinho.chlorides,
        "free_sulfur_dioxide": vinho.free_sulfur_dioxide,
        "total_sulfur_dioxide": vinho.total_sulfur_dioxide,
        "density": vinho.density,
        "pH": vinho.pH,
        "sulphates": vinho.sulphates,
        "alcohol": vinho.alcohol,
        "quality": vinho.quality
    }
