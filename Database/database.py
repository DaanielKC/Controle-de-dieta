from Classes.consumption import Consumption
from Classes.user import CuttingUser, MaintenanceUser, BulkingUser
from Classes.food import Drink, Food, SolidFood

import sqlite3

def connect():
    return sqlite3.connect('database.db')

def create_tables():
    connection = connect()
    cursor = connection.cursor()

    # Criação da tabela de usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            weight REAL NOT NULL,
            height REAL NOT NULL,
            sex TEXT NOT NULL,
            activity_level TEXT NOT NULL,
            goal TEXT NOT NULL
        )
    ''')

    # Criação da tabela de alimentos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS foods (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            base_quantity REAL NOT NULL,
            calories REAL NOT NULL,
            protein REAL NOT NULL,
            carbo REAL NOT NULL,
            fats REAL NOT NULL,
            category TEXT NOT NULL
        )
    ''')    

    # Criação da tabela de consumos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS consumptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            food_id INTEGER NOT NULL,
            quantity REAL NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (food_id) REFERENCES foods(id)
        )
    ''')

    connection.commit()
    connection.close()

# Adição de um usuário à tabela
def add_user(user):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO users (name, age, weight, height, sex, activity_level, goal)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        user.name, 
        user.age, 
        user.weight, 
        user.height, 
        user.sex, 
        user.activity_level, 
        user.goal
    ))

    connection.commit()
    connection.close()

# Função para pegar os dados dos usuários
def get_users():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()

    users = []
    for row in rows:
        if row[7] == "Cutting":
            user = CuttingUser(row[1], row[2], row[3], row[4], row[5], row[6])
        elif row[7] == "Maintenance":
            user = MaintenanceUser(row[1], row[2], row[3], row[4], row[5], row[6])
        elif row[7] == "Bulking":
            user = BulkingUser(row[1], row[2], row[3], row[4], row[5], row[6])
        user.id = row[0]  # Atribuindo o ID do banco de dados ao objeto User
        users.append(user)

    connection.close()
    return users

# Adição de um alimento
def add_food(food):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO foods (name, base_quantity, calories, protein, carbo, fats, category)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        food.name,
        food.base_quantity,
        food.calories,
        food.protein,
        food.carbo,
        food.fats,
        food.category
    ))

    connection.commit()
    connection.close()

# Função para pegar os dados dos alimentos
def get_foods():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM foods')
    rows = cursor.fetchall()

    foods = []
    for row in rows:
        if row[7] == "Solid":
            food = SolidFood(row[1], row[2], row[3], row[4], row[5], row[6])
        else:
            food = Drink(row[1], row[2], row[3], row[4], row[5], row[6])
        food.id = row[0]  # Atribuindo o ID do banco de dados ao objeto Food
        foods.append(food)

    connection.close()
    return foods

# Adição de um consumo
def add_consumption(consumption):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO consumptions (user_id, food_id, quantity, date)
        VALUES (?, ?, ?, ?)
    ''', (
        consumption.user.id,
        consumption.food.id,
        consumption.quantity,
        consumption.date
    ))

    connection.commit()
    connection.close()

# Função para pegar os dados dos consumos
def get_consumptions():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM consumptions')
    rows = cursor.fetchall()
    users = get_users()
    foods = get_foods()

    consumptions = []
    for row in rows:
        user_id = row[1]
        food_id = row[2]
        quantity = row[3]
        date = row[4]

        user = None
        food = None
        for user_object in users:
            if user_object.id == user_id:
                user = user_object

        for food_object in foods:
            if food_object.id == food_id:
                food = food_object

        consumption = Consumption(user, food, quantity, date)
        consumptions.append(consumption)

    connection.close()
    return consumptions
