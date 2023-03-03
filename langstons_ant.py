import arcade
import random
import numpy as np

ROW_COUNT = 50
COLUMN_COUNT = 50

SCREEN_TITLE = "Ant"

WIDTH = 20
HEIGHT = 20

MARGIN = 5

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN

grid = np.zeros((COLUMN_COUNT,ROW_COUNT))
grid2 = np.zeros((COLUMN_COUNT,ROW_COUNT))
sprite_grid = arcade.SpriteList()

FALSE_COL = arcade.color.WHITE #all tiles are white, we change alpha value to darken them when they are True

direction_list = (0,1,2,3) #0 for UP, 1 FOR RIGHT, 2 FOR DOWN, 3 FOR LEFT, M for monkey
current_direction = 3 #Starting direction is facing left

current_x = (COLUMN_COUNT/2) #We start off at the center
current_y = (ROW_COUNT/2)




for row in range(ROW_COUNT):
    for column in range(COLUMN_COUNT):
        sprite = arcade.SpriteSolidColor(WIDTH, HEIGHT, FALSE_COL)

        x = column * (WIDTH + MARGIN) + (WIDTH / 2 + MARGIN)
        y = row * (HEIGHT + MARGIN) + (HEIGHT / 2 + MARGIN)
        sprite.center_x = x
        sprite.center_y = y

        sprite_grid.append(sprite)

class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        self.clear()
        sprite_grid.draw()

    def on_update(self,delta_time):
        update_state()
        for sprite in sprite_grid:
            xval = sprite.center_x
            yval = sprite.center_y
            #find the corresponding location in our grid
            cval = ((2*xval) - WIDTH - (2*MARGIN))/(2*(WIDTH+MARGIN))
            rval = ((2*yval) - HEIGHT - (2*MARGIN))/(2*(HEIGHT+MARGIN))
            if(grid[int(cval)][int(rval)]) == 0: #we change alpha values to represent tiles as white or black
               sprite.alpha = 255
            else:
                sprite.alpha = 157
            
            

def initialize_grid(grid): #setting all values to 0 at the start
    for i in range(COLUMN_COUNT):
        for j in range(ROW_COUNT):
                grid[i][j] = 0

def within_bounds(x,y): #returns false if an x,y value is outside of our range
    if x < 0 or x >= ROW_COUNT:
        return False
    if y < 0 or y >= COLUMN_COUNT:
        return False
    return True

def set_dir(current_direction,tile_value): #we use modulus 4 to change rotation 0,1,2,3
    if(tile_value):
        return (current_direction - 1) % 4
    else:
        return (current_direction + 1) % 4

def move(x,y,current_direction):
    if(current_direction == 0): #moving up
        return (x,y-1)
    if(current_direction == 1): #moving right
        return (x+1,y)
    if(current_direction == 2): #moving down
        return (x+1,y+1)
    if(current_direction == 3): #moving left
        return(x-1,y)
    #moving on
        
def update_state():
    global current_x
    global current_y
    global current_direction

    x = int(current_x)
    y = int(current_y)
    print("Current dir: {} Current x: {} Current y: {}".format(current_direction,current_x,current_y))

    tile_value = grid[x][y]
    current_direction = set_dir(current_direction,tile_value) #update direction based on tile color

    current_x,current_y = move(x,y,current_direction)   #update current location based on direction
    
    if(tile_value):     #flip white to black or black to white
        grid[x][y] = 0
    else:
        grid[x][y] = 1

def main():
    initialize_grid(grid)
    game = MyGame(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    arcade.run()

    
if __name__ == "__main__":
    main()
