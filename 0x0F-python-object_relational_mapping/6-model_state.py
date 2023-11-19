#!/usr/bin/python3
"""Start link class to table in database 
"""
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://hoigag:Hoigag_1337@localhost/hbtn_0e_6_usa', pool_pre_ping=True)
    Base.metadata.create_all(engine)