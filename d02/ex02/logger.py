import time
from random import randint
import logging
import getpass
username = getpass.getuser()

formattage  =  '(' + username + ')Running: %(message)s '
logging.basicConfig(filename='machine.log',level=logging.DEBUG, format=formattage)
#formatter = logging.Formatter('%(asctime)s :: %(levelname)s :Running : %(message)s')
#ch.setFormatter(formatter)
#logging.Formatter.__init__(formatter)
#file_handler = FileHandler("machine.log", "w+")



def displayLog(func, funcName):
    func
    end = time.time()
    logging.info('{} [exec-time = {} ms]'.format(funcName, round(end - start, 3) / 1000))

class CoffeeMachine():

    water_level = 100

   @log("start_machine")
    def start_machine(self):
        end = time.time()
        logging.info('start machine [exec-time = {} ms]'.format(round(end - start, 3) / 1000))
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False
    
    def boil_water(self):
        return "boiling..."
    
    def log(statement):
        def decorator(func):
            @wraps(func)
        def wrapper(*args, **kwargs):
            # set name_override to func.__name__
            logger.info(statement, extra={'name_override': func.__name__})
            return func(*args, **kwargs)
            return wrapper
        return decorator
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

#http://sametmax.com/ecrire-des-logs-en-python/
if __name__ == "__main__":

    start = time.time()
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
