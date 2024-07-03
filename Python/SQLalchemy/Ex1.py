from urllib.parse import quote_plus
from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()
# create table
class Product(Base):
    __tablename__ = 'Product'
    id = Column(Integer,primary_key=True)
    productname = Column(String(50))
    productemail = Column(String(50))
    
engine = create_engine("mysql+pymysql://root:%s@localhost:3306/sakila" % quote_plus("rps@123"))
Base.metadata.create_all(engine)

# insert record into table
from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine)
dbsession = session()

product = Product(productname = 'shampoo', productemail = 'shampoo@godraj.com')

dbsession.add(product)
dbsession.commit()