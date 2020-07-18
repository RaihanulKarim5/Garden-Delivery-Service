class Flowers:
    flowers = {
        'Begonias': 6,
        'Geraniums': 6,
        'Lobelia': 9,
        'Petunias': 9
    }
    def __init__(self, b, g, l, p):
        self.begonius = b
        self.geraniums = g
        self.lobelia = l
        self.petunias = p
        self.total_packs = b + g + l + p
        self.total_plants = b * Flowers.flowers.get('Begonias') + g * Flowers.flowers.get('Geraniums') + l * Flowers.flowers.get('Lobelia') + p * Flowers.flowers.get('Petunias')


print("Welcome to Bingley Garden Centre Delivery Service..")
print("How many packs of the following plants would you like?")
begonias = int(input("Begonias (6 pack):"))
geraniums = int(input("geraniums (6 pack):"))
lobelia = int(input("Lobelia (9 pack):"))
petunias = int(input("Petunias (9 pack):"))

customer = Flowers(begonias, geraniums, lobelia, petunias)
print("Thank you for your order, you have ordered...")
print("{} packs of plants or {} individual plants.".format(customer.total_packs, customer.total_plants))