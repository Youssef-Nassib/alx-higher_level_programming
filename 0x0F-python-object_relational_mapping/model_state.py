from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Declare a base for your classes (a metaclass)
Base = declarative_base()

# Define the State class
class State(Base):
    __tablename__ = 'states'  # Links to the MySQL table states
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)  # Primary key, auto-generated
    name = Column(String(128), nullable=False)  # String column with max 128 characters

# Connect to the MySQL server
engine = create_engine('mysql+mysqlconnector://username:password@localhost:3306/dbname')

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create all tables stored in this metadata (necessary the first time)
Base.metadata.create_all(engine)

# Example of adding a new State to the database
new_state = State(name="New York")
session.add(new_state)
session.commit()

# Example of querying the database
states = session.query(State).order_by(State.id).all()
for state in states:
    print(state.id, state.name)

# Close the session
session.close()
