#!/usr/bin/env python
# coding: utf-8

# In[13]
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import shutil
import pandas as pd
import time 
from splinter import Browser
from IPython.display import Image

def init_browser():
    executable_path={"executable_path": "C:\\Users\Silsila Arsalla\\Downloads\\chromedriver.exe"}
    browser=Browser("chrome", **executable_path, headless=False)
    return(browser)

def scrape():
    browser = init_browser()
    mars_data = {}

# In[14]:


    url="https://mars.nasa.gov/news/"
    browser.visit(url)


# In[15]:


    html=browser.html
    soup=BeautifulSoup(html, 'html.parser')


# In[17]:


    article=soup.find("div", class_="list_text")
    news_p=article.find("div", class_="article_teaser_body").text
    news_title=article.find("div", class_="content_title").text
    news_date=article.find("div", class_="list_date").text
    print(news_date)
    print(news_title)
    print(news_p)


# In[18]:


    url2="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)


# In[22]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image = soup.find("img", class_="thumb")["src"]
    img_url = "https://jpl.nasa.gov"+image
    featured_image_url = img_url


# In[23]:


    
    response = requests.get(img_url, stream=True)
    with open('img.jpg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)


# In[24]:


    
    Image(url='img.jpg')


# In[25]:


    print(img_url)


# In[26]:


    url_weather="https://twitter.com/marswxreport?lang=en"
    browser.visit(url_weather)


# In[42]:


    html_weather = browser.html
    soup = BeautifulSoup(html_weather, "html.parser")
    mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    print(mars_weather)


# In[43]:


    url_facts="https://space-facts.com/mars/"


# In[47]:

    
    table=pd.read_html(url_facts)
    table[0]


# In[48]:


    df_mars_facts=table[0]
    df_mars_facts.columns=["Parameter", "Values"]
    df_mars_facts.set_index(["Parameter"])
    
    
    # In[49]:
    
    
    mars_html_table=df_mars_facts.to_html()
    mars_html_table=mars_html_table.replace("\n", "")
    mars_html_table
    
    
    # In[67]:
    
    
    url_hemisphere="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_hemisphere)
    
    
    # In[68]:
    
    
    hemisphere_base_url="{0.scheme}://{0.netloc}/".format(urlsplit(url_hemisphere))
    print(hemisphere_base_url)
    
    
    # In[69]:
    
    

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    mars_hemis=[]
    
    
    # In[70]:
    
    
    for i in range (4):
        time.sleep(5)
        images = browser.find_by_tag('h3')
        images[i].click()
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        partial = soup.find("img", class_="wide-image")["src"]
        img_title = soup.find("h2",class_="title").text
        img_url = 'https://astrogeology.usgs.gov'+ partial
        dictionary={"title":img_title,"img_url":img_url}
        mars_hemis.append(dictionary)
        browser.back()
    
    
    # In[71]:
    
    mars_data['mars_hemis'] = mars_hemis
        # Return the dictionary
    return(mars_data)
    
    
    
    
    # In[ ]:
    
    
    
    
