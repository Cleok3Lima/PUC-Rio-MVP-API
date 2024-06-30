from flask import Flask, jsonify, request, redirect
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS, cross_origin
from flask_openapi3 import Tag
from pydantic import ValidationError
from model.base import db
from model.usuario import Usuario
from model.tarefa import Tarefa
from schemas.usuario import UsuarioSchema
from schemas.tarefa import TarefaSchema
from datetime import datetime
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Deve ser substituida por uma chave SUPER secreta e segura ;)

db.init_app(app)
jwt = JWTManager(app)

# Configurar CORS globalmente para permitir o cabeçalho Authorization
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True, allow_headers=["Content-Type", "Authorization"], methods=["GET", "POST", "DELETE", "OPTIONS"])

# Documentação da API
SWAGGER_URL = '/api/docs'  # URL para acessar a interface do Swagger (sem o '/' final)
API_URL = '/static/swagger.json'  # API url

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Os arquivos estáticos da interface do usuário do Swagger serão mapeados para '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Gestão de Tempo API"
    }
)

app.register_blueprint(swaggerui_blueprint)

@app.route('/')
def index():
    return redirect('/api/docs')

@app.route('/register', methods=['POST'])
@cross_origin(origins="*", headers=["Content-Type", "Authorization"], methods=["POST"])
def register():
    try:
        data = request.get_json()
        print("Data received:", data)  # Log dos dados recebidos
        if not data or not 'username' in data or not 'password' in data:
            return jsonify({"message": "Username and password are required"}), 400

        try:
            user_data = UsuarioSchema(**data)
            new_user = Usuario(username=user_data.username)
            new_user.set_password(user_data.password)  # Ajuste para definir a senha corretamente
            db.session.add(new_user)
            db.session.commit()
            return jsonify(message="User created"), 201
        except ValidationError as ve:
            print("ValidationError:", ve.errors())  # Log dos erros de validação
            return jsonify(message=str(ve)), 400

    except Exception as e:
        print("Error:", str(e))  # Log the error
        return jsonify(message=str(e)), 500

@app.route('/login', methods=['POST'])
@cross_origin(origins="*", headers=["Content-Type", "Authorization"], methods=["POST"])
def login():
    try:
        data = request.get_json()
        print("Data received:", data)  # Log dos dados recebidos
        user = Usuario.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token)
        else:
            return jsonify(message="Invalid credentials"), 401
    except Exception as e:
        print("Error:", str(e))  # Log the error
        return jsonify(message=str(e)), 500

@app.route('/tarefas', methods=['GET', 'POST'])
@jwt_required()
@cross_origin(origins="*", headers=["Content-Type", "Authorization"], methods=["GET", "POST"])
def manage_tarefas():
    try:
        user_id = get_jwt_identity()
        if request.method == 'POST':
            data = request.get_json()
            print("Data received:", data)  # Log dos dados recebidos
            tarefa_schema = TarefaSchema(**data)
            tarefa_data = tarefa_schema.model_dump()
            if tarefa_data['due_date']:
                tarefa_data['due_date'] = datetime.strptime(tarefa_data['due_date'], '%d/%m/%Y')
            new_tarefa = Tarefa(user_id=user_id, **tarefa_data)
            db.session.add(new_tarefa)
            db.session.commit()
            return jsonify(message="Tarefa created"), 201
        elif request.method == 'GET':
            tarefas = Tarefa.query.filter_by(user_id=user_id).all()
            tarefas_schema = [TarefaSchema.model_validate(tarefa) for tarefa in tarefas]
            return jsonify([tarefa.model_dump() for tarefa in tarefas_schema])
    except Exception as e:
        print("Error:", str(e))  # Log the error
        return jsonify(message=str(e)), 500

@app.route('/tarefas/<int:tarefa_id>', methods=['DELETE'])
@jwt_required()
@cross_origin(origins="*", headers=["Content-Type", "Authorization"], methods=["DELETE"])
def delete_tarefa(tarefa_id):
    try:
        user_id = get_jwt_identity()
        tarefa = Tarefa.query.filter_by(id=tarefa_id, user_id=user_id).first()
        if not tarefa:
            return jsonify(message="Tarefa not found"), 404
        db.session.delete(tarefa)
        db.session.commit()
        return jsonify(message="Tarefa deleted"), 200
    except Exception as e:
        print("Error:", str(e))  # Log the error
        return jsonify(message=str(e)), 500

@app.route('/tarefas/<int:tarefa_id>/complete', methods=["POST"])
@jwt_required()
@cross_origin(origins="*", headers=["Content-Type", "Authorization"], methods=["POST"])
def complete_tarefa(tarefa_id):
    try:
        user_id = get_jwt_identity()
        tarefa = Tarefa.query.filter_by(id=tarefa_id, user_id=user_id).first()
        if not tarefa:
            return jsonify(message="Tarefa not found"), 404
        tarefa.completed = True
        db.session.commit()
        return jsonify(message="Tarefa completed"), 200
    except Exception as e:
        print("Error:", str(e))  # Log the error
        return jsonify(message=str(e)), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria todas as tabelas no banco de dados
    app.run(debug=True, port=8000)  # Rodar na porta 8000
