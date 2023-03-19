import os
import sys
from time import sleep

def user_done():
    done = input("Run Again? Y/N ")
    done = done.lower()
    if done == 'y':
        main()
    else:
        sys.exit()

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_intro():
    clear_screen()
    print("Zombie Health Scaling made easy by VeryInky")
    sleep(0.1)
    print("""Use base game defaults? Y/N
    Starting Health 150
    Round Increment 100
    Zombie Health Multiplier (after round 10) 1.1
    """)

def get_yes_no_input(prompt):
    while True:
        user_input = input(prompt).lower()
        if user_input == 'y' or user_input == 'n':
            return user_input
        else:
            print('No valid selection made')
            sleep(0.5)

def get_round_number():
    while True:
        try:
            round_number = int(input("Input the round number to find out what our zombie health will be: "))
            if round_number > 0:
                return round_number
            else:
                print("Round number must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid round number.")

def calculate_zombie_health(round_number, start_health, health_increase, health_multiplier):
    if round_number == 1:
        return start_health
    elif round_number < 10:
        return start_health + health_increase * (round_number - 1)
    else:
        health = start_health + health_increase * 8
        return int(health * (health_multiplier ** (round_number - 9)) - 10)

def main():
    print_intro()
    default = get_yes_no_input("Use base game defaults? Y/N: ")

    if default == 'y':
        zombie_start_health = 150
        zombie_round_health_increase = 100
        zombie_health_multiplier = 1.1
        health_cap = 0
    else:
        zombie_start_health = int(input('Input custom zombie start health. Vanilla is 150: '))
        zombie_round_health_increase = int(input('Input zombie health to be added for rounds 2-9. Vanilla is 100: '))
        zombie_health_multiplier = float(input('Input the factor for health to be multiplied PER ROUND. Default is 1.1. This is exponential: '))
        health_cap = int(input('Enter an optional health cap, or input 0 to disable the health cap: '))

    round_number = get_round_number()

    if health_cap > 0:
        cap_round = 0
        for i in range(1, round_number + 1):
            current_health = calculate_zombie_health(i, zombie_start_health, zombie_round_health_increase, zombie_health_multiplier)
            if current_health >= health_cap and cap_round == 0:
                cap_round = i
                print(f"Zombies will reach the health cap of {health_cap} at round {cap_round}.")
                break

    zombie_end_health = calculate_zombie_health(round_number, zombie_start_health, zombie_round_health_increase, zombie_health_multiplier)
    print(f"Zombie Health on round {round_number} = {zombie_end_health}")
    os.system('pause')
    user_done()

if __name__ == "__main__":
    main()
