
# coding: utf-8

# In[63]:


import os
import csv


# In[64]:


file_path = os.path.join('/Users/daryarudych/Desktop/repos/python-challenge/PyPoll','election_data.csv')
print(file_path)


# In[65]:


with open (file_path, newline = "") as file:
    csvreader = csv.reader(file, delimiter=",")
    headers = next(file).strip().split(',')
    print(headers)

    voter_id = []
    candidates = []
    
    for row in csvreader:
        voter_id.append(row[0])
        candidates.append(row[2])
    print(f"Total votes cast: {len(voter_id)}") 


# In[66]:


#See the runnning candidates
set(candidates)


# In[67]:


votes_Li = candidates.count('Li')
print(f"Li has won: {votes_Li} votes")



# In[68]:


#Calculating the number of votes each candidate has won

for x in set(candidates):
    votes = candidates.count(x)
    print(f"Candidate {x} has won {votes} votes")


# In[69]:


#Calculating the percentage of votes each candidate won
print(f"Election Results")
print(f"------------------------------")
print(f"Total votes cast: {len(voter_id)}") 
print(f"------------------------------")
max_percent = 0
winner_count = 0
for x in set(candidates):
    percentage = (candidates.count(x)*100)/len(voter_id)
    print(f"Candidate {x} has won {round(percentage)}% of votes ({candidates.count(x)})")
   
    if max_percent < percentage :
        max_percent = percentage
        winner_count = x
        
print(f"------------------------------")
print(f"Candidate {winner_count} won")


# In[ ]:



    

