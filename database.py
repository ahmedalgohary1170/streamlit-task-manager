from sqlalchemy import Column,Integer , String,create_engine
from sqlalchemy.orm import declarative_base,sessionmaker



engine = create_engine("sqlite:///todo.db")

Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer,primary_key=True)
    title = Column(String)
    description = Column(String)
    def __repr__(self):
        return f'id:{self.id}, title:{self.title}, description:{self.description}'



Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


def create_task(id:int,title:str,description:str):
    task = Task(id=id,title=title,description=description)
    session.add(task)
    session.commit()


def all_task():
    return session.query(Task).all()

def get_task(id):
    return session.query(Task).filter_by(id=id).first()



def update_task(id , title, description):
    task = get_task(id)
    task.title = title
    task.description = description
    session.commit()


def delete_task(id):
    if task := get_task(id):
        session.delete(task)
        session.commit()