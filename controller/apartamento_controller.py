from model.apartamento_model import Apartamento
from config import db

class ApartamentoNaoEncontrado(Exception):
    pass

class CamposVazio(Exception):
    pass

class NenhumDado (Exception):
    pass



def Adicionar_Apartamento(dados):
    campo_obrigatorio = ['Numero_AP']
    if campo_obrigatorio not in dados or dados[campo_obrigatorio] == '':
        return {"messagem": "Numero do apartamento obrigatorio"}
    
    novo_apartamento = Apartamento(
        Numero_AP = dados['Numero_AP'],
        Ocupado = dados['Ocupado'],
        Alugado = dados['Alugado'],
        Venda = dados['Venda']
    )

    db.session.add(novo_apartamento)
    db.session.commit()

    return {"messagem": "Novo apartamento adicionado ao banco de dados"}, 201


def Atualizar_Apartamento(Numero_AP, dados):
    apartamento = Apartamento.query.get(Numero_AP)
    if not apartamento:
        raise ApartamentoNaoEncontrado()

    if not dados:
        raise NenhumDado()

    campos = [
        'Ocupado', 'Alugado', 'Venda'
    ]
    campos_vazio = []
    for campo in campos: 
        if campo in dados and (dados[campo]is None or dados[campo]== ""):
            campos_vazio.append(campo)
    
    if campos_vazio:
        raise CamposVazio(campos_vazio)        
    
    apartamento.Ocupado = dados['Ocupado']
    apartamento.Alugado = dados['Alugado']
    apartamento.Venda = dados['Venda']

    db.session.commit()
    return{"messagem": "Informacoes atualizadas"}, 200


def String_Para_Booleano(valor, default = False):
    if valor is None:
        return default
    
    valor = str(valor).strip().lower()
    
    verdadeiros = {"true", "1", "sim", "yes", "y"}
    falsos = {"false", "0", "não", "nao", "no", "n"}
    
    if valor in verdadeiros:
        return True
    elif valor in falsos:
        return False
    else:
        return default


def Buscar_Apartamento(tipo=None, ocupado=None):
    apartamento = Apartamento.query
    if tipo == "Alugado":
        apartamento = apartamento.filter_by(Alugado=False)
    elif tipo == "Venda":
        apartamento = apartamento.filter_by(Venda=True)
    
    if ocupado is not None:
        apartamento = apartamento.filter_by(ocupado = String_Para_Booleano(ocupado))

    return apartamento.all()

