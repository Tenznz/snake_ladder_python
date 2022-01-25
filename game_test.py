from snake_ladder.game import SnakeLadder


def test_dice_rolled():
    snake_ladder = SnakeLadder()
    assert snake_ladder.dice_rolled() in range(1, 6)


def test_snake():
    snake_ladder = SnakeLadder()
    assert snake_ladder.snake(98) == 97


def test_ladder():
    snake_ladder = SnakeLadder()
    assert snake_ladder.ladder(18) == 41
