from sqlalchemy import ForeignKey, Column, Integer, String, MetaData,Float,create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)
engine = create_engine('sqlite:///restuarants.db')
Session = sessionmaker(bind=engine)
session = Session()
class Restaurant(Base):
    __tablename__="restaurants"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    price=Column(Float,nullable=False)

    def __repr__(self):
        return f'<Restaurant {self.name}>'
    

class Customer(Base):
    __tablename__="customers"  
    id=Column(Integer,primary_key=True) 
    first_name=Column(String) 
    last_name=Column(String)
    
    def __repr__(self):
        return f"<Customer {self.first_name} ,{self.last_name}>"

class Review(Base):
    __tablename__ = "reviews"
    
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    
    restaurant = relationship("Restaurant", backref=backref("reviews"))
    customer = relationship("Customer", backref=backref("reviews"))
    
    def review_customer(self):
        
        return self.customer
    def review_restaurant(self):
        
        return self.restaurant
    
    def __repr__(self):
        return f"<Review {self.star_rating}>"
