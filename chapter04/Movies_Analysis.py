'''
电影数据来源：http://grouplens.org/datasets/movielens/

下载数据文件解压，包含如下4个文件:

users.dat 用户数据
movies.dat 电影数据
ratings.dat 评分数据
README 文件解释


'''


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#读取数据，先定义字段名，因为源数据中无字段名，只有用’::’分割的每条数据.
user_names = ['user_id', 'gender', 'age', 'occupation', 'zip'] #用户表的数据字段名


users = pd.read_table(r"E:\code\python\test\chapter04\ml-1m\users.dat", sep='::', header=None, names=user_names, engine='python')

# print(len(users))
# print(users[:5])

# 同理将movies,ratings数据读进来.
ratings_names = ['user_id', 'movie_id', 'rating', 'Datetime']
ratings = pd.read_table(r"E:\code\python\test\chapter04\ml-1m\ratings.dat", sep='::', header=None, names=ratings_names, engine='python')
ratings["Datetime"] = pd.to_datetime(ratings['Datetime'],unit='s')
movies_names = ['movie_id', 'title', 'genres']
movies = pd.read_table(r"E:\code\python\test\chapter04\ml-1m\movies.dat", sep='::', header=None, names=movies_names, engine='python')

# print(ratings[:5])
# print(movies[:5])

#将3个表合并为一个表data .
data = pd.merge(pd.merge(users, ratings), movies)
# print(len(data))
# print(data.head())

# 查看用户id为1，对所有电影的评分.
# print(data[data.user_id==1])

# 不同性别对不同电影的平均评分.
mean_ratings_by_gender = data.pivot_table(values='rating',index='title',columns='gender', aggfunc='mean')
# print(mean_ratings_by_gender.head(10))#查看前10条数据


# mean_ratings_by_gender增加一列，男女的平均评分差.
mean_ratings_by_gender['diff'] = mean_ratings_by_gender.F - mean_ratings_by_gender.M
# print(mean_ratings_by_gender.head())


#哪些电影是男女评分差异最大的（男性评分高女生评分低，女性高男性低）.
#print(mean_ratings_by_gender.sort_values(by='diff',ascending=True).head())#男高女低
#print(mean_ratings_by_gender.sort_values(by='diff',ascending=False).head())#女高男低


# 不同电影的评分次数.
total_rating_by_title = data.groupby('title').size()
#print(total_rating_by_title)    #第一列是电影标题，第二列是评分次数

#评分次数最多的10部电影
top_10_total_rating = total_rating_by_title.sort_values(ascending=False).head(10)
print(top_10_total_rating)





