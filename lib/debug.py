from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant,Customer,Review


if __name__ == '__main__':
    engine = create_engine('sqlite:///restuarants.db')
    Session = sessionmaker(bind=engine)
    session = Session()

review = session.query(Review).first()
print( review.review_customer())
print(review.review_restaurant())


restaurant = session.query(Restaurant).first()
print(restaurant.restaurant_reviews())
print(restaurant.restaurant_customers())

customer = session.query(Customer).first()
print(customer.customer_reviews())
print(customer.customer_restaurants())
print(customer.full_name())  
print(customer.favorite_restaurant())
print(session.query(Customer).first().restaurants)
print(session.query(Review).first().customer)
print(session.query(Customer).first().restaurants)