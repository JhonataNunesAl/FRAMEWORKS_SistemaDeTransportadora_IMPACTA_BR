from flask import Blueprint, request, jsonify
from controller.morador_controller import (
    Buscar_Moradores, Adicionar_Morador, Atualizar_Morador, Deletar_Morador,
    MoradorNaoEncontrado, CamposInvalidos, NenhumDado
)

morador_blueprint = Blueprint("morador", __name__)


@morador_blueprint.route("/moradores", methods=["GET"])
def get_moradores():
    moradores = Buscar_Moradores()
    return jsonify(moradores), 200


@morador_blueprint.route("/moradores", methods=["POST"])
def criar_morador():
    data = request.json
    try:
        morador = Adicionar_Morador(data)
        return jsonify(morador), 201
    except CamposInvalidos as e:
        return jsonify({"mensagem": str(e)}), 400


@morador_blueprint.route("/morador/<int:id>", methods=["PUT"])
def atualizar_morador(id):
    data = request.json
    try:
        resp = Atualizar_Morador(id, data)
        return jsonify(resp), 200
    except MoradorNaoEncontrado:
        return jsonify({"mensagem": "Morador não encontrado"}), 404
    except NenhumDado:
        return jsonify({"mensagem": "Nenhum dado enviado"}), 400
    except CamposInvalidos as e:
        return jsonify({"mensagem": str(e)}), 400


@morador_blueprint.route("/morador/<int:id>", methods=["DELETE"])
def deletar_morador(id):
    try:
        resp = Deletar_Morador(id)
        return jsonify(resp), 200
    except MoradorNaoEncontrado:
        return jsonify({"mensagem": "Morador não encontrado"}), 404
