import random

def list_choice(index_of_list):
    list_of_destinations = ["St. Petersburg", "New York City", "Los Angeles", "Tuscon", "Moab"]
    list_of_restaurants = ["Bodega", "Peking Duck House", "Republique" , "Kingfisher", "Moab Brewery"]
    mode_of_transportation = ["Rental Car", "Uber", "Public Transportation", "Walking"]
    form_of_entertainment = ["Movie Theater", "Concert", "Hiking", "Museums", "Camping"]
    master_list = [list_of_destinations, list_of_restaurants, mode_of_transportation, form_of_entertainment]
    return master_list[index_of_list]


def randomizer(random_selector):
    random_destination = random.choices(random_selector, k = 1)
    return random_destination[0]

def destination_choice_evaluator(destination_choice):
    print(destination_choice)
    location = destination_choice
    destination = input("Is this a destination you would like to visit? If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()
    while destination_choice:
        if destination == "y" or destination == "yes":
            print(f"Perfect, {location} is where you're headed!")
            return location
        elif destination == "n" or destination == "no":
            new_location = randomizer(list_choice(0))
            print(new_location)
            destination = input("Does this destination sound more enticing?  If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()
            if destination == "y" or destination == "yes":
                print(f"Perfect, {new_location} is where you're headed!")
                return new_location


def restaurant_choice_evaluator(restaurant_choice):
    print(restaurant_choice)
    eatery = restaurant_choice
    restaurant = input("Does this restuarant sound appetizing to you? If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()
    while restaurant_choice:
        if restaurant == "y" or restaurant == "yes":
            print(f"Perfect, {eatery} is where you'll be dining!")
            return eatery
        elif restaurant == "n" or restaurant == "no":
            new_eatery = randomizer(list_choice(1))
            print(new_eatery)
            restaurant = input("Does this restaurant sound more appetizing to you?  If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()
            if restaurant == "y" or restaurant == "yes":
                print(f"Perfect, {new_eatery} is where you're headed!")
                return new_eatery


def transportation_choice_evaluator(transportation_choice):
    print(transportation_choice)
    movement = transportation_choice
    transportation = input("Is this how you'd prefer to get around town? If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()
    while transportation_choice:
        if transportation == "y" or transportation == "yes":
            print(f"Perfect, {movement} is how you'll be getting around town!")
            return movement
        elif transportation == "n" or transportation == "no":
            new_movement = randomizer(list_choice(2))
            print(new_movement)
            transportation = input("Does this restaurant sound more appetizing to you?  If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()
            if transportation == "y" or transportation == "yes":
                print(f"Perfect, {new_movement} is how you'll be getting around!")
                return new_movement               


def entertainment_choice_evaluator(entertainment_choice):
    print(entertainment_choice)
    amusement = entertainment_choice
    entertainment = input("Does this sound like something you'd enjoy doing? If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()
    while entertainment_choice:
        if entertainment == "y" or entertainment == "yes":
            print(f"Perfect, {amusement} is how you'll be spending your time while you're there!")
            return amusement
        elif entertainment == "n" or entertainment == "no":
            new_amusement = randomizer(list_choice(3))
            print(new_amusement)
            transportation = input("Does this activity sound more enjoyable?  If so, type 'y' for 'Yes' or 'n' for 'No.' ").lower()
            if transportation == "y" or transportation == "yes":
                print(f"Perfect, {new_amusement} is how you'll be spending your time!")
                return new_amusement

#Step 1 pass list into list choice to select the intended list
# list choice should have the index of the intended list for each corresponding function
chosen_list = list_choice(1)
#Step 2 pass the list choice function into destination randomizer to get a single location
destination_list = randomizer(list_choice(0))
restaurant_list = randomizer(list_choice(1))
transportation_list = randomizer(list_choice(2))
entertainment_list = randomizer(list_choice(3))
#Step 3 pass the destination randomizer into the destination choice evaluator to determine a final location
chosen_destination = destination_choice_evaluator(destination_list)
chosen_restaurant = restaurant_choice_evaluator(restaurant_list)
chosen_transportation = transportation_choice_evaluator(transportation_list)
chosen_entertainment = entertainment_choice_evaluator(entertainment_list)

