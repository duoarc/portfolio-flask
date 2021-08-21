import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class ContactForm(Base):
    __tablename__ = 'contact'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    email = Column(String(80))
    message = Column(String(450))
    subject = Column(String(80))


engine = create_engine('sqlite:///resume.db')

Base.metadata.create_all(engine)