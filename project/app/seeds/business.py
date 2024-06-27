from app.models import db, User, environment, SCHEMA, Business
from sqlalchemy.sql import text

def seed_businesses():

    # America
    Los_Danzantes = Business(
        owner_id= 4,
        title= "Los Danzantes Mexico City",
        address= "Parque Centenario 12",
        city= "Jardín Centenario",
        state= "Coyoacán",
        country= "Mexico",
        price= 2,
        category= "Mexican",
        lat= 19.432608,
        lng= -99.133209,
        phone_number= "555-555-5555",
        description= "Los Danzantes is often busy with a mix of locals and foreigners.",
        schedule= 'Monday: 5:00pm - 1:00am, Tuesday: :5:00pm - 1:00am, Wednesday: :5:00pm - 1:00am, Thursday: 5:00pm - 2:00am, Friday: 5:00pm - 4:00am, Saturday: 5:00pm - 4:00am, Sunday: 5:00pm - 2:00am'
    )

    Cotogna = Business(
        owner_id= 2,
        title= "Cotogna",
        address= "490 Pacific Ave.",
        city= "San Francisco",
        state= "California",
        country= "United States of America",
        price= 3,
        category= "Italian",
        lat= 37.7749,
        lng= 122.4194,
        phone_number= "555-555-5555",
        description= "Though rustic compared to high-end sibling Quince just next door, Michael and Lindsay Tusk’s casual offshoot would be elegant by any other standard",
        schedule= 'Monday: 5:00pm - 1:00am, Tuesday: :5:00pm - 1:00am, Wednesday: :5:00pm - 1:00am, Thursday: 5:00pm - 2:00am, Friday: 5:00pm - 4:00am, Saturday: 5:00pm - 4:00am, Sunday: 5:00pm - 2:00am'
    )

    Coni_Seafood = Business(
        owner_id= 2,
        title= "Coni'Seafood",
        address= "3544 W. Imperial Hwy",
        city= "Inglewood",
        state= "California",
        country= "United States of America",
        price= 3,
        category= "Mexican",
        lat= 34.0549,
        lng= 118.2426,
        phone_number= "555-555-5555",
        description= "Though rustic compared to high-end sibling Quince just next door, Michael and Lindsay Tusk’s casual offshoot would be elegant by any other standard",
        schedule= 'Monday: 5:00pm - 1:00am, Tuesday: :5:00pm - 1:00am, Wednesday: :5:00pm - 1:00am, Thursday: 5:00pm - 2:00am, Friday: 5:00pm - 4:00am, Saturday: 5:00pm - 4:00am, Sunday: 5:00pm - 2:00am'
    )
