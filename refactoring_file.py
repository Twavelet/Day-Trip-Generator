import random

def list_choice(list_index):
    list_of_destinations = ["St. Petersburg", "New York City", "Los Angeles", "Tuscon", "Moab"]
    list_of_restaurants = ["Bodega", "Peking Duck House", "Republique" , "Kingfisher", "Moab Brewery"]
    mode_of_transportation = ["Rental Car", "Uber", "Public Transportation", "Walking"]
    form_of_entertainment = ["Movie Theater", "Concert", "Hiking", "Museums", "Camping"]
    master_list = [list_of_destinations, list_of_restaurants, mode_of_transportation, form_of_entertainment]
    return master_list[list_index]


# def destination_randomizer(destination_selector):
def randomizer(list_selector):
    random_destination = random.choices(list_selector, k = 1)
    return random_destination
    # restaurant_selector[0], transportation_selector[0], entertainment_selector[0]

def itinerary_randomizer():
    list_type = []
    list_type.append(randomizer(list_choice(0)))
    list_type.append(randomizer(list_choice(1)))
    list_type.append(randomizer(list_choice(2)))
    list_type.append(randomizer(list_choice(3)))
    print(list_type[0], list_type[1], list_type[2], list_type[3])

itinerary_randomizer()


# def tentative_itinerary():
#     potential_itinerary = destination_randomizer(list_choice(0), list_choice(1), list_choice(2), list_choice(3))
#     print(f"Your potential itinerary is: {potential_itinerary}.")


    
# tentative_itinerary()


