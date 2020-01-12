#########
# Created by Eric Davidson
#########

# Size of the canvas
w, h = 1200, 1200

# Size of the dice grid
grid_pixel_width = 600
grid_pixel_height = 1000

# Individual die size
die_size = 50

# Level of bezeling on die corners
round_corners = 7

# Size of the die number indicators
dot_size = 8

# Line thickness
stroke_weight = 3

# Affects how closely the dots will get to the edge of the die face
edge = 3.0

# How far apart each die will be from another in a group
x_die_sep = die_size * .8
y_die_sep = die_size * .6


# Different grid Sizes for different dice count, use factor pairs
# 2 Dice - 21, 3 Dice - 56, 4 Dice - 126, 6 Dice - 462
grid_width = 3
grid_height = 7


# Draw the top face and dots
def draw_die(x, y, d):
    fill(255)
    stroke(0)
    strokeWeight(stroke_weight)
    rect(x - die_size/2, y - die_size/2, die_size, die_size, round_corners)
    
    fill(0)
    noStroke()
    if (d == 1):
        circle(x, y, dot_size)
    if (d == 2):
        circle(x - die_size/edge, y + die_size/edge, dot_size)
        circle(x + die_size/edge, y - die_size/edge, dot_size)
    if (d == 3):
        circle(x, y, dot_size)
        circle(x - die_size/edge, y + die_size/edge, dot_size)
        circle(x + die_size/edge, y - die_size/edge, dot_size)
    if (d == 4):
        circle(x - die_size/edge, y + die_size/edge, dot_size)
        circle(x + die_size/edge, y - die_size/edge, dot_size)
        circle(x + die_size/edge, y + die_size/edge, dot_size)
        circle(x - die_size/edge, y - die_size/edge, dot_size)
    if (d == 5):
        circle(x, y, dot_size)
        circle(x - die_size/edge, y + die_size/edge, dot_size)
        circle(x + die_size/edge, y - die_size/edge, dot_size)
        circle(x + die_size/edge, y + die_size/edge, dot_size)
        circle(x - die_size/edge, y - die_size/edge, dot_size)
    if (d == 6):
        circle(x - die_size/edge, y + die_size/edge, dot_size)
        circle(x + die_size/edge, y - die_size/edge, dot_size)
        circle(x + die_size/edge, y + die_size/edge, dot_size)
        circle(x - die_size/edge, y - die_size/edge, dot_size)
        circle(x + die_size/edge, y, dot_size)
        circle(x - die_size/edge, y, dot_size)
        
# Lots of manual placement for different group sizes
def draw_group(x, y, c):
    if len(c) == 1:
        draw_die(x, y, c[0])
    if len(c) == 2:
        draw_die(x - x_die_sep, y, c[0])
        draw_die(x + x_die_sep, y, c[1])
    if len(c) == 3:
        draw_die(x - x_die_sep, y, c[0])
        draw_die(x, y, c[1])
        draw_die(x + x_die_sep, y, c[2])
    if len(c) == 4:
        draw_die(x - x_die_sep, y - y_die_sep, c[0])
        draw_die(x + x_die_sep, y - y_die_sep, c[1])
        draw_die(x - x_die_sep, y + y_die_sep, c[2])
        draw_die(x + x_die_sep, y + y_die_sep, c[3])
    if len(c) == 6:
        draw_die(x - x_die_sep, y - y_die_sep, c[0])
        draw_die(x, y - y_die_sep, c[1])
        draw_die(x + x_die_sep, y - y_die_sep, c[2])
        draw_die(x - x_die_sep, y + y_die_sep, c[3])
        draw_die(x, y + y_die_sep, c[1])
        draw_die(x + x_die_sep, y + y_die_sep, c[2])
    
    
def setup():
    size(w, h)
    pixelDensity(2)
    strokeWeight(1)
    background(255)
    
    
    combinations = []
    
    # Load the generated combinations from permutations.py
    f = loadStrings('Out/comb_with_replace-2.txt')
    
    for c in f:
        combinations.append(list(int(x) for x in c.split(' ')))

    
    horizontal_sep = float(grid_pixel_width)/(grid_width - 1)
    vertical_sep = float(grid_pixel_height)/(grid_height - 1)
    
    current_position = (w/2.0 - grid_pixel_width/2.0, h/2.0 - grid_pixel_height/2.0)
    
    # Draw each dice group
    for c in range(grid_width):
        for r in range(grid_height):
            draw_group(current_position[0], current_position[1], combinations[c * grid_height + r])
        
            current_position = (current_position[0], current_position[1] + vertical_sep)
        current_position = (current_position[0] + horizontal_sep, h/2 - grid_pixel_height/2.0)
        
    save("Examples/comb-2.png")
    
    
