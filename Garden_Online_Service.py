class Flowers:
    flowers = {
        'Begonias': 6,
        'Geraniums': 6,
        'Lobelia': 9,
        'Petunias': 9
    }
    area = {
        'Begonias': 6 * 30 * 30,
        'Geraniums': 6 * 30 * 30,
        'Lobelia': 9 * 15 * 15,
        'Petunias': 9 * 30 * 30
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
        area_req = (self.begonius * Flowers.area.get( 'Begonias' ) + self.geraniums * Flowers.area.get(
            'Geraniums' ) + self.lobelia * Flowers.area.get( 'Lobelia' ) + self.petunias * Flowers.area.get(
            'Petunias' )) / 1000
        return area_req

    def display(self):
        print( "Thank you for your order, you have ordered..." )
        print( "{} packs of plants or {} individual plants.".format( self.total_packs, self.total_plants()))
        print( "You have enough plant to cover {} square metres.".format( self.areas()))


print( "Welcome to Bingley Garden Centre Delivery Service.." )
print( "How many packs of the following plants would you like?" )
begonias = int( input( "Begonias (6 pack):" ) )
geraniums = int( input( "geraniums (6 pack):" ) )
lobelia = int( input( "Lobelia (9 pack):" ) )
petunias = int( input( "Petunias (9 pack):" ) )

customer = Flowers( begonias, geraniums, lobelia, petunias )
customer.display()