from .base import db

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    due_date = db.Column(db.DateTime, nullable=True)
    completed = db.Column(db.Boolean, default=False)
    usuario = db.relationship('Usuario', backref=db.backref('tarefas', lazy=True))

    def __repr__(self):
            return f'<Tarefa {self.title}>'