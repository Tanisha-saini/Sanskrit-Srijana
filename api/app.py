from flask import Flask,render_template,request
from deep_translator import GoogleTranslator
import json 
 
# WSGI Application
# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name
app = Flask(__name__,template_folder='template',static_folder='static')
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate')
def translate():
    return render_template('translate.html')

@app.route('/alphabets')
def alphabets():
    return render_template('alphabets.html')

@app.route('/translate/<inputText>', methods=['GET'])
def translatetext(inputText="hello"):
    res= GoogleTranslator(source='auto', target='sa').translate(inputText)
    print(res)
    data = json.loads('{}') 
    data['translatedData']=res
    print(data)
    return data

@app.route('/translatetoen/<inputText>', methods=['GET'])
def translatetexttoen(inputText="hello"):
    res= GoogleTranslator(source='auto', target='en').translate(inputText)
    print(res)
    data = json.loads('{}') 
    data['translatedData']=res
    print(data)
    return data

if __name__=='__main__':
    app.run(debug = True)