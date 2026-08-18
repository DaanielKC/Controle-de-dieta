from datetime import datetime
from Classes.user import CuttingUser, MaintenanceUser, BulkingUser
from Classes.food import SolidFood, Drink
from Classes.consumption import Consumption
from Database.database import add_user, get_users, add_food, get_foods, add_consumption, get_consumptions
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Interface inicial
def initiate_interface():
    while True:
        clear()
        print("Bem-vindo ao Controle de Dieta!")
        print("Escolha uma opção:")
        print("1. Cadastro de usuário")
        print("2. Cadastro de alimento")
        print("3. Registro de consumo")
        print("4. Ver resumo do usuário")
        print("5. Ver resumo do alimento")
        print("6. Ver resumo diário")
        print("7. Ver histórico de consumo")
        print("8. Sair")
        print()
        choice = input("Digite o número da opção desejada: ")

        while True:
            if choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")
                choice = input("Digite o número da opção desejada: ")
        if choice == '1':
            user_registration()
        elif choice == '2':
            food_registration()
        elif choice == '3':
            consumption_registration()
        elif choice == '4':
            user_summary()
        elif choice == '5':
            food_summary()
        elif choice == '6':
            daily_summary()
        elif choice == '7':
            consumption_history()
        elif choice == '8':
            print("Obrigado por usar o Controle de Dieta!")
            break

# Registro do usuário
def user_registration():
    clear()
    name = input("Digite o nome do usuário: ")
    age = int(input("Digite sua idade: "))
    weight = float(input("Digite seu peso (em kg): "))
    height = float(input("Digite sua altura (em cm): "))
    sex = input("Digite seu sexo (M/F): ")
    print("Qual seu nível de atividade:")
    print("1. Sedentário")
    print("2. Levemente ativo")
    print("3. Moderadamente ativo")
    print("4. Muito ativo")
    print("5. Extremamente ativo")
    act_lvl = input("Digite o número correspondente ao seu nível de atividade: ")
    if act_lvl == "1":
        activity_level = "Sedentário"
    elif act_lvl == "2":
        activity_level = "Levemente ativo"
    elif act_lvl == "3":
        activity_level = "Moderadamente ativo"
    elif act_lvl == "4":
        activity_level = "Muito ativo"
    elif act_lvl == "5":
        activity_level = "Extremamente ativo"
    valid_goal = False
    while not valid_goal:
        print("Qual seu objetivo?")
        print("1. Perder peso")
        print("2. Manter o peso")
        print("3. Ganhar peso")
        goal_choice = input("Digite o número correspondente ao seu objetivo: ")
        if goal_choice in ['1', '2', '3']:
            valid_goal = True
        if goal_choice == '1':
            user = CuttingUser(name, age, weight, height, sex, activity_level)
        elif goal_choice == '2':
            user = MaintenanceUser(name, age, weight, height, sex, activity_level)
        elif goal_choice == '3':
            user = BulkingUser(name, age, weight, height, sex, activity_level)
        else:
            print("Opção inválida.")
            print()

    add_user(user)
    print()
    print(f"Usuário {user.name} cadastrado com sucesso!")
    print()
    returning = ""
    while returning != "1":
        returning = input("Digite 1 para voltar ao menu principal: ")

# Registro do alimento   
def food_registration():
    clear()
    name = input("Digite o nome do alimento: ")
    print("Digite o tipo de alimento: ")
    print("1. Comida")
    print("2. Bebida")
    category = input("Escolha o tipo de alimento (número): ")
    if category == "1":
        quantity = float(input("Digite a quantidade da porção (em gramas): "))
    elif category == "2":
        quantity = float(input("Digite a quantidade da porção (em ml): "))
    else:
        print("Opção inválida.")
        return
    calories = float(input("Digite as calorias (por porção): "))
    protein = float(input("Digite a quantidade de proteína (por porção): "))
    carbo = float(input("Digite a quantidade de carboidratos (por porção): "))
    fats = float(input("Digite a quantidade de gorduras (por porção): "))
    if category == "1":
        food = SolidFood(name, quantity, calories, protein, carbo, fats)
    elif category == "2":
        food = Drink(name, quantity, calories, protein, carbo, fats)

    add_food(food)
    print(f"Alimento {food.name} cadastrado com sucesso!")
    print()
    returning = ""
    while returning != "1":
        returning = input("Digite 1 para voltar ao menu principal: ")

# Registro do consumo
def consumption_registration():
    clear()
    print("Usuários:")
    users = get_users()
    for i, user in enumerate(users, start=1):
        print(f"{i}. {user.name}")

    print()
    user_choice = int(input("Escolha o usuário (número): "))
    user = users[user_choice - 1]

    print()
    print("Alimentos:")
    foods = get_foods()
    for i, food in enumerate(foods, start=1):
        print(f"{i}. {food.name}")

    print()
    food_choice = int(input("Escolha o alimento (número): "))
    food = foods[food_choice - 1]

    print()
    if food.category == "Solid":
        quantity = float(input("Digite a quantidade consumida (em gramas): "))
    else:
        quantity = float(input("Digite a quantidade consumida (em ml): "))
    
    consumption = Consumption(user, food, quantity)
    add_consumption(consumption)
    print()
    if food.category == "Solid":
        print(f"Consumo registrado: {user.name} consumiu {quantity}g de {food.name}.")
    else:
        print(f"Consumo registrado: {user.name} consumiu {quantity}ml de {food.name}.")
    print()
    returning = ""
    while returning != "1":
        returning = input("Digite 1 para voltar ao menu principal: ")

# Resumo de um usuário específico
def user_summary():
    clear()
    print("Usuários:")
    users = get_users()
    for i, user in enumerate(users, start=1):
        print(f"{i}. {user.name}")

    print()
    user_choice = int(input("Escolha o usuário (número): "))
    user = users[user_choice - 1]

    if user.goal == "Cutting":
            goal = "Perda de peso"
    elif user.goal == "Maintenance":
            goal = "Manutenção"
    elif user.goal == "Bulking":
            goal = "Ganho de massa muscular"

    clear()
    print(f"Resumo do usuário {user.name}:")
    print(f"Idade: {user.age} anos")
    print(f"Peso: {user.weight} kg")
    print(f"Altura: {user.height} cm")
    print(f"Sexo: {user.sex}")
    print(f"Nível de atividade: {user.activity_level}")
    print(f"Objetivo: {goal}")
    print(f"Taxa Metabólica Basal (TMB): {user.calculate_tmb():.2f} kcal")
    print(f"Gasto Energético Total (GET): {user.calculate_get():.2f} kcal")
    print(f"Meta de calorias: {user.calculate_goal():.2f} kcal")
    print()
    returning = ""
    while returning != "1":
        returning = input("Digite 1 para voltar ao menu principal: ")

# Resumo de um alimento específico
def food_summary():
    clear()
    print("Alimentos")
    foods = get_foods()
    for i, food in enumerate(foods, start=1):
        if food.category == "Solid":
            category = "Comida"
        else:
            category = "Bebida"
        print(f"{i}. {food.name} ({category})")

    print()
    food_choice = int(input("Escolha o alimento (número): "))
    food = foods[food_choice - 1]

    clear()
    print(f"Resumo do alimento {food.name}:")
    if food.category == "Solid":
        print(f"Categoria: Comida")
        print(f"Quantidade da porção: {food.base_quantity}g")
    else:
        print(f"Categoria: Bebida")
        print(f"Quantidade da porção: {food.base_quantity}ml")
    print(f"Quantidade de calorias por porção: {food.calories}g")
    print(f"Quantidade de proteína por porção: {food.protein}g")
    print(f"Quantidade de carboidrato por porção: {food.carbo}g")
    print(f"Quantidade de gordura por porção: {food.fats}g")
    print()
    returning = ""
    while returning != "1":
        returning = input("Digite 1 para voltar ao menu principal: ") 

# Resumo diário
def daily_summary():
    clear()
    print("Usuários:")
    users = get_users()
    for i, user in enumerate(users, start=1):
        print(f"{i}. {user.name}")

    print()
    user_choice = int(input("Escolha o usuário (número): "))
    user = users[user_choice - 1]

    consumptions = get_consumptions()
    user_consumptions = [c for c in consumptions if (c.user.id == user.id) and (c.date == datetime.now().strftime("%d-%m-%Y"))]

    total_calories = sum(consumption.calculate_total_calories() for consumption in user_consumptions)
    total_protein = sum(consumption.calculate_total_protein() for consumption in user_consumptions)
    total_carbo = sum(consumption.calculate_total_carbo() for consumption in user_consumptions)
    total_fats = sum(consumption.calculate_total_fats() for consumption in user_consumptions)

    if user.goal == "Cutting":
        goal = "Perda de peso"
    elif user.goal == "Maintenance":
        goal = "Manutenção"
    elif user.goal == "Bulking":
        goal = "Ganho de massa muscular"

    clear()
    print(f"RESUMO DIÁRIO:")
    print(f"Usuário: {user.name}")
    print(f"Data: {datetime.now().strftime('%d-%m-%Y')}")
    print(f"Objetivo: {goal}")
    print()
    print("Consumo:")
    print(f"Calorias totais: {total_calories:.2f} kcal")
    print(f"Proteínas totais: {total_protein:.2f}g")
    print(f"Carboidratos totais: {total_carbo:.2f}g")
    print(f"Gorduras totais: {total_fats:.2f}g")
    print()
    print(f"Meta de calorias: {user.calculate_goal():.2f} kcal")
    print(f"Restante: {max(0, user.calculate_goal() - total_calories):.2f} kcal")
    print()
    returning = ""
    while returning != "1":
        returning = input("Digite 1 para voltar ao menu principal: ")

# Histórico de consumo
def consumption_history():
    clear()
    print("Usuários:")
    users = get_users()
    for i, user in enumerate(users, start=1):
        print(f"{i}. {user.name}")

    print()
    user_choice = int(input("Escolha o usuário (número): "))
    user = users[user_choice - 1]

    clear()
    print(f"Histórico de consumo para {user.name}:")
    consumptions = get_consumptions()
    user_consumptions = [c for c in consumptions if c.user.id == user.id]
    for consumption in user_consumptions:
            if consumption.food.category == "Solid":
                print(f"- {consumption.date}: {consumption.food.name}, {consumption.quantity}g, {consumption.calculate_total_calories():.2f} kcal")
            else:
                print(f"- {consumption.date}: {consumption.food.name}, {consumption.quantity}ml, {consumption.calculate_total_calories():.2f} kcal")
    print()
    returning = ""
    while returning != "1":
        returning = input("Digite 1 para voltar ao menu principal: ")
