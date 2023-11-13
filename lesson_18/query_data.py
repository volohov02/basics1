from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///orm.sqlite', echo=True)

Base = declarative_base()
# create a configured "Session" class

class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.id}) {self.name}'

Session = sessionmaker(bind=engine)
# create a Session
session = Session()

# запрос с условием
news_data = session.query(News).filter(News.id > 10).all()

for data in news_data:
    print(data)
