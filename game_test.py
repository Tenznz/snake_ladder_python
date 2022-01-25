from snake_ladder.game import SnakeLadder


def test_dice_rolled():
    snake_ladder = SnakeLadder()
    assert snake_ladder.dice_rolled() in range(1, 6)
