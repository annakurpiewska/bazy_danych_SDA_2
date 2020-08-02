from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy import Sequence
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///:memory:')#, echo=True)
base = declarative_base()

class User(base):
    __tablename__ = 'user'
    id = Column(Integer,Sequence('user_id_seq'), primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    def __repr__(self):
        return f"User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})"

base.metadata.create_all(engine)


ed_user = User(name='ed', fullname='ed jones', nickname='ednickname')
print(ed_user.name)

sesion = sessionmaker(bind=engine)

session1 = sesion()
session1.add(ed_user)

our_user = session1.query(User).filter_by(name='ed').first()
print(our_user)

session1.commit()
session1.close()