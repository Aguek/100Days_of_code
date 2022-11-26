
import turtle
import pandas
screen = turtle.Screen()
image = "blank_states_img.gif"

screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)

screen.setup(700, 500)
# def get_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_coor)
state_file = pandas.read_csv("50_states.csv")
states = state_file.state.to_list()
# check if the guess is among the 50 states
score = 0
correct_guesses = []
while score < 50:
    screen.title(f"{score}/{50} States")
    answer_state = screen.textinput(title="Guess", prompt="What's another state name?").title()
    if answer_state in states:
        if answer_state not in correct_guesses:
            x_val = state_file[state_file.state == answer_state].x
            y_val = state_file[state_file.state == answer_state].y
            state_turtle = turtle.Turtle()
            state_turtle.hideturtle()
            state_turtle.penup()
            state_turtle.goto(float(x_val), float(y_val))
            state_turtle.write(answer_state)

            score += 1
        correct_guesses.append(answer_state)
       

turtle.mainloop()
