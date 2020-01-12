


w, h = 1500, 1500

grid_pixel_width = 800
grid_pixel_height = 1300


die_size = 50
round_corners = 7
dot_size = 8
stroke_weight = 3

edge = 3.0

die_sep = die_size * 1.2
group_sep = die_size * 1.75


# Different grid Sizes for different dice count
# 2 Dice - 21, 3 Dice - 56
grid_width = 4
grid_height = 14


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
        
def draw_group(x, y, c):
    if len(c) == 1:
        draw_die(x, y, c[0])
    if len(c) == 2:
        draw_die(x - die_sep, y, c[0])
        draw_die(x + die_sep, y, c[1])
    if len(c) == 3:
        draw_die(x - die_sep, y, c[0])
        draw_die(x, y, c[1])
        draw_die(x + die_sep, y, c[2])
    if len(c) == 4:
        draw_die(x - die_sep, y - die_sep, c[0])
        draw_die(x + die_sep, y - die_sep, c[0])
        draw_die(x - die_sep, y + die_sep, c[0])
        draw_die(x + die_sep, y + die_sep, c[0])

        
def get_permutations(n, m):
    dice = [1, 2, 3, 4, 5, 6]
    
    
    return permutations(dice)
    #return (p for p in permutations.combinations_with_replacement(dice, n) if sum(p) == m)
    
    
def setup():
    size(w, h)
    pixelDensity(2)
    strokeWeight(1)
    background(255)
    
    
    combinations = []
    f = loadStrings('Out/comb_with_replace-4.txt')
    
    for c in f:
        combinations.append(list(int(x) for x in c.split(' ')))
        
    print(len(combinations))

    
    horizontal_sep = float(grid_pixel_width)/(grid_width - 1)
    vertical_sep = float(grid_pixel_height)/(grid_height - 1)
    
    current_position = (w/2.0 - grid_pixel_width/2.0, h/2.0 - grid_pixel_height/2.0)
    
    for c in range(grid_width):
        for r in range(grid_height):
            draw_group(current_position[0], current_position[1], combinations[c * grid_height + r])
        
            current_position = (current_position[0], current_position[1] + vertical_sep)
        current_position = (current_position[0] + horizontal_sep, h/2 - grid_pixel_height/2.0)
        
    save("Examples/" + str(int(random(10000))) + ".png")
    
    
