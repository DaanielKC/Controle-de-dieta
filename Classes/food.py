class Food():
    def __init__(self, name, base_quantity, calories, protein, carbo, fats):
        self.name = name
        self.base_quantity = base_quantity
        self.calories = calories
        self.protein = protein
        self.carbo = carbo
        self.fats = fats

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("O nome do alimento não pode ser vazio.")
        self._name = value

    @property
    def base_quantity(self):
        return self._base_quantity

    @base_quantity.setter
    def base_quantity(self, value):
        if value <= 0:
            raise ValueError("A quantidade não pode ser nula ou negativa.")
        self._base_quantity = value

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        if value < 0:
            raise ValueError("As calorias não podem ser negativas.")
        self._calories = value

    @property
    def protein(self):
        return self._protein

    @protein.setter
    def protein(self, value):
        if value < 0:
            raise ValueError("A quantidade de proteína não pode ser negativa.")
        self._protein = value

    @property
    def carbo(self):
        return self._carbo

    @carbo.setter
    def carbo(self, value):
        if value < 0:
            raise ValueError("A quantidade de carboidratos não pode ser negativa.")
        self._carbo = value

    @property
    def fats(self):
        return self._fats

    @fats.setter
    def fats(self, value):
        if value < 0:
            raise ValueError("A quantidade de gorduras não pode ser negativa.")
        self._fats = value
