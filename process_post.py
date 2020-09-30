#!C:\Users\sketd\anaconda3\python.exe
import model
import cgi
import cgitb #useful to debug 
import os
import datetime
print("Content-Type: text/html\n")    # HTML is following
cgitb.enable() #in case of error, error detail displayed

#CGI and FieldStorage
#Form data from FieldStorage

form = cgi.FieldStorage()
BASE_URL = os.environ.get("BASE_URL", "http://localhost/twitter_project/")
name = form.getvalue('name')
text = form.getvalue('text')
image = form['tweet-image']

if image.filename :
  filename = os.path.basename(image.filename)
  filename = filename.replace(" ", "_")
  open("user_images/" + filename, "wb").write(image.file.read())
  imagepath = BASE_URL + "user_images/" + filename
else:
  imagepath = None

response = model.insert_tweet(None, name, text, imagepath, str(datetime.datetime.now()))

if response == "success":
  print('<script>window.location.replace("http://localhost/twitter_project/index.py");</script>')
else:
  print('data not inserted')
