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







# from flask import Flask, render_template, request
# from flask_wtf.csrf import CSRFProtect
# import forms  
# from forms import MyData

# csrf = CSRFProtect()
# app = Flask(__name__)
# app.config['SECRET_KEY'] = "en un lugar de la mancha"
# csrf.init_app(app)

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
# @app.route('/cajasDinamicas', methods=['GET', 'POST'])
# @csrf.exempt # Excluye la protección CSRF para las solicitudes GET
# def cajasDinamicas():
#     if request.method == 'GET':
#         formulario = MyData()
#         return render_template('cajas-dinamicas.html', form=formulario)
#     else:
#         formulario = MyData(request.form)
#         return render_template('cajas-dinamicas.html', form=formulario)
     
# @app.route('/cajasDinamicas2', methods=['POST'])
# @csrf.exempt # Excluye la protección CSRF para las solicitudes GET
# def cajasDinamicas2():
#     formulario = MyData(request.form)
#     valores = [int(number) for number in formulario.numeros.data]
    
#     repetidos = []

#     for valor in set(valores):
#         repeticiones = len([num for num in valores if num == valor])
#         if repeticiones > 1:
#             repetidos.append((valor, repeticiones))

#     return render_template('cajas-dinamicas2.html', valores=valores, minNum=min(valores), maxNum=max(valores), promedio=sum(valores) / len(valores), repetidos=repetidos)


# if __name__ == '__main__':
#     app.run(debug=True)

#-----------------------------------------------------------------------------------------------------------------
#------------------------------------------------Resistencias------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

from flask import Flask, render_template, request
import math
import forms
from forms import ResistenciaForm
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()
app = Flask(__name__)
app.config['SECRET_KEY'] = "en un lugar de la mancha"
csrf.init_app(app)

def calcular_resistencia(banda1, banda2, banda3, tolerancia):
    

    valores = {
        "negro": 0,
        "marron": 1,
        "rojo": 2,
        "naranja": 3,
        "amarillo": 4,
        "verde": 5,
        "azul": 6,
        "violeta": 7,
        "gris": 8,
        "blanco": 9
    }
    english_names = {
        "negro": "black",
        "marron": "brown",
        "rojo": "red",
        "naranja": "orange",
        "amarillo": "yellow",
        "verde": "green",
        "azul": "blue",
        "violeta": "violet",
        "gris": "gray",
        "blanco": "white",
        "oro": "gold",
        "plata": "silver"
    }
    banda1_en = english_names[banda1]
    banda2_en = english_names[banda2]
    banda3_en = english_names[banda3]
    tolerancia_en = english_names[tolerancia]

    valor1 = valores[banda1]
    valor2 = valores[banda2]
    multiplicador = math.pow(10, valores[banda3])
    tolerancia_valor = 0.05 if tolerancia == "oro" else 0.1

    valor = (valor1 * 10 + valor2) * multiplicador
    valor_minimo = valor * (1 - tolerancia_valor)
    valor_maximo = valor * (1 + tolerancia_valor)

    return {
        "colorBanda1": banda1_en,
        "colorBanda2": banda2_en,
        "colorBanda3": banda3_en,
        "colorTolerancia": tolerancia_en,
        "banda1": banda1,
        "banda2": banda2,
        "banda3": banda3,
        "tolerancia": tolerancia,
        "valor": valor,
        "valor_minimo": valor_minimo,
        "valor_maximo": valor_maximo
    }


@app.route('/', methods=['GET'])
def index():
    form = ResistenciaForm()

    with open("valores_guardados.txt", "r") as f:
        valores_guardados = [line.strip().split(",") for line in f]

    resultados_guardados = []
    for valores in valores_guardados:
        if len(valores) == 4:
            resultado_guardado = calcular_resistencia(*valores)
            resultados_guardados.append(resultado_guardado)

    return render_template('resistencias.html', form=form, resultados_guardados=resultados_guardados)


@app.route('/', methods=['POST'])
def calcular():
    form = ResistenciaForm()
    banda1 = request.form['banda1']
    banda2 = request.form['banda2']
    banda3 = request.form['banda3']
    tolerancia = request.form['tolerancia']

    resultado = calcular_resistencia(banda1, banda2, banda3, tolerancia)

    valores_guardados = []
    with open("valores_guardados.txt", "r") as f:
        for line in f:
            valores = line.strip().split(",")
            if len(valores) == 4:
                resultado_guardado = calcular_resistencia(*valores)
                valores_guardados.append(resultado_guardado)

    valores_guardados.append(resultado)

    with open("valores_guardados.txt", "a") as f:
        f.write(",".join([banda1, banda2, banda3, tolerancia]) + "\n")

    return render_template('resistencias.html', resultado=resultado, form=form, valores_guardados=valores_guardados)

if __name__ == '__main__':
    app.run(debug=True)
