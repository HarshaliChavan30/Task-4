import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("D://assignment//Task-4//USvideos1.csv")
df.head()
df.shape

df.describe()

df =df.drop_duplicates()
df.shape

df.info()

columns_to_remove =['thumbnail_link' ,'description']
df = df.drop(columns=columns_to_remove)
df.info()

from datetime import datetime
import datetime


df["trending_date"] = df["trending_date"].apply(lambda x :datetime.datetime.strptime(x ,'%y.%d.%m'))
df.head(3)

df['publish_time'] = pd.to_datetime(df["publish_time"])
df.head(2)

df['publish_month'] = df["publish_time"].dt.month
df['publish_day'] = df["publish_time"].dt.day
df['publish_hour'] = df["publish_time"].dt.hour
df.head(2)

print(sorted(df["category_id"].unique()))

df["category_name"] = np.nan

df.loc[(df["category_id"] == 1) ,"category_name"] = "film and animation"
df.loc[(df["category_id"] == 2) ,"category_name"] = "auto bikes"
df.loc[(df["category_id"] == 10) ,"category_name"] = "music"
df.loc[(df["category_id"] == 15) ,"category_name"] = "pets and animals"
df.loc[(df["category_id"] == 17) ,"category_name"] = "sports"
df.loc[(df["category_id"] == 19) ,"category_name"] = "gaming"
df.loc[(df["category_id"] == 20) ,"category_name"] = "people and blog"
df.loc[(df["category_id"] == 22) ,"category_name"] = "comedy"
df.loc[(df["category_id"] == 23) ,"category_name"] = "horror"
df.loc[(df["category_id"] == 24) ,"category_name"] = "masti"
df.loc[(df["category_id"] == 25) ,"category_name"] = "drama"
df.loc[(df["category_id"] == 26) ,"category_name"] = "dhamaka"
df.loc[(df["category_id"] == 27) ,"category_name"] = "laughter"
df.loc[(df["category_id"] == 28) ,"category_name"] = "news and politics"
df.loc[(df["category_id"] == 29) ,"category_name"] = "birthday"
df.loc[(df["category_id"] == 43) ,"category_name"] = "computer"
df.head()

df['year'] = df['publish_time'].dt.year
yearly_counts = df.groupby("year")['video_id'].count()

yearly_counts.plot(kind = 'bar', xlabel = 'Year',ylabel = 'Total Publish Count',title = 'Total Publish Video Per Year')

#show the chart
plt.show()

#Group by year and sum the viewss for each year
yearly_views = df.groupby('year')['views'].sum()

#creat a bar chart
yearly_views.plot(kind = 'bar' ,xlabel = 'Year' , ylabel ='Total Views', title ='Total Views Per Year')
plt.xticks(rotation=0)
plt.tight_layout()

#show the bar chart

plt.show()

#Group the data by 'category_name' and calculate the sum of 'views' in each category

category_views = df.groupby("category_name")['views'].sum().reset_index()

#sort the categories by views in decending order
top_categories = category_views.sort_values(by ='views' , ascending = False).head(5)

#create a bar plot to visualize the top 5 categories

plt.bar(top_categories['category_name'],top_categories['views'])
plt.xlabel('category name',fontsize =12)
plt.ylabel('Total Views' , fontsize=12)
plt.title('Top 5 Categories' , fontsize =15)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,6))
sns.countplot(x='category_name' , data=df, order=df['category_name'].value_counts().index)
plt.xticks(rotation=90)
plt.title("Video Count by Category")
plt.show

#Count the number of videos published per hour
video_per_hour = df["publish_hour"].value_counts().sort_index()


plt.figure(figsize=(12,6))
sns.barplot(x=video_per_hour.index , y=videos_per_hour.values , palette="rocket")
plt.title("Number of Videos Published per Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Videos")
plt.xticks(rotation=45)
plt.show()

df["publish_time"]=pd.to_datetime(df["publish_time"])
df["publish_date"] = df["publish_time"].dt.date
video_count_by_date = df.groupby("publish_date").size()
plt.figure(figsize=(12,6))
sns.lineplot(data =video_count_by_date)
plt.title("Videos Published Over Time")
plt.xlabel("Publish Date")
plt.ylabel("Number if Videos")
plt.xticks(rotation=45)
plt.show()

#scatter plot between 'views' and'likes'

sns.scatterplot(data=df , x= "views" , y="likes")
plt.title("Views vs Likes")
plt.xlabel("views")
plt.ylabel("Likes")
plt.show()


plt.figure(figsize =(14,8))
plt.subplots_adjust(wspace =0.2 ,hspace=0.4 ,top =0.9)
plt.subplot(2,2,1)
g =sns.countplot (x="comments_disabled" , data=df)
g.set_title("Comments Disabled" ,fontsize =16)
plt.subplot(2,2,2)
g1 = sns.countplot(x = "ratings_disabled" ,data=df)
g1.set_title("Rating Disabled" , fontsize =16)
plt.subplot(2,2,3)
g2 = sns.countplot(x="video_error_or_removed" ,data=df)
g2.set_title("video_Error_or_removed", fontsize =16)
plt.show()

corr_matrix =df["views"].corr(df["likes"])
corr_matrix