class User():
    def __init__(self, name, age, weight, height, sex, activity_level):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.sex = sex
        self.activity_level = activity_level
        self._goal = None

    # Getters e Setters
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("O nome do usuário não pode ser vazio.")
        self._name = value
   
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError("A idade não pode ser nula ou negativa.")
        self._age = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("O peso não pode ser nulo ou negativo.")
        self._weight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("A altura não pode ser nula ou negativa.")
        self._height = value

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        if value not in ['M', 'F']:
            raise ValueError("O sexo deve ser 'M' ou 'F'.")
        self._sex = value

    @property
    def activity_level(self):
        return self._activity_level

    @activity_level.setter
    def activity_level(self, value):
        valid_levels = ['Sedentário', 'Levemente ativo', 'Moderadamente ativo', 'Muito ativo', 'Extremamente ativo']
        if value not in valid_levels:
            raise ValueError("Nível de atividade inválido.")
        self._activity_level = value

    @property
    def goal(self):
        return self._goal

    # Fórmula de Mifflin-St Jeor para calcular a Taxa Metabólica Basal (TMB)
    def calculate_tmb(self):
        if self.sex == 'M':
            tmb = 10*self._weight + 6.25*self._height - 5*self._age + 5
        elif self.sex == 'F':
            tmb = 10*self._weight + 6.25*self._height - 5*self._age - 161
        return tmb

    # Cálculo do Gasto Energético Total (GET) com base no nível de atividade
    def calculate_get(self):
        tmb = self.calculate_tmb()
        if self.activity_level == 'Sedentário':
            get = tmb * 1.2
        elif self.activity_level == 'Levemente ativo':
            get = tmb * 1.375
        elif self.activity_level == 'Moderadamente ativo':
            get = tmb * 1.55
        elif self.activity_level == 'Muito ativo':
            get = tmb * 1.725
        elif self.activity_level == 'Extremamente ativo':
            get = tmb * 1.9
        return get

# Subclasses do User para diferentes objetivos
class CuttingUser(User):
    def __init__(self, name, age, weight, height, sex, activity_level):
            super().__init__(name, age, weight, height, sex, activity_level)
            self._goal = "Cutting"

    def calculate_goal(self):
        get = self.calculate_get()
        calories_goal = get - 300  # Redução de 300 calorias para perda de peso
        return calories_goal

class MaintenanceUser(User):
    def __init__(self, name, age, weight, height, sex, activity_level):
            super().__init__(name, age, weight, height, sex, activity_level)
            self._goal = "Maintenance"
    def calculate_goal(self):
        get = self.calculate_get()
        calories_goal = get  # Mantém o mesmo valor de GET para manutenção de peso
        return calories_goal

class BulkingUser(User):
    def __init__(self, name, age, weight, height, sex, activity_level):
        super().__init__(name, age, weight, height, sex, activity_level)
        self._goal = "Bulking"

    def calculate_goal(self):
        get = self.calculate_get()
        calories_goal = get + 300  # Adicão de 300 calorias para ganho de peso
        return calories_goal
