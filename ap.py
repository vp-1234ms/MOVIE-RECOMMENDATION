from flask import Flask,request,render_template,redirect
import pandas as pd
import re
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def start():
     data=pd.read_csv('Data.csv')
     l=data['genre'].to_list()
     h=[]
     for i in l:
          h.append(i.split(','))
     v=[]
     for i in h:
          for j in i:
               v.append(j)
     s=set(v)
     Genre=list(s)
     G=[]
     for i in Genre:
          G.append(i.strip())
     s=set(G)
     Genre=list(s)
     Genre.sort()

     l=data['year'].to_list()
     h=[]
     for i in l:
          try:
               h.append(re.findall(r'\d+',i)[0])
          except Exception as e:
               pass
     s=set(h)
     Year=list(s)
     G=[]
     for i in Year:
          G.append(i.strip())
     Year=G
     Year.sort(reverse=True)

     l=data['certificate'].to_list()
     s=set(l)
     Certificate=list(s)
     G=[]
     for i in Certificate:
          G.append(i.strip())
     Certificate=G

     return render_template("index.html",genre=Genre,x=len(Genre),year=Year,y=len(Year),certification=Certificate,z=len(Certificate))

@app.route("/home",methods=["GET","POST"])
def home():
     if request.method=='POST':
          movie_genre=request.form.getlist('mycheckbox1')
          movie_year=request.form.getlist('mycheckbox2')
          movie_certification=request.form.getlist('mycheckbox3')
          print(movie_genre)
          print(movie_year)
          print(movie_certification)
          data=pd.read_csv('Data.csv')
          data[data['genre'].str.contains('|'.join(Genre))]
          data=data[data['year'].str.contains('|'.join(Year))]
          data=data[data['certificate'].str.contains('|'.join(Certificate))]
          data=data['title'].to_list()
          return("Done")
     return('not done')
if __name__=="__main__":
    app.run(host="0.0.0.0")
