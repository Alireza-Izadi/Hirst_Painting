#import colorgram

#rgb_colors = []

#colors = colorgram.extract("./painting_image.jpg", 30)

#for color in colors:
#    r= color.rgb.r
#   g= color.rgb.g
#    b= color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)

#print(rgb_colors)
import turtle
import random

al = turtle.Turtle()

turtle.colormode(255)


color_list = [(233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]
def hirst_painting(size):
    x = 0
    y = 0
    al.penup()
    al.hideturtle()
    for _ in range(size):
        x= 0
        for _ in range(size):
            al.dot(20, random.choice(color_list))
            al.setpos(x, y)
            x += 50
        else:
            y += 50
            
            
            
hirst_painting(10)            
            
        
        
        
        
        
screen = turtle.Screen()
screen.exitonclick()