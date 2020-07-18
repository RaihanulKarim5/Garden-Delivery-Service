class Flowers:
    flowers = {
        'Begonias': 6,
        'Geraniums': 6,
        'Lobelia': 9,
        'Petunias': 9
    }
    area_per_packs = {
        'Begonias': 6 * 30 * 30,
        'Geraniums': 6 * 30 * 30,
        'Lobelia': 9 * 15 * 15,
        'Petunias': 9 * 30 * 30
    }
    cost_per_packs ={
        'Begonias': 4.25,
        'Geraniums':  4.25,
        'Lobelia': 3.55,
        'Petunias': 3.55
    }
    def __init__(self, b, g, l, p):
        self.begonius = b
        self.geraniums = g
        self.lobelia = l
        self.petunias = p
        self.total_packs = b + g + l + p

    def total_plants(self):
        plants = (self.begonius * Flowers.flowers.get( 'Begonias' ) + self.geraniums * Flowers.flowers.get(
            'Geraniums' ) + self.lobelia * Flowers.flowers.get( 'Lobelia' ) + self.petunias * Flowers.flowers.get(
            'Petunias' ))
        return plants

    def areas(self):
        area_req = (self.begonius * Flowers.area_per_packs.get( 'Begonias' ) + self.geraniums * Flowers.area_per_packs.get(
            'Geraniums' ) + self.lobelia * Flowers.area_per_packs.get( 'Lobelia' ) + self.petunias * Flowers.area_per_packs.get(
            'Petunias' )) / 1000
        return area_req

    def price(self):
        total_price = (self.begonius * Flowers.cost_per_packs.get( 'Begonias' ) + self.geraniums * Flowers.cost_per_packs.get(
            'Geraniums' ) + self.lobelia * Flowers.cost_per_packs.get( 'Lobelia' ) + self.petunias * Flowers.cost_per_packs.get(
            'Petunias' ))
        return total_price

    def discount(self):
        total_price = self.price()
        discount = total_price / 100 * 10
        return discount

    def display(self):
        print( "Thank you for your order, you have ordered..." )
        print( "{} packs of plants or {} individual plants.".format( self.total_packs, self.total_plants() ) )
        print( "You have enough plant to cover {} square metres.".format( self.areas() ) )
        if self.total_packs >= 5:
            print("You have qualified for a 10% discount")
            print("------------------------------------")
            print( "Sub Total: {} EURO".format( self.price() ) )
            print( "Discount: {} EURO".format( self.discount() ) )
        else:
            print( "Sub Total: {} EURO".format( self.price() ) )
            print( "Discount: 0.00 EURO")



print( "Welcome to Bingley Garden Centre Delivery Service.." )
print( "How many packs of the following plants would you like?" )
begonias = int( input( "Begonias (6 pack):" ) )
geraniums = int( input( "geraniums (6 pack):" ) )
lobelia = int( input( "Lobelia (9 pack):" ) )
petunias = int( input( "Petunias (9 pack):" ) )

customer = Flowers( begonias, geraniums, lobelia, petunias )
customer.display()