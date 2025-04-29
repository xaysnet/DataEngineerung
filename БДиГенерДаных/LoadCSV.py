import mysql.connector
import pandas as pd

db = mysql.connector.connect(
    host="localhost",
    user="root",  # 
    password="root",  
    database="mydatabase1" 
)
cursor = db.cursor()
# Загрузка данных из CSV в DataFrame
users_df = pd.read_csv('C://1/users.csv')
topics_df = pd.read_csv('C://1/topics.csv')
messages_df = pd.read_csv('C://1/messages.csv')
log_user_df = pd.read_csv('C://1/log_user.csv')
log_topic_df = pd.read_csv('C://1/log_topic.csv')


for index, row in users_df.iterrows():
    cursor.execute("INSERT INTO User (Name, Password) VALUES (%s, %s)", (row['Name'], row['Password']))
for index, row in topics_df.iterrows():
    cursor.execute("INSERT INTO Topic (idUser, Name, Description) VALUES (%s, %s, %s)", (row['idUser'], row['Name'], row['Description']))
for index, row in messages_df.iterrows():
    cursor.execute("INSERT INTO Messages (idUser, idTopic, Name, GuestBoolean) VALUES (%s, %s, %s, %s)", (row['idUser'], row['idTopic'], row['Name'], row['GuestBoolean']))
for index, row in log_user_df.iterrows():
    cursor.execute("INSERT INTO LogUser (idTopic, idUser) VALUES (%s, %s)", (row['idTopic'], row['idUser']))
for index, row in log_topic_df.iterrows():
    cursor.execute("INSERT INTO LogTopic (idTopic, idUser) VALUES (%s, %s)", (row['idTopic'], row['idUser']))
db.commit()
cursor.close()
db.close()