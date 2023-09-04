from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant,Customer,Review


if __name__ == '__main__':
    engine = create_engine('sqlite:///restuarants.db')
    Session = sessionmaker(bind=engine)
    session = Session()

review = session.query(Review).filter_by(id=1).first()
print( review.review_customer())
print(review.review_restaurant())
print(review.full_review())



restaurant = session.query(Restaurant).filter_by(id=8).first()
print(restaurant.restaurant_reviews())
print(restaurant.restaurant_customers())
print("FAAAANCY")
print(Restaurant.fanciest_restaurants())


customer = session.query(Customer).filter_by(id=1).first()
print(customer.customer_reviews())
print(customer.customer_restaurants())
print(customer.full_name())  
print(session.query(Customer).first().restaurants)
print(session.query(Review).first().customer)
print(session.query(Customer).first().restaurants)
print(review.full_review())
print(customer.favorite_restaurant())
print(restaurant.all_reviews())