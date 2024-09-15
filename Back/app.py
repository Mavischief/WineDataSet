from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Vinho
from model.modelo import Model, PreProcessador, loaded_model


from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
vinho_tag = Tag(name="Vinho", description="Adição, visualização e remoção de vinhos à base")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/vinho', tags=[vinho_tag],
          responses={"200": VinhoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_vinho(form: VinhoSchema):
    """Adiciona um novo vinho à base de dados

    Retorna uma representação dos vinhos associados.
    """

    #Recebendo valores do formulário
    name = form.name
    fixed_acidity = form.fixed_acidity
    volatile_acidity = form.volatile_acidity
    citric_acid = form.citric_acid
    residual_sugar = form.residual_sugar
    chlorides = form.chlorides
    free_sulfur_dioxide=  form.free_sulfur_dioxide
    total_sulfur_dioxide = form.total_sulfur_dioxide
    density = form.density
    pH = form.pH
    sulphates = form.sulphates
    alcohol = form.alcohol


    #prepara os dados de entrada para serem entendidos
    x_input = PreProcessador.preparar_form(form)
    #aplica o scaler na entrada
    rescaledX = Model.aplicando_scaler(x_input)
    #local do modelo
    model_path = './model/model.pkl'
    #resgata o modelo treinado
    modelo = Model.carrega_modelo(model_path)
    #realiza a predição
    quality = int(Model.preditor(modelo, rescaledX)[0])

    vinho = Vinho(
        name = name,
        fixed_acidity = fixed_acidity,
        volatile_acidity = volatile_acidity,
        citric_acid = citric_acid,
        residual_sugar = residual_sugar,
        chlorides = chlorides,
        free_sulfur_dioxide = free_sulfur_dioxide,
        total_sulfur_dioxide = total_sulfur_dioxide,
        density = density,
        pH = pH,
        sulphates = sulphates,
        alcohol = alcohol,
        quality = quality
       ) 
    
    if vinho.verifica_tudo():

        logger.debug(f"Vinho '{vinho.name}' adicionado.")
        
        try:
            # criando conexão com a base
            session = Session()
            # adicionando cinho
            session.add(vinho)
            # efetivando o comando de adição de novo item na tabela
            session.commit()
            logger.debug(f"'{vinho.name}' adicionado.")
            return apresenta_vinho(vinho), 200

        except IntegrityError as e:
            # como a duplicidade do nome é a provável razão do IntegrityError
            error_msg = "Vinho de mesmo nome já salvo na base :/"
            logger.warning(f"Erro ao adicionar o vinho '{vinho.name}', {error_msg}")
            return {"message": error_msg}, 409

        except Exception as e:
            # caso de algum erro fora do previsto
            error_msg = "Não foi possível salvar novo item :/"
            logger.warning(f"Erro ao adicionar o vinho'{vinho.name}', {error_msg}")
            return {"message": error_msg}, 400
    
    else:
        # se o vinho foi inserido com dados invalidos
        error_msg = "Vinho com dados invalidos :/"
        logger.warning(f"Erro nos valores dos dados do vinho '{vinho.name}', {error_msg}")
        return {"message": error_msg}, 406



@app.get('/vinhos', tags=[vinho_tag],
         responses={"200": ListagemVinhosSchema, "404": ErrorSchema})
def get_vinhos():
    """Faz a busca por todos vinhos cadastrados

    Retorna uma representação da listagem de vinhos.
    """
    logger.debug(f"Coletando vinhos ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    vinhos = session.query(Vinho).all()

    if not vinhos:
        # se não há notas cadastradas
        return {"Vinho": []}, 200
    else:
        logger.debug(f"%d vinhos encontradas" % len(vinhos))
        # retorna a representação de nota de crédito
        print(vinhos)
        return apresenta_vinhos(vinhos), 200


@app.get('/vinho', tags=[vinho_tag],
         responses={"200": VinhoViewSchema, "404": ErrorSchema})
def get_vinho(query: VinhoBuscaSchema):
    """Faz a busca por um vinho a partir do nome do vinho

    Retorna uma representação de vinho.
    """
    vinho_name = query.name
    logger.debug(f"Coletando dados sobre do vinho #{vinho_name}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    vinho = session.query(Vinho).filter(Vinho.name == vinho_name).first()

    if not vinho:
        # se o vinho não foi encontrado
        error_msg = "Vinho não encontrado na base :/"
        logger.warning(f"Erro ao buscar o vinho '{vinho_name}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Nota econtrada: '{vinho.name}'")
        # retorna a representação de nota
        return apresenta_vinho(vinho), 200


@app.delete('/vinho', tags=[vinho_tag],
            responses={"200": VinhoDelSchema, "404": ErrorSchema})
def del_vinho(query: VinhoBuscaSchema):
    """Deleta um vinho a partir do nome da nota informado

    Retorna uma mensagem de confirmação da remoção.
    """
    vinho_name = unquote(unquote(query.name))
    print(vinho_name)
    logger.debug(f"Deletando dados sobre o vinho #{vinho_name}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Vinho).filter(Vinho.name == vinho_name).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Vinho {vinho_name} deletado")
        return {"message": "Vinho removido", "id": vinho_name}
    else:
        # se o vinho não foi encontrado
        error_msg = "Vinho não encontrado na base :/"
        logger.warning(f"Erro ao deletar o vinho #'{vinho_name}', {error_msg}")
        return {"message": error_msg}, 404
