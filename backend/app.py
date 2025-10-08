from flask import Flask
from routes.alunos_routes import alunos_bp
from routes.empresas_routes import empresas_bp
from routes.escolas_routes import escolas_bp

app = Flask(__name__)

# Registro dos Blueprints de rotas
app.register_blueprint(alunos_bp, url_prefix="/alunos")
app.register_blueprint(empresas_bp, url_prefix="/empresas")
app.register_blueprint(escolas_bp, url_prefix="/escolas")

@app.route("/")
def home():
    return {
        "API": "Neo Conexão",
        "status": "online",
        "rotas": ["/alunos/", "/empresas/", "/escolas/"]
    }

if __name__ == "__main__":
    app.run(debug=True)