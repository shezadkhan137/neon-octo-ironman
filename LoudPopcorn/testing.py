from db_setup import Cinema, Showing, Film
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime


engine = create_engine('sqlite:///test.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


test_cinema = Cinema(name="test", chain_id="001", chain="test")
test_film 	= Film(name="test film", release_date=datetime.datetime.now(), showing=True)
test_time = datetime.datetime.now()
test_showing_1 = Showing(time=test_time)
test_showing_2 = Showing(time=test_time)

session.add(test_cinema)
session.add(test_film)
session.add(test_showing_1)
session.add(test_showing_2 )
session.commit()

test_cinema.showings.append(test_showing_2)
test_cinema.showings.append(test_showing_1)
test_film.showings.append(test_showing_2)
test_film.showings.append(test_showing_1)

session.commit()
