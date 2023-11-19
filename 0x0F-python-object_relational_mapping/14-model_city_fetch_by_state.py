#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""

from model_state import Base, State
from model_city import City
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
    all_cities = session.query(State, City).\
        filter(State.id == City.state_id).order_by(City.id).all()
    for state, city in all_cities:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
