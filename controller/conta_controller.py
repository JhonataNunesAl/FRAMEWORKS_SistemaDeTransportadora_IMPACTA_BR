from config import db
from model.conta_model import Conta
from model.morador_model import Morador
from model.apartamento_model import Apartamento



class ContaNaoEncontrada(Exception):
    pass


class CamposInvalidos(Exception):
    pass


class NenhumDado(Exception):
    pass




def Adicionar_Conta(dados):
    """Cria uma nova conta vinculada a um morador e apartamento."""
    campos_obrigatorios = ["valor", "morador_id", "numero_AP"]
    for campo in campos_obrigatorios:
        if campo not in dados or not dados[campo]:
            raise CamposInvalidos(f"Campo '{campo}' é obrigatório")

    try:
        valor = float(dados["valor"])
    except Exception:
        raise CamposInvalidos("Valor inválido")

    morador = Morador.query.get(int(dados["morador_id"]))
    if not morador:
        raise CamposInvalidos("Morador não encontrado para o ID informado")

    numero_ap_str = str(dados["numero_AP"])
    apartamento = Apartamento.query.get(numero_ap_str)
    if not apartamento:
        raise CamposInvalidos("Apartamento não encontrado para o número informado")

    conta = Conta(
        valor=valor,
        pendente=dados.get("pendente", True),
        morador_id=morador.id,
        numero_AP=numero_ap_str
    )

    db.session.add(conta)
    db.session.commit()
    return conta.to_dict()


def Buscar_Contas():

    contas = Conta.query.all()
    return [c.to_dict() for c in contas]


def Buscar_Conta_Por_ID(id):

    conta = Conta.query.get(id)
    if not conta:
        raise ContaNaoEncontrada()
    return conta.to_dict()


def Atualizar_Conta(id, dados):

    conta = Conta.query.get(id)
    if not conta:
        raise ContaNaoEncontrada()

    if not dados:
        raise NenhumDado()

    if "valor" in dados:
        try:
            conta.valor = float(dados["valor"])
        except Exception:
            raise CamposInvalidos("Valor inválido")


    if "pendente" in dados:
        conta.pendente = bool(dados["pendente"])


    if "morador_id" in dados:
        morador = Morador.query.get(dados["morador_id"])
        if not morador:
            raise CamposInvalidos("Morador não encontrado para o ID informado")
        conta.morador_id = dados["morador_id"]


    if "numero_AP" in dados:
        apartamento = Apartamento.query.get(dados["numero_AP"])
        if not apartamento:
            raise CamposInvalidos("Apartamento não encontrado para o número informado")
        conta.numero_AP = dados["numero_AP"]

    db.session.commit()
    return {"mensagem": "Conta atualizada com sucesso"}


def Deletar_Conta(id):

    conta = Conta.query.get(id)
    if not conta:
        raise ContaNaoEncontrada()

    db.session.delete(conta)
    db.session.commit()
    return {"mensagem": "Conta deletada com sucesso"}
