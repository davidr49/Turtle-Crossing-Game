import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()


    for cars in car_manager.all_cars:
        if player.distance(cars) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.reached_end()
        car_manager.level_up()
        scoreboard.next_level()


screen.exitonclick()


# Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful
# crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre.
