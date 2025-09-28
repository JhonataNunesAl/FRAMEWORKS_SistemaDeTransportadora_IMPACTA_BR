from config import db
from model.apartamento_model import Apartamento


class ApartamentoNaoEncontrado(Exception):
    pass


class CamposVazio(Exception):
    pass


class NenhumDado(Exception):
    pass


def Adicionar_Apartamento(dados):
    if 'Numero_AP' not in dados or dados['Numero_AP'] == '':
        raise CamposVazio()

    novo_apartamento = Apartamento(
        Numero_AP=dados['Numero_AP'],
        Ocupado=dados.get('Ocupado', False),
        Alugado=dados.get('Alugado', False),
        Venda=dados.get('Venda', False)
    )

    db.session.add(novo_apartamento)
    db.session.commit()

    return novo_apartamento.to_dict()


def Atualizar_Apartamento(Numero_AP, dados):
    apartamento = Apartamento.query.get(Numero_AP)
    if not apartamento:
        raise ApartamentoNaoEncontrado()

    if not dados:
        raise NenhumDado()

    campos = ['Ocupado', 'Alugado', 'Venda']
    campos_vazio = []
    for campo in campos:
        if campo in dados and (dados[campo] is None or dados[campo] == ""):
            campos_vazio.append(campo)

    if campos_vazio:
        raise CamposVazio(campos_vazio)

    if 'Ocupado' in dados:
        apartamento.Ocupado = dados['Ocupado']
    if 'Alugado' in dados:
        apartamento.Alugado = dados['Alugado']
    if 'Venda' in dados:
        apartamento.Venda = dados['Venda']

    db.session.commit()
    return {"messagem": "Informacoes atualizadas"}


def Buscar_Apartamento(tipo=None, ocupado=None):
    apartamento = Apartamento.query
    if tipo == "Alugado":
        apartamento = apartamento.filter_by(Alugado=False)
    elif tipo == "Venda":
        apartamento = apartamento.filter_by(Venda=True)

    if ocupado is not None:
        apartamento = apartamento.filter_by(Ocupado=(str(ocupado).lower() in ["true", "1", "sim", "yes", "y"]))

    return apartamento.all()
