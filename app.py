from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/sobre")
def sobre():
    return render_template('sobre.html') 

@app.route("/blog")
def blog():
    return "Blog - Em construção"

@app.route("/chat")
def chat():
    return "Chat - Em construção"

@app.route("/perfil")
def perfil():
    return "Perfil - Em construção"

if __name__ == "__main__":
    app.run(debug=True)