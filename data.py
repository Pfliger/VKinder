import sqlalchemy as sq
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
engine = sq.create_engine('Введите путь к базе')
Session = sessionmaker(bind=engine)
session = Session()



class User(Base):
    __tablename__ = 'user'
    id = sq.Column(sq.Integer, primary_key=True)
    vk_id = sq.Column(sq.Integer)
    first_name = sq.Column(sq.String)
    last_name = sq.Column(sq.String)




class FoundUser(Base):
    __tablename__ = 'founduser'
    id = sq.Column(sq.Integer, primary_key=True)
    vk_id = sq.Column(sq.Integer)
    first_name = sq.Column(sq.String)
    last_name = sq.Column(sq.String)
    top_photos = sq.Column(sq.String(1000))
    User_id = sq.Column(sq.Integer, sq.ForeignKey('user.id'))
    like = sq.Column(sq.Boolean)
    user = relationship(User)






def create_tables():
    Base.metadata.create_all(engine)



def add_user(user):
    session.expire_on_commit = False
    session.add(user)
    session.commit()

def add_user_list(user):
    session.expire_on_commit = False
    session.add_all(user)
    session.commit()

def get_viewed_user(user_id, users_list):
    list = session.query(FoundUser).filter(FoundUser.User_id == user_id).all()
    users = set()
    found_users = []
    for item in list:
        users.add(item.vk_id)
    for item in users_list:
        if item['id'] not in users:
            found_users.append(item)
    return found_users