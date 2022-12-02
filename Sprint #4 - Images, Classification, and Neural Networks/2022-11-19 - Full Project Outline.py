#!/usr/bin/env python
# coding: utf-8

# Let's work backward from the answer we need to how we get there.  We'll write the entire robot playing a board game.  We'll make empty or partial functions first, and then fill them out.

# In[ ]:


# don't run these yet -- they are defined below
state=read_state()     #  read the state from the world
move=get_move(state,1)   # from an agent
make_move(move)        # robot motion to move pieces, etc...


# # get_move

# In[1]:


from breakthrough import *


# there are several get_move functions one could use.  Like random....

# In[2]:


def random_move(state,player):
    moves=valid_moves(state,player)
    return random.choice(moves)

def get_move(state,player):
    return random_move(state,player)


# or minimax the same way.

# In[3]:


def get_move(state,player):
    return minimax_move(state,player)


# Q or skittles, the move comes from the table.

# In[3]:


def get_move(state,player):
    if player==1:
        Q=LoadTable("Q1_breakthrough_table.json")
    else:
        Q=LoadTable("Q2_breakthrough_table.json")
        
    
    if state not in Q:
        return random_move(state,player)
    else:
        return top_choice(Q[state])


# In[4]:


state=initial_state()


# In[5]:


get_move(state,1)


# ## make_move

# the minimal one just prints the move

# In[6]:


def make_move(move):
    print("If I could move, I would do move: ",move)


# everything else will be specific to your robot, but it might do something like this.

# In[7]:


move=[12,8]
move=[9,6]


# In[8]:


def move_forward(distance):
    print("forward ",distance)
    
def move_backward(distance):
    print("backward ",distance)    
    
def turn_robot_left_90():
    print("left 90")
    
def turn_robot_right_90():
    print("right 90")    
    
def turn_robot_left_45():
    print("left 45")    
    
def turn_robot_right_45():
    print("right 45")     
    
def arm_up():
    print("arm up")
def arm_down():
    print("arm down")


# In[9]:


def make_move(move):
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

    


# In[10]:


state=initial_state()
show_state(state)
state.show_locations()


# In[11]:


make_move([13,8])


# ## read_state

# a nice fall-back is to read the state from a file

# In[12]:


def read_state_from_file(filename='current_board.txt'):
    with open(filename) as fid:
        text=fid.read()

    text2=text.strip().split('\n')
    number_of_rows=len(text2)
    number_of_cols=len(text2[0].split())
    
    b=Board(number_of_rows,number_of_cols)
        
    board=[int(v) for v in text.split()]
    b.board=board
    return b


# In[13]:


def read_state():
    state=read_state_from_file()
    return state


# In[14]:


with open("current_board.txt","w") as fid:
    fid.write("""
2 0 2 0 
0 2 0 0
1 0 1 1
0 1 0 0
    """)


# In[15]:


state=read_state()
show_state(state)


# now we can do the reading from the world

# In[16]:


from classy import *


# Assuming you have collection of training images, train the classifier....

# In[17]:


def take_picture(fname):
    pass

def get_square(arr,index,shape,locations=None):
    import json
    
    if locations is None:
        with open('locations.json') as json_file:
            locations = json.load(json_file)        
    
    try:
        location=locations[index]
    except IndexError:
        print("locations.json file probably corrupt.")
        raise 
        
    c,r=location
    c1=int(c-shape[1]/2)
    c2=int(c+shape[1]/2)
    r1=int(r-shape[0]/2)
    r2=int(r+shape[0]/2)

    c2=c2+(shape[1]-(c2-c1))
    r2=r2+(shape[0]-(r2-r1))

    square=arr[r1:r2,c1:c2,:]
    
    return square


# In[18]:


from pylab import imread,imsave


# In[21]:


def read_state():
    from pylab import imread,imsave
    import os

    # train the classifier
    images=image.load_images('images/all_pieces',delete_alpha=True)
    shape=images.data[0].shape[:2]
    data_train=data=image.images_to_vectors(images,verbose=True)  # train on all of them

    #classifier=kNearestNeighbor()
    classifier=NaiveBayes()
    classifier.fit(data_train.vectors,data_train.targets)


    # get the picture
    take_picture('current_board.jpg')
    arr=imread('current_board.jpg')


    # slice the picture into squares of the right size
    shape=data_train.shape[:2]
    squares=[get_square(arr,i,shape) for i in range(16)]
    test_images=image.array_to_image_struct(squares)

    # get predictions
    test_data=image.images_to_vectors(test_images)
    predictions=classifier.predict(test_data.vectors)
    names=[data_train.target_names[p] for p in predictions]

    if not os.path.exists('images/predicted'):
        os.mkdir('images/predicted')
    for i,(square,prediction) in enumerate(zip(squares,predictions)):
        imsave('images/predicted/square %d predicted as %s.jpg' % (i,data_train.target_names[prediction]),square)

    
    # reconstruct the state from the predictions
    state=Board(4,4)
    for i in range(16):
        color=data_train.target_names[predictions[i]]
        if color=="white":
            state[i]=0
        elif color=="red":
            state[i]=1
        elif color=="black":
            state[i]=2
        else:
            raise ValueError("You can't get there from here.")

    print("Current state is:")
    print(state)

    x=input("""
    Hit return if this is correct, otherwise type a character 
    and the state will be read from current_board.txt.""")

    if x:
        state=read_state_from_file()

    print("Using")
    print(state)

    
    return state


# In[22]:


state=read_state()


# ## Now the full game

# In[23]:


state=read_state()     #  read the state from the world
move=get_move(state,1)   # from an agent
make_move(move)        # robot motion to move pieces, etc...


# In[ ]:




