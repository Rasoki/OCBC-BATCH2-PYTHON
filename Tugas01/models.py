from datetime import date, datetime
from config import db, ma
from marshmallow import fields
from sqlalchemy.orm import backref

class Avocado(db.Model):
    __tablename__ = 'avocado'
    # person_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Text)
    avgprice = db.Column(db.Real)
    totalvol = db.Column(db.Integer)
    avo_a = db.Column(db.Integer)
    avo_b = db.Column(db.Real)
    avo_c = db.Column(db.Real)
    type = db.Column(db.ForeignKey('avotype.typeid'))
    region_id = db.Column(db.ForeignKey('avoregion.regionid'))
    

class Avoregion(db.Model):
    __tablename__ = 'avoregion'
    regionid = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.Text)
    avocados = db.relatioship(
        'Avocado',
        backref = 'avoregion',
        cascade='all, delete, delete-orphan',
        single_parent=True,
        order_by='desc(Avocado.date)'
    )

class Avotype(db.Model):
    __tablename__ = 'avotype'
    typeid = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Text)

class AvoregionSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Avoregion
        # sqla_session = db.session
        load_instance = True

    notes = fields.Nested('AvoregionNoteSchema', default=[], many=True)

class AvoregionNoteSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    regionid = fields.Int()
    region = fields.Str()
   

class AvocadoSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Avocado
        # sqla_session = db.session
        load_instance = True

    avocados = fields.Nested("AvocadoAvoregionSchema", default=None)


class AvocadoAvoregionSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    date = fields.Str()
    avgprice = fields.Float()
    totalvol = fields.Int()
    avo_a = fields.Int()
    avo_b = fields.Float()
    avo_c = fields.Float()
    type = fields.Int()
    regionid = fields.Int()