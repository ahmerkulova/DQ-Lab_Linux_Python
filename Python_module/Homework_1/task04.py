# list of characters and actions to set
main = 'Бабушка, бабушка, купим'
characters = ['курочку', 'уточку', 'индюшонка', 'кисоньку', 'собачонку', 'коровёнку', 'поросёнка', 'телевизор']
actions = ['Курочка по зёрнышку кудах-тах-тах', 'Уточка та-ти-та-та', 'Индюшонок фалды-балды', 'А кисуня мяу-мяу', 'Собачонка гав-гав', 'Коровёнка муки-муки', 'Поросёнок хрюки-хрюки', 'Телевизор надо, надо, ведь у нас такое стадо']
counter = 0
for _ in range(len(characters) - 1):
    for _ in range(2):
        print(main, characters[counter], end='!\n')  # new character
    counter += 1
    counter_act = counter
    while counter_act != 0:  # character's action
        if counter_act > 1:
            print(actions[counter_act - 1], end=',\n')
        else:
            print(actions[counter_act - 1], end='.\n')
        counter_act -= 1
if counter == len(characters) - 1:  # final part
    print()
    for i in range(2):
        print(main, characters[-1], end='!\n')
    print(actions[-1], end='!\n')