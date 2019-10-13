import turtle

turtle.fillcolor("yellow")
turtle.begin_fill()
for i in range (360):
    turtle.right(1)
    turtle.forward(2)
turtle.circle(100)

turtle.end_fill()
mainloop()
