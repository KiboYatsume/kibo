import turtle as t , random as r

def design_court():
    text="--  --  -- --  -- -- -- --  -- --  -- -- --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  -- "
    g = t.Turtle()
    g.color("yellow")
    g.speed(1)
    g.penup()
    g.goto(-500,220)
    g.pendown()
    g.write(text,font=("verdana",14,"normal"))
    g.penup()
    g.goto(-500,170)
    g.pendown()
    g.write(text,font=("verdana",14,"normal"))
    g.penup()
    g.goto(-500,120)
    g.pendown()
    g.write(text,font=("verdana",14,"normal"))
    g.penup()
    g.goto(-500,70)
    g.pendown()
    g.write(text,font=("verdana",14,"normal"))
    g.penup()
    g.goto(-500,20)
    g.pendown()
    g.write(text,font=("verdana",14,"normal"))
    g.penup()
    g.goto(-500,-30)
    g.pendown()
    g.write(text,font=("verdana",14,"normal"))
    g.hideturtle()
s=t.Screen()
s.setup(height=1.0 , width=1.0 )
s.bgcolor("indigo")

design_court()



