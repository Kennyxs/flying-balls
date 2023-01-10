import sqlalchemy as sql
import sqlalchemy.orm as orm

Base = orm.declarative_base()

class Players(Base):
    __tablename__ = 'record'
    idd  = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String(30))
    record = sql.Column(sql.Integer)
    def __repr__(self):
        return f'  name : {self.name}, record : {self.record}'
    
engine = sql.create_engine("sqlite:///record.db", echo = True)

Session = orm.sessionmaker()