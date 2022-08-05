import random

list_of_destinations = ["St. Petersburg", "New York City", "Los Angeles", "Tuscon", "Moab"]
list_of_restaurants = ["Bodega", "Peking Duck House", "Republique" , "Kingfisher", "Moab Brewery"]
mode_of_transportation = ["Rental Car", "Uber", "Public Transportation", "Walking"]
list_of_entertainment = ["Movie Theater", "Concert", "Hiking", "Museums", "Camping"]

def destination_generator(destination_selector):
    while destination_selector:
        random_destination = random.choices(destination_selector, k = 1)
        print(random_destination)
        destination = input("Is this a destination you would like to visit? If so, type 'y' for 'Yes' or 'n' for 'No.'").lower()
        if destination == "n":
            random_destination = random.choices(destination_selector, k = 1)
            print(random_destination)
            destination = input("Does this destination sound more enticing?  If so, type 'y' for 'Yes' or 'n' for 'No.'").lower()
        elif destination == "y":
            chosen_destination = (f"Perfect, {random_destination} is where you're headed!")
            return chosen_destination

verified_destination = destination_generator(list_of_destinations)
print(verified_destination)
    
