#!/usr/bin/env python
# coding: utf-8

# In[1]:


from breakthrough import *


# In[2]:


Q1_agent=Agent(Q_move)
Q1_agent.post=Q_after
Q1_agent.Q=Table()  # makes an empty table
Q1_agent.learning=True

Q1_agent.α=0.3  # learning rate
Q1_agent.ϵ=0.1  # how often to take a random move
Q1_agent.γ=0.9  # memory constant -- how quickly does the table update back in time (earlier in the game)


# In[3]:


Q2_agent=Agent(Q_move)
Q2_agent.post=Q_after
Q2_agent.Q=Table()  # makes an empty table
Q2_agent.learning=True

Q2_agent.α=0.3  # learning rate
Q2_agent.ϵ=0.1  # how often to take a random move
Q2_agent.γ=0.9  # memory constant -- how quickly does the table update back in time (earlier in the game)


# In[4]:


Q1_agent.Q=Table()  # makes an empty table
Q2_agent.Q=Table()  # makes an empty table
SaveTable(Q1_agent.Q,"Q1_breakthrough_table.json")
SaveTable(Q2_agent.Q,"Q2_breakthrough_table.json")    


# In[ ]:





# In[ ]:





# In[ ]:





# In[5]:


Q1_agent.Q=LoadTable("Q1_breakthrough_table.json")
Q2_agent.Q=LoadTable("Q2_breakthrough_table.json")

N_train=100
N_test=100

percentage_player1_wins=[]
percentage_player2_wins=[]
percentage_ties=[]
total_number_of_games=[]

current_game_number=0

for i in tqdm(range(200)):
    
    Q1_agent.learning=Q2_agent.learning=True
    g=Game(number_of_games=N_train)  
    g.display=False
    g.run(Q1_agent,Q2_agent)

    current_game_number+=N_train
    
    Q1_agent.learning=Q2_agent.learning=False
    g=Game(number_of_games=N_test)
    g.display=False
    results=g.run(random_agent,Q2_agent)
    
    percentage_player1_wins.append(results.count(1))
    percentage_player2_wins.append(results.count(2))
    percentage_ties.append(results.count(0)) 
    total_number_of_games.append(current_game_number)
    
SaveTable(Q1_agent.Q,"Q1_breakthrough_table.json")
SaveTable(Q2_agent.Q,"Q2_breakthrough_table.json")    
    


# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib.pylab import figure,plot,legend,xlabel,ylabel,imshow,cm,axis
import matplotlib.pylab as plt


# In[8]:


figure(figsize=(8,6))
plot(total_number_of_games,percentage_player1_wins,'-o',label="Player 1 Wins")
plot(total_number_of_games,percentage_player2_wins,'-x',label="Player 2 Wins")
plot(total_number_of_games,percentage_ties,'-s',label="Ties")
xlabel('Number of Games')
ylabel('Percentage')
legend()


# In[ ]:




