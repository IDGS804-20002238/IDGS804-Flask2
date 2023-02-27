# from flask import Flask, render_template, request,make_response,flash
# from forms import WordForm, TranslateForm
# from forms import LoginForm
# import forms 
# from flask_wtf.csrf import CSRFProtect

# app = Flask(__name__)
# app.config['SECRET_KEY']="esta es una clave encriptada"
# csrf=CSRFProtect()
# csrf.init_app(app)
#-----------------------------------------------------------------------------------------------------------------
#----------------------------------------------LOGIN--------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
# @app.route("/cookie", methods = ['GET', 'POST'])
# def cookie():
    
#     reg_user = forms.LoginForm(request.form)
#     response = make_response(render_template('cookie.html', form = reg_user,))

#     if request.method == 'POST' and reg_user.validate():
#         user = reg_user.username.data
#         password = reg_user.password.data
#         datos = user + '@' + password
#         success_message = 'Bienvenido {}'.format(user)
#         response.set_cookie('datos_usuario', datos)
#         flash(success_message)
#     return response
#-----------------------------------------------------------------------------------------------------------------
#--------------------------------------------DICCIONARIO DATOS----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     word_form = WordForm()
#     translate_form = TranslateForm()

#     if word_form.validate_on_submit():
#         with open('words.txt', 'a') as f:
#             f.write(f'{word_form.spanish_word.data.lower()}={word_form.english_word.data.lower()}\n')
#         return render_template('traductor.html', word_form=word_form, translate_form=translate_form, message='Guardado con éxito')

#     if translate_form.validate_on_submit():
#         language = translate_form.language.data
#         with open('words.txt') as f:
#             words = dict(line.strip().lower().split('=') for line in f)
#             try:
#                 if language == 'english':
#                     translation = words[translate_form.word.data.lower()]
#                 else:
#                     translation = [key for key, value in words.items() if value == translate_form.word.data.lower()][0]
#                 message = f'Traducción: {translation}'
#             except (KeyError, IndexError):
#                 message = 'No se encuentra la traducción'
#         return render_template('traductor.html', word_form=word_form, translate_form=translate_form, message=message)

#     return render_template('traductor.html', word_form=word_form, translate_form=translate_form)





#-----------------------------------------------------------------------------------------------------------------
#--------------------------------------------ALUMNOS--------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------




# from flask import Flask, render_template
# from flask import request 
# import forms 
# from flask_wtf.csrf import CSRFProtect
# from collections import Counter


# app = Flask(__name__)
# app.config['SECRET_KEY']="esta es una clave encriptada"
# csrf=CSRFProtect()
# csrf.init_app(app)

# @app.route("/formprueba")
# def formprueba():

#     return render_template("formprueba.html")


# @app.route("/Alumnos", methods=['GET','POST'])
# def Alumnos():
#     reg_alum=forms.UserForm(request.form)
#     datos=list()
#     if request.method == 'POST':
#         datos.append(reg_alum.matricula.data)
#         datos.append(reg_alum.nombre.data)
#         print(reg_alum.matricula.data)
#         print(reg_alum.nombre.data)

#     return render_template("Alumnos.html",form=reg_alum, datos=datos)







from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
import forms  
from forms import MyData

csrf = CSRFProtect()
app = Flask(__name__)
app.config['SECRET_KEY'] = "en un lugar de la mancha"
csrf.init_app(app)

#-----------------------------------------------------------------------------------------------------------------
#--------------------------------------------ALUMNOS--------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

# @app.route("/formprueba")
# def formprueba():
    
#     return render_template("formprueba.html")

# @app.route("/Alumnos", methods=['GET','POST'])
# def Alumnos():
#     reg_alum=forms.UserForm(request.form)
#     datos = list()
#     if request.method=='POST':
#         datos.append(reg_alum.matricula.data)
#         datos.append(reg_alum.nombre.data)
#         print(reg_alum.matricula.data)
#         print(reg_alum.nombre.data)

#     return render_template('Alumnos.html', form=reg_alum,datos=datos)

#-----------------------------------------------------------------------------------------------------------------
#--------------------------------------------CAJAS DINAMICAS------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
@app.route('/cajasDinamicas', methods=['GET', 'POST'])
@csrf.exempt # Excluye la protección CSRF para las solicitudes GET
def cajasDinamicas():
    if request.method == 'GET':
        formulario = MyData()
        return render_template('cajas-dinamicas.html', form=formulario)
    else:
        formulario = MyData(request.form)
        return render_template('cajas-dinamicas.html', form=formulario)
     
@app.route('/cajasDinamicas2', methods=['POST'])
@csrf.exempt # Excluye la protección CSRF para las solicitudes GET
def cajasDinamicas2():
    formulario = MyData(request.form)
    valores = [int(number) for number in formulario.numeros.data]
    
    repetidos = []

    for valor in set(valores):
        repeticiones = len([num for num in valores if num == valor])
        if repeticiones > 1:
            repetidos.append((valor, repeticiones))

    return render_template('cajas-dinamicas2.html', valores=valores, minNum=min(valores), maxNum=max(valores), promedio=sum(valores) / len(valores), repetidos=repetidos)


if __name__ == '__main__':
    app.run(debug=True)