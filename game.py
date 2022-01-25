from random import randint


class SnakeLadder:

    def __init__(self):
        self.ladder_dict = {}
        self.snake_dict = {}

    def dice_rolled(self):
        return randint(1, 6)

    def snake(self, position):
        self.snake_dict = {
            98: 1,
            52: 20,
            87: 12,
            20: 3
        }
        if position in self.snake_dict:

            position = position - self.snake_dict.get(position)
        return position

    def ladder(self, position):
        self.ladder_dict = {
            20: 12,
            12: 40,
            92: 1,
            18: 23
        }
        if position in self.ladder_dict:

            position = position + self.ladder_dict.get(position)
        return position


if __name__ == "__main__":
    print("Snake and ladder")
    WIN = 100
    player_position = 0
    print("player initial position : {}".format(player_position))
    snake_ladder_obj = SnakeLadder()

    while player_position < WIN:
        dice = snake_ladder_obj.dice_rolled()
        print("dice: {}".format(dice))
        player_position = player_position + dice
        print(player_position)
        snake_ladder_obj.snake(player_position)
        snake_ladder_obj.ladder(player_position)
