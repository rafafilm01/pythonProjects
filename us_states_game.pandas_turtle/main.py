import turtle
import pandas

#setting up the screen and the map
screen = turtle.Screen()
screen.title('US States game')
image = 'blank_states_img.gif'
screen.addshape(image)
screen.bgcolor('Black')
turtle.shape(image)



#extract states from .csv and from a series create a lsit of states 
data = pandas.read_csv('50_states.csv')
all_states= data.state.to_list()
guessed_states =[]
states_to_learn =[]

while len(guessed_states) <50:
#user prompt and capturing user's response 
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50', prompt='What is another state' )
    answer_state = answer_state.title()
    
    if answer_state in all_states:
        print('state guessed correctly !')  
        #create a turtle to srite on the map the correct guess 
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        #pull the data from csv to use as coordinates 
        state_data= data[data.state ==answer_state]
        t.goto(int(state_data.x) , int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)

    #exiting out of hte game + saving all guessed states to a CSV file 
    if answer_state  =='Exit':
        # for state in all_states:
        #     if state not in guessed_states:
        #         states_to_learn.append(state)
       # print(states_to_learn)

       #USE LIST COMREHENSION INSTEAD OF THE FOR LOOP
        states_to_learn = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv('states_to_learn.csv')
        break

      

    
  

#getting the coordinnates of states ( so that they can  be written on the map) - NO LONGER NEEDED AS COORDINATES FOR STATES ARE ALREADY IN 50_STATES.CSV 

# def get_mouse_click_coor(x, y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

# screen.exitonclick() - no longer needed here as clicking on the screen closes the app , instead we use turtle.mainloop

# turtle.mainloop() - code no londer required as exit condition will break the loop and close the game . IF turtle.mainloop() stays the game screen would persist once 'Exit' had been introduced 
