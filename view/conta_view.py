from flask import Blueprint, request, jsonify
from controller.conta_controller import (
    Buscar_Contas,
    Buscar_Conta_Por_ID,
    Adicionar_Conta,
    Atualizar_Conta,
    Deletar_Conta,
    ContaNaoEncontrada,
    CamposInvalidos,
    NenhumDado,
)

conta_blueprint = Blueprint("conta", __name__)


# ==============================
# ROTAS (Views)
# ==============================

@conta_blueprint.route("/contas", methods=["GET"])
def get_contas():
    """Lista todas as contas"""
    contas = Buscar_Contas()
    return jsonify(contas), 200


@conta_blueprint.route("/contas/<int:id>", methods=["GET"])
def get_conta_por_id(id):
    """Busca uma conta específica"""
    try:
        conta = Buscar_Conta_Por_ID(id)
        return jsonify(conta), 200
    except ContaNaoEncontrada:
        return jsonify({"mensagem": "Conta não encontrada"}), 404


@conta_blueprint.route("/contas", methods=["POST"])
def criar_conta():
    """Cria uma nova conta"""
    data = request.json
    try:
        conta = Adicionar_Conta(data)
        return jsonify(conta), 201
    except CamposInvalidos as e:
        return jsonify({"mensagem": str(e)}), 400


@conta_blueprint.route("/conta/<int:id>", methods=["PUT"])
def atualizar_conta(id):
    """Atualiza uma conta existente"""
    data = request.json
    try:
        resp = Atualizar_Conta(id, data)
        return jsonify(resp), 200
    except ContaNaoEncontrada:
        return jsonify({"mensagem": "Conta não encontrada"}), 404
    except NenhumDado:
        return jsonify({"mensagem": "Nenhum dado enviado"}), 400
    except CamposInvalidos as e:
        return jsonify({"mensagem": str(e)}), 400


@conta_blueprint.route("/conta/<int:id>", methods=["DELETE"])
def deletar_conta(id):
    """Deleta uma conta"""
    try:
        resp = Deletar_Conta(id)
        return jsonify(resp), 200
    except ContaNaoEncontrada:
        return jsonify({"mensagem": "Conta não encontrada"}), 404
