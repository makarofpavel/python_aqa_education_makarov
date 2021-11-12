from abc import ABC, abstractmethod


class Transport:

    def __init__(self, is_engine, passenger, trunk_volume, max_speed, weight):
        self.is_engine = is_engine  # True or False
        self.passenger = passenger  # number
        self.trunk_volume = trunk_volume  # Number litres
        self.max_speed = max_speed  # km/h
        self.weight = weight  # kg

    def info(self):
        print(self.__dict__)

    def __gte__(self, allowed_weight):
        print("Overrided __gte__ magic method")
        STANDART_PASSANGER_WEIGHT = 80

        if self.passenger * STANDART_PASSANGER_WEIGHT >= allowed_weight:
            print(f"Transport overloaded if all average passengers weight "
                  f"will be {STANDART_PASSANGER_WEIGHT}kg")
        else:
            print(f"You can transport all available passengers seats even the average "
                  f"weight will be {STANDART_PASSANGER_WEIGHT}kg")

    def transport_start(self):
        try:
            if self.is_engine:
                print("Insert the key and start the engine")
            else:
                print("Hello, Flintstones")
        except Exception:
            print("Sorry, we have no info about your engine")


class Engine:
    DEFAULT_ENGINE_CAPACITY = 1.6

    def __init__(self, engine_capacity, engine_type):
        self.engine_capacity = engine_capacity
        self.engine_type = engine_type

    @property
    def engine_prop(self):
        return f"Engine type: {self.engine_type}, engine capacity: {self.engine_capacity}"

    @staticmethod
    def print_info(self):
        print("This Engine class which define the power of your car "
              "(for print this text I use @staticmethod decorator):")

    def enter_engine_capacity(self):
        Engine.print_info(self)
        if self.engine_capacity > self.DEFAULT_ENGINE_CAPACITY:
            print(f"You have a power transport. {self.engine_prop}")
        else:
            print(f"You have slow transport. {self.engine_prop}")


class ElectricCar(Transport):
    """
        Class with overloaded init. Added one additional property: kpp_type (Auto or Manual)
    """
    def __init__(self, is_engine, kpp_type, passenger, trunk_volume, max_speed, weight):
        super().__init__(is_engine, passenger, trunk_volume, max_speed, weight)
        self.kpp_type = kpp_type  # Auto or Manual


class Airplane(Transport):
    """
        Class with overloaded init. **kwargs uses as arguments
    """
    def __init__(self, is_engine, passenger, trunk_volume, max_speed, weight, **kwargs):
        super().__init__(is_engine, passenger, trunk_volume, max_speed, weight)
        self.number_engines = kwargs['number_engines']
        self.boat_long = kwargs['boat_long']


class Boat(Transport):
    """
        Class which do not use parent properties and uses only self properties
    """
    def __init__(self, *args):
        self.is_sailing_vessel = args[0]
        self.number_paddle = args[1]
        self.ship_cabin_number = args[2]
        self.captain_name = args[3]


class BicycleSpeed(ABC):

    def __init__(self, front_stars_number, back_stars_number):
        self.back_stars_number = back_stars_number
        self.front_stars_number = front_stars_number

    @abstractmethod
    def calc_speed_modes(self):
        ...


class Bicycle(Transport, BicycleSpeed):
    """
        Class which inherits 2 classes: Transport and class with abstract method: BicycleSpeed
    """
    def __init__(self, is_engine, passenger, trunk_volume, max_speed, weight, front_stars_number, back_stars_number):
        Transport.__init__(self, is_engine, passenger, trunk_volume, max_speed, weight)
        BicycleSpeed.__init__(self, back_stars_number, front_stars_number)

    @property
    def calc_speed_modes(self):
        return self.front_stars_number * self.back_stars_number

    def __str__(self):
        return f"Your bicycle has {self.calc_speed_modes} speed modes"


class Car(Transport, Engine):
    """
        Class which inherits 2 classes: Transport and Engine
    """
    def __init__(self, is_engine, passenger, trunk_volume, max_speed, weight, engine_capacity, engine_type):
        Transport.__init__(self, is_engine, passenger, trunk_volume, max_speed, weight)
        Engine.__init__(self, engine_capacity, engine_type)


tesla = ElectricCar(True, "Auto", 4, 500, 300, 1500)
print(tesla.__doc__)
print('It is Tesla electric car properties:')
tesla.info()
tesla.transport_start()
tesla.__gte__(200)

boeing777 = Airplane(is_engine=True, passenger=4, trunk_volume=500, max_speed=300, weight=1500, number_engines=8,
                     boat_long=50)
print(boeing777.__doc__)
print('It is Boeing 777 plane properties:')
boeing777.info()
boeing777.transport_start()

gondola = Boat(False, 1, 0, 'Gianluigi Buffon')
print(gondola.__doc__)
print('It is gondola properties:')
gondola.info()
gondola.transport_start()

trx = Bicycle(False, 0, 0, 80, 100, 7, 3)
print(trx.__doc__)
print('It is a TRX bicycle properties:')
trx.info()
trx.transport_start()
print(trx.__str__())

accent = Car(True, 4, 500, 300, 1500, 1.4, "GTI")
print(accent.__doc__)
print('It is an origin car properties:')
accent.info()
accent.transport_start()
accent.enter_engine_capacity()
