from app import app
from models import User, db, Event, Ticket
from datetime import datetime

users=[{
  "firstname": "Maureen",
  "lastname": "Chelangat",
  "email": "maureenchelangat955@gmail.com",
  "role": "ADMIN",
  "password": "test123"
}, {
  "firstname": "Tab",
  "lastname": "Dami",
  "email": "tdami1@shop-pro.jp",
  "role": "ADMIN",
  "password": "zC2&Y@4L0~Y!=w_"
}, {
  "firstname": "Javier",
  "lastname": "Fishenden",
  "email": "jfishenden2@clickbank.net",
  "role": "ADMIN",
  "password": "gI7`8D$6"
}, {
  "firstname": "Elisabetta",
  "lastname": "Frankis",
  "email": "efrankis3@unesco.org",
  "role": "ADMIN",
  "password": "nV1$2B_q@Rm7NM"
}, {
  "firstname": "Otes",
  "lastname": "Gainsbury",
  "email": "ogainsbury4@ed.gov",
  "role": "ADMIN",
  "password": "aM6{#HS6Q)QUH"
}, {
  "firstname": "Gran",
  "lastname": "Baunton",
  "email": "gbaunton5@opera.com",
  "role": "ADMIN",
  "password": "dN2*qJ)Y"
}, {
  "firstname": "Nevins",
  "lastname": "Worlidge",
  "email": "nworlidge6@de.vu",
  "role": "ADMIN",
  "password": "bH4=S*.MiD="
}, {
  "firstname": "Gilemette",
  "lastname": "Francino",
  "email": "gfrancino7@tripadvisor.com",
  "role": "ADMIN",
  "password": "aZ0&R3aF1.,gwa~K"
}, {
  "firstname": "Nixie",
  "lastname": "Cow",
  "email": "ncow8@google.com.au",
  "role": "USER",
  "password": "wB7\"\"+eL&i"
}, {
  "firstname": "Gael",
  "lastname": "Hamp",
  "email": "ghamp9@google.co.jp",
  "role": "USER",
  "password": "lW1*T)yLL"
}, {
  "firstname": "Rafaello",
  "lastname": "Towey",
  "email": "rtoweya@dion.ne.jp",
  "role": "ADMIN",
  "password": "sW1/>5`AQ,s+140"
}, {
  "firstname": "Jeromy",
  "lastname": "Hubbold",
  "email": "jhubboldb@prlog.org",
  "role": "USER",
  "password": "cH5_!>nCm|g"
}, {
  "firstname": "Elisha",
  "lastname": "Noah",
  "email": "enoahc@123-reg.co.uk",
  "role": "ADMIN",
  "password": "fB2<oH'tVY|"
}, {
  "firstname": "Edy",
  "lastname": "Beagley",
  "email": "ebeagleyd@icq.com",
  "role": "ADMIN",
  "password": "eF4}0Q(2Qgl"
}, {
  "firstname": "Faun",
  "lastname": "Leythley",
  "email": "fleythleye@loc.gov",
  "role": "ADMIN",
  "password": "qK3=(/.E!$TlM9c"
}, {
  "firstname": "Sharline",
  "lastname": "Scurr",
  "email": "sscurrf@51.la",
  "role": "ADMIN",
  "password": "sY4`hta6rnCsjNV"
}, {
  "firstname": "Casie",
  "lastname": "Stamp",
  "email": "cstampg@washingtonpost.com",
  "role": "ADMIN",
  "password": "sQ8$sW\"hkC&P"
}, {
  "firstname": "Karlotta",
  "lastname": "Nellis",
  "email": "knellish@amazon.de",
  "role": "USER",
  "password": "aL6*dI.b$eC6b=v,"
}, {
  "firstname": "Hubert",
  "lastname": "Lawtie",
  "email": "hlawtiei@tinyurl.com",
  "role": "ADMIN",
  "password": "iE0<talX"
}, {
  "firstname": "Phineas",
  "lastname": "Sheehy",
  "email": "psheehyj@tripadvisor.com",
  "role": "ADMIN",
  "password": "hE7&ZH%91$."
}]


events=[{
  "name": "STEM FAIR",
  "date": "2024-09-27",
  "start_time": "10:57",
  "location": "Glendale",
  "max_attendees": 205,
  "creator_id": 4
}, {
  "name": "ROBOTICS EXPO",
  "date": "2024-05-10",
  "start_time": "14:28",
  "location": "Maple Wood",
  "max_attendees": 244,
  "creator_id": 3
}, {
  "name": "STEM FAIR",
  "date": "2024-04-06",
  "start_time": "10:47",
  "location": "Algoma",
  "max_attendees": 195,
  "creator_id": 1
}, {
  "name": "STARTUP PITCH EVENT",
  "date": "2024-10-17",
  "start_time": "14:23",
  "location": "David",
  "max_attendees": 229,
  "creator_id": 2
}, {
  "name": "CODING COMPETITION",
  "date": "2024-10-15",
  "start_time": "21:27",
  "location": "2nd",
  "max_attendees": 191,
  "creator_id": 3
}, {
  "name": "DATA SCIENCE SYMPOSIUM",
  "date": "2024-12-23",
  "start_time": "17:44",
  "location": "Erie",
  "max_attendees": 221,
  "creator_id": 3
}, {
  "name": "STARTUP PITCH EVENT",
  "date": "2024-09-04",
  "start_time": "15:15",
  "location": "Mifflin",
  "max_attendees": 213,
  "creator_id": 2
}, {
  "name": "HACKATHON",
  "date": "2024-07-01",
  "start_time": "20:16",
  "location": "Knutson",
  "max_attendees": 227,
  "creator_id": 5
}, {
  "name": "CODING COMPETITION",
  "date": "2024-07-25",
  "start_time": "13:36",
  "location": "Florence",
  "max_attendees": 219,
  "creator_id": 1
}, {
  "name": "TECH CONFERENCE",
  "date": "2024-07-17",
  "start_time": "10:13",
  "location": "Hintze",
  "max_attendees": 58,
  "creator_id": 1
}, {
  "name": "INNOVATION SUMMIT",
  "date": "2024-09-24",
  "start_time": "20:39",
  "location": "Shelley",
  "max_attendees": 111,
  "creator_id": 1
}, {
  "name": "CODING COMPETITION",
  "date": "2024-11-13",
  "start_time": "17:17",
  "location": "Maple Wood",
  "max_attendees": 200,
  "creator_id": 2
}, {
  "name": "HACKATHON",
  "date": "2024-12-08",
  "start_time": "13:12",
  "location": "Dorton",
  "max_attendees": 222,
  "creator_id": 5
}, {
  "name": "STEM FAIR",
  "date": "2024-06-01",
  "start_time": "18:15",
  "location": "Delaware",
  "max_attendees": 170,
  "creator_id": 2
}, {
  "name": "STARTUP PITCH EVENT",
  "date": "2024-07-03",
  "start_time": "15:00",
  "location": "Brickson Park",
  "max_attendees": 98,
  "creator_id": 3
}, {
  "name": "CODING COMPETITION",
  "date": "2024-05-15",
  "start_time": "15:11",
  "location": "Harper",
  "max_attendees": 131,
  "creator_id": 3
}, {
  "name": "INNOVATION SUMMIT",
  "date": "2024-10-26",
  "start_time": "15:44",
  "location": "Del Mar",
  "max_attendees": 131,
  "creator_id": 1
}, {
  "name": "STEM FAIR",
  "date": "2024-12-13",
  "start_time": "14:07",
  "location": "Briar Crest",
  "max_attendees": 235,
  "creator_id": 3
}, {
  "name": "STEM FAIR",
  "date": "2024-09-14",
  "start_time": "9:31",
  "location": "Loomis",
  "max_attendees": 55,
  "creator_id": 3
}, {
  "name": "STARTUP PITCH EVENT",
  "date": "2024-07-23",
  "start_time": "22:44",
  "location": "Lawn",
  "max_attendees": 69,
  "creator_id": 1
}]

tickets=[{
  "ticket_type": "REGULAR",
  "reserved_by": 7,
  "event_id": 18,
  "price": 1500
}, {
  "ticket_type": "REGULAR",
  "reserved_by": 9,
  "event_id": 12,
  "price": 1871
}, {
  "ticket_type": "REGULAR",
  "reserved_by": 6,
  "event_id": 14,
  "price": 1700
}, {
  "ticket_type": "VIP",
  "reserved_by": 3,
  "event_id": 8,
  "price": 1500
}, {
  "ticket_type": "REGULAR",
  "reserved_by": 4,
  "event_id": 3,
  "price": 1500
}, {
  "ticket_type": "REGULAR",
  "reserved_by": 3,
  "event_id": 8,
  "price": 1500
}, {
  "ticket_type": "VIP",
  "reserved_by": 1,
  "event_id": 13,
  "price": 1500
}, {
  "ticket_type": "VIP",
  "reserved_by": 1,
  "event_id": 8,
  "price": 2000
}, {
  "ticket_type": "REGULAR",
  "reserved_by": 7,
  "event_id": 4,
  "price": 1680
}, {
  "ticket_type": "REGULAR",
  "reserved_by": 5,
  "event_id": 16,
  "price": 2000
}, {
  "ticket_type": "REGULAR",
  "reserved_by": 3,
  "event_id": 15,
  "price": 900
}, {
  "ticket_type": "REGULAR",
  "reserved_by": 8,
  "event_id": 20,
  "price": 700
}, {
  "ticket_type": "REGULAR",
  "reserved_by": 5,
  "event_id": 9,
  "price": 880
}, {
  "ticket_type": "REGULAR",
  "reserved_by": 8,
  "event_id": 5,
  "price": 1200
}, {
  "ticket_type": "VIP",
  "reserved_by": 2,
  "event_id": 1,
  "price": 1900
}, {
  "ticket_type": "VIP",
  "reserved_by": 9,
  "event_id": 10,
  "price": 500
}, {
  "ticket_type": "REGULAR",
  "reserved_by": 5,
  "event_id": 5,
  "price": 800
}, {
  "ticket_type": "VIP",
  "reserved_by": 10,
  "event_id": 3,
  "price": 1800
}, {
  "ticket_type": "REGULAR",
  "reserved_by": 4,
  "event_id": 19,
  "price": 1200
}, {
  "ticket_type": "REGULAR",
  "reserved_by": 2,
  "event_id": 15,
  "price": 1000
}]

with app.app_context():
    print("seeding...")
    db.session.add_all([Ticket(**ticket) for ticket in tickets])
    db.session.commit()
    print('seeding completed')


# with app.app_context():
#     print("Seeding events...")
#     for event_data in events:
#         # Convert date and start time strings to datetime objects
#         event_date = datetime.strptime(event_data['date'], '%Y-%m-%d')
#         event_start_time = datetime.strptime(event_data['start_time'], '%H:%M').time()

#         new_event = Event(
#             name=event_data['name'],
#             date=event_date,
#             start_time=event_start_time,
#             location=event_data['location'],
#             max_attendees=event_data['max_attendees'],
#             creator_id=event_data['creator_id']
#         )
#         db.session.add(new_event)
#     db.session.commit()
#     print("Seeding completed.")

