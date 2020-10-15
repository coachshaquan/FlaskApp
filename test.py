from flask import Flask, render_template, send_from_directory, request
import requests
import json

app = Flask(__name__)

   
@app.route('/', methods=["GET","POST"])
def makeAvatar():
    if request.method =="POST":
        print(request.form.get("username"))
        gender ="male"
        name =request.form.get("username")
        filename ="https://avatars.dicebear.com/api/" + \
             gender +"/"+ name + ".svg"
        url = "https://randomuser.me/api"
        req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'});
        req = req.json()
        data = req["results"][0]
    elif request.method =="GET":
        data = None;
        filename = None;
    #print(response["results"])
  
    return render_template("index.html",
                           data = data,
                           filename=filename)
app.run(host='0.0.0.0', port=8080, debug=True)
