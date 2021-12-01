# list of characters and actions to set

intro = 'Бабушка, бабушка, купим'
characters = [('курочку', 'Курочка по зёрнышку кудах-тах-тах'), ('уточку', 'Уточка та-ти-та-та'), ('индюшонка', 'Индюшонок фалды-балды'), ('кисоньку', 'А кисуня мяу-мяу'), ('собачонку', 'Собачонка гав-гав'), ('коровёнку', 'Коровёнка муки-муки'), ('поросёнка', 'Поросёнок хрюки-хрюки'), ('телевизор', 'Телевизор надо, надо, ведь у нас такое стадо')]
for idx, current in enumerate(characters):
    if current[0] == 'телевизор':
        break
    else:
        print(f'{intro} {current[0]}!\n{intro} {current[0]}!')
    for item in characters[0: idx+1][::-1]:
        if item[0] == 'курочку':
            print(item[1], end='.\n')
        else:
            print(item[1], end=',\n')
    print()
print(f'{intro} {characters[-1][0]}!\n{intro} {characters[-1][0]}!\n{characters[-1][1]}!')