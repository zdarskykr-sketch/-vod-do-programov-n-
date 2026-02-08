# vizualiyace kochovy pomocí turtle grafiky
# Kryštof Žďárský, 3. ročník, GE-KA
# zimní semestr 2025/2026
# Úvod do programování

import turtle
class KochFlake:
    def __init__(self, turtle_obj, side_length, order): # initialize snowflake and checks and limites the depth to recursion
        self.t = turtle_obj
        self.side_length = side_length
        
        if order > 5: # checks limits of recursion of input
            print("Value was set to 5.")
            self.order = 5
        elif order < 0:
            print("Value was set to 0.")
            self.order = 0
        else:
            self.order = order

    def konch_order(self, length, current_order): # Recursive method to draw one side of the Koch Snowflake (the curve).
        if current_order == 0:
            self.t.forward(length)
        else:
            new_length = length / 3
            self.konch_order(new_length, current_order - 1)
            self.t.left(60)
            self.konch_order(new_length, current_order - 1)
            self.t.right(120)
            self.konch_order(new_length, current_order - 1)
            self.t.left(60)
            self.konch_order(new_length, current_order - 1)
    
    def flake(self): # closes the snowflake by repeating the curve three times and it centers the snowflake on the screen.
        self.t.penup()
        self.t.goto(-self.side_length / 2, self.side_length / 3) # centering of the snowflake on the screen
        self.t.pendown()

        for _ in range(3):
            self.konch_order(self.side_length, self.order)
            self.t.right(120)

if __name__ == "__main__": # main method to run the program and get user input.

    side_length = int(input("Input the side length of the snowflake: "))  # user input for length of the side of the snowflake
    order = int(input("Input the depth of recursion (0-5): "))            # user input for the depth of recursion
    speed = int(input("Input the speed of drawing (1-11): "))             # user input for the speed fo drawing
    screen = turtle.Screen()
    t = turtle.Turtle()
    screen.title("Koch's Snowflake")
    t.speed(speed)

    moje_vlocka = KochFlake(t, side_length, order)
    moje_vlocka.vlocka()
    screen.exitonclick()