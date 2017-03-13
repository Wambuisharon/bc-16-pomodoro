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
     Time_set = Column(String(250), nullable =False)
     First_break = Column(String(250),nullable =False)
     Second_break = Column(String(250), nullable =False)
     Third_break = Column(String(250), nullable= False )
     Forth_break = Column(String(200), nullable= False )
     Long_break =Column(String(140), nullable=False )

     
     engine = create_engine('sqlite:///sqlalchemy_example.db')

     Base.metadata.create_all(engine)