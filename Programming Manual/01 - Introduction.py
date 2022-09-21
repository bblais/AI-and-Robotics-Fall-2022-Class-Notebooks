#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# This guide is written to provide an introduction to programming, for
# those who may have no programming experience. It uses a
# language/environment called Python (available for free online at
# `www.python.org`), although for Windows I prefer the Enthought
# (`www.enthought.com`) version. At the time of writing this guide, the
# current version of Python is 2.7 (with the Enthought version). The guide
# includes example code and exercises for the reader (with solutions for
# the instructor). Programming is a skill which can only be learned by
# doing, so the examples covered later in the guide depend on code written
# as exercises earlier on. It is therefore important to do all of the
# exercises along the way.
# 
# ## What is Programming?
# 
# A *program* is a sequence of instructions telling the computer what to
# do to accomplish some task. Programming amounts to determining the
# proper sequence of instructions to accomplish the task, writing these
# instructions in some language (also called computer *code*), and testing
# the results of running the program to make sure that the program is in
# fact accomplishing the task correctly. When people write these programs
# for computers to read and execute, difficulties arise because computers
# read languages very differently than people read languages. There are
# two main qualities of computers which are important here: 
# 
# - Computers are *syntactically picky*.
# 
# Syntax refers to the rules about about is allowed in a language. For
# example, the following is *not* syntactically correct English:
# 
# > Th.e qui’ck br.own f/ox ju[mps ov]er t=he 1azy blog.
# 
# There are rules in English for the placement of punctuation marks which
# are seriously violated in this "sentence" (to call it a sentence is to
# infer that it is syntactically correct). Unless you are really
# observant, you may not have even noticed the difference between "lazy"
# and "1azy", the latter having the digit "1" (one) in front. As humans we
# can overlook these small syntactical problems and still infer the
# meaning of the sentence (or *most* of the meaning, if we refuse to
# assume we meant "dog" instead of "blog"). The computer cannot do this.
# Any small syntactical error will cause the program to fail.
# 
# 
# - Computers are *completely literal*.
# 
# Computer languages have *unambiguous* rules: each statement has one, and
# only one, meaning. One example of this we will encounter later is in
# translating an English sentence like "$x$ is less than $y$ and $z$" into
# code. What we *mean* is "$x$ is less than $y$ and $x$ is also less than
# $z$". Depending on how we translate the code, the computer could
# interpret the sentence as "($x$ is less than $y$) and $z$" which, in
# more proper English, would be "$z$ is a true statement and, in addition,
# $x$ is less than $y$". Quite a different meaning than what we intended!
# 
# Solving the syntax problems are the easiest, because the computer will
# generally tell you where they are (even if the error messages it gives
# are a bit obtuse). Solving the problems in *meaning* or what I refer to
# as the *logic* of the program, is much harder. It is very common for a
# programmer to stare at the computer swearing that it is not doing "what
# I told it to do", when in fact the computer does *exactly* what you tell
# it to do. It may not be doing what you *meant* it to do. Tracking down
# these problems, a process known as *debugging*, takes time and practice.
# 
# Learning to program is like learning to play a musical instrument. You
# can read all you want, you can watch others do it, but until you program
# the computer yourself you will never really learn how to do it.
# 

# ## What is Python?
# 
# Python is, as stated in the official introduction,
# 
# > ... an easy to learn, powerful programming language. It has efficient
# > high-level data structures and a simple but effective approach to
# > object-oriented programming. Python's elegant syntax and dynamic
# > typing, together with its interpreted nature, make it an ideal
# > language for scripting and rapid application development in many areas
# > on most platforms.
# 
# When you run Jupyter you will will be greeted with your webbrowser, with a form-field called a *Cell*,
# 
# ![Jupyter Cell.](attachment:d9aa1443-2334-4ae4-8742-856c8a437752.png)
# 
# Everything in this tutorial which is written in `this font` is the text
# displayed in the cell or in a Python program. When I give
# commands to type on the command line, like the command for help, I will
# display it like this
# 

# In[3]:


print("Hello world!")


# ::: callout-tip
# Useful keyboard shortcut: **Shift-enter:  execute (i.e. run) the current cell**
# :::
# 

# At minimum, the Python interpreter is a fancy calculator. For example,
# 
# 

# In[4]:


365*454


# In[5]:


43.0/324.0


# In[6]:


2**10


# In[7]:


import math  # import the math functions


# In[8]:


math.sin(5)


# In[9]:


math.cos(3.14159)


# In[10]:


2+2+2+2+2


# In[11]:


(3+2)*(6+5)


# 
# All of the arithmetic operators (+, -, \*, /, \*\*) are supported. To
# use the standard math functions, like the trigonometric functions (sin,
# cos, tan), one needs to import the math module, with
# 
# ```python
#     In [7]:import math 
# ```
# 
# After that, one can use them, preceding them with `math.`, like
# ` math.sin`, `math.cos`, etc...  Or one can be lazy and load all of the math functions all at once,

# ```python
# from math import *  # load all the math functions
# ```

# ## Your First Program: Hello World
# 
# It is programming tradition to have your first program, in whatever
# language, simply print out a message saying "Hello, World!". Although it
# is perhaps the most basic program to write, in order to get it to run
# you will already have to be able to do several steps: 
# 
# 1. Edit the program
# 2. Save it in the proper place 
# 3. Run the program
# 
# if you're reading this in a Jupyter notebook, you are already done with two thirds of these steps.  All we need is the **Shift-Enter** to run it.

# In[13]:


print("Hello world!")


# 
# ### Error!
# 
# You may find the following error happens:

# ```python
# [11]: prnt("hello world")
# ```
# 
# ![An Error.](attachment:dd773ee7-a46c-4498-a494-5b7f64b902b0.png)
# 
# 
# this is because of a typo -- check your spelling!

# ### A Slightly More Complex Program

# In[14]:


print("Hello, World!")
print("The result of 2+2 is",2+2)


# ### One More Example Program

# In[15]:


import random

print("Hello, World!")
a=random.randint(1,10) # random number from 1-10
b=random.randint(1,10)  # random number from 1-10

c=a+b

print("The result of",a,"+",b,"=",c)


# Try running it several times! What does it do?

# In[ ]:





# In[ ]:




