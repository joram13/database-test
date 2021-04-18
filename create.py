import sqlalchemy
from sqlalchemy import create_engine
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, Numeric, Index
from sqlalchemy.orm import relationship, sessionmaker

#create engine and base
engine = create_engine('sqlite:///realest.db')
Base = declarative_base()

#define classes that are the tables of the database

    #indexing
    #I create indexes for all rows that are searched in the later prompts or that might get searched
    #I used datanormalization by splitting up the organizatin into normalized tables
    #the tables office, agents, person, houses just have information about the specific
    #the table officeAgents is a many to many relationship between affices and Agents
    #the tables listings and sales store all the information about specific transactions
    #the sales table has the listings id to avoid repetative data
    #the summary table stores some summary informaiton


class Offices(Base):
    """
    This table stores all important information about the offices.
    """

    __tablename__ = 'offices'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), index = True)
    country = Column(String(50), index = True)
    location = Column(String(50), index = True)

    officeAgent = relationship("OfficeAgent", backref="Offices")
    listings = relationship("Listings", backref="Offices")



class Agents(Base):
    """
    This table stores all the important information about agents.
    """

    __tablename__= 'agents'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(50), index = True)
    lastname = Column(String(50), index = True)
    email = Column(String(50))

    officeAgent = relationship("OfficeAgent", backref="agents")
    listings = relationship("Listings", backref="agents")

    #__table_args__ = ((Index('search', "firstname", "lastname")))

class OfficeAgent(Base):
    """
    This table stores the many to many office agent relationship.
    """

    __tablename__= 'officeAgent'

    id = Column(Integer, primary_key=True)
    office_id = Column(Integer, ForeignKey('offices.id'), index=True)
    agent_id = Column(Integer, ForeignKey('agents.id'), index=True)


class Houses(Base):
    """
    This table stores all information about houses.
    """

    __tablename__ = 'houses'

    id = Column(Integer, primary_key=True)
    zip_code = Column(Integer, index = True)
    address = Column(String(50))
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    squaremeeters = Column(Integer)
    garden = Column(Boolean)

    listings = relationship("Listings", backref="houses")




class Person(Base):
    """
    This table stores all information about persons.
    These are potential buyers or sellers.
    """

    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(50), index = True)
    lastname = Column(String(50), index=True)
    email = Column(String(50))

    listings = relationship("Listings", backref="person")
    sales = relationship("Sales", backref="person")





class Listings(Base):
    """
    This table stores information about listings.
    """

    __tablename__ = 'listings'

    id = Column(Integer, primary_key=True)
    house = Column(Integer, ForeignKey('houses.id'), index = True)
    seller = Column(Integer, ForeignKey('person.id'), index = True)
    listing_price = Column(Integer, index = True)
    date_of_listing = Column(Date, index =True)
    listing_agent = Column(Integer, ForeignKey('agents.id'), index = True)
    listing_office = Column(Integer, ForeignKey('offices.id'), index = True)
    sold  = Column(Boolean, index = True)

    sales = relationship("Sales", backref="listings")

class Sales(Base):
    """
    This table stores information about sales.
    """

    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True)
    buyer = Column(Integer, ForeignKey('person.id'), index = True)
    listing = Column(Integer, ForeignKey('listings.id'), index = True)
    sale_price = Column(Integer, index = True)
    date_of_sale = Column(Date, index = True)
    commission = Column(String, index = True)



class Summary(Base):
    """
    This table stores a summary about offices, agents, and sales.
    """

    __tablename__ = 'summary'

    id = Column(Integer, primary_key=True)
    number_of_offices = Column(Integer, index = True)
    number_of_agents = Column(Integer, index = True)
    number_of_listings_open = Column(Integer, index = True)
    number_of_sales = Column(Integer, index = True)
    sum_sales = Column(Integer, index = True)


Base.metadata.create_all(engine)
