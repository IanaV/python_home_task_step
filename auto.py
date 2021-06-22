# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
# название модели, год выпуска, произво- дителя, объем двигателя, цвет машины, цену.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

# К уже реализованному классу «Автомобиль» добавьте конструктор, а также необходимые перегруженные методы.

import pickle
import json
import os

class Car():

    def __init__(self,model= "no data",year= "no data",production= "no data",m_capacity= "no data",color = "no data",price = "no data"):
        self.__model = model
        self.__year = year
        self.__production = production
        self.__m_capacity = m_capacity
        self.__color = color
        self.__price = price

    def set_model(self,new_data):
        self.__model = new_data

    def set_year(self,new_data):
        self.__year = new_data

    def set_production(self,prod):
        self.__production = prod

    def set_m_capacity(self,cap):
            self.__m_capacity = cap

    def set_color(self,color):
            self.__color = color

    def set_price(self,pr):
            self.__price = pr

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_production(self):
        return self.__production

    def get_m_capacity(self):
        return self.__m_capacity

    def get_color(self):
        return self.__color

    def get_price(self):
        return self.__price

    def data_from_keybord(self):
        m = input("Enter a model: ")
        self.set_model(m)
        y = input("Enter a year: ")
        self.set_year(self, y)
        p = input("Enter a production name: ")
        self.set_production(self,p)
        c = input("Enter a capacity of motor: ")
        self.set_m_capacity(self,c)
        col = input("Enter a color of car: ")
        self.set_color(self,col)
        price = input("Enter a price of car: ")
        self.set_price(self,price)


    def __str__(self):
        return f"{self.__model}: {self.__color}, {self.__price} $, {self.__year}, {self.__production}, {self.__m_capacity}."


    def ser(self):
        result = {}
        for key in self.__dict__:
            result[key.replace(f"_{self.__class__.__name__}__","")] = self.__dict__[key]
        return result

    def save_to_pickle(self):
        result = self.ser()
        try:
           with open("save.pickle",'wb') as f:
               pickle.dumps(result)
        except FileNotFoundError:
            print("No file to save.")

    def save_to_json(self):
        result = self.ser()
        try:
            with open("save.json", 'w') as f:
                f.write(json.dumps(result))
        except FileNotFoundError:
            print("No file to save.")

    def load_from_pickle(self):
       if(os.stat("save.pickle").st_size == 0):
           return self.__init__()
       else:
            try:
                with open("save.pickle",'rb') as f:
                    D = pickle.load(f)
                    self.__model = D['model']
                    self.__year = D['year']
                    self.__production = D['production']
                    self.__m_capacity = D['m_capacity']
                    self.__color = D['color']
                    self.__price = D['price']
                    return self
            except FileNotFoundError:
                print ("No file to load.")

    def load_from_json(self):
        if (os.stat("save.json").st_size == 0):
            return self
        else:
            try:
                with open("save.json") as f:
                    D = json.load(f)
                    self.__model = D['model']
                    self.__year = D['year']
                    self.__production = D['production']
                    self.__m_capacity = D['m_capacity']
                    self.__color = D['color']
                    self.__price = D['price']
                return self
            except FileNotFoundError:
                print("No file to load.")


car_one = Car()
print(str(car_one))
car_one.set_color("green")
car_one.set_price(13.500)
car_one.set_m_capacity(1998)
car_one.set_year(2017)
car_one.set_model("Mazda 3")
car_one.set_production("Mazda")
print(str(car_one))
car_one.save_to_json()
car_two = Car()
car_two.load_from_json()
print("Car 2")
print(car_two)






