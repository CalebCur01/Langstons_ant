import arcade
import random
import numpy as np

# {{{1, 1, 1}, {1, 8, 0}}, {{1, 2, 1}, {0, 1, 0}}}
#This is 2 state 2 color "Spiral Growth" turmite


ROW_COUNT = 100
COLUMN_COUNT = 100

SCREEN_TITLE = "Spiral Growth"

WIDTH = 10
HEIGHT = 10

MARGIN = 0

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN

grid = np.zeros((COLUMN_COUNT,ROW_COUNT))
grid2 = np.zeros((COLUMN_COUNT,ROW_COUNT))
sprite_grid = arcade.SpriteList()

FALSE_COL = arcade.color.PORTLAND_ORANGE #all tiles are white, we change alpha value to darken them when they are True

rules = ((1,1,1),(1,2,1),(1,8,0),(0,1,0))

direction_list = (1,2,4,8) #1 = noturn, 2=right,4 = uturn, 8 = left

cur_dir = 0 #0 = UP 1 = RIGHT, 2 = DOWN, 3 = LEFT
cur_col = (int(COLUMN_COUNT/2)) #We start off at the center
cur_row = (int(ROW_COUNT/2))
cur_state = 0 #is 0 or 1
cur_rule = rules[0] #selected from our triples of instructions


step = 0 #to keep track of what step we are on



class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)

        arcade.set_background_color(arcade.color.OXFORD_BLUE)
        self.spritelist = arcade.SpriteList() #list of sprites for tiles

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                x = column * (WIDTH + MARGIN) + (WIDTH / 2 + MARGIN)
                y = row * (HEIGHT + MARGIN) + (HEIGHT / 2 + MARGIN)
                sprite = arcade.SpriteSolidColor(WIDTH,HEIGHT,FALSE_COL)
                sprite.center_x = x
                sprite.center_y = y
                self.spritelist.append(sprite)

    def on_draw(self):
        self.clear()
        self.spritelist.draw()
        

    def on_update(self,delta_time):
        update_state()
        for row in range(ROW_COUNT):                    #[][][]
            for column in range(COLUMN_COUNT):          #[][][]
                location = row * COLUMN_COUNT + column  #[][][]
                if grid[row][column] == 0:
                    self.spritelist[location].alpha = 0 #we change alpha values to paint tiles darker for TRUE
                else:
                    self.spritelist[location].alpha = 255
        
            
            

def initialize_grid(grid): #setting all values to 0 at the start
    for row in range(ROW_COUNT):
        for column in range(COLUMN_COUNT):
                grid[row][column] = 0


def set_dir(cur_dir,change_val): # 1 -> no turn, 2 -> right, 8 -> left, 4 -> Uturn
    if(change_val == 1):                 
        return cur_dir
    if(change_val == 2): # 2 -> turn right
        if(cur_dir == 0):
            return 1
        if(cur_dir == 1):
            return 2
        if(cur_dir == 2):
            return 3
        if(cur_dir == 3):
            return 0
    if(change_val == 8): #8 -> turn left 
        if(cur_dir == 0):
            return 3
        if(cur_dir == 1):
            return 0
        if(cur_dir == 2):
            return 1
        if(cur_dir == 3):
            return 2
    if(change_val == 4): #4 -> Uturn
        if(cur_dir == 0):
            return 2
        if(cur_dir == 1):
            return 3
        if(cur_dir == 2):
            return 0
        if(cur_dir == 3):
            return 1
            


def move(row,column,cur_dir):
    if(cur_dir == 0): #moving up
        return (row+1,column)
    if(cur_dir == 1): #moving right
        return (row,column+1)
    if(cur_dir == 2): #moving down
        return (row-1,column)
    if(cur_dir == 3): #moving left
        return(row,column-1)
    #moving on
        
def update_state():
    global cur_row
    global cur_col
    global cur_dir
    global step
    global cur_state
    global cur_rule

    print("step {}".format(step))
    step +=1

    color = grid[cur_row][cur_col]
    if(not color):
        if(cur_state == 0):
            cur_rule = rules[0] #{1,1,1}
        if(cur_state == 1):
            cur_rule = rules[1] #{1,2,1}
    if(color):
        if(cur_state == 0):
            cur_rule = rules[2] #{1,8,0}
        if(cur_state == 1):
            cur_rule = rules[3] #{0,1,0}          

    grid[cur_row][cur_col] = cur_rule[0]
    cur_dir = set_dir(cur_dir,cur_rule[1])
    cur_state = cur_rule[2]
    cur_row,cur_col = move(cur_row,cur_col,cur_dir)



        

def main():
    initialize_grid(grid)
    game = MyGame(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    arcade.run()

    
if __name__ == "__main__":
    main()
