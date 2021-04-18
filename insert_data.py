#import all important packages and the classes defining the tables
import sqlalchemy
from sqlalchemy import create_engine, MetaData, update
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, Numeric
from sqlalchemy.orm import relationship, sessionmaker
import datetime
from create import Summary, Listings

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

#Here I use session to commit the code in transactions. Either everyting within a session or nothing will be executed

#create first session
Session = sessionmaker(bind=engine)
session = Session()

#create fake data for the first table
O1 = [1001, 1002, 1003, 1004, 1005]
O2 = ["office1", "office2", "office3", "office4","office5"]
O3 = ["USA", "USA","USA","Germany", "Germany"]
O4 = ["SF", "NYC", "LA", "Berlin", "Hamburg"]

#input data and commit session
for i in range(len(O1)):
    session.execute(offices.insert().values(id = O1[i], name = O2[i], country = O3[i], location = O4[i]))

session.commit()
#create session
session = Session()
#create fake data for the next table
A1 = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 20010]
A2 = ["Tommas", "Arthur", "Alfie","John", "Grace", "Polly","Michael", "Ada", "Lizzy", "Finn"]
A3 = ["Shelby", "Shelby", "Solomons","Shelby", "Burgess", "Grey","Grey", "Shelby", "Some", "Shelby"]
A4 = ["Tommas@some.com", "Arthur@some.com", "Alfie@some.com","John@some.com", "Grace@some.com", "Polly@some.com","Michael@some.com", "Ada@some.com", "Lizzy@some.com", "Finn@some.com"]
#input data and commit session
for i in range(len(A1)):
    session.execute(agents.insert().values(id = A1[i], firstname = A2[i], lastname = A3[i], email = A4[i]))

session.commit()
#create session
session = Session()
#create fake data for the next table
OA1 = [3001, 3002, 3003, 3004, 3005, 3006, 3007, 3008, 3009, 30010, 30011, 30012, 30013, 30014, 30015]
OA2 = [1001, 1001, 1001, 1002, 1002, 1002, 1003, 1003, 1003, 1004, 1004, 1004, 1005, 1005, 1005]
OA3 = [2001, 2002, 2003, 2004, 2005, 2001, 2006, 2007, 2002, 2008, 2009, 2003, 20010, 2009, 2008]
#input data and commit session
for i in range(len(OA1)):
    session.execute(officeAgent.insert().values(id = OA1[i], office_id = OA2[i], agent_id = OA3[i]))

session.commit()
#create session
session = Session()
#create fake data for the next table
H1 = [4001, 4002, 4003, 4004, 4005, 4006, 4007, 4008, 4009, 40010, 40011, 40012, 40013, 40014, 40015, 40016, 40017, 40018, 40019, 40020]
H2 = [1234, 1234, 34534, 5678, 5678, 9876, 9876, 9876, 9090, 9090, 4567, 4567, 877, 877, 987, 987, 5432, 5432, 980, 980]
H3 = ["add1", "add2", "add3", "add4", "add5","add6", "add7", "add8", "add9", "add10","add11", "add12", "add13", "add14", "add15","add16", "add17", "add18", "add19", "add20"]
H4 = [2, 4, 3, 1, 1, 2, 3, 1, 2, 1, 3 ,1 , 4, 2, 2, 4, 1, 1 ,2 ,1]
H5 = [2, 4, 3, 1, 1, 2, 3, 1, 2, 1, 3 ,1 , 4, 2, 2, 4, 1, 1 ,2 ,1]
H6 = [200, 200, 300, 60, 90, 83, 96, 93, 100 ,100, 200, 20, 30, 60, 90, 83, 96, 93, 100 ,100]
H7 = [True, False, True, False, True, True, False, True, False, True,True, False, True, False, True,True, False, True, False, True]
#input data and commit session
for i in range(len(H1)):
    session.execute(houses.insert().values(id = H1[i], zip_code = H2[i], address = H3[i], bedrooms = H4[i], bathrooms = H5[i], squaremeeters = H6[i], garden = H7[i]))

session.commit()
#create session
session = Session()
#create fake data for the next table
P1 = [5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009, 50010, 50011, 50012, 50013, 50014, 50015, 50016, 50017, 50018, 50019, 50020, 50021, 50022, 50023, 50024, 50025]
P2 = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12", "f13", "f14", "f15", "f16", "f17", "f18", "f19", "f20", "f21", "f22", "f23", "f24", "25"]
P3 = ["l1", "l2", "l3", "l4", "l5", "l6", "l7", "l8", "l9", "l10", "l11", "l12", "l13", "l14", "l15", "l16", "l17", "l18", "l19", "l20", "l21", "l22", "l23", "l24", "25"]
P4 = ["f1@some.com", "f2@some.com", "f3@some.com", "f4@some.com", "f5@some.com", "f6@some.com", "f7@some.com", "f8@some.com", "f9@some.com", "f10@some.com", "f11@some.com", "f12@some.com", "f13@some.com", "f14@some.com", "f15@some.com", "f16@some.com", "f17@some.com", "f18@some.com", "f19@some.com", "f20@some.com", "f21@some.com", "f22@some.com", "f23@some.com", "f24@some.com", "25@some.com"]
#input data and commit session
for i in range(len(P1)):
    session.execute(person.insert().values(id = P1[i], firstname = P2[i], lastname = P3[i], email = P4[i]))

session.commit()
#create session
session = Session()
#create fake data for the next table
L1 = [6001, 6002, 6003, 6004, 6005, 6006, 6007, 6008, 6009, 60010, 60011, 60012, 60013, 60014, 60015, 60016, 60017, 60018, 60019, 60020]
L2 = [4001, 4002, 4003, 4004, 4005, 4006, 4007, 4008, 4009, 40010, 40011, 40012, 40013, 40014, 40015, 40016, 40017, 40018, 40019, 40020]
L3 = [5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009, 50010, 50011, 50012, 50013, 50014, 50015, 50016, 50017, 50018, 50019, 50020]
L4 = [10000000, 50000, 200000, 500000, 300000, 80000, 200000, 60000, 150000, 600000, 100000, 50000, 200000, 500000, 300000, 80000, 200000, 60000, 150000, 600000]
L5 = [datetime.date(2020,1,5), datetime.date(2020,1,7), datetime.date(2020,1,10), datetime.date(2020,1,30), datetime.date(2020,2,9), datetime.date(2020,2,22), datetime.date(2020,3,20), datetime.date(2020,3,22), datetime.date(2020,4,5),datetime.date(2021,4,6), datetime.date(2021,4,7), datetime.date(2021,2,5), datetime.date(2021,3,5), datetime.date(2021,1,5), datetime.date(2021,1,5), datetime.date(2021,1,5), datetime.date(2021,1,5), datetime.date(2021,1,5), datetime.date(2020,3,5),datetime.date(2020,1,5)]
L6 = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 20010, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 20010]
L7 = [1001, 1001, 1001,1002, 1002, 1003, 1003, 1004,1005, 1005, 1001, 1001, 1001,1002, 1002,1003, 1003, 1004,1005, 1005]
L8 = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
#input data and commit session
for i in range(len(L1)):
    session.execute(listings.insert().values(id = L1[i], house = L2[i], seller = L3[i], listing_price = L4[i], date_of_listing = L5[i], listing_agent = L6[i], listing_office = L7[i], sold = L8[i]))

session.commit()
#create session
session = Session()
session.execute(summary.insert().values(id = 7001, number_of_offices = session.query(offices).count(), number_of_agents = session.query(agents).count(), number_of_listings_open = session.query(listings).count(), number_of_sales = session.query(sales).count(), sum_sales = 0))

session.commit()
#we print the initial data before any sales
print("Initial Data")
print()
for table in tables:
    print("Table: " + str(table))
    print(metadata.tables[str(table)].columns.keys())
    s = table.select()
    #print(s)
    conn = engine.connect()
    result = conn.execute(s)
    #print(result)
    for row in result:
        print (row)
    print()

#now we will simulate some sales
#create fake data for the next table
S1 = [8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009, 80010]
S2 = [50021, 50022, 50023, 50024, 50025, 50016, 50017, 50018, 50019, 50020]
S3 = [6001, 6002, 6003, 6004, 6005, 6006, 6007, 6008, 6009, 60010]
S4 = [20000000, 60000, 100000, 500000, 300000, 80000, 200000, 60000, 150000, 600000]
S5 = [datetime.date(2020,1,5), datetime.date(2021,1,5), datetime.date(2021,1,11), datetime.date(2021,1,30), datetime.date(2021,2,9), datetime.date(2021,2,22), datetime.date(2021,3,20), datetime.date(2021,3,22), datetime.date(2021,4,5),datetime.date(2021,4,7)]
#we input the commission based based on the price of the house (loop over all prices)
S6 = []
for price in S4:
    if price >= 1000000:
        S6.append(str(0.04 * price))
    elif price >= 500000:
        S6.append(str(0.05 * price))
    elif price >= 200000:
        S6.append(str(0.06 * price))
    elif price >= 100000:
        S6.append(str(0.075 *price))
    else:
        S6.append(str(0.1 *price))

#we create a session for each sell
#this is important becuase it means that either all changes are made (updating summary and listings) or there is a rollback non of the sale information is stored
#this makes sure we dont have any inconsistancies (like house sold but still on listings as not sold)
for i in range(len(S1)):
    session = Session()
    #insert sale info into sales table
    session.execute(sales.insert().values(id = S1[i], buyer = S2[i], listing = S3[i], sale_price = S4[i], date_of_sale = S5[i], commission = S6[i]))
    #update summary table
    stmt1 = update(Summary).where(Summary.id == 7001).values(sum_sales = session.query(summary).first().sum_sales + S4[i] ).\
        execution_options(synchronize_session="fetch")
    result1 = session.execute(stmt1)
    stmt2 = update(Summary).where(Summary.id == 7001).values(number_of_sales = session.query(summary).first().number_of_sales + 1).\
        execution_options(synchronize_session="fetch")
    result2 = session.execute(stmt2)
    stmt3 = update(Summary).where(Summary.id == 7001).values(number_of_listings_open = session.query(summary).first().number_of_listings_open + 1 ).\
        execution_options(synchronize_session="fetch")
    result3 = session.execute(stmt3)
    #update listings tables
    stmt4 = update(Listings).where(Listings.id == S3[i]).values(sold = True).\
        execution_options(synchronize_session="fetch")
    result4 = session.execute(stmt4)
    session.commit()

#print the final database after sales are simulated
print()
print("Full Test Data: ")
print()
for table in tables:
    print("Table: " + str(table))
    print(metadata.tables[str(table)].columns.keys())
    s = table.select()
    #print(s)
    conn = engine.connect()
    result = conn.execute(s)
    #print(result)
    for row in result:
        print (row)
    print()
