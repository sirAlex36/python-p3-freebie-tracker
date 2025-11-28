#!/usr/bin/env python3

# Script goes here!

from models import Company, Dev, Freebie, create_session

# Create a session
session = create_session()

# Clear existing data
session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()
session.commit()

# Create companies
c1 = Company(name="Nintendo", founding_year=1889)
c2 = Company(name="GameFreak", founding_year=1989)
c3 = Company(name="Niantic", founding_year=2010)

# Create devs
d1 = Dev(name="Ash")
d2 = Dev(name="Misty")
d3 = Dev(name="Brock")

# Add companies and devs to session
session.add_all([c1, c2, c3, d1, d2, d3])
session.commit()

# Give some freebies
f1 = c1.give_freebie(d1, "Pokeball", 50)
f2 = c2.give_freebie(d2, "Potion", 30)
f3 = c1.give_freebie(d3, "T-shirt", 20)
f4 = c3.give_freebie(d1, "Sticker", 5)

# Add freebies to session
session.add_all([f1, f2, f3, f4])
session.commit()

print(f1.print_details())       
print(f2.print_details())        

print(d1.received_one("Sticker")) 
print(d2.received_one("Sticker")) 

# Give away freebie
d1.give_away(d2, f4)  
session.commit()
print(f4.print_details())        

# Oldest company
oldest = Company.oldest_company(session)
print(f"Oldest company: {oldest.name}") 

# Dev's companies
print([c.name for c in d2.companies])  

# Company devs
print([dev.name for dev in c1.devs])    
print("Seeding complete!")



