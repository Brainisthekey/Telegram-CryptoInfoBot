from utils.db_api.database import db
from sqlalchemy import sql, Column, Sequence, String


class MenuOptions(db.Model):
    __tablename__ = 'menuoptions'
    query: sql.Select

    id = Column(db.Integer, Sequence("user_id_seq"), primary_key=True)
    category_code = Column(db.String(20))
    category_name = Column(db.String(50))

    subcategory_code = Column(db.String(20))
    subcategory_name = Column(db.String(50))

    name = Column(db.String(50))
    photo = Column(db.String(250))