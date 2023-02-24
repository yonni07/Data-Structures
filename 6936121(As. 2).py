#sales at a car dealership
# Github link: https://github.com/yonni07/Data-Structures.git
carPrices={
    'Hyundai':{'Elantra':20000,'Creta':25000,'Verna':24500,'Venue':25000,'i20':30000,'Aura':20370},
    'BMW':{'X5':30000,'iX':32000,'M3':33000,'i7':32300,'Z4':40000,'X3':32100},
    'Chevrolet':{'Cruze':25000,'Impala':32000,'Corvette':23000,'Camaro':32000},
    'Toyota':{'Prius':37295,'Camry':26220,'Corolla':21550,'Rav4':32570,'4Runner':42710},
    'Lamborghini':{'Urus':655000,'Aventador':700000,'Gallardo':300000,'Huracan':325000},
    'Nissan':{'Navara':2000,'Pathfinder':2300,'Altima':2500,'Titan':2550},
    'Honda':{'Accord':25000,'Amaze':27000,'Civic':27500}
    }
#User inputs the car brand and model and returns the corresponding prices
def getCarPrice():
 carBrand=input('Please enter the brand of the car: ')
 carModel=input('PLease enter the model of the car: ')
#Search for the car model in the carPrices dictionary
 if carBrand in carPrices and carModel in carPrices[carBrand]:
    return carPrices[carBrand][carModel]
 else:
    return None
price=getCarPrice()
if price is not None:
    print('The price of the car is: ${}'.format(price))
else:
    print('Car brand or model not available.')