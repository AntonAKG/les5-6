# # name = 'John'
# # print(f'Hello, {name}!') # f string
# # print('Hello, ' + name + '!') # concatenation
# #
# # # f string
# # print(f'Hello, {name*2}!') # Hello, JohnJohn!
# #
# # print(f'Hello, {len(name)}') # Hello, 4
# #
#
# name = 'John'
# age = 18
#
# print(f'Hello {name:s}! You are {age:d} years old.') # Hello John! You are 18 years old.

# PI = 3.141592653589793
# print(f'{PI:9.2f}')


# income = 202356
# costs = 124365
#
# profit = income/costs-1
#
# print(f'profit: {profit:.2%}')


# day = 13
# name = 'Nick'
# king_of_the_hill = 'Ann'
#
# print(f'Today is friday, {day:<15d}')
# print(f'{name:>25} jhvytjvukbivkcjyu')
# print(f'{king_of_the_hill:^25} jhvytjvukbivkcjyu')

details_damage_price = {'energy_gun': 100, 'minigun': 200, 'rail gun': 300}
details_survive_price = {'shield': 100, 'armor': 200, 'force field': 300}
users_bot = {}
player_list = []

def player_maker(player: list) -> None:
    user_choose = 'yes'

    while user_choose == 'yes' or user_choose == 'y':
        user_input = input('Enter your name: ')
        if len(user_input) < 3:
            print('Name is too short')
            continue

        player.append(str.capitalize(user_input))
        user_choose = input('yes/no')
    print(f"Players: {str(player)[1:-1]}")

def bot_maker(start_sum: int, players: list) -> None:
    for player in players:
        wallet = start_sum
        users_bot[player] = {}

        while wallet > min(details_damage_price.values()):
            string_1 = f'{player}, u have {wallet} coins.'
            print(f'{string_1:=^82}')
            string_2 = 'U can buy: '
            print(f'{string_2:-^82}')

            for gun, price in details_damage_price.items():
                print(f'{gun} - {price}')

            print(wallet)

            for survive, price in details_survive_price.items():
                print(f'{survive} - {price}')

            user_choose = str.lower(input('Enter your choice: '))

            if user_choose in users_bot[player].keys():
                string = 'You already have this item'
                print(f'{string:!^80}'.format(string='You already have this item'))

                continue

            if user_choose in details_damage_price.keys():

                if wallet < details_damage_price.keys():
                    print('Not enough money')
                    continue

                wallet -= details_damage_price[user_choose]

                # wallet = wallet - details_damage_price[user_choose]

                users_bot[player][user_choose] = details_damage_price[user_choose]



player_maker(player_list)