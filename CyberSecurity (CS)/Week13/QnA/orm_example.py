from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///example.db')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

    def __str__(self):
        return f"User({self.id},{self.name},{self.age})"


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Add users
user1 = User(name="Jake", age=25)
user2 = User(name="Tina", age=32)

session.add(user1)
session.add(user2)
session.commit()

# Get users
users = session.query(User).all()
for user in users:
    print(user)

# Update User
user = session.query(User).filter_by(id=2).first()
if user:
    user.name = "Alice"
    session.commit()


# Delete User
user = session.query(User).filter_by(id=1).first()
if user:
    session.delete(user)
    session.commit()
