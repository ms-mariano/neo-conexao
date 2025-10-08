from flask import Flask
from controllers.alunos_controller import alunos_bp
from controllers.empresas_controller import empresas_bp
from controllers.escolas_controller import escolas_bp

app = Flask(__name__)

# Registro dos controladores
app.register_blueprint(alunos_bp, url_prefix="/alunos")
app.register_blueprint(empresas_bp, url_prefix="/empresas")
app.register_blueprint(escolas_bp, url_prefix="/escolas")

@app.route("/")
def home():
    return {
        "API": "Neo Conexão",
        "status": "online",
        "rotas_disponiveis": ["/alunos/", "/empresas/", "/escolas/"]
    }

if __name__ == "__main__":
    app.run(debug=True)