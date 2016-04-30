import simplegui
import random

WIDTH = 800
HEIGHT = 100
MAX_NUMBER = 8

cards = range(MAX_NUMBER)*2
is_overturn = [False] * MAX_NUMBER * 2
turns = 0
state = 0
choice1_index = 0
choice2_index = 0

def new_game():
    global cards, is_overturn, turns, state, choice1_index, choice2_index
    random.shuffle(cards)
    for index in range(MAX_NUMBER*2):
        is_overturn[index] = False
    state = 0
    turns = 0
    
def mouseclick(pos):
    global state, turns, choice1_index, choice2_index
    index = pos[0] / (WIDTH/(MAX_NUMBER*2))
    if(is_overturn[index] == False):
        #card overturn
        if state == 0:
            #one card overturn
            state = 1
            choice1_index = index
            is_overturn[index] = True
        elif state == 1:
            #two card overturn
            state = 2
            choice2_index = index
            is_overturn[index] = True
        else:
            #is the same?
            if(cards[choice1_index] == cards[choice2_index]):
                pass
            else:
                #overturn the two cards
                is_overturn[choice1_index] = False
                is_overturn[choice2_index] = False
            turns = turns + 1
            choice1_index = index
            is_overturn[index] = True
            state = 1
    else:
        #do nothing
        pass
    pass
    
def draw(canvas):
    global l, turns
    #draw dividing line
    for i in range(MAX_NUMBER*2):
        canvas.draw_line((i*WIDTH/2/MAX_NUMBER, HEIGHT), (i*WIDTH/2/MAX_NUMBER, 0), 1, "Black")
    #draw cards that already overturn
    for i in range(MAX_NUMBER*2):
        if is_overturn[i] == True:
            #show number
            canvas.draw_text(str(cards[i]), (i*WIDTH/MAX_NUMBER/2, 90), 100, "White")
    
    l.set_text("Turns = %d" % turns)

    
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_button("Restart", new_game)
l = frame.add_label("Turns = 0")

frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
frame.set_canvas_background('Green')

new_game()
frame.start()