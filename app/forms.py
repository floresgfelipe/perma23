from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import (
    StringField, 
    SubmitField, 
    SelectField,
    HiddenField,
)
from wtforms.validators import (
    DataRequired,
    InputRequired,
    Length,
    EqualTo,
    Regexp,
)

class LoginForm(FlaskForm):
    apellido_p = StringField(
        'Apellido Paterno', 
        validators=[DataRequired(message='Este campo es obligatorio')],
        render_kw={'class':'input is-large'}
    )

    apellido_m = StringField(
        'Apellido Materno', 
        validators=[DataRequired(message='Este campo es obligatorio')],
        render_kw={'class':'input is-large'}
    )

    dia_nac = SelectField(
        'Día', 
        validators=[
            DataRequired(message='Este campo es obligatorio'),
        ],
        choices=['', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', 
            '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', 
            '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        render_kw={'autocomplete':'off', 'class':'select'}
    )

    mes_nac = SelectField(
        'Mes',
        validators=[
            DataRequired(message='Este campo es obligatorio'),
        ],
        choices=['', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
            'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 
            'Diciembre'],
        render_kw={'autocomplete':'off', 'class':'select'}
    )

    año_nac = SelectField(
        'Año',
        validators=[
            DataRequired(message='Este campo es obligatorio'),
        ],
        choices=['', '1920','1921','1922','1923','1924','1925','1926','1927',
            '1928','1929','1930','1931','1932','1933','1934','1935','1936',
            '1937','1938','1939','1940','1941','1942','1943','1944','1945',
            '1946','1947','1948','1949','1950','1951','1952','1953','1954',
            '1955','1956','1957','1958','1959','1960','1961','1962','1963',
            '1964','1965','1966','1967','1968','1969','1970','1971','1972',
            '1973','1974','1975','1976','1977','1978','1979','1980','1981',
            '1982','1983','1984','1985','1986','1987','1988','1989','1990',
            '1991','1992','1993','1994','1995','1996','1997','1998','1999',
            '2000','2001','2002','2003','2004','2005','2006','2007','2008',
            '2009','2010','2011','2012','2013','2014','2015'],
        render_kw={'autocomplete':'off', 'class':'select'}
    )

    submit = SubmitField(
        'Entrar', 
        render_kw={'class':'button is-link is-large mt-4 is-size-1-touch'}
        )
    

class RegisterForm(FlaskForm):
    nombres = StringField('Nombre(s)', validators=[
        DataRequired(message='Este campo es obligatorio'), 
        Length(min=1, max=50, 
            message='El largo del nombre debe ser entre 1 y 50 caracteres')
        ],
        render_kw={'class':'input is-large'}
    )

    apellido_p = StringField('Apellido Paterno', validators=[
        DataRequired(message='Este campo es obligatorio'), 
        Length(min=1, max=50,
             message='El largo del apellido debe ser entre 1 y 50 caracteres')
        ],
        render_kw={'class':'input is-large'}
    )

    apellido_m = StringField('Apellido Materno', validators=[
        DataRequired(message='Este campo es obligatorio'), 
        Length(min=1, max=50,
             message='El largo del apellido debe ser entre 1 y 50 caracteres')
        ],
        render_kw={'class':'input is-large'}
    )

    dia_nac = SelectField(
        'Día', 
        validators=[
            DataRequired(message='Este campo es obligatorio'),
        ],
        choices=['', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', 
            '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', 
            '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        render_kw={'autocomplete':'off', 'class':'select'}
    )

    mes_nac = SelectField(
        'Mes',
        validators=[
            DataRequired(message='Este campo es obligatorio'),
        ],
        choices=['', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
            'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 
            'Diciembre'],
        render_kw={'autocomplete':'off', 'class':'select'}
    )

    año_nac = SelectField(
        'Año',
        validators=[
            DataRequired(message='Este campo es obligatorio'),
        ],
        choices=['', '1920','1921','1922','1923','1924','1925','1926','1927',
            '1928','1929','1930','1931','1932','1933','1934','1935','1936',
            '1937','1938','1939','1940','1941','1942','1943','1944','1945',
            '1946','1947','1948','1949','1950','1951','1952','1953','1954',
            '1955','1956','1957','1958','1959','1960','1961','1962','1963',
            '1964','1965','1966','1967','1968','1969','1970','1971','1972',
            '1973','1974','1975','1976','1977','1978','1979','1980','1981',
            '1982','1983','1984','1985','1986','1987','1988','1989','1990',
            '1991','1992','1993','1994','1995','1996','1997','1998','1999',
            '2000','2001','2002','2003','2004','2005','2006','2007','2008',
            '2009','2010','2011','2012','2013','2014','2015'],
        render_kw={'autocomplete':'off', 'class':'select'}
    )

    decanato = SelectField(
        'Decanato',
        validators=[DataRequired(message='Este campo es obligatorio')],
        choices=[
            '',
            'Nuestra Señora de la Asunción',
            'Cristo Rey',
            'San Felipe de Jesús',
            'Santa Ana',
            'San José',
            'Soledad',
            'Nuestra Señora del Rosario',
            'Guadalupe',
            'Inmaculada'
        ], 
        render_kw={'autocomplete':'off', 'class':'select'}
    )

    parroquia = SelectField(
        'Parroquia', 
        validators=[DataRequired(message='Este campo es obligatorio')], 
        choices=[
            
        ],
        render_kw={'autocomplete':'off', 'class':'select'},
        validate_choice=False
    )

    grado = SelectField(
        'Grado al que se inscribe', 
        validators=[DataRequired(message='Este campo es obligatorio')], 
        choices=[
            ('', ''),
            (1, 'Primer Grado'), 
            (4, 'Curso Especializado')
        ],
        render_kw={'autocomplete':'off', 'class':'select'}
    )

    servicio = SelectField(
        '¿Se encuentra actualmente prestando servicio como catequista?', 
        validators=[DataRequired(message='Este campo es obligatorio')], 
        choices=['', 'Si', 'No'],
        render_kw={'autocomplete':'off','class':'select'}
    )

    telefono = StringField('Celular Personal', validators=[
        DataRequired(message='Este campo es obligatorio'),
        EqualTo('confirma_telefono', 
                message='Los dos números de celular deben ser iguales'),
        Regexp('^\d{10}$', message='El número debe tener 10 dígitos sin espacios ni guiones')
        ],
        render_kw={'class':'input is-large'}
    )

    confirma_telefono = StringField('Confirma Número Celular', validators=[
        DataRequired(message='Este campo es obligatorio'),   
        ],
        render_kw={'class':'input is-large'}
    )

    correo = StringField('Correo Electrónico', 
        render_kw={'class':'input is-large'}
    )
 
    submit = SubmitField(
        'Enviar', 
        render_kw={'class':'button is-link is-large is-size-2-touch'}
    )

class RegisterFormOnline(FlaskForm):
    nombres = StringField('Nombre(s)', validators=[
        DataRequired(message='Este campo es obligatorio'), 
        Length(min=1, max=50, 
            message='El largo del nombre debe ser entre 1 y 50 caracteres')
        ],
        render_kw={'class':'input is-large'}
    )

    apellido_p = StringField('Apellido Paterno', validators=[
        DataRequired(message='Este campo es obligatorio'), 
        Length(min=1, max=50,
             message='El largo del apellido debe ser entre 1 y 50 caracteres')
        ],
        render_kw={'class':'input is-large'}
    )

    apellido_m = StringField('Apellido Materno', validators=[
        DataRequired(message='Este campo es obligatorio'), 
        Length(min=1, max=50,
             message='El largo del apellido debe ser entre 1 y 50 caracteres')
        ],
        render_kw={'class':'input is-large'}
    )

    dia_nac = SelectField(
        'Día', 
        validators=[
            DataRequired(message='Este campo es obligatorio'),
        ],
        choices=['', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', 
            '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', 
            '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        render_kw={'autocomplete':'off', 'class':'select'}
    )

    mes_nac = SelectField(
        'Mes',
        validators=[
            DataRequired(message='Este campo es obligatorio'),
        ],
        choices=['', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
            'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 
            'Diciembre'],
        render_kw={'autocomplete':'off', 'class':'select'}
    )

    año_nac = SelectField(
        'Año',
        validators=[
            DataRequired(message='Este campo es obligatorio'),
        ],
        choices=['', '1920','1921','1922','1923','1924','1925','1926','1927',
            '1928','1929','1930','1931','1932','1933','1934','1935','1936',
            '1937','1938','1939','1940','1941','1942','1943','1944','1945',
            '1946','1947','1948','1949','1950','1951','1952','1953','1954',
            '1955','1956','1957','1958','1959','1960','1961','1962','1963',
            '1964','1965','1966','1967','1968','1969','1970','1971','1972',
            '1973','1974','1975','1976','1977','1978','1979','1980','1981',
            '1982','1983','1984','1985','1986','1987','1988','1989','1990',
            '1991','1992','1993','1994','1995','1996','1997','1998','1999',
            '2000','2001','2002','2003','2004','2005','2006','2007','2008',
            '2009','2010','2011','2012','2013','2014','2015'],
        render_kw={'autocomplete':'off', 'class':'select'}
    )

    decanato = SelectField(
        'Decanato',
        validators=[DataRequired(message='Este campo es obligatorio')],
        choices=[
            '',
            'Nuestra Señora de la Asunción',
            'Cristo Rey',
            'San Felipe de Jesús',
            'Santa Ana',
            'San José',
            'Soledad',
            'Nuestra Señora del Rosario',
            'Guadalupe',
            'Inmaculada'
        ], 
        render_kw={'autocomplete':'off', 'class':'select'}
    )

    parroquia = SelectField(
        'Parroquia', 
        validators=[DataRequired(message='Este campo es obligatorio')], 
        choices=[
            
        ],
        render_kw={'autocomplete':'off', 'class':'select'},
        validate_choice=False
    )

    grado = SelectField(
        'Grado al que se inscribe', 
        validators=[DataRequired(message='Este campo es obligatorio')], 
        choices=[
            ('', ''),
            (1, 'Primer Grado'), 
            #(2, 'Segundo Grado'), 
            (3, 'Tercer Grado'),
            (4, 'Curso Especializado')
        ],
        render_kw={'autocomplete':'off', 'class':'select'}
    )

    servicio = SelectField(
        '¿Se encuentra actualmente prestando servicio como catequista?', 
        validators=[DataRequired(message='Este campo es obligatorio')], 
        choices=['', 'Si', 'No'],
        render_kw={'autocomplete':'off','class':'select'}
    )

    telefono = StringField('Celular Personal', validators=[
        DataRequired(message='Este campo es obligatorio'),
        EqualTo('confirma_telefono', 
                message='Los dos números de celular deben ser iguales'),
        Regexp('^\d{10}$', message='El número debe tener 10 dígitos sin espacios ni guiones')
        ],
        render_kw={'class':'input is-large'}
    )

    confirma_telefono = StringField('Confirma Número Celular', validators=[
        DataRequired(message='Este campo es obligatorio'),
        ],
        render_kw={'class':'input is-large'}
    )

    correo = StringField('Correo Electrónico', 
        render_kw={'class':'input is-large'}
    )
 
    submit = SubmitField(
        'Enviar', 
        render_kw={'class':'button is-link is-large is-size-2-touch'}
    )


class UploadForm(FlaskForm):
    file = FileField('File', validators=[
            FileRequired(message='Selecciona un archivo'),
            FileAllowed(upload_set=['jpg','png','gif','jpeg'], 
                message='Selecciona una imagen, por favor. Extensiones permitidas: png, jpg, jpeg, gif.'),
        ],
        render_kw={'class':'file-input is-large', 'accept':'.png,.jpg,.jpeg,.gif'}
    )
    submit = SubmitField('Subir Foto', render_kw={'class':'button is-link is-large is-size-2-touch'})


class RegisterParticipanteForm(FlaskForm):
    diocesis = HiddenField( 
        validators=[InputRequired()]
    )

    nombres = StringField('Nombre(s)', validators=[
        InputRequired(message='Este campo es obligatorio'), 
        Length(min=1, max=50, 
            message='El largo del nombre debe ser entre 1 y 50 caracteres')
        ],
        render_kw={}
    )

    apellido_p = StringField('Apellido Paterno', validators=[
        InputRequired(message='Este campo es obligatorio'), 
        Length(min=1, max=50,
             message='El largo del apellido debe ser entre 1 y 50 caracteres')
        ],
        render_kw={}
    )

    apellido_m = StringField('Apellido Materno', validators=[
        InputRequired(message='Este campo es obligatorio'), 
        Length(min=1, max=50,
             message='El largo del apellido debe ser entre 1 y 50 caracteres')
        ],
        render_kw={}
    )

    sexo = SelectField('Sexo', choices=['', 'Hombre', 'Mujer'],
        validators=[InputRequired(message='Este campo es obligatorio')],
        default=''
    )

    telefono = StringField('Número de celular', validators=[
        InputRequired(message='Este campo es obligatorio'),
        EqualTo('confirma_telefono', 
                message='Los dos números de celular deben ser iguales'),
        Regexp('^\d{10}$', message='El número debe tener 10 dígitos sin espacios ni guiones')
        ],
        render_kw={}
    )

    confirma_telefono = StringField('Confirma el número de celular', validators=[
        InputRequired(message='Este campo es obligatorio'),
        ],
        render_kw={}
    )

    correo = StringField('Correo Electrónico')

    servicio = SelectField('Apostolado', choices=[
        '', 
        'Presbítero', 
        'Diácono',
        'Religiosa',
        'Laico'
        ],
        validators=[InputRequired(message='Este campo es obligatorio')],
        default=''
    )

    coordinador = SelectField(
        '¿Eres coordinador de equipo diocesano?', 
        choices=['', 'Si', 'No'],
        validators=[InputRequired(message='Este campo es obligatorio')],
        default=''
    )

    submit = SubmitField(
        'Enviar', 
        render_kw={}
    )
