#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[2]:


import xmlrpc.client


# In[3]:


def to_string(arr):
    import json
    s=json.dumps(arr.tolist())
    return s

def from_string(s):
    import json
    from numpy import array
    arr=array(json.loads(s))
    return arr


# In[4]:


def make_move(move):
    from Game import Board
    print("Making move ",move)
    
    board=Board(4,4)  # just to get the conversion functions for free
    
    start,end=move
    rs,cs=board.rc_from_index(start)  # convert to row, column
    re,ce=board.rc_from_index(end)
    
    distance_to_board=10
    length_column=4
    length_row=4

    type_of_move=ce-cs  # 0 for a forward move, +1 for a right-hand diagonal, -1 for left-hand diagonal
    distance_to_column=distance_to_board+length_column*cs
    distance_to_row=(4-rs)*length_row

    if type_of_move==0:  # forward

        move_forward(distance_to_column)
        turn_robot_left_90()
        move_forward(distance_to_row)
        arm_down()  # to push the piece
        move_forward( 1*length_row )
        arm_up()

        # go back
        move_backward(distance_to_row + 1*length_row)
        turn_robot_right_90()
        move_backward(distance_to_column)

    elif type_of_move==1:  # right-hand diagonal

        move_forward(distance_to_column)
        turn_robot_left_90()
        move_forward(distance_to_row)


        arm_down()  # to push the piece
        turn_robot_right_45()
        move_forward( 1*length_row )

        # go back
        move_backward(1*length_row)
        turn_robot_left_45()    
        move_backward(distance_to_row )
        turn_robot_right_90()
        move_backward(distance_to_column)

    elif type_of_move==-1:  # left-hand diagonal
        move_forward(distance_to_column)
        turn_robot_left_90()
        move_forward(distance_to_row)


        arm_down()  # to push the piece
        turn_robot_left_45()
        move_forward( 1*length_row )

        # go back
        move_backward(1*length_row)
        turn_robot_right_45()    
        move_backward(distance_to_row )
        turn_robot_right_90()
        move_backward(distance_to_column)

    else:
        raise ValueError("You can't get there from here.")


# In[44]:


robot = xmlrpc.client.ServerProxy('http://dex.local:8002')

move_forward=robot.move_forward
move_backward=robot.move_backward
turn_robot_left_90=robot.turn_robot_left_90
turn_robot_right_90=robot.turn_robot_right_90
turn_robot_left_45=robot.turn_robot_left_45
turn_robot_right_45=robot.turn_robot_right_45
arm_up=robot.arm_up
arm_down=robot.arm_down


# In[53]:


robot.move_forward(5)


# In[54]:


robot.arm_up()


# In[60]:


im=from_string(server.take_picture('current_board.jpg'))


# In[61]:


imshow(im)


# In[64]:


make_move([12,8])


# In[65]:


robot.quit()


# In[ ]:




