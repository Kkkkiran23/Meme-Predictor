"""

@author: Kiran Solapure (ksolapur@andrew.cmu.edu)
"""


from bs4 import  BeautifulSoup
import requests
import pandas as pd

#ith open('scrapping.html','r') as html_file:
 #   content = html_file.read()
  #  soup = BeautifulSoup(content, 'lxml')

   #  courses_html_tags = soup.findAll('')
   
def get_memedroid_data():
    '''
    

    Returns
    -------
    df : TYPE- dataframe
        DESCRIPTION. returns dataframe containing meme attributes

    '''
     
    html_text = requests.get('https://www.memedroid.com/search?query=trending').text
    #print(html_text)
    soup = BeautifulSoup(html_text, 'lxml')   
    memes = soup.findAll('img')
    
    source=[]
    names=[]
    for image in memes:
        name=image.get('alt')
        link=image.get('src')
        if link.startswith("http"):
         source.append(link)
         names.append(name)
       
        
        
        
    total_list=[]    
    totalvotes = soup.findAll('div')
    
    for totalvote in totalvotes:
       total=totalvote.get('data-votes')
       if total is not None:
        total_list.append(total)
     
    
       
        
    upvotes_list=[]   
    upvotes=soup.findAll('div')
    # print(upvotes)
    for upvote in upvotes:
       up=upvote.get('data-positive-votes')
       if up is not None:
         upvotes_list.append(up)
    
    
    downvotes_list=[int(tot) - int(up) for tot, up in zip(total_list, upvotes_list)]
    
    
    score=[int(up) - int(down) for up, down in zip(upvotes_list, downvotes_list)]
   
    
    df = pd.DataFrame(list(zip(names, score, source, total_list, upvotes_list, downvotes_list)),
                   columns =['title','score', 'url', 'total_votes','upvotes','downvotes']) 
    
    
    return df
   
   
    

    

  