from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True
form = ''' <!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
          <form method="post">
        <label>
            <h3>Rotate by:</h3>
            <input type = "text" value = "0" name="rot"/><br>
        </label>
        <textarea name = "msg" rows = "4" cols = "50">{0}</textarea><br>
        <input type = "submit" value = "Encrypt">
    </form>
    </body>
</html>'''
@app.route("/", methods = ['post'])
def encrypt():
    rotation = int(request.form["rot"])
    message = request.form["msg"]
    cypher = rotate_string(message, rotation)
    return form.format(cypher)

@app.route("/")
def index():
    return form.format("")

app.run()