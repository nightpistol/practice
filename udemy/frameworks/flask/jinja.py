from flask import Flask,render_template,request

'''
creating an instance of Flask class which will be our wsgi application
'''

#wsgi application
app = Flask(__name__)

@app.route("/")
def welcome():
  return "<html> <h1> welcome to flask homepage</h1></html>"

@app.route("/index")
def index():
  return render_template('index.html')

@app.route("/submit",methods=['GET','POST'])
def submit():
  if request.method=='POST':
    name = request.form['name']
    return f"hello {name}"
  return render_template('form.html')

@app.route('/success/<int:score>')
def success(score):
  res =""
  if score>=50 :
    res="passed"
  else:
    res="failed"
  return render_template('results.html',results=res)    

if __name__ == "__main__":
  app.run(debug=True)