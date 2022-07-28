import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player.go_up, 'Up')
screen.onkeypress(screen.bye, 'space')

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detecting collision between car and player
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.ycor() > 280:
        car_manager.level_up()
        player.go_to_start()
        scoreboard.increase_level()

screen.exitonclick()
