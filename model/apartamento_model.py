from config import db


class Apartamento(db.Model):
    __tablename__ = "Apartamentos"

    Numero_AP = db.Column(db.String(20), prymary_key = True)
    Ocupado = db.Column(db.Boolean, default = False)
    Alugado = db.Column(db.Boolean, default = False)
    Venda = db.Column(db.Boolean, default = False)


    morador_id = db.Column(db.Integer, db.ForegeinKey("Moradores.id"))
    morador = db.relationship("morador", back_populates="Apartamentos")
    
    def __repr__(self):
        return f"<Apartamento {self.Numero_AP} - Ocupado {self.Ocupado} - Alugado {self.Alugado} - Venda {self.Venda}"