#!/usr/bin/env python
# coding: utf-8

# In[1]:


from classy import *
from pylab import imread,imsave


# In[2]:


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


# In[3]:


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


# In[4]:


def read_state():
    from pylab import imread,imsave
    import os
    from Game import Board

    # train the classifier
    images=image.load_images('images/Boards/squares/',delete_alpha=True)  #<=========
    shape=images.data[0].shape[:2]
    data_train=data=image.images_to_vectors(images,verbose=True)  # train on all of them

    #classifier=kNearestNeighbor()
    classifier=NaiveBayes()
    classifier.fit(data_train.vectors,data_train.targets)


    # get the picture
    #take_picture('current_board.jpg')
    arr=imread('current_board.jpg')


    # slice the picture into squares of the right size
    shape=data_train.shape[:2]
    squares=[get_square(arr,i,shape) for i in range(16)]    #<========= change the size
    test_images=image.array_to_image_struct(squares)

    # get predictions
    test_data=image.images_to_vectors(test_images)
    predictions=classifier.predict(test_data.vectors)
    names=[data_train.target_names[p] for p in predictions]

    if not os.path.exists('images'):
        os.mkdir('images')
    if not os.path.exists('images/predicted'):
        os.mkdir('images/predicted')
    for i,(square,prediction) in enumerate(zip(squares,predictions)):
        imsave('images/predicted/square %d predicted as %s.jpg' % (i,data_train.target_names[prediction]),square)

    
    # reconstruct the state from the predictions
    state=Board(4,4)                                         #<========= change the size
    for i in range(16):                                      #<========= change the size
        color=data_train.target_names[predictions[i]]
        if color=="Nothing":                                   #<========= change the colors and values
            state[i]=0                                       #<========= change the colors and values
        elif color=="White":
            state[i]=1
        elif color=="Black":
            state[i]=2
        else:
            raise ValueError("You can't get there from here.")

    print("Current state is:")
    print(state)

    x=input("""
    Hit return if this is correct, otherwise type a character 
    and the state will be read from current_board.txt.""")

    if x:
        print("Reading from file...")
        state=read_state_from_file()

    print("Using")
    print(state)

    
    return state


# In[ ]:


state=read_state()


# In[ ]:




