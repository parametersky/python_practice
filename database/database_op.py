from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant,MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
myfirstres = Restaurant(name = "Pizza Palace")
session.add(myfirstres)
session.commit()
firstResult = session.query(Restaurant).first()
print firstResult.name
