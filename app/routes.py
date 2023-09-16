import imghdr
import os
from app import app, db
from functools import wraps
from flask import (
    redirect, 
    render_template, 
    url_for, 
    flash, 
    session,
    request,
    redirect,
    url_for,
    abort,
    send_from_directory
)
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Alumno, Participante
from app.forms import (
    LoginForm,
    RegisterForm, 
    RegisterFormOnline, 
    UploadForm, 
    RegisterParticipanteForm,
)
from werkzeug.utils import secure_filename
from PIL import Image, ImageOps
from sqlalchemy import func

def validate_image(stream):
    header = stream.read(512)
    stream.seek(0) 
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

DIOCESIS = {'xalapa': 'Xalapa',
            'cordoba': 'Córdoba',
            'coatza': 'Coatzacoalcos',
            'papantla': 'Papantla',
            'orizaba': 'Orizaba',
            'sanandres': 'San Andrés',
            'tuxpan': 'Tuxpan',
            'veracruz': 'Veracruz'}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Inicio')

@app.route('/entrar', methods=['GET', 'POST'])
def entrar():
    if current_user.is_authenticated:
        return redirect(url_for('perfil'))

    form = LoginForm()
    if form.validate_on_submit():
        alumnos = Alumno.query.filter(
            func.lower(
                Alumno.apellido_p
            ) == func.lower(str(form.apellido_p.data).strip()),
            func.lower(
                Alumno.apellido_m
            ) == func.lower(str(form.apellido_m.data).strip())
        ).all()   
        if len(alumnos) == 0:
            flash('No hay ningún alumno con esos apellidos')
            return redirect(url_for('entrar'))
        else:
            for alumno in alumnos:
                if (
                    str(alumno.dia_nac) == str(form.dia_nac.data) and
                    str(alumno.mes_nac) == str(form.mes_nac.data) and
                    str(alumno.año_nac) == str(form.año_nac.data)
                ):  
                    login_user(alumno, remember=True)
                    session['account_type'] = 'Alumno'
                    return redirect(url_for('perfil'))

            flash('Fecha de nacimiento incorrecta')
            return redirect(url_for('entrar'))
    
    return render_template('entrar.html', title='Entrar al Curso', form=form)


@app.route('/online', methods=['GET', 'POST'])
def online():
    """ if current_user.is_authenticated:
        return redirect(url_for('perfil'))

    form = RegisterFormOnline()

    if form.validate_on_submit():

        alumno = Alumno(
            nombres = form.nombres.data.strip(),
            apellido_p = form.apellido_p.data.strip(),
            apellido_m = form.apellido_m.data.strip(),
            dia_nac = form.dia_nac.data,
            mes_nac = form.mes_nac.data,
            año_nac = form.año_nac.data,
            decanato = form.decanato.data.strip(),
            parroquia = form.parroquia.data.strip(),
            telefono = form.telefono.data,
            correo = form.correo.data.strip(),
            grado = form.grado.data,
            servicio = form.servicio.data,
            modalidad = 0
        )

        db.session.add(alumno)
        db.session.commit()

        login_user(alumno, remember=True)
        session['account_type'] = 'Alumno'
        flash('¡Felicidades! Te has inscrito en el Curso Permanente de la \
               Escuela Diocesana de Catequesis')
        return redirect(url_for('perfil'))  """
    return render_template(
        'terminado.html',
        title='Registro al Curso Permanente'
    )


@app.route('/presencial', methods=['GET', 'POST'])
def presencial():
    """if current_user.is_authenticated:
        return redirect(url_for('perfil'))

    form = RegisterForm()

    if form.validate_on_submit():

        alumno = Alumno(
            nombres = form.nombres.data.strip(),
            apellido_p = form.apellido_p.data.strip(),
            apellido_m = form.apellido_m.data.strip(),
            dia_nac = form.dia_nac.data,
            mes_nac = form.mes_nac.data,
            año_nac = form.año_nac.data,
            decanato = form.decanato.data.strip(),
            parroquia = form.parroquia.data.strip(),
            telefono = form.telefono.data,
            correo = form.correo.data.strip(),
            grado = form.grado.data,
            servicio = form.servicio.data,
            modalidad = 1
        )

        db.session.add(alumno)
        db.session.commit()

        login_user(alumno, remember=True)
        session['account_type'] = 'Alumno'
        flash('¡Felicidades! Te has inscrito en el Curso Permanente de la \
               Escuela Diocesana de Catequesis')
        return redirect(url_for('perfil'))  """
    
    return render_template(
        'terminado.html',
        title='Registro al Curso Permanente'
    )

@app.route('/perfil')
@login_required
def perfil():
    return render_template(
        'perfil.html',
        title='Perfil del Alumno',
        basename=os.path.basename
    )

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/subir-foto', methods=['GET', 'POST'])
@login_required
def subir_foto():
    form = UploadForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            uploaded_file = form.file.data
            filename = secure_filename(uploaded_file.filename)
            if filename != '':
                file_ext = os.path.splitext(filename)[1]
                file_ext = str.lower(file_ext)
                if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                        file_ext != validate_image(uploaded_file.stream):
                    abort(400)

                saved_filename = os.path.join(
                        app.config['UPLOAD_PATH_FOTOS'], 
                        current_user.get_id() + file_ext
                    )
                
                pic = Image.open(uploaded_file)
                pic = ImageOps.exif_transpose(pic)
                pic.thumbnail((1200,1200))

                pic.save(saved_filename)
                
                current_user.foto = saved_filename
                db.session.commit()
            
            flash('La foto se ha subido exitosamente')
            return redirect(url_for('perfil'))
    return render_template('subir.html', title='Subir Foto', form=form)

@app.route('/fotos/<filename>')
@login_required
def fotos(filename):
    return send_from_directory(app.config['UPLOAD_PATH_FOTOS'], filename)


@app.route('/subir-boleta', methods=['GET', 'POST'])
@login_required
def subir_boleta():
    form = UploadForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            uploaded_file = form.file.data
            filename = secure_filename(uploaded_file.filename)
            if filename != '':
                file_ext = os.path.splitext(filename)[1]
                file_ext = str.lower(file_ext)
                if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                        file_ext != validate_image(uploaded_file.stream):
                    abort(400)

                saved_filename = os.path.join(
                        app.config['UPLOAD_PATH_BOLETAS'], 
                        current_user.get_id() + file_ext
                    )

                pic = Image.open(uploaded_file)
                pic = ImageOps.exif_transpose(pic)
                pic.thumbnail((1200,1200))

                pic.save(saved_filename)
                
                current_user.boleta_carta = saved_filename
                db.session.commit()

            flash('La boleta se ha subido exitosamente')
            return redirect(url_for('perfil'))
    return render_template('subir.html', title='Subir Foto', form=form)

@app.route('/boletas/<filename>')
@login_required
def boletas(filename):
    return send_from_directory(app.config['UPLOAD_PATH_BOLETAS'], filename)

@app.route('/admin')
@login_required
def admin():
    if current_user.id == 1:
        alumnos = Alumno.query
        return render_template(
            'admin.html',
            alumnos=alumnos,
            basename=os.path.basename,
        )
        
    return render_template('index.html', title='Inicio')

@app.route('/fotos_admin/<filename>')
@login_required
def fotos_admin(filename):
    return send_from_directory(app.config['UPLOAD_PATH_FOTOS'], filename)

@app.route('/boletas_admin/<filename>')
@login_required
def boletas_admin(filename):
    return send_from_directory(app.config['UPLOAD_PATH_BOLETAS'], filename)

@app.route('/provincial', methods=['GET', 'POST'])
def provincial():
    form = RegisterParticipanteForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            participante = Participante(
                nombres=form.nombres.data.strip(),
                apellido_p=form.apellido_p.data.strip(),
                apellido_m=form.apellido_m.data.strip(),
                sexo=form.sexo.data,
                telefono=form.telefono.data,
                servicio=form.servicio.data,
                coordinador=form.coordinador.data,
                diocesis=form.diocesis.data,
                correo=form.correo.data
            )

            db.session.add(participante)
            db.session.commit()

            return render_template('registrado.html', participante=participante)

    diocesis = request.args.get('diocesis')

    if diocesis in DIOCESIS:
        registrados = Participante.query.filter_by(
            diocesis=DIOCESIS[diocesis]
            ).count()
        
        if diocesis == 'veracruz' and registrados < 25:
            form.diocesis.label = "Diócesis: Veracruz"
            form.diocesis.data = "Veracruz"

            return render_template(
                'provincial.html', 
                diocesis="Veracruz", 
                registrados=registrados,
                form=form
            )
        elif registrados < 15:
            form.diocesis.label = "Diócesis: " + DIOCESIS[diocesis]
            form.diocesis.data = DIOCESIS[diocesis]

            return render_template(
                'provincial.html', 
                diocesis=DIOCESIS[diocesis], 
                registrados=registrados,
                form=form
            )
        
        return render_template('sincupo.html')
    
    return render_template('provincial.html')



