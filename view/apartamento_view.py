from flask import Blueprint, request, jsonify
from controller.apartamento_controller import (
    Buscar_Apartamento, Adicionar_Apartamento, Atualizar_Apartamento, Deletar_Apartamento,
    CamposVazio, ApartamentoNaoEncontrado, NenhumDado
)

apartamento_blueprint = Blueprint("apartamento", __name__)


@apartamento_blueprint.route('/apartamento', methods=['GET'])
def pegar_apartamentos():
    tipo = request.args.get("tipo")
    ocupado = request.args.get("Ocupado")
    apartamentos = Buscar_Apartamento(tipo, ocupado)
    return jsonify([ap.to_dict() for ap in apartamentos]), 200


@apartamento_blueprint.route('/apartamento', methods=['POST'])
def criar_apartamento():
    data = request.json
    try:
        apartamento = Adicionar_Apartamento(data)
        return jsonify(apartamento), 201
    except CamposVazio:
        return jsonify({'mensagem': 'Numero do apartamento obrigatório'}), 400


@apartamento_blueprint.route('/apartamento/<string:Numero_AP>', methods=['PUT'])
def atualizar_apartamento(Numero_AP):
    data = request.json
    try:
        apartamento_atualizado = Atualizar_Apartamento(Numero_AP, data)
        return jsonify(apartamento_atualizado), 200
    except ApartamentoNaoEncontrado:
        return jsonify({'messagem': 'Apartamento não encontrado ou não existe'}), 404
    except NenhumDado:
        return jsonify({'messagem': 'Nenhum dado enviado'}), 400
    except CamposVazio as e:
        return jsonify({'Mensagem': f'Os seguintes campos não podem estar vazios: {", ".join(e.args[0])}'}), 400


# ADICIONE ESTA ROTA PARA DELETAR APARTAMENTO
@apartamento_blueprint.route('/apartamento/<string:Numero_AP>', methods=['DELETE'])
def deletar_apartamento(Numero_AP):
    try:
        resultado = Deletar_Apartamento(Numero_AP)
        
        # Se a função retornar uma tupla (mensagem, status), use o status
        if isinstance(resultado, tuple):
            mensagem, status_code = resultado
            return jsonify(mensagem), status_code
        else:
            return jsonify(resultado), 200
            
    except ApartamentoNaoEncontrado:
        return jsonify({'mensagem': 'Apartamento não encontrado ou não existe'}), 404
    except Exception as e:
        return jsonify({'mensagem': f'Erro ao deletar apartamento: {str(e)}'}), 500