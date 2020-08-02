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

    # def __str__(self):
    #     return('test')

base.metadata.create_all(engine) # wrzuć tabele do bazy danych


ed_user = User(name='ed', fullname='ed jones', nickname='ednickname')
print(ed_user.name)

session = sessionmaker(bind=engine)

session1 = session()
session1.add(ed_user)



session1.commit()
session1.close()



session2 = session()

our_user = session1.query(User).filter_by(name='ed').first()
print(our_user)
print(f"id > {our_user.id}  name > {our_user.name}  fullname > {our_user.fullname}")

session2.commit()
session2.close()
