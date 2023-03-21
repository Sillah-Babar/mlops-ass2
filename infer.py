from flask import Flask, render_template, request
import numpy
import pickle
from sklearn import preprocessing, svm

app = Flask(__name__) #creating the Flask class object   
 
def getResults(num):
    # save the model to disk
    num1=int(num)
    arr=numpy.array(num,dtype=float)
 
    num2=arr.reshape(1,-1)
    print(num2)

    filename = 'C:\\Users\\sillah\\_model_\\model\\finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    value= loaded_model.predict(num2)
    print(value)
    return str(value[0][0])

@app.route('/', methods =["GET", "POST"])
def home():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       years = request.form.get("years")
       predictedSal=getResults(years)
       return "Your predicted Salary is "+predictedSal 
    return render_template("home.html")
  
if __name__ =='__main__':  
    app.run(debug = True)  
    
# # start flask
# app = Flask(__name__)

# # render default webpage
# @app.route('/')
# def home():
#     if request.method == 'POST':
#         if request.form.get('action1') == 'VALUE1':
#             print("yeah")
#     elif request.method == 'GET':
#         return render_template('home.html', form=form)
    
#     return render_template('home.html')

# # when the post method detect, then redirect to success function
# @app.route('/', methods=['POST', 'GET'])
# def get_data():
#     if request.method == 'POST':
#         user = request.form['search']
#         return redirect(url_for('success', name=user))

# # get the data for the requested query
# @app.route('/success/<name>')
# def success(name):
#     return "<xmp>" + str(requestResults(name)) + " </xmp> "
