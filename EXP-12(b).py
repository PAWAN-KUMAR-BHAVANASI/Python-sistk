import turtle

def draw_square(t, pos, size):
    t.penup()
    t.setpos(pos)
    t.pendown()
    t.setheading(0)
    for i in range(4):
        t.forward(size)
        t.right(90)

def draw_rectangle(t, pos, width, height):
    t.penup()
    t.setpos(pos)
    t.pendown()
    t.setheading(0)
    for i in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)

def draw_circle(t, pos, radius):
    t.penup()
    t.setpos(pos)
    t.pendown()
    t.setheading(0)
    t.circle(radius)

def draw_triangle(t, pos, side):
    t.penup()
    t.setpos(pos)
    t.pendown()
    t.setheading(0)
    t.forward(side)
    t.right(120)
    t.forward(side)
    t.right(120)
    t.forward(side)

def main():
    # Create the turtle
    t = turtle.Turtle()

    # Draw the square
    draw_square(t, (-100, 0), 50)

    # Draw the rectangle
    draw_rectangle(t, (-25, 0), 100, 50)

    # Draw the circle
    draw_circle(t, (0, 30), 25)

    # Draw the triangle
    draw_triangle(t, (50, -50), 50)

    # Keep the window open until closed manually
    turtle.done()

if __name__ == "__main__":
    main()
