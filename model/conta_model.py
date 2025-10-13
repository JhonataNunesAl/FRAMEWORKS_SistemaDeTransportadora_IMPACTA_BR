from config import db


class Conta(db.Model):
    __tablename__ = "contas"

    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False)
    pendente = db.Column(db.Boolean, default=True)

    # FK → Moradores.id
    morador_id = db.Column(db.Integer, db.ForeignKey("Moradores.id"), nullable=False)

    # FK → Apartamentos.Numero_AP
    numero_AP = db.Column(db.String, db.ForeignKey("Apartamentos.Numero_AP"), nullable=False)

    # Relacionamentos
    morador = db.relationship("Morador", back_populates="contas")
    apartamento = db.relationship("Apartamento", back_populates="contas")

    def to_dict(self):
        return {
            "id": self.id,
            "valor": self.valor,
            "pendente": self.pendente,
            "morador_id": self.morador_id,
            "numero_AP": self.numero_AP
        }
