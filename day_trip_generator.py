import random

list_of_destinations = ["St. Petersburg", "New York City", "Los Angeles", "Tuscon", "Moab"]
list_of_restaurants = ["Bodega", "Peking Duck House", "Republique" , "Kingfisher", "Moab Brewery"]
mode_of_transportation = ["Rental Car", "Uber", "Public Transportation", "Walking"]
form_of_entertainment = ["Movie Theater", "Concert", "Hiking", "Museums", "Camping"]


def destination_generator(destination_selector):
    random_destination = random.choices(destination_selector, k = 1)
    print(random_destination[0])
    destination = input("Is this a destination you would like to visit? If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()
    while destination_selector:
        if destination == "y":
            print(f"Perfect, {random_destination[0]} is where you're headed!")
            return random_destination[0]
        elif destination == "n":
            random_destination = random.choices(destination_selector, k = 1)
            print(random_destination[0])
            destination = input("Does this destination sound more enticing?  If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()
            
verified_destination = destination_generator(list_of_destinations)

    
def restaurant_generator(restaurant_selector):
    random_restaurant = random.choices(restaurant_selector, k = 1)
    print(random_restaurant[0])
    restaurant = input("Does this restuarant sound appetizing to you? If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()
    while restaurant_selector:
        if restaurant == "y":
            print(f"Perfect, {random_restaurant[0]} is where you'll be dining!")
            return random_restaurant[0]
        elif restaurant == "n":
            random_restaurant = random.choices(restaurant_selector, k = 1)
            print(random_restaurant[0])
            restaurant = input("Does this restaurant seem more appealing?  If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()

verified_restaurant = restaurant_generator(list_of_restaurants)


def transportation_generator(transportation_selector):
    random_transportation = random.choices(transportation_selector, k = 1)
    print(random_transportation[0])
    transportation = input("Is this how you'd prefer to get around town? If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()
    while transportation_selector:
        if transportation == "y":
            print(f"Perfect, {random_transportation[0]} is how you'll be getting around town!")
            return random_transportation[0]
        elif transportation == "n":
            random_transportation = random.choices(transportation_selector, k = 1)
            print(random_transportation[0])
            transportation = input("Does this mode of transportation sound better?  If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()

verified_transportation = transportation_generator(mode_of_transportation)


def entertainment_generator(entertainment_selector):
    random_entertainment = random.choices(entertainment_selector, k = 1)
    print(random_entertainment[0])
    entertainment = input("Does this sound like something you'd enjoy doing? If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()
    while entertainment_selector:
        if entertainment == "y":
            print(f"Perfect, {random_entertainment[0]} is how you'll be spending your time while you're there!")
            return random_entertainment[0]
        elif entertainment == "n":
            random_entertainment = random.choices(entertainment_selector, k = 1)
            print(random_entertainment[0])
            entertainment = input("Does this seem like an activity you'd enjoy more?  If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()

verified_entertainment = entertainment_generator(form_of_entertainment)


def itinerary_generator():
    print(f"Awesome! Now that you have selected everything for your upcoming trip, here is your itinerary:\nDestination: {verified_destination}\nRestaurant: {verified_restaurant}\nTransportation: {verified_transportation}\nEntertainment: {verified_entertainment}")
    final_user_input = input("Does your itinerary suit your fancy? If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()
    while ():
        if final_user_input == "y":
            print("Awesome! All thats left to do now is pack and get on over there!")
        elif final_user_input == "n":
            return itinerary_generator()


itinerary_generator()