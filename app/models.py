from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login
from flask import session

APROBADO = 'ACREDITADO'
REPROBADO = 'NO ACREDITADO'

class Alumno(UserMixin, db.Model):
    __tablename__ = 'alumno'

    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(50), nullable=False)
    apellido_p = db.Column(db.String(50), nullable=False)
    apellido_m = db.Column(db.String(50), nullable=False)
    dia_nac = db.Column(db.Integer,nullable=False)
    mes_nac = db.Column(db.String(20), nullable=False)
    año_nac = db.Column(db.Integer, nullable=False)
    decanato = db.Column(db.String(50), nullable=False)
    parroquia = db.Column(db.String(80), nullable=False)
    telefono = db.Column(db.String(10), nullable=False)    
    correo = db.Column(db.String(50), nullable=False)
    foto = db.Column(db.String(200), nullable=False, default='none')
    grado = db.Column(db.Integer, nullable=False)
    modalidad = db.Column(db.Integer, nullable=False)
    boleta_carta = db.Column(db.String(200), nullable=False, default='none')
    servicio = db.Column(db.String(2), nullable=False)
    
    def get_modalidad(self):
        if self.modalidad == 0:
            return "En línea"
        else:
            return "Presencial"
        
    def __repr__(self) -> str:
        return f'<Alumno {self.id} {self.nombres} \
            {self.apellido_p} {self.apellido_m}>'
    
    def get_grado(self):
        if self.grado == 1:
            return 'Primero'
        elif self.grado == 2:
            return 'Segundo'
        elif self.grado == 3:
            return 'Tercero'
        else:
            return 'Curso Especializado'
        
class Participante(db.Model):
    __tablename__ = "participante"

    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(50), nullable=False)
    apellido_p = db.Column(db.String(50), nullable=False)
    apellido_m = db.Column(db.String(50), nullable=False)
    sexo = db.Column(db.String(20), nullable= False)
    telefono = db.Column(db.String(10), nullable=False)
    servicio = db.Column(db.String(20), nullable= False)
    coordinador = db.Column(db.String(2), nullable=False)
    


@login.user_loader
def load_user(id):
    return Alumno.query.get(int(id))






