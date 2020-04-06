destinations = [
'Paris, France',
'Shanghai, China',
'Los Angeles, USA',
'São Paulo, Brazil',
'Cairo, Egypt']

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(dest):
  #for i in range(len(destinations)):
  #  if dest == destinations[i]:
  #    return i
  return destinations.index(dest)
  
#print(get_destination_index("Cairo, Egypt"))


def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
#print(test_destination_index)

#attractions = [[], [], [], [], []]

attractions = [ [] for x in destinations]

#print(attractions, "goood")

def add_attraction(dest, attr):
  try:
    destination_index = get_destination_index(dest)
  except ValueError:
    return
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attr)
  return

add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(dest, interests):
  destination_index = get_destination_index(dest)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  possible_attraction = [x for x in attractions_in_city]
  
  for x in possible_attraction:
    #print(x, "|| possible_attraction")
    attraction_tags = x[1]
    #print(attraction_tags, "                || attraction_tags")
    
    for i in interests:
      #print(i, "                             || interests")
      if i in attraction_tags:
        #print(i, "                         || if")
        attractions_with_interest.append(x[0]) 
  return attractions_with_interest

la_arts = find_attractions("Los Angeles, USA", ["art"])
#print(la_arts)
  
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler[1] + ": "
  for i in traveler_attractions:
    interests_string += i
    if i != traveler_attractions[-1]:
      interests_string += ", "
    else:
      interests_string += "."
  return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)

  
