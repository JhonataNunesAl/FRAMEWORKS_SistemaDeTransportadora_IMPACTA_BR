from config import db
from model.morador_model import Morador
from model.apartamento_model import Apartamento


class MoradorNaoEncontrado(Exception):
    pass


class CamposInvalidos(Exception):
    pass


class NenhumDado(Exception):
    pass


def Adicionar_Morador(dados):
    if "nome" not in dados or not dados["nome"]:
        raise CamposInvalidos("Nome é obrigatório")
    if "idade" not in dados or not isinstance(dados["idade"], int):
        raise CamposInvalidos("Idade inválida")

    novo_morador = Morador(
        nome=dados["nome"],
        idade=dados["idade"]
    )

    if "apartamentos" in dados:
        for numero in dados["apartamentos"]:
            numero_str = str(numero)
            apartamento = Apartamento.query.get(numero_str)
            if apartamento:
                novo_morador.apartamentos.append(apartamento)

    db.session.add(novo_morador)
    db.session.commit()

    return novo_morador.to_dict()


def Buscar_Moradores():
    moradores = Morador.query.all()
    return [m.to_dict() for m in moradores]


def Atualizar_Morador(id, dados):
    morador = Morador.query.get(id)
    if not morador:
        raise MoradorNaoEncontrado()

    if not dados:
        raise NenhumDado()

    if "nome" in dados and dados["nome"]:
        morador.nome = dados["nome"]
    if "idade" in dados and isinstance(dados["idade"], int):
        morador.idade = dados["idade"]

    if "apartamentos" in dados:
        morador.apartamentos.clear()
        for numero in dados["apartamentos"]:
            numero_str = str(numero)
            apartamento = Apartamento.query.get(numero_str)
            if apartamento:
                morador.apartamentos.append(apartamento)

    db.session.commit()
    return {"mensagem": "Morador atualizado com sucesso"}


def Deletar_Morador(id):
    morador = Morador.query.get(id)
    if not morador:
        raise MoradorNaoEncontrado()

    db.session.delete(morador)
    db.session.commit()
    return {"mensagem": "Morador deletado com sucesso"}