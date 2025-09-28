from config import db


morador_apartamento = db.Table(
    "morador_apartamento",
    db.Column("morador_id", db.Integer, db.ForeignKey("Moradores.id"), primary_key=True),
    db.Column("apartamento_numero", db.String(20), db.ForeignKey("Apartamentos.Numero_AP"), primary_key=True)
)


class Morador(db.Model):
    __tablename__ = "Moradores"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)


    apartamentos = db.relationship(
        "Apartamento",  
        secondary=morador_apartamento,
        back_populates="moradores"
    )

    def __repr__(self):
        return f"<Morador {self.nome} - Idade {self.idade}>"

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "apartamentos": [ap.Numero_AP for ap in self.apartamentos]
        }
