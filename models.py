from sqlalchemy import Column, String, Integer, Float,create_engine,select
from sqlalchemy.orm import declarative_base,sessionmaker


engine = create_engine('sqlite:///database.db')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,unique=True)
    full_name = Column(String)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

class Model: 
    def fetch_user_password(email): 
        password = session.execute(select(User.password))
        return password
