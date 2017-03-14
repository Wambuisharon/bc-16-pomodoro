import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base= declarative_base()
 
class Pomodoro_timer(Base):

     __tablename__ = 'Pomodoro_timer'
     id =Column(String(250), primary_key=True)
     Task_name = Column(String(250), nullable = False)
     Task_duration = Column(String(250), nullable =False)
     Short_break = Column(String(250),nullable =False)
     Long_break = Column(String(250), nullable =False)
     Stop=Column(String(250), nullable=False)
     
     engine = create_engine('sqlite:///sqlalchemy_example.db')

     Base.metadata.create_all(engine)