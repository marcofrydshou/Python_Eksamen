
# coding: utf-8

# In[9]:


import urllib.request, json 
import json


# In[32]:


with urllib.request.urlopen("http://api.population.io:80/1.0/countries") as url:
    data = json.loads(url.read().decode())
    countries = data
    print(countries)


# In[52]:


date = '2015-12-24'
country = 'Brazil/'
url = "http://api.population.io:80/1.0/population/"
with urllib.request.urlopen(url + country + date) as url:
    data = json.loads(url.read().decode())
    print(data)
    print(data['total_population']['population'])
  

