from flask import Flask,render_template,request
import pyodbc
import pandas as pd
import re
import json

connected=pyodbc.connect("DSN=Hive_Connection",autocommit=True,ansi=True)

app = Flask(__name__)

@app.route("/")
@app.route("/executeQuery",methods=["GET","POST"])
def index():
   flash_messages=[]
   if(request.method=="POST"):
      entered_query=(str)(request.form.get("query"))
      lowercase_query=entered_query.lower()
      lowercase_query.replace("\r\n","")
      if(lowercase_query.find(";")==-1 and lowercase_query.find('\;')==-1):
         flash_messages.append("query should contain semi colon")
         return render_template("index.html",flash_messages=json.dumps(flash_messages),query=lowercase_query)
      queries=lowercase_query.split(";")
      results_table=[]
      for query in queries:
         query=query.replace("\r\n","")
         query=query.strip(' ')
         if query!="":
            # 2 Types of Queries
            # 1- Using Select
            # 2- Not using select like update,alter,delete,insert,create etc
            choose_option=re.search("^select",query)
            # It is a query that belongs to 2nd type
            if choose_option==None:
               try:
                  cursor_object=connected.cursor()
                  cursor_object.execute(query)
                  success_msg="Query Exceuted Successfully"
                  flash_messages.append(query+"\n"+success_msg)
               except Exception as e:
                  error_msg=str(e)
                  flash_messages.append(query+"\n"+error_msg)
         
            # It is a query that belongs to 1st type
            else:
               try:
                  results_df=pd.read_sql(query,connected)
                  results_table.append(results_df.to_html())
               except Exception as e:
                  error_msg=str(e)
                  flash_messages.append(query+"\n"+error_msg)
      return render_template("index.html",queries=queries,flash_messages=json.dumps(flash_messages),tables=results_table)
   return render_template("index.html",query="",flash_messages=json.dumps(flash_messages))
  
@app.route("/clear",methods=["GET","POST"])
def clearQuery():
   if (request.method=="POST"):
      return render_template("index.html",query="")

if __name__ == '__main__':
   app.run()