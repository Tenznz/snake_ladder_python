from random import randint


class SnakeLadder:

    def dice_rolled(self):
        return randint(1, 6)


if __name__ == "__main__":
    print("Snake and ladder")
    WIN = 100
    player_position = 0
    print("player position : {}".format(player_position))
    snake_ladder_obj = SnakeLadder()
    dice = snake_ladder_obj.dice_rolled()
    print("dice: {}".format(dice))
