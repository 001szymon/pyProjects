class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
  def __repr__(self):
    return "{a}. \"{t}\". {y}, {m}. OWNER: {o_n}, {o_l}.".format(a=self.artist, t=self.title, m=self.medium, y=self.year, o_n=self.owner.name, o_l=self.owner.location)
  
class Marketplace:
  def __init__(self):
    self.listings = []
  def add_listing(self, new):
    self.listings.append(new)
  def remove_listing(self, old):
    self.listings.remove(old)
  def show_listings(self):
    print([x for x in self.listings]) #return [x for x in self.listings]  
  
class Client:
  def __init__(self, name, location, museum):
    self.name = name
    self.is_museum = museum
    if museum:
      self.location = location
    else:
      self.location = "Private Collection"
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:   #artwork.owner.name !! bo owner to class Client
      newListing = Listing(artwork, price, self) # not self.name
      veneer.add_listing(newListing)
  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
      for i in veneer.listings:
        if artwork == i.art:
          art_listing = i
          break
      if art_listing != None:
        artwork.owner = self  # self.name changes only name, but we need location also
        veneer.remove_listing(art_listing)

class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  def __repr__(self):
    return "Listing. ART: {a}. PRICE: {p}.".format(a=self.art.title, p=self.price)
  
veneer = Marketplace()
edytta = Client("Edytta Halpirt", None, False)  # None obj as 2nd argument
moma = Client("The MOMA", "New York", True)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)
print(girl_with_mandolin)

edytta.sell_artwork(girl_with_mandolin, "$6M (USD)")
veneer.show_listings()
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
veneer.show_listings()

