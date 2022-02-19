"""

@author: Muskan Sharma (muskans@andrew.cmu.edu)
"""


from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


def get_chive_data():
    '''
    

    Returns
    -------
    meme_data : TYPE-dataframe
        DESCRIPTION.  returns dataframe containing memes from chive

    '''

    html = urlopen('https://thechive.com/')
    
    
    tc_table_list = []
    
    content = html.read()
    content = BeautifulSoup(content, 'html.parser')
    
    
   
    
    tc_table_list = content.findAll('h1',attrs = {'class': 'post-title entry-title card-title'})
    

    topic_list = []
    
    for row in tc_table_list:
        topic_list.append(row.text.split("\n\n\t\t\t\t")[1].split("\t\t\t\n")[0])
        
    
    
    downvotes = []
    upvotes = []
    
    #upvotes
    tc_vote_list = content.findAll('span',attrs = {'class': 'card-count icon-card-up upvotes-count'})
    for rows in tc_vote_list:
        upvotes.append(rows.text.split("\t\t\t\t")[1])
                       
    #downvotes
    tc_vote_list2 = content.findAll('span',attrs = {'class': 'card-count icon-card-down downvotes-count'})
    for rows in tc_vote_list2:
        downvotes.append(rows.text.split("\t\t\t\t")[1])
    
    scores = [int(a) -int(b) for a,b in zip(upvotes,downvotes)]
    
    total_votes = [int(a) + int(b) for a,b in zip(upvotes,downvotes)]
    
    #url
    url = []
    url_list = content.findAll('a',attrs = {'class': 'card-img-link'})
    
    for rows in url_list:
        image = content.find('img')
        url.append(image['src'])
    
    
    meme_data = pd.DataFrame(
        {'title': topic_list,
         'score' : scores,
         'url': url,
         'total_votes': total_votes,
         'upvotes': upvotes,
         'downvotes': downvotes
        })
    
 
    
    return meme_data
    


    