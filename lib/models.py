from sqlalchemy import ForeignKey, Column, Integer, String, MetaData,Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)
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
        return f"<Customer {self.first_name}{self.last_name}"