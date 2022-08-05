import random

list_of_destinations = ["St. Petersburg", "New York City", "Los Angeles", "Tuscon", "Moab"]
list_of_restaurants = ["Bodega", "Peking Duck House", "Republique" , "Kingfisher", "Moab Brewery"]
mode_of_transportation = ["Rental Car", "Uber", "Public Transportation", "Walking"]
form_of_entertainment = ["Movie Theater", "Concert", "Hiking", "Museums", "Camping"]

# def destination_generator(destination_selector):
#     while destination_selector:
#         random_destination = random.choices(destination_selector, k = 1)
#         print(random_destination)
#         destination = input("Is this a destination you would like to visit? If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()
#         if destination == "y":
#             chosen_destination = (f"Perfect, {random_destination} is where you're headed!")
#             return chosen_destination
#         elif destination == "n":
#             random_destination = random.choices(destination_selector, k = 1)
#             print(random_destination)
#             destination = input("Does this destination sound more enticing?  If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()
            
# verified_destination = destination_generator(list_of_destinations)
# print(verified_destination)
    
# def restaurant_generator(restaurant_selector):
#     while restaurant_selector:
#         random_restaurant = random.choices(restaurant_selector, k = 1)
#         print(random_restaurant)
#         restaurant = input("Does this restuarant sound appetizing to you? If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()
#         if restaurant == "y":
#             chosen_restaurant = (f"Perfect, {random_restaurant} is where you'll be dining!")
#             return chosen_restaurant
#         elif restaurant == "n":
#             random_restaurant = random.choices(restaurant_selector, k = 1)
#             print(random_restaurant)
#             restaurant = input("Does this restaurant seem more appealing?  If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()

# verified_restaurant = restaurant_generator(list_of_restaurants)
# print(verified_restaurant)

def transportation_generator(transportation_selector):
    while transportation_selector:
        random_transportation = random.choices(transportation_selector, k = 1)
        print(random_transportation)
        transportation = input("Is this how you'd prefer to get around town? If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()
        if transportation == "y":
            chosen_transportation = (f"Perfect, {random_transportation} is how you'll be getting around town!")
            return chosen_transportation
        elif transportation == "n":
            random_transportation = random.choices(transportation_selector, k = 1)
            print(random_transportation)
            transportation = input("Does this mode of transportation sound better?  If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()

verified_transportation = transportation_generator(mode_of_transportation)
print(verified_transportation)

def entertainment_generator(entertainment_selector):
    while entertainment_selector:
        random_entertainment = random.choices(entertainment_selector, k = 1)
        print(random_entertainment)
        entertainment = input("Does this sound like something you'd enjoy doing? If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()
        if entertainment == "y":
            chosen_entertainment = (f"Perfect, {random_entertainment} is how you'll be spending your time while you're there!")
            return chosen_entertainment
        elif entertainment == "n":
            random_entertainment = random.choices(entertainment_selector, k = 1)
            print(random_entertainment)
            entertainment = input("Does this seem like an activity you'd enjoy more?  If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()

verified_entertainment = entertainment_generator(form_of_entertainment)
print(verified_entertainment)