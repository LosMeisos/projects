
## all libraries
import random
import PySimpleGUI as sg
import select_color as sc

def give_out_pb_color(i, pb, u):
    playboard = pb

    if playboard[i] == 0:
       msg =[sg.Button(image_filename='white.png')]
    elif playboard[i] == 1:
      msg =f[sg.Button(image_filename='red.png')]  
    elif playboard[i] == 2:
        msg =[sg.Button(image_filename='blue.png')] 
    elif playboard[i] == 3:
        msg =[sg.Button(image_filename='white.png')] 
    return msg
   



#blayboard numbers stand for colors
# 0=white, 1==red, 2==blue, 3==green
playboard = [
             0,1,0,0,0,0,
             0,2,0,2,0,0,
             0,3,0,1,0,0,
             0,0,0,0,0,0,
             0,3,0,2,0,0,
             0,0,0,0,0,0,
             ]


print("#### welcoem to the game")


i = 0
u = 0
## creating the layout for the gui
layout = [
  [sg.Text('welcome to darwins play simulator')]

]


while i<=len(playboard):
    while u < 5:
        layout.append(sc.give_out_pb_color(i, playboard, 0))
        u+=1
        i+=1
    
    if i+1 == len(playboard):
        break    
        
    layout.append([sg.Text(sc.give_out_pb_color(i, playboard, 1))]) 
    u=0
    i+=1
    

##setting the window title and adding cancel button
layout.append([sg.Button('cancel')])
print(layout)
window = sg.Window('darwin-game', layout)
    
    
while True:
    
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'cancel':
        break
    
    