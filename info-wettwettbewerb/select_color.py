
def give_out_pb_color(i, pb, u):
    playboard = pb

    if playboard[i] == 0:
       msg ="[sg.Button(image_filename='white.png')]
    elif playboard[i] == 1:
      msg =f[sg.Button(image_filename='red.png')]  
    elif playboard[i] == 2:
        msg =[sg.Button(image_filename='blue.png')] 
    elif playboard[i] == 3:
        msg =[sg.Button(image_filename='white.png')] 
    return msg
   