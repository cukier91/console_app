import random


def roll(dice_no, dice_type, modify):
    dices = [100, 12, 10, 8, 6, 4, 3]
    rolls = 0
    if dice_type not in dices:
        return f"Not such dice! "
    else:
        for i in range(1, int(dice_no + 1)):
            rolls += random.randint(1, dice_type) + modify
        return rolls


print(roll(2, 3, +2))
