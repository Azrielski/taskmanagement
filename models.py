from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

#initialise the db
Base = declarative_base()
engine =  create_engine("sqlite:///tasks.db")
Session = sessionmaker(bind=engine)
Session = Session()

#user model
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer , primary_key=True)
    name = Column(String, nullable=False, unique=True)
    tasks = relationship("Task", back_populates = "user", cascade= "all, delete")
    
    def __repre__(self):
        return f"User(id={self.id}, name'{self.name})"
    
    
#Task model
class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    status = Column(String, default="Pending")
    user_id = Column(Integer, ForeignKey("users.id"))
    
    user = relationship("User", back_populates = "tasks")
    
    def __repr__(self):
        return f"Task(id{self.id}, description='{self.description}', status='{self.status}, user = '{self.user_id}')"




Base.metadata.create_all(engine)
    