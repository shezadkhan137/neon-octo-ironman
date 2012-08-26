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


class Film(Base):
    """"""
    __tablename__   = "films"
 
    id              = Column(Integer, primary_key=True)
    name            = Column(String)
    release_date    = Column(Date)
    showing         = Column(Boolean)


class Showing(Base):
    """"""
    __tablename__   = "showings"
 
    id              = Column(Integer, primary_key=True)
    time            = Column(DateTime)
    film            = relationship("Film", backref=backref("showings", order_by=time))
    cinema          = relationship("Cinema", backref=backref("showings", order_by=time))
 
# create tables in database
Base.metadata.create_all(engine)