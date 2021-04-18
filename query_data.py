#import all important packages and the classes defining the tables
import sqlalchemy
from sqlalchemy import create_engine, MetaData, update
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, Numeric
from sqlalchemy.orm import relationship, sessionmaker
import datetime
from create import Summary, Listings, Sales, Offices

#create engine and get metadata from it
engine = create_engine('sqlite:///realest.db')
metadata = sqlalchemy.MetaData(bind=engine)

#get the tables of the database
offices = sqlalchemy.Table('offices', metadata, autoload = True)
agents = sqlalchemy.Table('agents', metadata, autoload = True)
officeAgent = sqlalchemy.Table('officeAgent', metadata, autoload = True)
houses = sqlalchemy.Table('houses', metadata, autoload = True)
person = sqlalchemy.Table('person', metadata, autoload = True)
listings = sqlalchemy.Table('listings', metadata, autoload = True)
sales = sqlalchemy.Table('sales', metadata, autoload = True)
summary = sqlalchemy.Table('summary', metadata, autoload = True)

#create a summary list of all tables)
tables = [offices, agents, officeAgent, houses, person, listings, sales, summary]

#create first session
Session = sessionmaker(bind=engine)
session = Session()

#we print all neccessary information for the monthly report
print("Monthly report: ")
print()
#define the first daay of the moth for the query
firstofmonth = datetime.date(2021,1,1)
print("Top selling Offices: ")
with engine.connect() as con:
    #query database using sql for the top 5 best selling offices of the month
    t = con.execute('SELECT offices.id, offices.name, Sum(sub.sale_price) AS sp FROM offices JOIN (SELECT sale_price, listing_office FROM sales JOIN listings ON sales.listing = listings.id WHERE sales.date_of_sale > \'' + str(firstofmonth) + "\' ) AS sub ON offices.id =  sub.listing_office GROUP BY offices.id ORDER BY sp desc limit 5 " )
    #print the table
    for row in t:
        print("name: " + str(row[1]), " | overall sales: " + str(row[2]))

print()
print("Top selling Agents: ")
with engine.connect() as con:
    #query database to get the top 5 best selling agents of the month
    t = con.execute('SELECT agents.id, agents.firstname, agents.lastname, agents.email, Sum(sub.sale_price) AS sp FROM agents JOIN (SELECT sale_price, listing_agent FROM sales JOIN listings ON sales.listing = listings.id WHERE sales.date_of_sale > \'' + str(firstofmonth) + "\' ) AS sub ON agents.id =  sub.listing_agent GROUP BY agents.id ORDER BY sp desc limit 5 " )
    #print the results
    for row in t:
        print("name: " + str(row[1]) +" " + str(row[2]) + " eamil: " + str(row[3]) + "| overall sales: " + str(row[4]))

print()
print("Agent Commissions: ")
with engine.connect() as con:
    #query databse to get the commission of agents
    #agents without sales in the month will not be displayed
    t = con.execute('SELECT agents.id, agents.firstname, agents.lastname, agents.email, Sum(sub.commission) AS sp FROM agents JOIN (SELECT commission, listing_agent FROM sales JOIN listings ON sales.listing = listings.id WHERE sales.date_of_sale > \'' + str(firstofmonth) + "\' ) AS sub ON agents.id =  sub.listing_agent GROUP BY agents.id ORDER BY sp desc limit 5 " )
    #print results
    for row in t:
        print("name: " + str(row[1]) +" " + str(row[2]) + " eamil: " + str(row[3]) + "| commission: " + str(row[4]))


print()
print("Houses: ")
with engine.connect() as con:
    #query db to get listing and selling dates of all houses sold last month
    t = con.execute(' SELECT  date_of_listing, date_of_sale FROM sales JOIN listings ON sales.listing = listings.id  WHERE sales.date_of_sale > \'' + str(firstofmonth) + "\'" )
    #calculate the average number of days on the market
    daysdiff = 0
    numberofsales = 0
    for row in t:
        daysdiff += (datetime.datetime.strptime(row[1], '%Y-%m-%d').date()-datetime.datetime.strptime(row[0], '%Y-%m-%d').date()).days
        numberofsales += 1
    #print result
    print("average number of days on market: " + str(daysdiff / numberofsales))

with engine.connect() as con:
    #query db to get average sellig price of all houses sold this moth
    t = con.execute(' SELECT  AVG(sale_price) FROM sales JOIN listings ON sales.listing = listings.id  WHERE sales.date_of_sale > \'' + str(firstofmonth) + "\'" )
    #print results
    for row in t:
        print("average number selling price: " + str(row[0]))

print()
print("Zip codes with the highest average selling prices: ")
with engine.connect() as con:
    #query db to get top 5 zip codes with the highest average selling price last month
    t = con.execute('SELECT  houses.zip_code, AVG(sale_price) AS sp FROM houses JOIN (SELECT sale_price, house FROM sales JOIN listings ON sales.listing = listings.id WHERE sales.date_of_sale > \'' + str(firstofmonth) + "\' ) AS sub ON houses.id =  sub.house GROUP BY zip_code ORDER BY sp desc limit 5 " )
    #print result
    for row in t:
        print("zip code: " + str(row[0]) + " average selling price: " + str(row[1]))
