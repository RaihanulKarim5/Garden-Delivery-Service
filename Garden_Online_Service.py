import sys
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
    cost_per_packs = {
        'Begonias': 4.25,
        'Geraniums':  4.25,
        'Lobelia': 3.55,
        'Petunias': 3.55
    }
    delivery_area_charges = {
        'BD16': ['Bingley', 3.55],
        'BD21': ['Central Kingley & Shipley', 4.00],
        'BD16': ['Central Kingley & Shipley', 4.00],
        'BD17': ['Central Kingley & Shipley', 4.00],
        'BD20': ['Outer Keighley', 5.00],
        'BD22': ['Outer Keighley', 5.00]
    }

    def __init__(self, b, g, l, p, pc):
        self.begonius = b
        self.geraniums = g
        self.lobelia = l
        self.petunias = p
        self.postcode = pc
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
        if self.total_packs >= 5:
            total_price = self.price()
            discount = total_price / 100 * 10
        else:
            discount = 0.00
        return discount

    def delivery_charge(self):
        try:
            for code, info in self.delivery_area_charges.items():
                if self.postcode in code:
                    for i in range( len( info ) ):
                        charge = info[1]
                        place = info[0]
                        # print("Delivery:{} EURO ({})" .format(charge, info[0]))
                        break
            return charge, place
        except:
            print("Sorry We don't have the facility to delivery there!")
            sys.exit(1)

    def display(self):
        delivery_result = self.delivery_charge()
        print( "Thank you for your order, you have ordered..." )
        print( "{} packs of plants or {} individual plants.".format( self.total_packs, self.total_plants() ) )
        print( "You have enough plant to cover {} square metres.".format( self.areas() ) )
        if self.total_packs >= 5:
            print("You have qualified for a 10% discount")
            print("------------------------------------")
            print( "Sub Total: \u20ac{0:.2f}".format( self.price() ) )
            print( "Discount: \u20ac{0:.2f}".format( self.discount() ) )
        else:
            print( "You have not qualified for any discount" )
            print( "------------------------------------" )
            print( "Sub Total: \u20ac{0:.2f}".format( self.price() ) )
            print( "Discount: \u20ac{0:.2f} ".format( self.discount() ) )

        price_after_discount = self.price() - self.discount()
        print( "Delivery: \u20ac{} ({})".format( delivery_result[0], delivery_result[1]) )
        print("Grand Total: \u20ac{0:.2f} " .format(price_after_discount + delivery_result[0]))


print("Welcome to Bingley Garden Centre Delivery Service.." )
print("How many packs of the following plants would you like?")
begonias = int( input( "Begonias (6 pack):" ) )
geraniums = int( input( "geraniums (6 pack):" ) )
lobelia = int( input( "Lobelia (9 pack):" ) )
petunias = int( input( "Petunias (9 pack):" ) )
postcode = input("What is the first part of your postcode(BD??):")

customer = Flowers( begonias, geraniums, lobelia, petunias, postcode.upper())
customer.display()