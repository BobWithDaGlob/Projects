from random import randint
from random import seed
import time

#Add Car class here
class Car:
    def __init__(self, driver, model="unknown"):
        self.driver = driver
        self.model = model
        self.hits = 0

    def __str__(self):
        return f"{self.driver}\t{self.model}"

    def get_driver(self):
        return self.driver

    def get_model(self):
        return self.model

    def get_hits(self):
        return self.hits

    def add_hit(self):
        self.hits += 1

def main():
    num = int(input("Let's get started with a number between 0 and 10:  "))
    seed(num)
    
    # Registration from the file competitors.txt
    cars = []

    with open("competitors.txt", "r") as car_file:
        for line in car_file:
            driver, model = line.strip().split('\t')
            new_entry = Car(driver, model)
            cars.append(new_entry)



#Do not change any code past this point
def main():
    num = int(input("Let's get started with a number between 0 and 10:  "))
    seed(num)
    #Registration from the file competitors.txt
    cars = []

    car_file = open("competitors.txt")

    for each in car_file:
        car, type_car = each.split('\t')
        new_entry = Car(car.strip(), type_car.strip())
        cars.append(new_entry)
        
    print("There are now", len(cars), "cars in this here demolition derby.")    
    print("Registration is now closed.  Here's who we have in our race:\n")
    for each in cars:
        print(each)

    #Welcome
    print("\nAnd now it's time for the race!\n")
    print("Welcome ladies and gentlemen to the CSE 1284 Demolition Derby.")
    print("We have cars in the arena to rock your world with all of the smashing")
    print("and crashing that you could ever hope for.  It promises to be an")
    print("exciting night.\n")

    print("Our returning champion, " + cars[0].get_driver()+ ", has come tonight")
    print("with his newest " + cars[0].get_model()+ ".")
    print("The race hasn't started yet so he has " + str(cars[0].get_hits()) + " hits so far,")
    print("but is he ever mobile.\nYee-haa!  Look at him move.  Yessiree, it should")
    print("be a fine show.")


    #Start of commented out section -- starting the derby  
    print("Let's start this game.\n\nBANG!\n\nAnd we're off!\n\n")

    while len(cars) > 1:    #Continue until one champ remains
        if len(cars) < 5:
            print("We're down to", len(cars), "cars in the race.")
        else:
            print("We still have", len(cars), "cars in the race.")

        car_total = len(cars)
        #Collisions
        basher = randint(0, car_total - 1)
        bashed = randint(0, car_total - 1)
        #A car can't hit itself
        while basher == bashed:
            bashed = randint(0, car_total - 1)
        
        print(cars[basher].get_driver(), "just hit", cars[bashed].get_driver(), "and...")

        hit_hard = randint(1, 10)
        if hit_hard > 6: #Can no longer move
            out = cars.pop(bashed)
            print("Yes!  It looks like he can't get his ol' ", out.get_model(), "movin'.")
            print("He's out of the game!")
            
        else: #Add a hit to the car
            cars[bashed].add_hit()
            print("But he's still moving -- so he's still in the game.")
        print("\n")
        time.sleep(2)

    #Ending announcements
    print("The crowd is going WILD!  There's only one car left now.")
    print("So with ", cars[0].get_hits(), "hits in this game, our new champion is.....")
    print("drum-roll please.....\n")
    print(cars[0].get_driver() + "!!!")
    print("\nEverybody be sure to say a big CONGRATULATIONS to our champion.")
    print("And be sure to come back next year, but until then, keep on crashin'")
    print("and a-smashin'!")
    print()
    
                   


if __name__ == "__main__":
    main()
