from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/data',methods=['POST','GET'])
def data():
    if request.method=="POST":
        data=request.form.get('editor1')
        return render_template('data.html',data=data)
    return ""


app.run(debug=True)