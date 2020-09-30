#%/usr/bin/python
import connection as con


def insert_tweet(parent_tweet_id, name,text,image_path, create_at):
  conn = con.mysql_connect()
  cursor = conn.cursor()

  if(parent_tweet_id is None and image_path is None):
    mySql_insert_query = """INSERT INTO tweet (name,text, create_at) VALUES ( '""" + \
        name+"""', '"""+text+"""', '"""+create_at+"""')"""

  elif(image_path is None):
    mySql_insert_query = """INSERT INTO tweet (parent_tweet_id, name,text, create_at) VALUES ( '"""+parent_tweet_id+"""', '""" +name+"""', '"""+text+"""', '"""+create_at+"""')"""

  elif(parent_tweet_id is None):
    mySql_insert_query = """INSERT INTO tweet (name,text, image_path, create_at) VALUES ( '""" + \
        name+"""', '"""+text+"""', '"""+image_path+"""', '"""+create_at+"""')"""

  else:
    mySql_insert_query = """INSERT INTO tweet (parent_tweet_id, name,text, image_path, create_at) VALUES ( '""" + \
        parent_tweet_id+"""','"""+name+"""', '"""+text + \
        """', '"""+image_path+"""','"""+create_at+"""')"""
  
  try:
    cursor.execute(mySql_insert_query)
    conn.commit()
    return "success"
  except: 
    conn.rollback()
    return "failed"

# insert_tweet(None,"Moto","I am moto", None,"2020-09-14")
# insert_tweet(None,"Tomo","I am Tomo", "ok","2020-09-14")
# insert_tweet("1","Moto","I am moto", None,"2020-09-14")
# insert_tweet("1","Moto","I am moto", "ko","2020-09-14")

# No parent Id
# No image
# No parent id and image
# Insert into parent_tweet_id, name, text, image_path, create_at


def get_tweet():
  # fetchall tweet from database
  conn = con.mysql_connect()
  cursor = conn.cursor()

  fetch_tweet = """
  SELECT * FROM tweet;
  """
  cursor.execute(fetch_tweet)
  result = cursor.fetchall()
  return result
  # print(result)
# get_tweet()


def get_reply_count(parent_tweet_id):
  #counting replies for every tweets
  conn = con.mysql_connect()
  cursor = conn.cursor()

  reply_count = """
  SELECT COUNT(*) FROM tweet
  WHERE parent_tweet_id = '"""+str(parent_tweet_id)+"""'
  """
  
  cursor.execute(reply_count)
  result = cursor.fetchall()
  cursor.close()
  return result
  # print(result)

# get_reply_count(56)




