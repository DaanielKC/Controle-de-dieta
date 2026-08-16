from Classes.user import User, CuttingUser, MaintenanceUser, BulkingUser
from Classes.food import Food
from Classes.consumption import Consumption
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
    print(f"Alimento {food.name} cadastrado com sucesso!")
    print()
    returning = ""
    while returning != "1":
        returning = input("Digite 1 para voltar ao menu principal: ")

def consumption_registration():
    clear()
    user_name = input("Digite o nome do usuário: ")
    food_name = input("Digite o nome do alimento consumido: ")
    quantity = float(input("Digite a quantidade consumida (em gramas): "))
    
    consumption = Consumption(user, food, quantity)
    print(f"Consumo registrado: {user.name} consumiu {quantity}g de {food.name} em {consumption.date}.")
    print()
    returning = ""
    while returning != "1":
        returning = input("Digite 1 para voltar ao menu principal: ")

def daily_summary():
    clear()
    user_name = input("Digite o nome do usuário para ver o resumo diário: ")
    

    total_calories = consumption.calculate_total_calories()
    total_protein = consumption.calculate_total_protein()
    total_carbo = consumption.calculate_total_carbo()
    total_fats = consumption.calculate_total_fats()

    print(f"Resumo diário para {user.name} em {consumption.date}:")
    print(f"Calorias totais: {total_calories} kcal")
    print(f"Proteínas totais: {total_protein} g")
    print(f"Carboidratos totais: {total_carbo} g")
    print(f"Gorduras totais: {total_fats} g")
    print()
    returning = ""
    while returning != "1":
        returning = input("Digite 1 para voltar ao menu principal: ")

def consumption_history():
    clear()
    user_name = input("Digite o nome do usuário para ver o histórico de consumo: ")
    
    print(f"Histórico de consumo para {user.name}:")
    
    pass
    print()
    returning = ""
    while returning != "1":
        returning = input("Digite 1 para voltar ao menu principal: ")
