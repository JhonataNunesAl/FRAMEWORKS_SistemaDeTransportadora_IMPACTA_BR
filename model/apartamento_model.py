from config import db
from model.morador_model import morador_apartamento  


class Apartamento(db.Model):
    __tablename__ = "Apartamentos"

    Numero_AP = db.Column(db.String(20), primary_key=True)
    Ocupado = db.Column(db.Boolean, default=False)
    Alugado = db.Column(db.Boolean, default=False)
    Venda = db.Column(db.Boolean, default=False)

 
    moradores = db.relationship(
        "Morador", 
        secondary=morador_apartamento,
        back_populates="apartamentos"
    )

    contas = db.relationship("Conta", back_populates="apartamento", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Apartamento {self.Numero_AP} - Ocupado {self.Ocupado} - Alugado {self.Alugado} - Venda {self.Venda}>"

    def to_dict(self):
        return {
            "Numero_AP": self.Numero_AP,
            "Ocupado": self.Ocupado,
            "Alugado": self.Alugado,
            "Venda": self.Venda,
            "moradores": [m.id for m in self.moradores]
        }
