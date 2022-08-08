def list_collection(index_of_list):
    list_of_destinations = ["St. Petersburg", "New York City", "Los Angeles", "Tuscon", "Moab"]
    list_of_restaurants = ["Bodega", "Peking Duck House", "Republique" , "Kingfisher", "Moab Brewery"]
    mode_of_transportation = ["Rental Car", "Uber", "Public Transportation", "Walking"]
    form_of_entertainment = ["Movie Theater", "Concert", "Hiking", "Museums", "Camping"]
    master_list = [list_of_destinations, list_of_restaurants, mode_of_transportation, form_of_entertainment]
    return master_list[index_of_list]

chosen_list = list_collection(3)

print(chosen_list)