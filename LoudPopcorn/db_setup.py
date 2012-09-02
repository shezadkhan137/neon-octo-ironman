from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table, ForeignKey
from sqlalchemy import Integer, String, Float, Date, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
Base = declarative_base()
 
engine = create_engine('sqlite:///test.db',
                       echo=True)
 
metadata = MetaData(bind=engine)

film_cinema = Table('post_keywords', Base.metadata,
Column('film_id', Integer, ForeignKey('films.id')),
Column('cinema_id', Integer, ForeignKey('cinemas.id'))
)

locale_cinema = Table('locale_cinema', Base.metadata,
Column('locale_id', Integer, ForeignKey('locales.id')),
Column('cinema_id', Integer, ForeignKey('cinemas.id'))
)

class Cinema(Base):
    """"""
    __tablename__   = "cinemas"
 
    id              = Column(Integer, primary_key=True)
    name            = Column(String)
    chain           = Column(String)
    chain_id        = Column(String)
    address         = Column(String)
    lng             = Column(Float)
    lat             = Column(Float)
    films           = relationship('Film', secondary=film_cinema, backref='cinemas')
    locales         = relationship('Locale', secondary=locale_cinema, backref='cinemas')
    showings        = relationship("Showing", backref="cinema")

    def __eq__(self, other):
        if self.name == other.name and self.chain_id == other.chain_id:
            return True
        else:
            return False


class Film(Base):
    """"""
    __tablename__   = "films"
 
    id              = Column(Integer, primary_key=True)
    name            = Column(String)
    release_date    = Column(DateTime)
    showing         = Column(Boolean)
    showings        = relationship("Showing", backref="film")

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False


class Showing(Base):
    """"""
    __tablename__   = "showings"
 
    id              = Column(Integer, primary_key=True)
    time            = Column(DateTime)
    link            = Column(String)
    film_id         = Column(Integer, ForeignKey('films.id'))
    cinema_id       = Column(Integer, ForeignKey('cinemas.id'))
    #film            = relationship("Film", backref=backref("showings", order_by=time))
    #cinema          = relationship("Cinema", backref=backref("showings", order_by=time))

    def __eq__(self, other):
        if self.time == other.time and self.cinema == other.cinema and self.film == other.film:
            return True
        else:
            return False

class Locale(Base):
    """"""
    __tablename__   = "locales"
 
    id              = Column(Integer, primary_key=True)
    name            = Column(String)
    lat             = Column(Float)
    lng             = Column(Float)
    radius          = Column(Integer)

    def __eq__(self, other):
        if self.lat == other.lat and self.lng == other.lng and self.radius == other.radius:
            return True
        else:
            return False
 
# create tables in database
Base.metadata.create_all(engine)