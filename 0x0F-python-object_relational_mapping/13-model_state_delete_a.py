#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sys import argv, exit
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(argv) != 4:
        print("please provide the right args")
        exit(1)
    user_name = argv[1]
    password = argv[2]
    dbname = argv[3]
    engine = create_engine(f"mysql\
+mysqldb://{user_name}:{password}\
@localhost/{dbname}", pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()
    states = session.query(State).filter(State.name.like("%a%")).all()
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
