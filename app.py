from flask import Flask , render_template , request
from google import genai

from dotenv import load_dotenv
import os

# Load variables from .env into os.environ
load_dotenv()

# Access variables using standard os module methods
gemini_api_key = os.getenv('gemini_api_key')
client = genai.Client(api_key=gemini_api_key)

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    if request.method =='GET':
        return render_template('index.html')

    elif request.method=='POST':

        v1=request.form['name']
        v2=int(request.form['age'])
        v3=request.form['des']
        v4=int(request.form['budget'])
        v5 = int(request.form['days'])
        v6 = int(request.form['num_of_people'])
        v7 = request.form['hotel']
        v8 = request.form['transport']
        v9 = request.form['food']
        v10 = request.form['climate']

        response = client.models.generate_content(
            model="gemini-3.5-flash", contents=f"my name is {v1} and i am {v2} year old. We are planning to"
                                               f""
                                               f" visit {v3} in {v4} budget. we are total {v6} people and "
                                               f"we are planning to stay {v5}days. we are planning to visit"
                                               f" our destination by {v8} and we want {v7} type of hotels."
                                               f" so suggest me to visit at which location in {v10} weather"
                                               f" and also suggest {v9} type of food . suggest some good "
                                               f"places to visit according to the weather and time we must "
                                               f"has to visit maximum place. give the output in pure html "
                                               f"u/format and dont add any additional information on the page"
        )
        return render_template('result.html',result=response.text)

app.run(debug=True)
