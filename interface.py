from datetime import datetime
from Classes.user import CuttingUser, MaintenanceUser, BulkingUser
from Classes.food import Food
from Classes.consumption import Consumption
from Database.database import add_user, get_users, add_food, get_foods, add_consumption, get_consumptions
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def initiate_interface():
    while True:
        clear()
        print("Bem-vindo ao Controle de Dieta!")
        print("Escolha uma opção:")
        print("1. Cadastro de usuário")
        print("2. Cadastro de alimento")
        print("3. Registro de consumo")
        print("4. Ver resumo diário")
        print("5. Ver histórico de consumo")
        print("6. Sair")
        choice = input("Digite o número da opção desejada: ")

        if choice == '1':
            user_registration()
        elif choice == '2':
            food_registration()
        elif choice == '3':
            consumption_registration()
        elif choice == '4':
            daily_summary()  
        elif choice == '5':
            consumption_history()
        elif choice == '6':
            print("Obrigado por usar o Controle de Dieta!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

def user_registration():
    clear()
    name = input("Digite o nome do usuário: ")
    age = int(input("Digite sua idade: "))
    weight = float(input("Digite seu peso (em kg): "))
    height = float(input("Digite sua altura (em cm): "))
    sex = input("Digite seu sexo (M/F): ")
    activity_level = input("Digite seu nível de atividade (Sedentário, Levemente ativo, Moderadamente ativo, Muito ativo, Extremamente ativo): ")
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
    print(f"Usuário {user.name} cadastrado com sucesso!")
    print()
    returning = ""
    while returning != "1":
        returning = input("Digite 1 para voltar ao menu principal: ")
    

def food_registration():
    clear()
    name = input("Digite o nome do alimento: ")
    quantity = float(input("Digite a quantidade da porção (em gramas): "))
    calories = float(input("Digite as calorias (por porção): "))
    protein = float(input("Digite a quantidade de proteína (por porção): "))
    carbo = float(input("Digite a quantidade de carboidratos (por porção): "))
    fats = float(input("Digite a quantidade de gorduras (por porção): "))
    food = Food(name, quantity, calories, protein, carbo, fats)

    add_food(food)
    print(f"Alimento {food.name} cadastrado com sucesso!")
    print()
    returning = ""
    while returning != "1":
        returning = input("Digite 1 para voltar ao menu principal: ")

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
    quantity = float(input("Digite a quantidade consumida (em gramas): "))
    
    consumption = Consumption(user, food, quantity)
    add_consumption(consumption)
    print()
    print(f"Consumo registrado: {user.name} consumiu {quantity}g de {food.name}.")
    print()
    returning = ""
    while returning != "1":
        returning = input("Digite 1 para voltar ao menu principal: ")

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
            print(f"- {consumption.date}: {consumption.food.name}, {consumption.quantity}g, {consumption.calculate_total_calories():.2f} kcal")
    print()
    returning = ""
    while returning != "1":
        returning = input("Digite 1 para voltar ao menu principal: ")
