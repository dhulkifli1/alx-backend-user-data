#!/usr/bin/env python3
'''Contains SQLALCHEMY model User'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    '''SQLAlchemy model of User'''
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(1000), nullable=False)
    hashed_password = Column(String(1000), nullable=False)
    session_id = Column(String(1000))
    reset_token = Column(String(1000))
