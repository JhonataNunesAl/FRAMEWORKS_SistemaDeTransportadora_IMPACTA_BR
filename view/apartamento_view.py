from flask import Blueprint, request, jsonify
from controller.apartamento_controller import Buscar_Apartamento, Adicionar_Apartamento, Atualizar_Apartamento, CamposVazio, ApartamentoNaoEncontrado, NenhumDado

apartamento_blueprint = Blueprint('apartamento', __name__)

@apartamento_blueprint.route('/apartamento', methods=['GET'])
def pegar_apartamentos():
    tipo =  request.args.get("tipo")
    ocupado = request.args.get("Ocupado")
    apartamentos = Buscar_Apartamento(tipo, ocupado)
    return jsonify([ap.to_dict() for ap in apartamentos])


@apartamento_blueprint.route('/apartamento', methods = ['POST'])
def criar_apartamento():
    data = request.json
    try:
        professor = Adicionar_Apartamento(data)
        return jsonify(professor), 201
    except CamposVazio:
        return jsonify({'mensagem': 'Numero do apartamento obrigatorio'}), 400
    

@apartamento_blueprint.route('/apartamento/<int:Numero_AP>', methods=['PUT'])
def atualizar_apartamento(Numero_AP):
    data = request.json
    try:
        apartamento_atualizado = Atualizar_Apartamento(Numero_AP, data)
        return jsonify(apartamento_atualizado), 200
    except ApartamentoNaoEncontrado:
        return jsonify({'messagem': 'Apartamento nao encontrado ou nao existe'}), 404
    except NenhumDado:
        return jsonify({'messagem': 'Nenhum dado enviado'}), 400
    except CamposVazio as e:
        return jsonify({'Mensagem': f'Os seguintes campos nao podem estar vazios: {", ".join(e.args[0])}'}), 400


