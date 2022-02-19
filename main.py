# -*- coding: utf-8 -*-
"""

@author: Sumeet Shinde (sshinde@andrew.cmu.edu)
@author: Muskan Sharma (muskans@andrew.cmu.edu)
"""

from reddit_scrape import get_reddit_data
from chive_scrape import get_chive_data
from memedroid_scrape import get_memedroid_data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap


### get data from r/memes (subreddit)
reddit_df_1 = get_reddit_data(sub='memes',
                              limit=100,
                            post_type='hot'
                            )

### get data from r/MemeEconomy (subreddit)
reddit_df_2 = get_reddit_data(sub='MemeEconomy',
                              limit=100,
                            post_type='hot'
                            )

### get data from chive.com
chive_df = get_chive_data()

### get data from memedroid.com
memedroid_df = get_memedroid_data()

### get data from memegenerator.net using CSV file
memegenerator_df = pd.read_csv('memegenerator.csv')
memegenerator_df['score'] = memegenerator_df['upvotes'] - memegenerator_df['downvotes']
print(memegenerator_df.head())


### integrate data from all websites
df_all = pd.concat([reddit_df_1,
                   reddit_df_2,
                    chive_df,
                   memegenerator_df,
                   memedroid_df],ignore_index=True)


### get memes with highest score
df_sorted = df_all.sort_values(by=['score'],ascending=False)

#print(df_sorted.shape)


### data cleaning
df_clean = df_sorted.drop(['Meme ID', 'Meme Page URL', 'MD5 Hash', 'File Size (In Bytes)', 'Alternate Text', 'Display Name', 'Upper Text'], axis = 1)


# visualizations
df_clean.nlargest(10,['score']).plot(kind="bar",x='title',y='score',title='Top 10 Trendiest Memes based on Score',figsize=(8,8));


df_clean["downvotes"] = df_clean["downvotes"].replace('None', np.nan).astype(float)
df_clean.nlargest(10,['downvotes']).plot(kind="bar",x='title',y='downvotes',title='Most Disliked Memes',figsize=(8,8));

df_clean["upvotes"] = df_clean["upvotes"].replace('None', np.nan).astype(float)
df_clean.nlargest(10,['upvotes']).plot(kind="bar",x='title',y='upvotes',title='Memes having the highest number of Upvotes',figsize=(8,8));

df_clean["total_votes"] = df_clean["total_votes"].replace('None', np.nan).astype(float)
df_clean.nlargest(10,['total_votes']).plot(kind="bar",x='title',y='total_votes',title='Memes having highest poll participation',figsize=(8,8));



