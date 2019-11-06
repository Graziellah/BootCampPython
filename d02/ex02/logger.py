import time
from random import randint
import logging

formattage  =  '(%(name)s)Running: %(message)s '
logging.basicConfig(filename='machine.log',level=logging.DEBUG, format=formattage)
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :Running : %(message)s')
#ch.setFormatter(formatter)
#logging.Formatter.__init__(formatter)
#file_handler = FileHandler("machine.log", "w+")
class CoffeeMachine():

    water_level = 100

    logging.info('start machine [exec-time={}]'.format(round(end - start, 2)))
    def start_machine(self):
        start = time.time()
        if self.water_level > 20:
            end = time.time()
            return True
        else:
            print("Please add water!")
            end = time.time()
            return False
    
    logging.info('boil_water')
    def boil_water(self):
        return "boiling..."
    
    
    logging.info('make_coffe')
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    
    logging.info('add_water')
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

#http://sametmax.com/ecrire-des-logs-en-python/
if __name__ == "__main__":
    
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)