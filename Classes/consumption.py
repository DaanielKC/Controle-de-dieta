from datetime import date
from Classes.user import User
from Classes.food import Food

class Consumption():
    def __init__(self, user, food, quantity):
        self.user = user
        self.food = food
        self.quantity = quantity
        self.date = date.today()

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if not isinstance(value, User):
            raise ValueError("O usuário deve ser uma instância da classe User.")
        self._user = value

    @property
    def food(self):
        return self._food

    @food.setter
    def food(self, value):
        if not isinstance(value, Food):
            raise ValueError("O alimento deve ser uma instância da classe Food.")
        self._food = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("A quantidade não pode ser nula ou negativa.")
        self._quantity = value

    def calculate_total_calories(self):
        total_calories = (self.food.calories * self.quantity) / self.food.base_quantity
        return total_calories

    def calculate_total_protein(self):
        total_protein = (self.food.protein * self.quantity) / self.food.base_quantity
        return total_protein

    def calculate_total_carbo(self):
        total_carbo = (self.food.carbo * self.quantity) / self.food.base_quantity
        return total_carbo

    def calculate_total_fats(self):
        total_fats = (self.food.fats * self.quantity) / self.food.base_quantity
        return total_fats

    