#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 21:55:26 2021

@author: danzig
"""

# In[0]:

#################################################
## 0. IMPORTAMOS LAS LIBRERÍAS
#################################################    
import os    
import psycopg2
#import pandas as pd
from datetime import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
#from itertools import repeat
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pickle
from dash.exceptions import PreventUpdate

## importar desde datos_muni
from datos_muni import proyecto, lista_encuestadores, lista_supervisores

# In[1]:

#################################################
## 1. CREACION DE LISTAS A UTILIZAR
#################################################   

# Repetir strings
#def rep(s,n):
#    return (', '.join(list(repeat(s,n))))

# Día de hoy
now = datetime.now()
hoy = now.strftime('%Y-%m-%d')

#proyecto = 'Ampliación y mejoramiento del Mercado de Abastos del Distrito de San Juan Bautista,\
#            Departamento de Loreto, Provincia de Maynas, Distrito de San Juan Bautista'


# Listas y tablas
with open('./pickles/columnas.pkl', 'rb') as i:
    columnas = pickle.load(i)


with open('./pickles/val_num.pkl', 'rb') as j:
    val_num = pickle.load(j)



# Listas para guardar datos
#lista_datos_gen = []
#lista_datos_carne = []
#lista_datos_pescados = []
#lista_datos_aves = []
#lista_datos_embutidos = []
#lista_datos_verduras = []
#lista_datos_frutas = []
#lista_datos_abarrotes = []
#lista_datos_comidas = []
#lista_datos_otros = []
#lista_total = []



#LIstas de respuestas
# Activar
listax = [{'label':'Activado', 'value':'si'},
          {'label':'Desactivado', 'value':'no'}]


# SI/NO
lista1 = [{'label':'Si', 'value':'si'},
          {'label':'No', 'value':'no'}]


# Género
lista3 = [
    {'label':'Varón', 'value':'varón'},
    {'label':'Mujer', 'value':'mujer'}
    ]


# Destino de Productos
lista4 = [
    {'label':'Sólo para consumo en el hogar', 'value':'hogar'},
    {'label':'Sólo para el negocio', 'value':'negocio'},
    {'label':'Ambos, hogar y negocio', 'value':'hogar y negocio'}
    ]
# Importante, añadir una pregunta de porcentaje de compra para el negocio, si es ambos


# Horario de compra

lista5 = [
    {'label':'Antes de las 06 am', 'value':'Antes de las 06 am'},
    {'label':'Entre las 06 y 10 am', 'value':'Entre las 06 y 10 am'},
    {'label':'Entre las 10 am y 01 pm', 'value':'Entre las 10 am y 01 pm'},
    {'label':'Entre la 01 y 03 pm', 'value':'Entre la 01 y 03 pm'},
    {'label':'Entre las 03 y 06 pm', 'value':'Entre las 03 y 06 pm'},
    {'label':'Después de las 06 pm', 'value':'Después de las 06 pm'}
    ]



# Transporte

lista6 = [
    {'label':'A pie', 'value':'a pie'},
    {'label':'Moto particular', 'value':'moto particular'},
    {'label':'Moto taxi (Motocar)', 'value':'mototaxi'},
    {'label':'Bus o auto colectivo', 'value':'colectivo'},
    {'label':'Taxi', 'value':'taxi'},
    {'label':'Auto particular', 'value':'auto particular'},
    {'label':'Otro medio', 'value':'otro'}
    ]


# Número de veces que acude al mercado

lista7 = [
    {'label':'A diario', 'value':'A diario'}, #'30'
    {'label':'Tres días a la semana', 'value':'Tres días a la semana'}, #'12'
    {'label':'Dos días a la semana', 'value':'Dos días a la semana'}, #'8'
    {'label':'Un día a la semana', 'value':'Un día a la semana'}, #'4'
    {'label':'Un día cada 2 semanas', 'value':'Un día cada 2 semanas'}, #'2'
    {'label':'Un día al mes', 'value':'Un día al mes'}, #'1'
    {'label':'Seleccione frecuencia de compra ...', 'value':'0'}
    ]


# Modificar el formato de encuesta

# Unidades de Medida

lista_leche = [
    {'label':'Litros (Lt)', 'value':'l'},
    {'label':'Unidad (Und)', 'value':'und'},
    {'label':'Seleccione unidad de medida ...', 'value':'0'}
    ]

lista8 = [
    {'label':'Kilogramos (Kg)', 'value':'kg'},
    {'label':'Seleccione unidad de medida ...', 'value':'0'}
    ]

lista9 = [
    {'label':'Litros (Lt)', 'value':'l'},
    {'label':'Seleccione unidad de medida ...', 'value':'0'}
    ]

lista10 = [
    {'label':'Unidad (Und)', 'value':'und'},
    {'label':'Seleccione unidad de medida ...', 'value':'0'}
    ]

lista11 = [
    {'label':'Kilogramos (Kg)', 'value':'kg'},
    {'label':'Unidad (Und)', 'value':'und'},
    {'label':'Seleccione unidad de medida ...', 'value':'0'}
    ]

lista12 = [
    {'label':'Kilogramos (Kg)', 'value':'kg'},
    {'label':'Litros (Lt)', 'value':'l'},
    {'label':'Seleccione unidad de medida ...', 'value':'0'}
    ]

lista13 = [
    {'label':'Kilogramos (Kg)', 'value':'kg'},
    {'label':'Unidad', 'value':'und'},
    {'label':'Docena', 'value':'doc'},
    {'label':'Jaba/Atado', 'value':'jab'},
    {'label':'Seleccione unidad de medida ...', 'value':'0'}
    ]

lista14 = [
    {'label':'Kilogramos (Kg)', 'value':'kg'},
    {'label':'Unidad', 'value':'und'},
    {'label':'Docena', 'value':'doc'},
    {'label':'Jaba/Atado', 'value':'jab'},
    {'label':'Caja/Cajón', 'value':'caj'},
    {'label':'Seleccione unidad de medida ...', 'value':'0'}
    ]

# Lugar de compra
lista15 = [
    {'label':'Mercado San Pedro', 'value':'minorista1'},
    {'label':'Mercado Casccaparo', 'value':'minorista2'},
    {'label':'Mercado Rosaspata', 'value':'minorista3'},
    {'label':'Mercado San Blas', 'value':'minorista4'},
    {'label':'Mercado Tica Tica', 'value':'minorista5'},
    {'label':'Mercado Virgen Natividad', 'value':'minorista6'},
    {'label':'Mercado El Pueblo', 'value':'minorista7'},
    {'label':'Mercado Ccolloryti', 'value':'minorista8'},	
    {'label':'Mercado mayorista', 'value':'mayorista'},
    {'label':'Feria', 'value':'feria'},
    {'label':'Distribuidora', 'value':'distribuidora'},
    {'label':'Otros', 'value':'otros'},
    {'label':'Seleccione lugar de abastecimiento...', 'value':'0'}
    ]
# Importante, añadir las nuevas alternativas en el lugar de compra

# Satisfaccion
#lista16 = [
#    {'label':'Nada importante', 'value':1},
#    {'label':'Poco importante', 'value':2},
#    {'label':'Indiferente', 'value':3},
#    {'label':'Importante', 'value':4},
#    {'label':'Muy importante', 'value':5}
#    ]

# Satisfaccion
#lista17 = [
#    {'label':'Muy insatisfecho', 'value':1},
#    {'label':'Insatisfecho', 'value':2},
#    {'label':'Indiferente', 'value':3},
#    {'label':'Satisfecho', 'value':4},
#    {'label':'Muy satisfecho', 'value':5}
#    ]

# Encuestadores

#lista_encuestadores =  [
#    {'label':'Encuestador 1', 'value':'DNI00001'},
#    {'label':'Encuestador 2', 'value':'DNI00002'},
#    {'label':'Encuestador 3', 'value':'DNI00003'},
#    {'label':'Encuestador 4', 'value':'DNI00004'},
#    {'label':'Encuestador 5', 'value':'DNI00005'}
#    ]


#lista_supervisores =  [
#    {'label':'Supervisor 1', 'value':'DNI00011'},
#    {'label':'Supervisor 2', 'value':'DNI00022'}
#    ]


# In[2]:

#################################################
## 2. CREACION DE FUNCIONES
#################################################   

# FUNCIONES PARA INSERCION DE DATOS
#######################################

# Aplanar listas
def flatten(xs):
    res = []
    def loop(ys):
        for i in ys:
            if isinstance(i, list):
                loop(i)
            else:
                res.append(i)
    loop(xs)
    return res


#db_user = os.environ.get('CLOUD_SQL_USERNAME')
#db_password = os.environ.get('CLOUD_SQL_PASSWORD')
#db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
#db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')
#host = '/cloudsql/{}'.format(db_connection_name)


# GRABAR REGISTRO
def grabar_reg(lista_total, cols, vals):
    #conexion = psycopg2.connect(host='localhost', database='encuesta', user='postgres', password='ingresar') #entrar
    
    conexion = psycopg2.connect(
    host='ec2-18-207-95-219.compute-1.amazonaws.com', 
    database='d9a3ij616gcmoa', 
    user='dyzhcvdvjugzsi', 
    password='3983489fc52c8cccf8219446d14be14ca806e5bb826cbcc4008bf740d19f098d')
    
    cursor1 = conexion.cursor()
    sql = 'INSERT INTO tabla_encuesta ('+ cols + ') VALUES (' + vals +')'
    cursor1.execute(sql, lista_total)
    conexion.commit()
    #print ('Registro guardado en la base de datos')
    conexion.close()



# FUNCIONES PARA PREGUNTAS EN DASH
#######################################

# Función para preguntas con respuesta INTEGER
def pregunta_integer_dbc(etiqueta,identificador,etiqueta_input):
    html_out = [
        dbc.Label(etiqueta, width=10),
        dbc.Col(
            dbc.Input(
                type='number',
                id=identificador,
                min=1,
                max=380,
                step=1,
                placeholder=etiqueta_input
                ),width=10
            )
        ]
    return(html_out)


def pregunta_integer_dbc2(etiqueta,identificador,etiqueta_input):
    html_out = [
        dbc.Label(etiqueta, width=10),
        dbc.Col(
            dbc.Input(
                type='number',
                id=identificador,
                min=0,
                max=100,
                step=10,
                value=0,
                placeholder=etiqueta_input
                ),width=10
            )
        ]
    return(html_out)




# Función para preguntas con respuesta Texto
def pregunta_text_dbc(etiqueta,identificador,etiqueta_input):
    html_out = [
        dbc.Label(etiqueta, width=10),
        dbc.Col(
            dbc.Input(
                type='text',
                id=identificador,
                placeholder=etiqueta_input
                ),width=10
            )
        ]
    return(html_out)



# Función para preguntas con respuesta listas (dropdown)
def pregunta_list_dbc(etiqueta,identificador,lista_opciones):  #lista de opciones es diccionario en principio
    html_out = [
        dbc.Label(etiqueta, width=10),
        dbc.Col(
            dbc.Select(
                id=identificador,
                options=lista_opciones
                ),width=10
            )
        ]
    #html.Br()
    return(html_out)



# Función para preguntas con respuesta de fechas
def pregunta_date(etiqueta,identificador):
    html_out = [
        dbc.Label(etiqueta, width=10),
        dbc.Col(
            dcc.DatePickerSingle(
                id=identificador,
                month_format='MMMM Y',
                placeholder='MMMM Y',
                date=hoy,
                style={'font-family':'sans-serif', 'fontSize':12}
                ),width=10
            ) 
        ]
    #html.Br()
    return(html_out)




# Función para preguntas con respuesta listas (dropdown)
def pregunta_rubro(etiqueta,id_check,lista_check,nombre_prod,
                   id_selec1,lista_selec1,
                   id_selec2,lista_selec2,
                   id_selec3,lista_selec3,
                   id_selec4):
    html_out = [
        dbc.Label(etiqueta, width=3),
        
        html.Br(),
        
        dbc.Row([
            dbc.Col([
                dbc.Select(
                id=id_check,
                options=lista_check,
                placeholder=nombre_prod,
                value='no',
                )],width=2),
            
            dbc.Col(
                dbc.Select(
                    id=id_selec1,
                    options=lista_selec1,
                    value='0',
                    ),width=2),
            dbc.Col(
                dbc.Select(
                    id=id_selec2,
                    options=lista_selec2,
                    value='0',
                    ),width=2),
            dbc.Col(
                dbc.Select(
                    id=id_selec3,
                    options=lista_selec3,
                    value='0',
                    ),width=2),
            dbc.Col(
                dbc.Input(
                type='number',
                id=id_selec4,
                min=0.0,
                max=1000.0,
                step=0.25,
                value=0.0,
                ),width=2)
            ])
        ]
    return(html_out)



# In[3]:

#################################################
## 3. APLICACION DASH
#################################################   

# APLICACION DASH
app = dash.Dash(external_stylesheets=[dbc.themes.SLATE], suppress_callback_exceptions=True)
server = app.server

# DATOS PREGUNTAS GENERALES
############################

# PREGUNTAS 1er bloque
######################
preg_a = dbc.FormGroup(
            pregunta_integer_dbc(
                etiqueta='A. N° de Encuesta: ',
                identificador='num_encuesta',
                etiqueta_input='Seleccione ...'),
            row=True
            )


preg_b = dbc.FormGroup(
            pregunta_list_dbc(
                etiqueta='B. Encuestador: ',
                identificador='encuestador',
                lista_opciones=lista_encuestadores),
            row=True
            )

preg_c = dbc.FormGroup(
            pregunta_list_dbc(
                etiqueta='C. Supervisor: ',
                identificador='supervisor',
                lista_opciones=lista_supervisores),
            row=True
            )

preg_d = dbc.FormGroup(
            pregunta_date(
                etiqueta='D. Fecha de encuesta: ',
                identificador='fecha'),
            row=True
            )

preg_e = dbc.FormGroup(
            pregunta_text_dbc(
                etiqueta='E. Sector: ',
                identificador='sector',
                etiqueta_input='Seleccione ...'),
            row=True
            )


preg_f = dbc.FormGroup(
            pregunta_text_dbc(
                etiqueta='F. Manzana: ',
                identificador='mz',
                etiqueta_input='Seleccione ...'),
            row=True
            )


preg_g = dbc.FormGroup(
            pregunta_text_dbc(
                etiqueta='G. Vivienda: ',
                identificador='viv',
                etiqueta_input='Seleccione ...'),
            row=True
            )




# PREGUNTAS 2do bloque
######################
preg_1 = dbc.FormGroup(
            pregunta_integer_dbc(
                etiqueta='1. N° de hogares en la vivienda: ',
                identificador='p1',
                etiqueta_input='Seleccione ...'),
            row=True
            )


preg_2 = dbc.FormGroup(
            pregunta_integer_dbc(
                etiqueta='2. N° de personas en el hogar: ',
                identificador='p2',
                etiqueta_input='Seleccione ...'),
            row=True
            )


preg_3 = dbc.FormGroup(
            pregunta_list_dbc(
                etiqueta='3. Decisor de compra: ',
                identificador='p3',
                lista_opciones=lista1),
            row=True
            )


preg_4_1 = dbc.FormGroup(
            pregunta_integer_dbc2(
                etiqueta='4.1. Lugar de compra - Mercado de Abastos (%): ',
                identificador='p4_1',
                etiqueta_input='Seleccione ...'),
            row=True
            )


preg_4_2 = dbc.FormGroup(
            pregunta_integer_dbc2(
                etiqueta='4.2. Lugar de compra - Bodegas/Tienda (%): ',
                identificador='p4_2',
                etiqueta_input='Seleccione ...'),
            row=True
            )


preg_4_3 = dbc.FormGroup(
            pregunta_integer_dbc2(
                etiqueta='4.3. Lugar de compra - Feria (%): ',
                identificador='p4_3',
                etiqueta_input='Seleccione ...'),
            row=True
            )

preg_5 = dbc.FormGroup(
            pregunta_integer_dbc(
                etiqueta='5. Edad del entrevistado: ',
                identificador='p5',
                etiqueta_input='Seleccione ...'),
            row=True
            )


preg_6 = dbc.FormGroup(
            pregunta_list_dbc(
                etiqueta='6. Género del entrevistado: ',
                identificador='p6',
                lista_opciones=lista3),
            row=True
            )


preg_7 = dbc.FormGroup(
            pregunta_list_dbc(
                etiqueta='7. Destino de los productos: ',
                identificador='p7',
                lista_opciones=lista4),
            row=True
            )


preg_7_1 = dbc.FormGroup(
            pregunta_integer_dbc2(
                etiqueta='7.1. Destino Producto: Hogar/Negocio (% hogar): ',
                identificador='p7_1',
                etiqueta_input='Seleccione ...'),
            row=True
            )


preg_8 = dbc.FormGroup(
            pregunta_list_dbc(
                etiqueta='8. Horario de compra: ',
                identificador='p8',
                lista_opciones=lista5),
            row=True
            )



preg_9 = dbc.FormGroup(
            pregunta_list_dbc(
                etiqueta='9. Medio de transporte: ',
                identificador='p9',
                lista_opciones=lista6),
            row=True
            )


preg_10 = dbc.FormGroup(
            pregunta_list_dbc(
                etiqueta='10. Frecuencia de compra (mensual): ',
                identificador='p10',
                lista_opciones=lista7),
            row=True
            )



# PREGUNTAS RUBRO: CARNE
########################


preg_11_1 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p101_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Carne de Res',
        
        id_selec1='p101_4',
        lista_selec1=lista15,
        
        id_selec2='p101_3',
        lista_selec2=lista7,
        
        id_selec3='p101_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p101_1'),
    row=False,
    id='p11_1'
    )

					

preg_11_2 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p102_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Carne de Cerdo',
        
        id_selec1='p102_4',
        lista_selec1=lista15,
        
        id_selec2='p102_3',
        lista_selec2=lista7,
        
        id_selec3='p102_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p102_1'),
    row=False,
    id='p11_2'
    )



preg_11_3 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p103_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Menudencia',
        
        id_selec1='p103_4',
        lista_selec1=lista15,
        
        id_selec2='p103_3',
        lista_selec2=lista7,
        
        id_selec3='p103_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p103_1'),
    row=False,
    id='p11_3'
    )



preg_11_4 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p104_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Otras carnes',
        
        id_selec1='p104_4',
        lista_selec1=lista15,
        
        id_selec2='p104_3',
        lista_selec2=lista7,
        
        id_selec3='p104_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p104_1'),
    row=False,
    id='p11_4'
    )



# PREGUNTAS RUBRO: PESCADOS
###########################


preg_12_1 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p201_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Pescados',
        
        id_selec1='p201_4',
        lista_selec1=lista15,
        
        id_selec2='p201_3',
        lista_selec2=lista7,
        
        id_selec3='p201_2',
        lista_selec3=lista11, #unidad de medida
        
        id_selec4='p201_1'),
    row=False,
    id='p12_1'
    )


preg_12_2 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p202_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Mariscos',
        
        id_selec1='p202_4',
        lista_selec1=lista15,
        
        id_selec2='p202_3',
        lista_selec2=lista7,
        
        id_selec3='p202_2',
        lista_selec3=lista11, #unidad de medida
        
        id_selec4='p202_1'),
    row=False,
    id='p12_2'
    )



# PREGUNTAS RUBRO: AVES
###########################


preg_13_1 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p301_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Pollo',
        
        id_selec1='p301_4',
        lista_selec1=lista15,
        
        id_selec2='p301_3',
        lista_selec2=lista7,
        
        id_selec3='p301_2',
        lista_selec3=lista11, #unidad de medida
        
        id_selec4='p301_1'),
    row=False,
    id='p13_1'
    )



preg_13_2 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p302_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Gallina',
        
        id_selec1='p302_4',
        lista_selec1=lista15,
        
        id_selec2='p302_3',
        lista_selec2=lista7,
        
        id_selec3='p302_2',
        lista_selec3=lista11, #unidad de medida
        
        id_selec4='p302_1'),
    row=False,
    id='p13_2'
    )



preg_13_3 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p303_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Pavo',
        
        id_selec1='p303_4',
        lista_selec1=lista15,
        
        id_selec2='p303_3',
        lista_selec2=lista7,
        
        id_selec3='p303_2',
        lista_selec3=lista11, #unidad de medida
        
        id_selec4='p303_1'),
    row=False,
    id='p13_3'
    )



preg_13_4 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p304_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Otras aves',
        
        id_selec1='p304_4',
        lista_selec1=lista15,
        
        id_selec2='p304_3',
        lista_selec2=lista7,
        
        id_selec3='p304_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p304_1'),
    row=False,
    id='p13_4'
    )



# PREGUNTAS RUBRO: EMBUTIDOS
###########################


preg_14_1 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p401_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Embutidos',
        
        id_selec1='p401_4',
        lista_selec1=lista15,
        
        id_selec2='p401_3',
        lista_selec2=lista7,
        
        id_selec3='p401_2',
        lista_selec3=lista11, #unidad de medida
        
        id_selec4='p401_1'),
    row=False,
    id='p14_1'
    )




# PREGUNTAS RUBRO: VERDURAS
###########################


preg_15_1 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p501_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Papa',
        
        id_selec1='p501_4',
        lista_selec1=lista15,
        
        id_selec2='p501_3',
        lista_selec2=lista7,
        
        id_selec3='p501_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p501_1'),
    row=False,
    id='p15_1'
    )



preg_15_2 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p502_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Camote',
        
        id_selec1='p502_4',
        lista_selec1=lista15,
        
        id_selec2='p502_3',
        lista_selec2=lista7,
        
        id_selec3='p502_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p502_1'),
    row=False,
    id='p15_2'
    )



preg_15_3 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p503_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Yuca',
        
        id_selec1='p503_4',
        lista_selec1=lista15,
        
        id_selec2='p503_3',
        lista_selec2=lista7,
        
        id_selec3='p503_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p503_1'),
    row=False,
    id='p15_3'
    )



preg_15_4 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p504_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Tomate',
        
        id_selec1='p504_4',
        lista_selec1=lista15,
        
        id_selec2='p504_3',
        lista_selec2=lista7,
        
        id_selec3='p504_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p504_1'),
    row=False,
    id='p15_4'
    )


preg_15_5 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p505_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Ajo entero',
        
        id_selec1='p505_4',
        lista_selec1=lista15,
        
        id_selec2='p505_3',
        lista_selec2=lista7,
        
        id_selec3='p505_2',
        lista_selec3=lista11, #unidad de medida
        
        id_selec4='p505_1'),
    row=False,
    id='p15_5'
    )


preg_15_6 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p506_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Zapallo',
        
        id_selec1='p506_4',
        lista_selec1=lista15,
        
        id_selec2='p506_3',
        lista_selec2=lista7,
        
        id_selec3='p506_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p506_1'),
    row=False,
    id='p15_6'
    )



preg_15_7 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p507_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Apio',
        
        id_selec1='p507_4',
        lista_selec1=lista15,
        
        id_selec2='p507_3',
        lista_selec2=lista7,
        
        id_selec3='p507_2',
        lista_selec3=lista11, #unidad de medida
        
        id_selec4='p507_1'),
    row=False,
    id='p15_7'
    )



preg_15_8 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p508_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Cebolla',
        
        id_selec1='p508_4',
        lista_selec1=lista15,
        
        id_selec2='p508_3',
        lista_selec2=lista7,
        
        id_selec3='p508_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p508_1'),
    row=False,
    id='p15_8'
    )



preg_15_9 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p509_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Zanahoria',
        
        id_selec1='p509_4',
        lista_selec1=lista15,
        
        id_selec2='p509_3',
        lista_selec2=lista7,
        
        id_selec3='p509_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p509_1'),
    row=False,
    id='p15_9'
    )


preg_15_10 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p510_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Lechuga',
        
        id_selec1='p510_4',
        lista_selec1=lista15,
        
        id_selec2='p510_3',
        lista_selec2=lista7,
        
        id_selec3='p510_2',
        lista_selec3=lista11, #unidad de medida
        
        id_selec4='p510_1'),
    row=False,
    id='p15_10'
    )


preg_15_11 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p511_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Limón',
        
        id_selec1='p511_4',
        lista_selec1=lista15,
        
        id_selec2='p511_3',
        lista_selec2=lista7,
        
        id_selec3='p511_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p511_1'),
    row=False,
    id='p15_11'
    )



preg_15_12 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p512_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Poro',
        
        id_selec1='p512_4',
        lista_selec1=lista15,
        
        id_selec2='p512_3',
        lista_selec2=lista7,
        
        id_selec3='p512_2',
        lista_selec3=lista11, #unidad de medida
        
        id_selec4='p512_1'),
    row=False,
    id='p15_12'
    )



preg_15_13 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p513_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Otras verduras',
        
        id_selec1='p513_4',
        lista_selec1=lista15,
        
        id_selec2='p513_3',
        lista_selec2=lista7,
        
        id_selec3='p513_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p513_1'),
    row=False,
    id='p15_13'
    )


# PREGUNTAS RUBRO: FRUTAS
###########################


preg_16_1 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p601_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Manzana',
        
        id_selec1='p601_4',
        lista_selec1=lista15,
        
        id_selec2='p601_3',
        lista_selec2=lista7,
        
        id_selec3='p601_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p601_1'),
    row=False,
    id='p16_1'
    )



preg_16_2 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p602_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Plátano',
        
        id_selec1='p602_4',
        lista_selec1=lista15,
        
        id_selec2='p602_3',
        lista_selec2=lista7,
        
        id_selec3='p602_2',
        lista_selec3=lista11, #unidad de medida
        
        id_selec4='p602_1'),
    row=False,
    id='p16_2'
    )



preg_16_3 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p603_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Papaya',
        
        id_selec1='p603_4',
        lista_selec1=lista15,
        
        id_selec2='p603_3',
        lista_selec2=lista7,
        
        id_selec3='p603_2',
        lista_selec3=lista11, #unidad de medida
        
        id_selec4='p603_1'),
    row=False,
    id='p16_3'
    )



preg_16_4 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p604_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Naranja',
        
        id_selec1='p604_4',
        lista_selec1=lista15,
        
        id_selec2='p604_3',
        lista_selec2=lista7,
        
        id_selec3='p604_2',
        lista_selec3=lista11, #unidad de medida
        
        id_selec4='p604_1'),
    row=False,
    id='p16_4'
    )


preg_16_5 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p605_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Piña',
        
        id_selec1='p605_4',
        lista_selec1=lista15,
        
        id_selec2='p605_3',
        lista_selec2=lista7,
        
        id_selec3='p605_2',
        lista_selec3=lista11, #unidad de medida
        
        id_selec4='p605_1'),
    row=False,
    id='p16_5'
    )


preg_16_6 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p606_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Maracuyá',
        
        id_selec1='p606_4',
        lista_selec1=lista15,
        
        id_selec2='p606_3',
        lista_selec2=lista7,
        
        id_selec3='p606_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p606_1'),
    row=False,
    id='p16_6'
    )



preg_16_7 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p607_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Mango',
        
        id_selec1='p607_4',
        lista_selec1=lista15,
        
        id_selec2='p607_3',
        lista_selec2=lista7,
        
        id_selec3='p607_2',
        lista_selec3=lista11, #unidad de medida
        
        id_selec4='p607_1'),
    row=False,
    id='p16_7'
    )



preg_16_8 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p608_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Mandarina',
        
        id_selec1='p608_4',
        lista_selec1=lista15,
        
        id_selec2='p608_3',
        lista_selec2=lista7,
        
        id_selec3='p608_2',
        lista_selec3=lista11, #unidad de medida
        
        id_selec4='p608_1'),
    row=False,
    id='p16_8'
    )



preg_16_9 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p609_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Otras frutas',
        
        id_selec1='p609_4',
        lista_selec1=lista15,
        
        id_selec2='p609_3',
        lista_selec2=lista7,
        
        id_selec3='p609_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p609_1'),
    row=False,
    id='p16_9'
    )




# PREGUNTAS RUBRO: ABARROTES
###########################


preg_17_1 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p701_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Arroz',
        
        id_selec1='p701_4',
        lista_selec1=lista15,
        
        id_selec2='p701_3',
        lista_selec2=lista7,
        
        id_selec3='p701_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p701_1'),
    row=False,
    id='p17_1'
    )



preg_17_2 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p702_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Azúcar',
        
        id_selec1='p702_4',
        lista_selec1=lista15,
        
        id_selec2='p702_3',
        lista_selec2=lista7,
        
        id_selec3='p702_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p702_1'),
    row=False,
    id='p17_2'
    )



preg_17_3 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p703_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Menestras',
        
        id_selec1='p703_4',
        lista_selec1=lista15,
        
        id_selec2='p703_3',
        lista_selec2=lista7,
        
        id_selec3='p703_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p703_1'),
    row=False,
    id='p17_3'
    )



preg_17_4 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p704_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Leche evaporada',
        
        id_selec1='p704_4',
        lista_selec1=lista15,
        
        id_selec2='p704_3',
        lista_selec2=lista7,
        
        id_selec3='p704_2',
        lista_selec3=lista_leche, #unidad de medida
        
        id_selec4='p704_1'),
    row=False,
    id='p17_4'
    )


preg_17_5 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p705_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Mantequilla',
        
        id_selec1='p705_4',
        lista_selec1=lista15,
        
        id_selec2='p705_3',
        lista_selec2=lista7,
        
        id_selec3='p705_2',
        lista_selec3=lista12, #unidad de medida
        
        id_selec4='p705_1'),
    row=False,
    id='p17_5'
    )


preg_17_6 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p706_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Sal',
        
        id_selec1='p706_4',
        lista_selec1=lista15,
        
        id_selec2='p706_3',
        lista_selec2=lista7,
        
        id_selec3='p706_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p706_1'),
    row=False,
    id='p17_6'
    )



preg_17_7 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p707_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Café',
        
        id_selec1='p707_4',
        lista_selec1=lista15,
        
        id_selec2='p707_3',
        lista_selec2=lista7,
        
        id_selec3='p707_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p707_1'),
    row=False,
    id='p17_7'
    )



preg_17_8 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p708_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Aceite',
        
        id_selec1='p708_4',
        lista_selec1=lista15,
        
        id_selec2='p708_3',
        lista_selec2=lista7,
        
        id_selec3='p708_2',
        lista_selec3=lista9, #unidad de medida
        
        id_selec4='p708_1'),
    row=False,
    id='p17_8'
    )



preg_17_9 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p709_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Harina de trigo / Harina de maiz',
        
        id_selec1='p709_4',
        lista_selec1=lista15,
        
        id_selec2='p709_3',
        lista_selec2=lista7,
        
        id_selec3='p709_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p709_1'),
    row=False,
    id='p17_9'
    )


preg_17_10 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p710_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Sillao',
        
        id_selec1='p710_4',
        lista_selec1=lista15,
        
        id_selec2='p710_3',
        lista_selec2=lista7,
        
        id_selec3='p710_2',
        lista_selec3=lista9, #unidad de medida
        
        id_selec4='p710_1'),
    row=False,
    id='p17_10'
    )


preg_17_11 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p711_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Maní',
        
        id_selec1='p711_4',
        lista_selec1=lista15,
        
        id_selec2='p711_3',
        lista_selec2=lista7,
        
        id_selec3='p711_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p711_1'),
    row=False,
    id='p17_11'
    )



preg_17_12 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p712_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Conservas de pescado',
        
        id_selec1='p712_4',
        lista_selec1=lista15,
        
        id_selec2='p712_3',
        lista_selec2=lista7,
        
        id_selec3='p712_2',
        lista_selec3=lista11, #unidad de medida
        
        id_selec4='p712_1'),
    row=False,
    id='p17_12'
    )



preg_17_13 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p713_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Fideos',
        
        id_selec1='p713_4',
        lista_selec1=lista15,
        
        id_selec2='p713_3',
        lista_selec2=lista7,
        
        id_selec3='p713_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p713_1'),
    row=False,
    id='p17_13'
    )


preg_17_14 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p714_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Huevos',
        
        id_selec1='p714_4',
        lista_selec1=lista15,
        
        id_selec2='p714_3',
        lista_selec2=lista7,
        
        id_selec3='p714_2',
        lista_selec3=lista11, #unidad de medida
        
        id_selec4='p714_1'),
    row=False,
    id='p17_14'
    )



preg_17_15 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p715_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Especerías',
        
        id_selec1='p715_4',
        lista_selec1=lista15,
        
        id_selec2='p715_3',
        lista_selec2=lista7,
        
        id_selec3='p715_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p715_1'),
    row=False,
    id='p17_15'
    )



preg_17_16 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p716_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Yogurt',
        
        id_selec1='p716_4',
        lista_selec1=lista15,
        
        id_selec2='p716_3',
        lista_selec2=lista7,
        
        id_selec3='p716_2',
        lista_selec3=lista9, #unidad de medida
        
        id_selec4='p716_1'),
    row=False,
    id='p17_16'
    )



preg_17_17 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p717_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Otros abarrotes',
        
        id_selec1='p717_4',
        lista_selec1=lista15,
        
        id_selec2='p717_3',
        lista_selec2=lista7,
        
        id_selec3='p717_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p717_1'),
    row=False,
    id='p17_17'
    )




# PREGUNTAS RUBRO: COMIDAS PREPARADAS
#####################################


preg_18_1 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p801_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Comida Preparada',
        
        id_selec1='p801_4',
        lista_selec1=lista15,
        
        id_selec2='p801_3',
        lista_selec2=lista7,
        
        id_selec3='p801_2',
        lista_selec3=lista10, #unidad de medida
        
        id_selec4='p801_1'),
    row=False,
    id='p18_1'
    )



preg_18_2 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p802_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Jugos y refrescos',
        
        id_selec1='p802_4',
        lista_selec1=lista15,
        
        id_selec2='p802_3',
        lista_selec2=lista7,
        
        id_selec3='p802_2',
        lista_selec3=lista9, #unidad de medida
        
        id_selec4='p802_1'),
    row=False,
    id='p18_2'
    )



preg_18_3 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p803_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Panes',
        
        id_selec1='p803_4',
        lista_selec1=lista15,
        
        id_selec2='p803_3',
        lista_selec2=lista7,
        
        id_selec3='p803_2',
        lista_selec3=lista11, #unidad de medida
        
        id_selec4='p803_1'),
    row=False,
    id='p18_3'
    )



preg_18_4 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p804_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Quesos',
        
        id_selec1='p804_4',
        lista_selec1=lista15,
        
        id_selec2='p804_3',
        lista_selec2=lista7,
        
        id_selec3='p804_2',
        lista_selec3=lista11, #unidad de medida
        
        id_selec4='p804_1'),
    row=False,
    id='p18_4'
    )


preg_18_5 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p805_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Otras comidas',
        
        id_selec1='p805_4',
        lista_selec1=lista15,
        
        id_selec2='p805_3',
        lista_selec2=lista7,
        
        id_selec3='p805_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p805_1'),
    row=False,
    id='p18_5'
    )




# PREGUNTAS RUBRO: OTROS RUBROS
#####################################


preg_19_1 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p901_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Ropa',
        
        id_selec1='p901_4',
        lista_selec1=lista15,
        
        id_selec2='p901_3',
        lista_selec2=lista7,
        
        id_selec3='p901_2',
        lista_selec3=lista10, #unidad de medida
        
        id_selec4='p901_1'),
    row=False,
    id='p19_1'
    )



preg_19_2 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p902_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Calzado',
        
        id_selec1='p902_4',
        lista_selec1=lista15,
        
        id_selec2='p902_3',
        lista_selec2=lista7,
        
        id_selec3='p902_2',
        lista_selec3=lista10, #unidad de medida
        
        id_selec4='p902_1'),
    row=False,
    id='p19_2'
    )



preg_19_3 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p903_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Mercería',
        
        id_selec1='p903_4',
        lista_selec1=lista15,
        
        id_selec2='p903_3',
        lista_selec2=lista7,
        
        id_selec3='p903_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p903_1'),
    row=False,
    id='p19_3'
    )



preg_19_4 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p904_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Medicina natural',
        
        id_selec1='p904_4',
        lista_selec1=lista15,
        
        id_selec2='p904_3',
        lista_selec2=lista7,
        
        id_selec3='p904_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p904_1'),
    row=False,
    id='p19_4'
    )



preg_19_5 = dbc.FormGroup(
    pregunta_rubro(
        id_check='p905_0',
        lista_check=listax,
        nombre_prod='Activar producto...',
        etiqueta='Otros rubros',
        
        id_selec1='p905_4',
        lista_selec1=lista15,
        
        id_selec2='p905_3',
        lista_selec2=lista7,
        
        id_selec3='p905_2',
        lista_selec3=lista8, #unidad de medida
        
        id_selec4='p905_1'),
    row=False,
    id='p19_5'
    )






# BOTONES
########################

boton_guardar_tab1 = dbc.Button('Guardar registro', id='guardar_tab1', n_clicks=0, color="success", className="mr-1", size="lg")
boton_corregir_tab1 = dbc.Button('Corregir registro', id='corregir_tab1', n_clicks=0, color="primary", className="mr-1", size="lg")


boton_guardar_tab2 = dbc.Button('Guardar registro', id='guardar_tab2', n_clicks=0, color="success", className="mr-1", size="lg")
boton_corregir_tab2 = dbc.Button('Corregir registro', id='corregir_tab2', n_clicks=0, color="primary", className="mr-1", size="lg")


boton_guardar_tab3 = dbc.Button('Guardar registro', id='guardar_tab3', n_clicks=0, color="success", className="mr-1", size="lg")
boton_corregir_tab3 = dbc.Button('Corregir registro', id='corregir_tab3', n_clicks=0, color="primary", className="mr-1", size="lg")


boton_guardar_tab4 = dbc.Button('Guardar registro', id='guardar_tab4', n_clicks=0, color="success", className="mr-1", size="lg")
boton_corregir_tab4 = dbc.Button('Corregir registro', id='corregir_tab4', n_clicks=0, color="primary", className="mr-1", size="lg")


boton_guardar_tab5 = dbc.Button('Guardar registro', id='guardar_tab5', n_clicks=0, color="success", className="mr-1", size="lg")
boton_corregir_tab5 = dbc.Button('Corregir registro', id='corregir_tab5', n_clicks=0, color="primary", className="mr-1", size="lg")


boton_guardar_tab6 = dbc.Button('Guardar registro', id='guardar_tab6', n_clicks=0, color="success", className="mr-1", size="lg")
boton_corregir_tab6 = dbc.Button('Corregir registro', id='corregir_tab6', n_clicks=0, color="primary", className="mr-1", size="lg")


boton_guardar_tab7 = dbc.Button('Guardar registro', id='guardar_tab7', n_clicks=0, color="success", className="mr-1", size="lg")
boton_corregir_tab7 = dbc.Button('Corregir registro', id='corregir_tab7', n_clicks=0, color="primary", className="mr-1", size="lg")


boton_guardar_tab8 = dbc.Button('Guardar registro', id='guardar_tab8', n_clicks=0, color="success", className="mr-1", size="lg")
boton_corregir_tab8 = dbc.Button('Corregir registro', id='corregir_tab8', n_clicks=0, color="primary", className="mr-1", size="lg")


boton_guardar_tab9 = dbc.Button('Guardar registro', id='guardar_tab9', n_clicks=0, color="success", className="mr-1", size="lg")
boton_corregir_tab9 = dbc.Button('Corregir registro', id='corregir_tab9', n_clicks=0, color="primary", className="mr-1", size="lg")


boton_guardar_tab10 = dbc.Button('Guardar registro', id='guardar_tab10', n_clicks=0, color="success", className="mr-1", size="lg")
boton_corregir_tab10 = dbc.Button('Corregir registro', id='corregir_tab10', n_clicks=0, color="primary", className="mr-1", size="lg")


boton_resultado = dbc.Button('Finalizar registro', id='finalizar', n_clicks=0, color="info", className="mr-1", size="lg")
boton_corregir_resultado = dbc.Button('Corregir finalizar', id='corregir_finalizar', n_clicks=0, color="primary", className="mr-1", size="lg")


#boton_reset = dbc.Button('Reset', id='reset_button', n_clicks=0, color="warning", className="mr-1", size="lg")


# ORGANIZARLOS en un formulario
###############################

# Preguntas Generales

form_datos1 = dbc.Form([html.H5('Datos de la encuesta'), html.Br(),
                        preg_a, preg_b, preg_c, preg_d, preg_e, preg_f, preg_g])

form_datos2 = dbc.Form([html.H5('Datos del hogar'), html.Br(),
                        preg_1, preg_2, preg_3, preg_4_1, preg_4_2, preg_4_3])


form_datos3 = dbc.Form([html.H5(), html.Br(),html.Br(),
                        preg_5, preg_6, preg_7, preg_7_1, preg_8, preg_9, preg_10, 
                        boton_guardar_tab1, boton_corregir_tab1])


# Preguntas Rubro: Carnes

form_datos4 = dbc.Form([html.H5('Cantidad Consumida. Rubro: CARNES'), html.Br(), 
                        preg_11_1, preg_11_2, preg_11_3, preg_11_4,
                        boton_guardar_tab2, boton_corregir_tab2])



# Preguntas Rubro: Pescados

form_datos5 = dbc.Form([html.H5('Cantidad Consumida. Rubro: PESCADOS Y MARISCOS'), html.Br(), 
                        preg_12_1, preg_12_2,
                        boton_guardar_tab3, boton_corregir_tab3])


# Preguntas Rubro: Aves

form_datos6 = dbc.Form([html.H5('Cantidad Consumida. Rubro: AVES'), html.Br(), 
                        preg_13_1, preg_13_2, preg_13_3, preg_13_4,
                        boton_guardar_tab4, boton_corregir_tab4])



# Preguntas Rubro: Embutidos

form_datos7 = dbc.Form([html.H5('Cantidad Consumida. Rubro: EMBUTIDOS'), html.Br(), 
                        preg_14_1,
                        boton_guardar_tab5, boton_corregir_tab5])



# Preguntas Rubro: Verduras

form_datos8 = dbc.Form([html.H5('Cantidad Consumida. Rubro: VERDURAS'), html.Br(), 
                        preg_15_1,preg_15_2,preg_15_3,preg_15_4,preg_15_5,
                        preg_15_6,preg_15_7,preg_15_8,preg_15_9,preg_15_10,
                        preg_15_11,preg_15_12,preg_15_13,
                        boton_guardar_tab6, boton_corregir_tab6])



# Preguntas Rubro: Frutas

form_datos9 = dbc.Form([html.H5('Cantidad Consumida. Rubro: FRUTAS'), html.Br(), 
                        preg_16_1,preg_16_2,preg_16_3,preg_16_4,preg_16_5,
                        preg_16_6,preg_16_7,preg_16_8,preg_16_9,
                        boton_guardar_tab7, boton_corregir_tab7])


# Preguntas Rubro: Abarrotes

form_datos10 = dbc.Form([html.H5('Cantidad Consumida. Rubro: ABARROTES'), html.Br(), 
                        preg_17_1,preg_17_2,preg_17_3,preg_17_4,preg_17_5,
                        preg_17_6,preg_17_7,preg_17_8,preg_17_9,preg_17_10,
                        preg_17_11,preg_17_12,preg_17_13,preg_17_14,preg_17_15,
                        preg_17_16,preg_17_17,
                        boton_guardar_tab8, boton_corregir_tab8])


# Preguntas Rubro: Comidas

form_datos11 = dbc.Form([html.H5('Cantidad Consumida. Rubro: COMIDAS PREPARADAS'), html.Br(), 
                        preg_18_1,preg_18_2,preg_18_3,preg_18_4,preg_18_5,
                        boton_guardar_tab9, boton_corregir_tab9])


# Preguntas Rubro: Otros

form_datos12 = dbc.Form([html.H5('Cantidad Consumida. Rubro: OTROS'), html.Br(), 
                        preg_19_1,preg_19_2,preg_19_3,preg_19_4,preg_19_5,
                        boton_guardar_tab10, boton_corregir_tab10])


# ORGANIZACION LAYOUT
##############################

## HTMLS

html_1 = [
    html.Div(children=[
        dbc.Col([
            dbc.Row([
                dbc.Jumbotron(form_datos1),
                dbc.Jumbotron(form_datos2),
                dbc.Jumbotron(form_datos3),
                ])
        ])
    ]),
    html.Br(),
    html.Div(children=[
		html.Div(id='lista_datos')
			]),
    #html.Div(children=[
	#	dcc.Store(id='lista_datos_store', storage_type='local')
    #    ]),
    html.Br()
    ]



html_2 = [
    html.Div(children=[
        dbc.Row([
            dbc.Col(
                dbc.Jumbotron(form_datos4))
            ])
        ]),
    html.Br(),
    html.Div(children=[
        html.Div(id='lista_datos_carne')
        ]),
    #html.Div(children=[
	#	dcc.Store(id='lista_datos_carne_store', storage_type='local')
    #    ]),
    html.Br()
    ]


html_3 = [
    html.Div(children=[
        dbc.Row([
            dbc.Col(
                dbc.Jumbotron(form_datos5))
            ])
        ]),
    html.Br(),
    html.Div(children=[
        html.Div(id='lista_datos_pescados')
        ]),
	#html.Div(children=[
	#	dcc.Store(id='lista_datos_pescados_store')
    #    ]),
    html.Br()
    ]


html_4 = [
    html.Div(children=[
        dbc.Row([
            dbc.Col(
                dbc.Jumbotron(form_datos6))
            ])
        ]),
    html.Br(),
    html.Div(children=[
        html.Div(id='lista_datos_aves')
        ]),
	#html.Div(children=[
	#	dcc.Store(id='lista_datos_aves_store')
    #    ]),
    html.Br()
    ]


html_5 = [
    html.Div(children=[
        dbc.Row([
            dbc.Col(
                dbc.Jumbotron(form_datos7))
            ])
        ]),
    html.Br(),
    html.Div(children=[
        html.Div(id='lista_datos_embutidos')
        ]),
	#html.Div(children=[
	#	dcc.Store(id='lista_datos_embutidos_store')
    #    ]),
    html.Br()
    ]


html_6 = [
    html.Div(children=[
        dbc.Row([
            dbc.Col(
                dbc.Jumbotron(form_datos8))
            ])
        ]),
    html.Br(),
    html.Div(children=[
        html.Div(id='lista_datos_verduras')
        ]),
	#html.Div(children=[
	#	dcc.Store(id='lista_datos_verduras_store')
    #    ]),
    html.Br()
    ]


html_7 = [
    html.Div(children=[
        dbc.Row([
            dbc.Col(
                dbc.Jumbotron(form_datos9))
            ])
        ]),
    html.Br(),
    html.Div(children=[
        html.Div(id='lista_datos_frutas')
        ]),
	#html.Div(children=[
	#	dcc.Store(id='lista_datos_frutas_store')
    #    ]),
    html.Br()
    ]


html_8 = [
    html.Div(children=[
        dbc.Row([
            dbc.Col(
                dbc.Jumbotron(form_datos10))
            ])
        ]),
    html.Br(),
    html.Div(children=[
        html.Div(id='lista_datos_abarrotes')
        ]),
	#html.Div(children=[
	#	dcc.Store(id='lista_datos_abarrotes_store')
    #    ]),
    html.Br()
    ]


html_9 = [
    html.Div(children=[
        dbc.Row([
            dbc.Col(
                dbc.Jumbotron(form_datos11))
            ])
        ]),
    html.Br(),
    html.Div(children=[
        html.Div(id='lista_datos_comidas')
        ]),
	#html.Div(children=[
	#	dcc.Store(id='lista_datos_comidas_store')
    #    ]),
    html.Br()
    ]


html_10 = [
    html.Div(children=[
        dbc.Row([
            dbc.Col(
                dbc.Jumbotron(form_datos12))
            ])
        ]),
    html.Br(),
    html.Div(children=[
        boton_resultado,
        boton_corregir_resultado,
        #boton_reset,
        html.Div(id='lista_datos_otros')
        ]),
	#html.Div(children=[
	#	dcc.Store(id='lista_datos_otros_store')
    #    ]),
    html.Br()
    ]



## TABS

tabs = [
        dbc.Tabs(
            [
                dbc.Tab(label='Datos Generales', tab_id='tab_1'),
                dbc.Tab(label='Rubro: Carnes', tab_id='tab_2'),
                dbc.Tab(label='Rubro: Pescados y Mariscos', tab_id='tab_3'),
                dbc.Tab(label='Rubro: Aves', tab_id='tab_4'),
                dbc.Tab(label='Rubro: Embutidos', tab_id='tab_5'),
                dbc.Tab(label='Rubro: Verduras', tab_id='tab_6'),
                dbc.Tab(label='Rubro: Frutas', tab_id='tab_7'),
                dbc.Tab(label='Rubro: Abarrotes', tab_id='tab_8'),
                dbc.Tab(label='Rubro: Comidas Preparadas', tab_id='tab_9'),
                dbc.Tab(label='Rubro: Otros', tab_id='tab_10')
            ],
            id='tabs',
            active_tab='tab_1',
        ),
        html.Div(id='tabs_contenido')
        ]



## LAYOUT GENERAL

app.layout = html.Div(
    children=[
        dbc.Jumbotron(
            html.Div(children=[
                html.H2(children='FORMULARIO - ENCUESTA DE DIMENSIONAMIENTO',
                        style={'font-family':'sans-serif','text-align':'left'}),
                html.H4(children='Estudio de Dimensionamiento para el Proyecto: ' + proyecto,
                        style={'font-family':'sans-serif'}),
                html.H6(children='Fecha: ' + hoy,
                        style={'font-family':'sans-serif'}),
                html.Br(),
                html.Div(children=tabs),
                html.Div(children=[
                    html.Div(id='resultado')
                    ]),   
                html.Div(children=[
                    dcc.Store(id='lista_datos_store', storage_type='memory'),
                    dcc.Store(id='lista_datos_carne_store', storage_type='memory'),
                    dcc.Store(id='lista_datos_pescados_store', storage_type='memory'),
                    dcc.Store(id='lista_datos_aves_store', storage_type='memory'),
                    dcc.Store(id='lista_datos_embutidos_store', storage_type='memory'),
                    dcc.Store(id='lista_datos_verduras_store', storage_type='memory'),
                    dcc.Store(id='lista_datos_frutas_store', storage_type='memory'),
                    dcc.Store(id='lista_datos_abarrotes_store', storage_type='memory'),
                    dcc.Store(id='lista_datos_comidas_store', storage_type='memory'),
                    dcc.Store(id='lista_datos_otros_store', storage_type='memory')
                    ])
                ])
            )]
    )



# FUNCIONES CALLBACKS
############################


# CALLBACK TABS

@app.callback(Output(component_id='tabs_contenido', component_property='children'),
              Input(component_id='tabs', component_property='active_tab'))


def render_content(tab):
    if tab == 'tab_1':
        return html.Div(html_1)
    elif tab == 'tab_2':
        return html.Div(html_2)
    elif tab == 'tab_3':
        return html.Div(html_3)
    elif tab == 'tab_4':
        return html.Div(html_4)
    elif tab == 'tab_5':
        return html.Div(html_5)
    elif tab == 'tab_6':
        return html.Div(html_6)
    elif tab == 'tab_7':
        return html.Div(html_7)
    elif tab == 'tab_8':
        return html.Div(html_8)
    elif tab == 'tab_9':
        return html.Div(html_9)
    elif tab == 'tab_10':
        return html.Div(html_10)



# CALLBACK DATOS GENERALES

@app.callback(
	Output(component_id='lista_datos_store', component_property='data'),
    Input(component_id='guardar_tab1', component_property='n_clicks'),
    [State(component_id='num_encuesta', component_property='value'),
     State(component_id='encuestador', component_property='value'),
     State(component_id='supervisor', component_property='value'),
     State(component_id='fecha', component_property='date'),
     State(component_id='sector', component_property='value'),
     State(component_id='mz', component_property='value'),
     State(component_id='viv', component_property='value'),
     State(component_id='p1', component_property='value'),
     State(component_id='p2', component_property='value'),
     State(component_id='p3', component_property='value'),
     State(component_id='p4_1', component_property='value'),
     State(component_id='p4_2', component_property='value'),
     State(component_id='p4_3', component_property='value'),
     State(component_id='p5', component_property='value'),
     State(component_id='p6', component_property='value'),
     State(component_id='p7', component_property='value'),
     State(component_id='p7_1', component_property='value'),
     State(component_id='p8', component_property='value'),
     State(component_id='p9', component_property='value'),
     State(component_id='p10', component_property='value')
     ]
)


def output1(n_clicks,num_encuesta,encuestador,supervisor,fecha,sector,mz,viv,p1,p2,p3,
            p4_1,p4_2,p4_3,p5,p6,p7,p7_1,p8,p9,p10):
    
    lista_datos_gen = []
    
    if n_clicks > 0:
        
        if (num_encuesta == None or encuestador == None or supervisor == None or 
            sector == None or mz == None or viv == None or p1 == None or p2 == None or 
            p3 == None or p4_1 == None or p4_2 == None or p4_3 == None or p5 == None or 
            p6 == None or p7 == None or p7_1 == None or p8 == None or p9 == None or p10 == None):
            
            return {'lista_prod':lista_datos_gen, 'alerta':dbc.Alert("No se puede continuar, registros vacíos...", color="danger")}
        
        elif (p3 == 'no' and p7 == 'negocio'):
            return {'lista_prod':lista_datos_gen, 'alerta':dbc.Alert('No se puede continuar con el registro. Revisar P3 y P7', color='danger')}
        
        elif p3 == 'no':
            return {'lista_prod':lista_datos_gen, 'alerta':dbc.Alert('No se puede continuar con el registro. Revisar P3', color='danger')}
        
        elif p7 == 'negocio':
            return {'lista_prod':lista_datos_gen, 'alerta':dbc.Alert('No se puede continuar con el registro. Revisar P7', color='danger')}
        
        elif (p4_1 + p4_2 + p4_3) != 100:
            return {'lista_prod':lista_datos_gen, 'alerta':dbc.Alert('No se puede continuar con el registro. \
					Revisar P4_1 + P4_2 + P4_3, debe sumar 100%', color='danger')}
        else:
            lista_datos_gen.clear()
            lista_datos_gen.append(num_encuesta)
            lista_datos_gen.append(encuestador)
            lista_datos_gen.append(supervisor)
            lista_datos_gen.append(fecha)
            lista_datos_gen.append(sector)
            lista_datos_gen.append(mz)
            lista_datos_gen.append(viv)
            lista_datos_gen.append(p1)
            lista_datos_gen.append(p2)
            lista_datos_gen.append(p3)
            lista_datos_gen.append(p4_1)
            lista_datos_gen.append(p4_2)
            lista_datos_gen.append(p4_3)
            lista_datos_gen.append(p5)
            lista_datos_gen.append(p6)
            lista_datos_gen.append(p7)
            lista_datos_gen.append(p7_1)
            lista_datos_gen.append(p8)
            lista_datos_gen.append(p9)
            lista_datos_gen.append(p10)
						
			#df1 = pd.DataFrame(lista_datos_gen)
			#df1.to_excel('lista_datos_gen.xlsx')
            return {'lista_prod':lista_datos_gen, 'alerta':dbc.Alert('Registro de Encuesta Nº '+ str(num_encuesta) + ', \
                                                                     satisfactorio. Continúe en la siguiente pestaña.', color='success')}


@app.callback(
Output(component_id='lista_datos', component_property='children'),
Input(component_id='lista_datos_store', component_property='data')
)

def output1_1(data):
	if data is None:
		raise PreventUpdate
	return data['alerta']





# CALLBACK RUBRO CARNE
#######################

@app.callback(
    Output(component_id='lista_datos_carne_store', component_property='data'),
    Input(component_id='guardar_tab2', component_property='n_clicks'),
    [State(component_id='lista_datos_store', component_property='data'),
     State(component_id='p101_0', component_property='value'),
     State(component_id='p101_1', component_property='value'),
     State(component_id='p101_2', component_property='value'),
     State(component_id='p101_3', component_property='value'),
     State(component_id='p101_4', component_property='value'),
     State(component_id='p102_0', component_property='value'),
     State(component_id='p102_1', component_property='value'),
     State(component_id='p102_2', component_property='value'),
     State(component_id='p102_3', component_property='value'),
     State(component_id='p102_4', component_property='value'),
     State(component_id='p103_0', component_property='value'),
     State(component_id='p103_1', component_property='value'),
     State(component_id='p103_2', component_property='value'),
     State(component_id='p103_3', component_property='value'),
     State(component_id='p103_4', component_property='value'),
     State(component_id='p104_0', component_property='value'),
     State(component_id='p104_1', component_property='value'),
     State(component_id='p104_2', component_property='value'),
     State(component_id='p104_3', component_property='value'),
     State(component_id='p104_4', component_property='value')
     ]
)


def output2(n_clicks,data,
            p101_0,p101_1,p101_2,p101_3,p101_4,
            p102_0,p102_1,p102_2,p102_3,p102_4,
            p103_0,p103_1,p103_2,p103_3,p103_4,
            p104_0,p104_1,p104_2,p104_3,p104_4):
    
    lista_datos_carne = []
    
    if n_clicks > 0:
        if len(data['lista_prod']) == 0:
            return {'lista_prod':lista_datos_carne, 'alerta':dbc.Alert('Registre los Datos Generales de la encuesta.', color='danger')}
        else:
            lista_datos_carne.clear()
            lista_datos_carne.append(p101_0)
            lista_datos_carne.append(p101_1)
            lista_datos_carne.append(p101_2)
            lista_datos_carne.append(p101_3)
            lista_datos_carne.append(p101_4)
            lista_datos_carne.append(p102_0)
            lista_datos_carne.append(p102_1)
            lista_datos_carne.append(p102_2)
            lista_datos_carne.append(p102_3)
            lista_datos_carne.append(p102_4)
            lista_datos_carne.append(p103_0)
            lista_datos_carne.append(p103_1)
            lista_datos_carne.append(p103_2)
            lista_datos_carne.append(p103_3)
            lista_datos_carne.append(p103_4)
            lista_datos_carne.append(p104_0)
            lista_datos_carne.append(p104_1)
            lista_datos_carne.append(p104_2)
            lista_datos_carne.append(p104_3)
            lista_datos_carne.append(p104_4)
            #df1 = pd.DataFrame(lista_datos_carne)
            #df1.to_excel('lista_datos_carne.xlsx')
            return {'lista_prod':lista_datos_carne, 'alerta':dbc.Alert('Registro Nº ' + str(data['lista_prod'][0]) + ', \
					satisfactorio. Continúe en la siguiente pestaña.', color='success')}


@app.callback(
Output(component_id='lista_datos_carne', component_property='children'),
Input(component_id='lista_datos_carne_store', component_property='data')
)

def output2_1(data):
	if data is None:
		raise PreventUpdate
	return data['alerta']




# CALLBACK RUBRO PESCADOS
#########################

@app.callback(
     Output(component_id='lista_datos_pescados_store', component_property='data'),
     Input(component_id='guardar_tab3', component_property='n_clicks'),
    [State(component_id='lista_datos_carne_store', component_property='data'),
     State(component_id='lista_datos_store', component_property='data'),
     State(component_id='p201_0', component_property='value'),
     State(component_id='p201_1', component_property='value'),
     State(component_id='p201_2', component_property='value'),
     State(component_id='p201_3', component_property='value'),
     State(component_id='p201_4', component_property='value'),
     State(component_id='p202_0', component_property='value'),
     State(component_id='p202_1', component_property='value'),
     State(component_id='p202_2', component_property='value'),
     State(component_id='p202_3', component_property='value'),
     State(component_id='p202_4', component_property='value')
     ]
)


def output3(n_clicks,data,data1,
            p201_0,p201_1,p201_2,p201_3,p201_4,
            p202_0,p202_1,p202_2,p202_3,p202_4):
    
    lista_datos_pescados = []

    if n_clicks > 0:
        if len(data['lista_prod']) == 0:
            return {'lista_prod':lista_datos_pescados, 'alerta':dbc.Alert('Registre las pestañas anteriores.', color='danger')}
        else:
            lista_datos_pescados.clear()
            lista_datos_pescados.append(p201_0)
            lista_datos_pescados.append(p201_1)
            lista_datos_pescados.append(p201_2)
            lista_datos_pescados.append(p201_3)
            lista_datos_pescados.append(p201_4)
            lista_datos_pescados.append(p202_0)
            lista_datos_pescados.append(p202_1)
            lista_datos_pescados.append(p202_2)
            lista_datos_pescados.append(p202_3)
            lista_datos_pescados.append(p202_4)
        
            #df1 = pd.DataFrame(lista_datos_pescados)
            #df1.to_excel('lista_datos_pescados.xlsx')
            return {'lista_prod':lista_datos_pescados, 'alerta':dbc.Alert('Registro Nº ' + str(data1['lista_prod'][0]) + ', \
					satisfactorio. Continúe en la siguiente pestaña.', color='success')}


@app.callback(
Output(component_id='lista_datos_pescados', component_property='children'),
Input(component_id='lista_datos_pescados_store', component_property='data')
)

def output3_1(data):
	if data is None:
		raise PreventUpdate
	return data['alerta']



# CALLBACK RUBRO AVES
#########################

@app.callback(
     Output(component_id='lista_datos_aves_store', component_property='data'),
     Input(component_id='guardar_tab4', component_property='n_clicks'),
    [State(component_id='lista_datos_pescados_store', component_property='data'),
     State(component_id='lista_datos_store', component_property='data'),
     State(component_id='p301_0', component_property='value'),
     State(component_id='p301_1', component_property='value'),
     State(component_id='p301_2', component_property='value'),
     State(component_id='p301_3', component_property='value'),
     State(component_id='p301_4', component_property='value'),
     State(component_id='p302_0', component_property='value'),
     State(component_id='p302_1', component_property='value'),
     State(component_id='p302_2', component_property='value'),
     State(component_id='p302_3', component_property='value'),
     State(component_id='p302_4', component_property='value'),
     State(component_id='p303_0', component_property='value'),
     State(component_id='p303_1', component_property='value'),
     State(component_id='p303_2', component_property='value'),
     State(component_id='p303_3', component_property='value'),
     State(component_id='p303_4', component_property='value'),
     State(component_id='p304_0', component_property='value'),
     State(component_id='p304_1', component_property='value'),
     State(component_id='p304_2', component_property='value'),
     State(component_id='p304_3', component_property='value'),
     State(component_id='p304_4', component_property='value')
     ]
)


def output4(n_clicks,data,data1,
            p301_0,p301_1,p301_2,p301_3,p301_4,
            p302_0,p302_1,p302_2,p302_3,p302_4,
            p303_0,p303_1,p303_2,p303_3,p303_4,
            p304_0,p304_1,p304_2,p304_3,p304_4):
    
    lista_datos_aves = []

    if n_clicks > 0:
        if len(data['lista_prod']) == 0:
            return {'lista_prod':lista_datos_aves, 'alerta':dbc.Alert('Registre las pestañas anteriores.', color='danger')}
        else:
            lista_datos_aves.clear()
            lista_datos_aves.append(p301_0)
            lista_datos_aves.append(p301_1)
            lista_datos_aves.append(p301_2)
            lista_datos_aves.append(p301_3)
            lista_datos_aves.append(p301_4)
            lista_datos_aves.append(p302_0)
            lista_datos_aves.append(p302_1)
            lista_datos_aves.append(p302_2)
            lista_datos_aves.append(p302_3)
            lista_datos_aves.append(p302_4)
            lista_datos_aves.append(p303_0)
            lista_datos_aves.append(p303_1)
            lista_datos_aves.append(p303_2)
            lista_datos_aves.append(p303_3)
            lista_datos_aves.append(p303_4)
            lista_datos_aves.append(p304_0)
            lista_datos_aves.append(p304_1)
            lista_datos_aves.append(p304_2)
            lista_datos_aves.append(p304_3)
            lista_datos_aves.append(p304_4)
        
            #df1 = pd.DataFrame(lista_datos_aves)
            #df1.to_excel('lista_datos_aves.xlsx')
            return {'lista_prod':lista_datos_aves, 'alerta':dbc.Alert('Registro Nº ' + str(data1['lista_prod'][0]) + ', \
					satisfactorio. Continúe en la siguiente pestaña', color='success')}


@app.callback(
Output(component_id='lista_datos_aves', component_property='children'),
Input(component_id='lista_datos_aves_store', component_property='data')
)

def output4_1(data):
	if data is None:
		raise PreventUpdate
	return data['alerta']






# CALLBACK RUBRO EMBUTIDOS
#########################

@app.callback(
     Output(component_id='lista_datos_embutidos_store', component_property='data'),
     Input(component_id='guardar_tab5', component_property='n_clicks'),
    [State(component_id='lista_datos_aves_store', component_property='data'),
     State(component_id='lista_datos_store', component_property='data'),
     State(component_id='p401_0', component_property='value'),
     State(component_id='p401_1', component_property='value'),
     State(component_id='p401_2', component_property='value'),
     State(component_id='p401_3', component_property='value'),
     State(component_id='p401_4', component_property='value')
     ]
)


def output5(n_clicks,data,data1,
            p401_0,p401_1,p401_2,p401_3,p401_4):
    
    lista_datos_embutidos = []

    if n_clicks > 0:
        if len(data['lista_prod']) == 0:
            return {'lista_prod':lista_datos_embutidos, 'alerta':dbc.Alert('Registre las pestañas anteriores.', color='danger')}
        else:
            lista_datos_embutidos.clear()
            lista_datos_embutidos.append(p401_0)
            lista_datos_embutidos.append(p401_1)
            lista_datos_embutidos.append(p401_2)
            lista_datos_embutidos.append(p401_3)
            lista_datos_embutidos.append(p401_4)
        
            #df1 = pd.DataFrame(lista_datos_embutidos)
            #df1.to_excel('lista_datos_embutidos.xlsx')
            return {'lista_prod':lista_datos_embutidos, 'alerta':dbc.Alert('Registro Nº ' + str(data1['lista_prod'][0]) + ', \
                    satisfactorio. Continúe en la siguiente pestaña', color='success')}


@app.callback(
Output(component_id='lista_datos_embutidos', component_property='children'),
Input(component_id='lista_datos_embutidos_store', component_property='data')
)

def output5_1(data):
	if data is None:
		raise PreventUpdate
	return data['alerta']




# CALLBACK RUBRO VERDURAS
#########################

@app.callback(
     Output(component_id='lista_datos_verduras_store', component_property='data'),
     Input(component_id='guardar_tab6', component_property='n_clicks'),
    [State(component_id='lista_datos_embutidos_store', component_property='data'),
     State(component_id='lista_datos_store', component_property='data'),
     State(component_id='p501_0', component_property='value'),
     State(component_id='p501_1', component_property='value'),
     State(component_id='p501_2', component_property='value'),
     State(component_id='p501_3', component_property='value'),
     State(component_id='p501_4', component_property='value'),
     
     State(component_id='p502_0', component_property='value'),
     State(component_id='p502_1', component_property='value'),
     State(component_id='p502_2', component_property='value'),
     State(component_id='p502_3', component_property='value'),
     State(component_id='p502_4', component_property='value'),
     
     State(component_id='p503_0', component_property='value'),
     State(component_id='p503_1', component_property='value'),
     State(component_id='p503_2', component_property='value'),
     State(component_id='p503_3', component_property='value'),
     State(component_id='p503_4', component_property='value'),
     
     State(component_id='p504_0', component_property='value'),
     State(component_id='p504_1', component_property='value'),
     State(component_id='p504_2', component_property='value'),
     State(component_id='p504_3', component_property='value'),
     State(component_id='p504_4', component_property='value'),
     
     State(component_id='p505_0', component_property='value'),
     State(component_id='p505_1', component_property='value'),
     State(component_id='p505_2', component_property='value'),
     State(component_id='p505_3', component_property='value'),
     State(component_id='p505_4', component_property='value'),
     
     State(component_id='p506_0', component_property='value'),
     State(component_id='p506_1', component_property='value'),
     State(component_id='p506_2', component_property='value'),
     State(component_id='p506_3', component_property='value'),
     State(component_id='p506_4', component_property='value'),
     
     State(component_id='p507_0', component_property='value'),
     State(component_id='p507_1', component_property='value'),
     State(component_id='p507_2', component_property='value'),
     State(component_id='p507_3', component_property='value'),
     State(component_id='p507_4', component_property='value'),
     
     State(component_id='p508_0', component_property='value'),
     State(component_id='p508_1', component_property='value'),
     State(component_id='p508_2', component_property='value'),
     State(component_id='p508_3', component_property='value'),
     State(component_id='p508_4', component_property='value'),
     
     State(component_id='p509_0', component_property='value'),
     State(component_id='p509_1', component_property='value'),
     State(component_id='p509_2', component_property='value'),
     State(component_id='p509_3', component_property='value'),
     State(component_id='p509_4', component_property='value'),
     
     State(component_id='p510_0', component_property='value'),
     State(component_id='p510_1', component_property='value'),
     State(component_id='p510_2', component_property='value'),
     State(component_id='p510_3', component_property='value'),
     State(component_id='p510_4', component_property='value'),
     
     State(component_id='p511_0', component_property='value'),
     State(component_id='p511_1', component_property='value'),
     State(component_id='p511_2', component_property='value'),
     State(component_id='p511_3', component_property='value'),
     State(component_id='p511_4', component_property='value'),
     
     State(component_id='p512_0', component_property='value'),
     State(component_id='p512_1', component_property='value'),
     State(component_id='p512_2', component_property='value'),
     State(component_id='p512_3', component_property='value'),
     State(component_id='p512_4', component_property='value'),
     
     State(component_id='p513_0', component_property='value'),
     State(component_id='p513_1', component_property='value'),
     State(component_id='p513_2', component_property='value'),
     State(component_id='p513_3', component_property='value'),
     State(component_id='p513_4', component_property='value')
     ]
)


def output6(n_clicks,data,data1,
            p501_0,p501_1,p501_2,p501_3,p501_4,
            p502_0,p502_1,p502_2,p502_3,p502_4,
            p503_0,p503_1,p503_2,p503_3,p503_4,
            p504_0,p504_1,p504_2,p504_3,p504_4,
            p505_0,p505_1,p505_2,p505_3,p505_4,
            p506_0,p506_1,p506_2,p506_3,p506_4,
            p507_0,p507_1,p507_2,p507_3,p507_4,
            p508_0,p508_1,p508_2,p508_3,p508_4,
            p509_0,p509_1,p509_2,p509_3,p509_4,
            p510_0,p510_1,p510_2,p510_3,p510_4,
            p511_0,p511_1,p511_2,p511_3,p511_4,
            p512_0,p512_1,p512_2,p512_3,p512_4,
            p513_0,p513_1,p513_2,p513_3,p513_4):
    
    lista_datos_verduras = []

    if n_clicks > 0:
        if len(data['lista_prod']) == 0:
            return {'lista_prod':lista_datos_verduras, 'alerta':dbc.Alert('Registre las pestañas anteriores.', color='danger')}
        else:
            lista_datos_verduras.clear()
            lista_datos_verduras.append(p501_0)
            lista_datos_verduras.append(p501_1)
            lista_datos_verduras.append(p501_2)
            lista_datos_verduras.append(p501_3)
            lista_datos_verduras.append(p501_4)
            
            lista_datos_verduras.append(p502_0)
            lista_datos_verduras.append(p502_1)
            lista_datos_verduras.append(p502_2)
            lista_datos_verduras.append(p502_3)
            lista_datos_verduras.append(p502_4)
            
            lista_datos_verduras.append(p503_0)
            lista_datos_verduras.append(p503_1)
            lista_datos_verduras.append(p503_2)
            lista_datos_verduras.append(p503_3)
            lista_datos_verduras.append(p503_4)
            
            lista_datos_verduras.append(p504_0)
            lista_datos_verduras.append(p504_1)
            lista_datos_verduras.append(p504_2)
            lista_datos_verduras.append(p504_3)
            lista_datos_verduras.append(p504_4)
            
            lista_datos_verduras.append(p505_0)
            lista_datos_verduras.append(p505_1)
            lista_datos_verduras.append(p505_2)
            lista_datos_verduras.append(p505_3)
            lista_datos_verduras.append(p505_4)
            
            lista_datos_verduras.append(p506_0)
            lista_datos_verduras.append(p506_1)
            lista_datos_verduras.append(p506_2)
            lista_datos_verduras.append(p506_3)
            lista_datos_verduras.append(p506_4)
            
            lista_datos_verduras.append(p507_0)
            lista_datos_verduras.append(p507_1)
            lista_datos_verduras.append(p507_2)
            lista_datos_verduras.append(p507_3)
            lista_datos_verduras.append(p507_4)
            
            lista_datos_verduras.append(p508_0)
            lista_datos_verduras.append(p508_1)
            lista_datos_verduras.append(p508_2)
            lista_datos_verduras.append(p508_3)
            lista_datos_verduras.append(p508_4)
            
            lista_datos_verduras.append(p509_0)
            lista_datos_verduras.append(p509_1)
            lista_datos_verduras.append(p509_2)
            lista_datos_verduras.append(p509_3)
            lista_datos_verduras.append(p509_4)
            
            lista_datos_verduras.append(p510_0)
            lista_datos_verduras.append(p510_1)
            lista_datos_verduras.append(p510_2)
            lista_datos_verduras.append(p510_3)
            lista_datos_verduras.append(p510_4)
            
            lista_datos_verduras.append(p511_0)
            lista_datos_verduras.append(p511_1)
            lista_datos_verduras.append(p511_2)
            lista_datos_verduras.append(p511_3)
            lista_datos_verduras.append(p511_4)
            
            lista_datos_verduras.append(p512_0)
            lista_datos_verduras.append(p512_1)
            lista_datos_verduras.append(p512_2)
            lista_datos_verduras.append(p512_3)
            lista_datos_verduras.append(p512_4)
            
            lista_datos_verduras.append(p513_0)
            lista_datos_verduras.append(p513_1)
            lista_datos_verduras.append(p513_2)
            lista_datos_verduras.append(p513_3)
            lista_datos_verduras.append(p513_4)
        
            #df1 = pd.DataFrame(lista_datos_verduras)
            #df1.to_excel('lista_datos_verduras.xlsx')
            return {'lista_prod':lista_datos_verduras, 'alerta':dbc.Alert('Registro Nº ' + str(data1['lista_prod'][0]) + ', \
					satisfactorio. Continúe en la siguiente pestaña', color='success')}



@app.callback(
Output(component_id='lista_datos_verduras', component_property='children'),
Input(component_id='lista_datos_verduras_store', component_property='data')
)

def output6_1(data):
	if data is None:
		raise PreventUpdate
	return data['alerta']





# CALLBACK RUBRO FRUTAS
#########################

@app.callback(
     Output(component_id='lista_datos_frutas_store', component_property='data'),
     Input(component_id='guardar_tab7', component_property='n_clicks'),
    [State(component_id='lista_datos_verduras_store', component_property='data'),
     State(component_id='lista_datos_store', component_property='data'),
     State(component_id='p601_0', component_property='value'),
     State(component_id='p601_1', component_property='value'),
     State(component_id='p601_2', component_property='value'),
     State(component_id='p601_3', component_property='value'),
     State(component_id='p601_4', component_property='value'),
     
     State(component_id='p602_0', component_property='value'),
     State(component_id='p602_1', component_property='value'),
     State(component_id='p602_2', component_property='value'),
     State(component_id='p602_3', component_property='value'),
     State(component_id='p602_4', component_property='value'),
     
     State(component_id='p603_0', component_property='value'),
     State(component_id='p603_1', component_property='value'),
     State(component_id='p603_2', component_property='value'),
     State(component_id='p603_3', component_property='value'),
     State(component_id='p603_4', component_property='value'),
     
     State(component_id='p604_0', component_property='value'),
     State(component_id='p604_1', component_property='value'),
     State(component_id='p604_2', component_property='value'),
     State(component_id='p604_3', component_property='value'),
     State(component_id='p604_4', component_property='value'),
     
     State(component_id='p605_0', component_property='value'),
     State(component_id='p605_1', component_property='value'),
     State(component_id='p605_2', component_property='value'),
     State(component_id='p605_3', component_property='value'),
     State(component_id='p605_4', component_property='value'),
     
     State(component_id='p606_0', component_property='value'),
     State(component_id='p606_1', component_property='value'),
     State(component_id='p606_2', component_property='value'),
     State(component_id='p606_3', component_property='value'),
     State(component_id='p606_4', component_property='value'),
     
     State(component_id='p607_0', component_property='value'),
     State(component_id='p607_1', component_property='value'),
     State(component_id='p607_2', component_property='value'),
     State(component_id='p607_3', component_property='value'),
     State(component_id='p607_4', component_property='value'),
     
     State(component_id='p608_0', component_property='value'),
     State(component_id='p608_1', component_property='value'),
     State(component_id='p608_2', component_property='value'),
     State(component_id='p608_3', component_property='value'),
     State(component_id='p608_4', component_property='value'),
     
     State(component_id='p609_0', component_property='value'),
     State(component_id='p609_1', component_property='value'),
     State(component_id='p609_2', component_property='value'),
     State(component_id='p609_3', component_property='value'),
     State(component_id='p609_4', component_property='value')
     ]
)


def output7(n_clicks,data,data1,
            p601_0,p601_1,p601_2,p601_3,p601_4,
            p602_0,p602_1,p602_2,p602_3,p602_4,
            p603_0,p603_1,p603_2,p603_3,p603_4,
            p604_0,p604_1,p604_2,p604_3,p604_4,
            p605_0,p605_1,p605_2,p605_3,p605_4,
            p606_0,p606_1,p606_2,p606_3,p606_4,
            p607_0,p607_1,p607_2,p607_3,p607_4,
            p608_0,p608_1,p608_2,p608_3,p608_4,
            p609_0,p609_1,p609_2,p609_3,p609_4):
    
    lista_datos_frutas = []

    if n_clicks > 0:
        if len(data['lista_prod']) == 0:
            return {'lista_prod':lista_datos_frutas, 'alerta':dbc.Alert('Registre las pestañas anteriores.', color='danger')}
        else:
            lista_datos_frutas.clear()
            lista_datos_frutas.append(p601_0)
            lista_datos_frutas.append(p601_1)
            lista_datos_frutas.append(p601_2)
            lista_datos_frutas.append(p601_3)
            lista_datos_frutas.append(p601_4)
            
            lista_datos_frutas.append(p602_0)
            lista_datos_frutas.append(p602_1)
            lista_datos_frutas.append(p602_2)
            lista_datos_frutas.append(p602_3)
            lista_datos_frutas.append(p602_4)
            
            lista_datos_frutas.append(p603_0)
            lista_datos_frutas.append(p603_1)
            lista_datos_frutas.append(p603_2)
            lista_datos_frutas.append(p603_3)
            lista_datos_frutas.append(p603_4)
            
            lista_datos_frutas.append(p604_0)
            lista_datos_frutas.append(p604_1)
            lista_datos_frutas.append(p604_2)
            lista_datos_frutas.append(p604_3)
            lista_datos_frutas.append(p604_4)
            
            lista_datos_frutas.append(p605_0)
            lista_datos_frutas.append(p605_1)
            lista_datos_frutas.append(p605_2)
            lista_datos_frutas.append(p605_3)
            lista_datos_frutas.append(p605_4)
            
            lista_datos_frutas.append(p606_0)
            lista_datos_frutas.append(p606_1)
            lista_datos_frutas.append(p606_2)
            lista_datos_frutas.append(p606_3)
            lista_datos_frutas.append(p606_4)
            
            lista_datos_frutas.append(p607_0)
            lista_datos_frutas.append(p607_1)
            lista_datos_frutas.append(p607_2)
            lista_datos_frutas.append(p607_3)
            lista_datos_frutas.append(p607_4)
            
            lista_datos_frutas.append(p608_0)
            lista_datos_frutas.append(p608_1)
            lista_datos_frutas.append(p608_2)
            lista_datos_frutas.append(p608_3)
            lista_datos_frutas.append(p608_4)
            
            lista_datos_frutas.append(p609_0)
            lista_datos_frutas.append(p609_1)
            lista_datos_frutas.append(p609_2)
            lista_datos_frutas.append(p609_3)
            lista_datos_frutas.append(p609_4)
        
            #df1 = pd.DataFrame(lista_datos_frutas)
            #df1.to_excel('lista_datos_frutas.xlsx')
            return {'lista_prod':lista_datos_frutas, 'alerta':dbc.Alert('Registro Nº ' + str(data1['lista_prod'][0]) + ', \
					satisfactorio. Continúe en la siguiente pestaña', color='success')}



@app.callback(
Output(component_id='lista_datos_frutas', component_property='children'),
Input(component_id='lista_datos_frutas_store', component_property='data')
)

def output7_1(data):
	if data is None:
		raise PreventUpdate
	return data['alerta']





# CALLBACK RUBRO ABARROTES
##########################

@app.callback(
     Output(component_id='lista_datos_abarrotes_store', component_property='data'),
     Input(component_id='guardar_tab8', component_property='n_clicks'),
    [State(component_id='lista_datos_frutas_store', component_property='data'),
     State(component_id='lista_datos_store', component_property='data'),
     State(component_id='p701_0', component_property='value'),
     State(component_id='p701_1', component_property='value'),
     State(component_id='p701_2', component_property='value'),
     State(component_id='p701_3', component_property='value'),
     State(component_id='p701_4', component_property='value'),
     
     State(component_id='p702_0', component_property='value'),
     State(component_id='p702_1', component_property='value'),
     State(component_id='p702_2', component_property='value'),
     State(component_id='p702_3', component_property='value'),
     State(component_id='p702_4', component_property='value'),
     
     State(component_id='p703_0', component_property='value'),
     State(component_id='p703_1', component_property='value'),
     State(component_id='p703_2', component_property='value'),
     State(component_id='p703_3', component_property='value'),
     State(component_id='p703_4', component_property='value'),
     
     State(component_id='p704_0', component_property='value'),
     State(component_id='p704_1', component_property='value'),
     State(component_id='p704_2', component_property='value'),
     State(component_id='p704_3', component_property='value'),
     State(component_id='p704_4', component_property='value'),
     
     State(component_id='p705_0', component_property='value'),
     State(component_id='p705_1', component_property='value'),
     State(component_id='p705_2', component_property='value'),
     State(component_id='p705_3', component_property='value'),
     State(component_id='p705_4', component_property='value'),
     
     State(component_id='p706_0', component_property='value'),
     State(component_id='p706_1', component_property='value'),
     State(component_id='p706_2', component_property='value'),
     State(component_id='p706_3', component_property='value'),
     State(component_id='p706_4', component_property='value'),
     
     State(component_id='p707_0', component_property='value'),
     State(component_id='p707_1', component_property='value'),
     State(component_id='p707_2', component_property='value'),
     State(component_id='p707_3', component_property='value'),
     State(component_id='p707_4', component_property='value'),
     
     State(component_id='p708_0', component_property='value'),
     State(component_id='p708_1', component_property='value'),
     State(component_id='p708_2', component_property='value'),
     State(component_id='p708_3', component_property='value'),
     State(component_id='p708_4', component_property='value'),
     
     State(component_id='p709_0', component_property='value'),
     State(component_id='p709_1', component_property='value'),
     State(component_id='p709_2', component_property='value'),
     State(component_id='p709_3', component_property='value'),
     State(component_id='p709_4', component_property='value'),
     
     State(component_id='p710_0', component_property='value'),
     State(component_id='p710_1', component_property='value'),
     State(component_id='p710_2', component_property='value'),
     State(component_id='p710_3', component_property='value'),
     State(component_id='p710_4', component_property='value'),
     
     State(component_id='p711_0', component_property='value'),
     State(component_id='p711_1', component_property='value'),
     State(component_id='p711_2', component_property='value'),
     State(component_id='p711_3', component_property='value'),
     State(component_id='p711_4', component_property='value'),
     
     State(component_id='p712_0', component_property='value'),
     State(component_id='p712_1', component_property='value'),
     State(component_id='p712_2', component_property='value'),
     State(component_id='p712_3', component_property='value'),
     State(component_id='p712_4', component_property='value'),
     
     State(component_id='p713_0', component_property='value'),
     State(component_id='p713_1', component_property='value'),
     State(component_id='p713_2', component_property='value'),
     State(component_id='p713_3', component_property='value'),
     State(component_id='p713_4', component_property='value'),
     
     State(component_id='p714_0', component_property='value'),
     State(component_id='p714_1', component_property='value'),
     State(component_id='p714_2', component_property='value'),
     State(component_id='p714_3', component_property='value'),
     State(component_id='p714_4', component_property='value'),
     
     State(component_id='p715_0', component_property='value'),
     State(component_id='p715_1', component_property='value'),
     State(component_id='p715_2', component_property='value'),
     State(component_id='p715_3', component_property='value'),
     State(component_id='p715_4', component_property='value'),
     
     State(component_id='p716_0', component_property='value'),
     State(component_id='p716_1', component_property='value'),
     State(component_id='p716_2', component_property='value'),
     State(component_id='p716_3', component_property='value'),
     State(component_id='p716_4', component_property='value'),
     
     State(component_id='p717_0', component_property='value'),
     State(component_id='p717_1', component_property='value'),
     State(component_id='p717_2', component_property='value'),
     State(component_id='p717_3', component_property='value'),
     State(component_id='p717_4', component_property='value')
     ]
)


def output8(n_clicks,data,data1,
            p701_0,p701_1,p701_2,p701_3,p701_4,
            p702_0,p702_1,p702_2,p702_3,p702_4,
            p703_0,p703_1,p703_2,p703_3,p703_4,
            p704_0,p704_1,p704_2,p704_3,p704_4,
            p705_0,p705_1,p705_2,p705_3,p705_4,
            p706_0,p706_1,p706_2,p706_3,p706_4,
            p707_0,p707_1,p707_2,p707_3,p707_4,
            p708_0,p708_1,p708_2,p708_3,p708_4,
            p709_0,p709_1,p709_2,p709_3,p709_4,
            p710_0,p710_1,p710_2,p710_3,p710_4,
            p711_0,p711_1,p711_2,p711_3,p711_4,
            p712_0,p712_1,p712_2,p712_3,p712_4,
            p713_0,p713_1,p713_2,p713_3,p713_4,
            p714_0,p714_1,p714_2,p714_3,p714_4,
            p715_0,p715_1,p715_2,p715_3,p715_4,
            p716_0,p716_1,p716_2,p716_3,p716_4,
            p717_0,p717_1,p717_2,p717_3,p717_4):
    
    lista_datos_abarrotes = []

    if n_clicks > 0:
        if len(data['lista_prod']) == 0:
            return {'lista_prod':lista_datos_abarrotes, 'alerta':dbc.Alert('Registre las pestañas anteriores.', color='danger')}
        else:
            lista_datos_abarrotes.clear()
            lista_datos_abarrotes.append(p701_0)
            lista_datos_abarrotes.append(p701_1)
            lista_datos_abarrotes.append(p701_2)
            lista_datos_abarrotes.append(p701_3)
            lista_datos_abarrotes.append(p701_4)
            
            lista_datos_abarrotes.append(p702_0)
            lista_datos_abarrotes.append(p702_1)
            lista_datos_abarrotes.append(p702_2)
            lista_datos_abarrotes.append(p702_3)
            lista_datos_abarrotes.append(p702_4)
            
            lista_datos_abarrotes.append(p703_0)
            lista_datos_abarrotes.append(p703_1)
            lista_datos_abarrotes.append(p703_2)
            lista_datos_abarrotes.append(p703_3)
            lista_datos_abarrotes.append(p703_4)
            
            lista_datos_abarrotes.append(p704_0)
            lista_datos_abarrotes.append(p704_1)
            lista_datos_abarrotes.append(p704_2)
            lista_datos_abarrotes.append(p704_3)
            lista_datos_abarrotes.append(p704_4)
            
            lista_datos_abarrotes.append(p705_0)
            lista_datos_abarrotes.append(p705_1)
            lista_datos_abarrotes.append(p705_2)
            lista_datos_abarrotes.append(p705_3)
            lista_datos_abarrotes.append(p705_4)
            
            lista_datos_abarrotes.append(p706_0)
            lista_datos_abarrotes.append(p706_1)
            lista_datos_abarrotes.append(p706_2)
            lista_datos_abarrotes.append(p706_3)
            lista_datos_abarrotes.append(p706_4)
            
            lista_datos_abarrotes.append(p707_0)
            lista_datos_abarrotes.append(p707_1)
            lista_datos_abarrotes.append(p707_2)
            lista_datos_abarrotes.append(p707_3)
            lista_datos_abarrotes.append(p707_4)
            
            lista_datos_abarrotes.append(p708_0)
            lista_datos_abarrotes.append(p708_1)
            lista_datos_abarrotes.append(p708_2)
            lista_datos_abarrotes.append(p708_3)
            lista_datos_abarrotes.append(p708_4)
            
            lista_datos_abarrotes.append(p709_0)
            lista_datos_abarrotes.append(p709_1)
            lista_datos_abarrotes.append(p709_2)
            lista_datos_abarrotes.append(p709_3)
            lista_datos_abarrotes.append(p709_4)
            
            lista_datos_abarrotes.append(p710_0)
            lista_datos_abarrotes.append(p710_1)
            lista_datos_abarrotes.append(p710_2)
            lista_datos_abarrotes.append(p710_3)
            lista_datos_abarrotes.append(p710_4)
            
            lista_datos_abarrotes.append(p711_0)
            lista_datos_abarrotes.append(p711_1)
            lista_datos_abarrotes.append(p711_2)
            lista_datos_abarrotes.append(p711_3)
            lista_datos_abarrotes.append(p711_4)
            
            lista_datos_abarrotes.append(p712_0)
            lista_datos_abarrotes.append(p712_1)
            lista_datos_abarrotes.append(p712_2)
            lista_datos_abarrotes.append(p712_3)
            lista_datos_abarrotes.append(p712_4)
            
            lista_datos_abarrotes.append(p713_0)
            lista_datos_abarrotes.append(p713_1)
            lista_datos_abarrotes.append(p713_2)
            lista_datos_abarrotes.append(p713_3)
            lista_datos_abarrotes.append(p713_4)
            
            lista_datos_abarrotes.append(p714_0)
            lista_datos_abarrotes.append(p714_1)
            lista_datos_abarrotes.append(p714_2)
            lista_datos_abarrotes.append(p714_3)
            lista_datos_abarrotes.append(p714_4)
            
            lista_datos_abarrotes.append(p715_0)
            lista_datos_abarrotes.append(p715_1)
            lista_datos_abarrotes.append(p715_2)
            lista_datos_abarrotes.append(p715_3)
            lista_datos_abarrotes.append(p715_4)
            
            lista_datos_abarrotes.append(p716_0)
            lista_datos_abarrotes.append(p716_1)
            lista_datos_abarrotes.append(p716_2)
            lista_datos_abarrotes.append(p716_3)
            lista_datos_abarrotes.append(p716_4)
            
            lista_datos_abarrotes.append(p717_0)
            lista_datos_abarrotes.append(p717_1)
            lista_datos_abarrotes.append(p717_2)
            lista_datos_abarrotes.append(p717_3)
            lista_datos_abarrotes.append(p717_4)
        
            #df1 = pd.DataFrame(lista_datos_abarrotes)
            #df1.to_excel('lista_datos_abarrotes.xlsx')
            return {'lista_prod':lista_datos_abarrotes, 'alerta':dbc.Alert('Registro Nº ' + str(data1['lista_prod'][0]) + ', \
					satisfactorio. Continúe en la siguiente pestaña', color='success')}



@app.callback(
Output(component_id='lista_datos_abarrotes', component_property='children'),
Input(component_id='lista_datos_abarrotes_store', component_property='data')
)


def output8_1(data):
	if data is None:
		raise PreventUpdate
	return data['alerta']






# CALLBACK RUBRO COMIDAS PREPARADAS
###################################

@app.callback(
     Output(component_id='lista_datos_comidas_store', component_property='data'),
     Input(component_id='guardar_tab9', component_property='n_clicks'),
    [State(component_id='lista_datos_abarrotes_store', component_property='data'),
     State(component_id='lista_datos_store', component_property='data'),
     State(component_id='p801_0', component_property='value'),
     State(component_id='p801_1', component_property='value'),
     State(component_id='p801_2', component_property='value'),
     State(component_id='p801_3', component_property='value'),
     State(component_id='p801_4', component_property='value'),
     
     State(component_id='p802_0', component_property='value'),
     State(component_id='p802_1', component_property='value'),
     State(component_id='p802_2', component_property='value'),
     State(component_id='p802_3', component_property='value'),
     State(component_id='p802_4', component_property='value'),
     
     State(component_id='p803_0', component_property='value'),
     State(component_id='p803_1', component_property='value'),
     State(component_id='p803_2', component_property='value'),
     State(component_id='p803_3', component_property='value'),
     State(component_id='p803_4', component_property='value'),
     
     State(component_id='p804_0', component_property='value'),
     State(component_id='p804_1', component_property='value'),
     State(component_id='p804_2', component_property='value'),
     State(component_id='p804_3', component_property='value'),
     State(component_id='p804_4', component_property='value'),
     
     State(component_id='p805_0', component_property='value'),
     State(component_id='p805_1', component_property='value'),
     State(component_id='p805_2', component_property='value'),
     State(component_id='p805_3', component_property='value'),
     State(component_id='p805_4', component_property='value')
     ]
)


def output9(n_clicks,data,data1,
            p801_0,p801_1,p801_2,p801_3,p801_4,
            p802_0,p802_1,p802_2,p802_3,p802_4,
            p803_0,p803_1,p803_2,p803_3,p803_4,
            p804_0,p804_1,p804_2,p804_3,p804_4,
            p805_0,p805_1,p805_2,p805_3,p805_4):
    
    lista_datos_comidas = []
    
    if n_clicks > 0:
        if len(data['lista_prod']) == 0:
            return (dbc.Alert('Registre las pestañas anteriores.', color='danger'))
        else:
            lista_datos_comidas.clear()
            lista_datos_comidas.append(p801_0)
            lista_datos_comidas.append(p801_1)
            lista_datos_comidas.append(p801_2)
            lista_datos_comidas.append(p801_3)
            lista_datos_comidas.append(p801_4)
            
            lista_datos_comidas.append(p802_0)
            lista_datos_comidas.append(p802_1)
            lista_datos_comidas.append(p802_2)
            lista_datos_comidas.append(p802_3)
            lista_datos_comidas.append(p802_4)
            
            lista_datos_comidas.append(p803_0)
            lista_datos_comidas.append(p803_1)
            lista_datos_comidas.append(p803_2)
            lista_datos_comidas.append(p803_3)
            lista_datos_comidas.append(p803_4)
            
            lista_datos_comidas.append(p804_0)
            lista_datos_comidas.append(p804_1)
            lista_datos_comidas.append(p804_2)
            lista_datos_comidas.append(p804_3)
            lista_datos_comidas.append(p804_4)
            
            lista_datos_comidas.append(p805_0)
            lista_datos_comidas.append(p805_1)
            lista_datos_comidas.append(p805_2)
            lista_datos_comidas.append(p805_3)
            lista_datos_comidas.append(p805_4)
        
            #df1 = pd.DataFrame(lista_datos_comidas)
            #df1.to_excel('lista_datos_comidas.xlsx')
            return {'lista_prod':lista_datos_comidas, 'alerta':dbc.Alert('Registro Nº ' + str(data1['lista_prod'][0]) + ', \
					satisfactorio. Continúe en la siguiente pestaña', color='success')}


@app.callback(
Output(component_id='lista_datos_comidas', component_property='children'),
Input(component_id='lista_datos_comidas_store', component_property='data')
)

def output9_1(data):
	if data is None:
		raise PreventUpdate
	return data['alerta']





# CALLBACK RUBRO OTROS
###################################

@app.callback(
     Output(component_id='lista_datos_otros_store', component_property='data'),
     Input(component_id='guardar_tab10', component_property='n_clicks'),
    [State(component_id='lista_datos_comidas_store', component_property='data'),
     State(component_id='lista_datos_store', component_property='data'),
     State(component_id='p901_0', component_property='value'),
     State(component_id='p901_1', component_property='value'),
     State(component_id='p901_2', component_property='value'),
     State(component_id='p901_3', component_property='value'),
     State(component_id='p901_4', component_property='value'),
     
     State(component_id='p902_0', component_property='value'),
     State(component_id='p902_1', component_property='value'),
     State(component_id='p902_2', component_property='value'),
     State(component_id='p902_3', component_property='value'),
     State(component_id='p902_4', component_property='value'),
     
     State(component_id='p903_0', component_property='value'),
     State(component_id='p903_1', component_property='value'),
     State(component_id='p903_2', component_property='value'),
     State(component_id='p903_3', component_property='value'),
     State(component_id='p903_4', component_property='value'),
     
     State(component_id='p904_0', component_property='value'),
     State(component_id='p904_1', component_property='value'),
     State(component_id='p904_2', component_property='value'),
     State(component_id='p904_3', component_property='value'),
     State(component_id='p904_4', component_property='value'),
     
     State(component_id='p905_0', component_property='value'),
     State(component_id='p905_1', component_property='value'),
     State(component_id='p905_2', component_property='value'),
     State(component_id='p905_3', component_property='value'),
     State(component_id='p905_4', component_property='value')
     ]
)


def output10(n_clicks,data,data1,
             p901_0,p901_1,p901_2,p901_3,p901_4,
             p902_0,p902_1,p902_2,p902_3,p902_4,
             p903_0,p903_1,p903_2,p903_3,p903_4,
             p904_0,p904_1,p904_2,p904_3,p904_4,
             p905_0,p905_1,p905_2,p905_3,p905_4):
    
    lista_datos_otros = []

    if n_clicks > 0:
        if len(data['lista_prod']) == 0:
            return {'lista_prod':lista_datos_otros, 'alerta':dbc.Alert('Registre las pestañas anteriores.', color='danger')}
        else:
            lista_datos_otros.clear()
            lista_datos_otros.append(p901_0)
            lista_datos_otros.append(p901_1)
            lista_datos_otros.append(p901_2)
            lista_datos_otros.append(p901_3)
            lista_datos_otros.append(p901_4)
            
            lista_datos_otros.append(p902_0)
            lista_datos_otros.append(p902_1)
            lista_datos_otros.append(p902_2)
            lista_datos_otros.append(p902_3)
            lista_datos_otros.append(p902_4)
            
            lista_datos_otros.append(p903_0)
            lista_datos_otros.append(p903_1)
            lista_datos_otros.append(p903_2)
            lista_datos_otros.append(p903_3)
            lista_datos_otros.append(p903_4)
            
            lista_datos_otros.append(p904_0)
            lista_datos_otros.append(p904_1)
            lista_datos_otros.append(p904_2)
            lista_datos_otros.append(p904_3)
            lista_datos_otros.append(p904_4)
            
            lista_datos_otros.append(p905_0)
            lista_datos_otros.append(p905_1)
            lista_datos_otros.append(p905_2)
            lista_datos_otros.append(p905_3)
            lista_datos_otros.append(p905_4)
        
            #df1 = pd.DataFrame(lista_datos_otros)
            #df1.to_excel('lista_datos_otros.xlsx')
            return {'lista_prod':lista_datos_otros, 'alerta':dbc.Alert('Registro Nº ' + str(data1['lista_prod'][0]) + ', \
					satisfactorio.', color='success')}


@app.callback(
Output(component_id='lista_datos_otros', component_property='children'),
Input(component_id='lista_datos_otros_store', component_property='data')
)

def output10_1(data):
	if data is None:
		raise PreventUpdate
	return data['alerta']





#####################################
### CALLBACKS PRODUCTOS: RUBRO CARNE
#####################################

##Extra
@app.callback(
    Output('p7_1', 'disabled'),
    Input('p7', 'value'))

def mostrar_preg_p7_1(valor):
    if valor == 'hogar y negocio':
        return False
    else:
        return True



@app.callback(
    [Output('p101_1', 'disabled'),
     Output('p101_2', 'disabled'),
     Output('p101_3', 'disabled'),
     Output('p101_4', 'disabled')],
    [Input('p101_0', 'value')])

def mostrar_preg_p11_1(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p102_1', 'disabled'),
     Output('p102_2', 'disabled'),
     Output('p102_3', 'disabled'),
     Output('p102_4', 'disabled')],
    [Input('p102_0', 'value')])

def mostrar_preg_p11_2(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p103_1', 'disabled'),
     Output('p103_2', 'disabled'),
     Output('p103_3', 'disabled'),
     Output('p103_4', 'disabled')],
    [Input('p103_0', 'value')])

def mostrar_preg_p11_3(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p104_1', 'disabled'),
     Output('p104_2', 'disabled'),
     Output('p104_3', 'disabled'),
     Output('p104_4', 'disabled')],
    [Input('p104_0', 'value')])

def mostrar_preg_p11_4(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False





# CALLBACKS PRODUCTOS: RUBRO PESCADOS

@app.callback(
    [Output('p201_1', 'disabled'),
     Output('p201_2', 'disabled'),
     Output('p201_3', 'disabled'),
     Output('p201_4', 'disabled')],
    [Input('p201_0', 'value')])

def mostrar_preg_p12_1(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p202_1', 'disabled'),
     Output('p202_2', 'disabled'),
     Output('p202_3', 'disabled'),
     Output('p202_4', 'disabled')],
    [Input('p202_0', 'value')])

def mostrar_preg_p12_2(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False





# CALLBACKS PRODUCTOS: RUBRO AVES

@app.callback(
    [Output('p301_1', 'disabled'),
     Output('p301_2', 'disabled'),
     Output('p301_3', 'disabled'),
     Output('p301_4', 'disabled')],
    [Input('p301_0', 'value')])

def mostrar_preg_p13_1(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p302_1', 'disabled'),
     Output('p302_2', 'disabled'),
     Output('p302_3', 'disabled'),
     Output('p302_4', 'disabled')],
    [Input('p302_0', 'value')])

def mostrar_preg_p13_2(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p303_1', 'disabled'),
     Output('p303_2', 'disabled'),
     Output('p303_3', 'disabled'),
     Output('p303_4', 'disabled')],
    [Input('p303_0', 'value')])

def mostrar_preg_p13_3(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p304_1', 'disabled'),
     Output('p304_2', 'disabled'),
     Output('p304_3', 'disabled'),
     Output('p304_4', 'disabled')],
    [Input('p304_0', 'value')])

def mostrar_preg_p13_4(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False




# CALLBACKS PRODUCTOS: RUBRO EMBUTIDOS

@app.callback(
    [Output('p401_1', 'disabled'),
     Output('p401_2', 'disabled'),
     Output('p401_3', 'disabled'),
     Output('p401_4', 'disabled')],
    [Input('p401_0', 'value')])

def mostrar_preg_p14_1(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False




# CALLBACKS PRODUCTOS: RUBRO VERDURAS

@app.callback(
    [Output('p501_1', 'disabled'),
     Output('p501_2', 'disabled'),
     Output('p501_3', 'disabled'),
     Output('p501_4', 'disabled')],
    [Input('p501_0', 'value')])

def mostrar_preg_p15_1(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p502_1', 'disabled'),
     Output('p502_2', 'disabled'),
     Output('p502_3', 'disabled'),
     Output('p502_4', 'disabled')],
    [Input('p502_0', 'value')])

def mostrar_preg_p15_2(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p503_1', 'disabled'),
     Output('p503_2', 'disabled'),
     Output('p503_3', 'disabled'),
     Output('p503_4', 'disabled')],
    [Input('p503_0', 'value')])

def mostrar_preg_p15_3(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p504_1', 'disabled'),
     Output('p504_2', 'disabled'),
     Output('p504_3', 'disabled'),
     Output('p504_4', 'disabled')],
    [Input('p504_0', 'value')])

def mostrar_preg_p15_4(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p505_1', 'disabled'),
     Output('p505_2', 'disabled'),
     Output('p505_3', 'disabled'),
     Output('p505_4', 'disabled')],
    [Input('p505_0', 'value')])

def mostrar_preg_p15_5(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p506_1', 'disabled'),
     Output('p506_2', 'disabled'),
     Output('p506_3', 'disabled'),
     Output('p506_4', 'disabled')],
    [Input('p506_0', 'value')])

def mostrar_preg_p15_6(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p507_1', 'disabled'),
     Output('p507_2', 'disabled'),
     Output('p507_3', 'disabled'),
     Output('p507_4', 'disabled')],
    [Input('p507_0', 'value')])

def mostrar_preg_p15_7(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p508_1', 'disabled'),
     Output('p508_2', 'disabled'),
     Output('p508_3', 'disabled'),
     Output('p508_4', 'disabled')],
    [Input('p508_0', 'value')])

def mostrar_preg_p15_8(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p509_1', 'disabled'),
     Output('p509_2', 'disabled'),
     Output('p509_3', 'disabled'),
     Output('p509_4', 'disabled')],
    [Input('p509_0', 'value')])

def mostrar_preg_p15_9(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p510_1', 'disabled'),
     Output('p510_2', 'disabled'),
     Output('p510_3', 'disabled'),
     Output('p510_4', 'disabled')],
    [Input('p510_0', 'value')])

def mostrar_preg_p15_10(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False



@app.callback(
    [Output('p511_1', 'disabled'),
     Output('p511_2', 'disabled'),
     Output('p511_3', 'disabled'),
     Output('p511_4', 'disabled')],
    [Input('p511_0', 'value')])

def mostrar_preg_p15_11(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False



@app.callback(
    [Output('p512_1', 'disabled'),
     Output('p512_2', 'disabled'),
     Output('p512_3', 'disabled'),
     Output('p512_4', 'disabled')],
    [Input('p512_0', 'value')])

def mostrar_preg_p15_12(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False

@app.callback(
    [Output('p513_1', 'disabled'),
     Output('p513_2', 'disabled'),
     Output('p513_3', 'disabled'),
     Output('p513_4', 'disabled')],
    [Input('p513_0', 'value')])

def mostrar_preg_p15_13(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False




# CALLBACKS PRODUCTOS: RUBRO FRUTAS

@app.callback(
    [Output('p601_1', 'disabled'),
     Output('p601_2', 'disabled'),
     Output('p601_3', 'disabled'),
     Output('p601_4', 'disabled')],
    [Input('p601_0', 'value')])

def mostrar_preg_p16_1(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p602_1', 'disabled'),
     Output('p602_2', 'disabled'),
     Output('p602_3', 'disabled'),
     Output('p602_4', 'disabled')],
    [Input('p602_0', 'value')])

def mostrar_preg_p16_2(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p603_1', 'disabled'),
     Output('p603_2', 'disabled'),
     Output('p603_3', 'disabled'),
     Output('p603_4', 'disabled')],
    [Input('p603_0', 'value')])

def mostrar_preg_p16_3(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p604_1', 'disabled'),
     Output('p604_2', 'disabled'),
     Output('p604_3', 'disabled'),
     Output('p604_4', 'disabled')],
    [Input('p604_0', 'value')])

def mostrar_preg_p16_4(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p605_1', 'disabled'),
     Output('p605_2', 'disabled'),
     Output('p605_3', 'disabled'),
     Output('p605_4', 'disabled')],
    [Input('p605_0', 'value')])

def mostrar_preg_p16_5(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p606_1', 'disabled'),
     Output('p606_2', 'disabled'),
     Output('p606_3', 'disabled'),
     Output('p606_4', 'disabled')],
    [Input('p606_0', 'value')])

def mostrar_preg_p16_6(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p607_1', 'disabled'),
     Output('p607_2', 'disabled'),
     Output('p607_3', 'disabled'),
     Output('p607_4', 'disabled')],
    [Input('p607_0', 'value')])

def mostrar_preg_p16_7(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p608_1', 'disabled'),
     Output('p608_2', 'disabled'),
     Output('p608_3', 'disabled'),
     Output('p608_4', 'disabled')],
    [Input('p608_0', 'value')])

def mostrar_preg_p16_8(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p609_1', 'disabled'),
     Output('p609_2', 'disabled'),
     Output('p609_3', 'disabled'),
     Output('p609_4', 'disabled')],
    [Input('p609_0', 'value')])

def mostrar_preg_p16_9(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False





# CALLBACKS PRODUCTOS: RUBRO ABARROTES

@app.callback(
    [Output('p701_1', 'disabled'),
     Output('p701_2', 'disabled'),
     Output('p701_3', 'disabled'),
     Output('p701_4', 'disabled')],
    [Input('p701_0', 'value')])

def mostrar_preg_p17_1(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p702_1', 'disabled'),
     Output('p702_2', 'disabled'),
     Output('p702_3', 'disabled'),
     Output('p702_4', 'disabled')],
    [Input('p702_0', 'value')])

def mostrar_preg_p17_2(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p703_1', 'disabled'),
     Output('p703_2', 'disabled'),
     Output('p703_3', 'disabled'),
     Output('p703_4', 'disabled')],
    [Input('p703_0', 'value')])

def mostrar_preg_p17_3(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p704_1', 'disabled'),
     Output('p704_2', 'disabled'),
     Output('p704_3', 'disabled'),
     Output('p704_4', 'disabled')],
    [Input('p704_0', 'value')])

def mostrar_preg_p17_4(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p705_1', 'disabled'),
     Output('p705_2', 'disabled'),
     Output('p705_3', 'disabled'),
     Output('p705_4', 'disabled')],
    [Input('p705_0', 'value')])

def mostrar_preg_p17_5(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p706_1', 'disabled'),
     Output('p706_2', 'disabled'),
     Output('p706_3', 'disabled'),
     Output('p706_4', 'disabled')],
    [Input('p706_0', 'value')])

def mostrar_preg_p17_6(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p707_1', 'disabled'),
     Output('p707_2', 'disabled'),
     Output('p707_3', 'disabled'),
     Output('p707_4', 'disabled')],
    [Input('p707_0', 'value')])

def mostrar_preg_p17_7(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p708_1', 'disabled'),
     Output('p708_2', 'disabled'),
     Output('p708_3', 'disabled'),
     Output('p708_4', 'disabled')],
    [Input('p708_0', 'value')])

def mostrar_preg_p17_8(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p709_1', 'disabled'),
     Output('p709_2', 'disabled'),
     Output('p709_3', 'disabled'),
     Output('p709_4', 'disabled')],
    [Input('p709_0', 'value')])

def mostrar_preg_p17_9(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p710_1', 'disabled'),
     Output('p710_2', 'disabled'),
     Output('p710_3', 'disabled'),
     Output('p710_4', 'disabled')],
    [Input('p710_0', 'value')])

def mostrar_preg_p17_10(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False



@app.callback(
    [Output('p711_1', 'disabled'),
     Output('p711_2', 'disabled'),
     Output('p711_3', 'disabled'),
     Output('p711_4', 'disabled')],
    [Input('p711_0', 'value')])

def mostrar_preg_p17_11(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False



@app.callback(
    [Output('p712_1', 'disabled'),
     Output('p712_2', 'disabled'),
     Output('p712_3', 'disabled'),
     Output('p712_4', 'disabled')],
    [Input('p712_0', 'value')])

def mostrar_preg_p17_12(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p713_1', 'disabled'),
     Output('p713_2', 'disabled'),
     Output('p713_3', 'disabled'),
     Output('p713_4', 'disabled')],
    [Input('p713_0', 'value')])

def mostrar_preg_p17_13(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False



@app.callback(
    [Output('p714_1', 'disabled'),
     Output('p714_2', 'disabled'),
     Output('p714_3', 'disabled'),
     Output('p714_4', 'disabled')],
    [Input('p714_0', 'value')])

def mostrar_preg_p17_14(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p715_1', 'disabled'),
     Output('p715_2', 'disabled'),
     Output('p715_3', 'disabled'),
     Output('p715_4', 'disabled')],
    [Input('p715_0', 'value')])

def mostrar_preg_p17_15(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p716_1', 'disabled'),
     Output('p716_2', 'disabled'),
     Output('p716_3', 'disabled'),
     Output('p716_4', 'disabled')],
    [Input('p716_0', 'value')])

def mostrar_preg_p17_16(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False



@app.callback(
    [Output('p717_1', 'disabled'),
     Output('p717_2', 'disabled'),
     Output('p717_3', 'disabled'),
     Output('p717_4', 'disabled')],
    [Input('p717_0', 'value')])

def mostrar_preg_p17_17(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False




# CALLBACKS PRODUCTOS: RUBRO COMIDAS

@app.callback(
    [Output('p801_1', 'disabled'),
     Output('p801_2', 'disabled'),
     Output('p801_3', 'disabled'),
     Output('p801_4', 'disabled')],
    [Input('p801_0', 'value')])

def mostrar_preg_p18_1(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p802_1', 'disabled'),
     Output('p802_2', 'disabled'),
     Output('p802_3', 'disabled'),
     Output('p802_4', 'disabled')],
    [Input('p802_0', 'value')])

def mostrar_preg_p18_2(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p803_1', 'disabled'),
     Output('p803_2', 'disabled'),
     Output('p803_3', 'disabled'),
     Output('p803_4', 'disabled')],
    [Input('p803_0', 'value')])

def mostrar_preg_p18_3(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p804_1', 'disabled'),
     Output('p804_2', 'disabled'),
     Output('p804_3', 'disabled'),
     Output('p804_4', 'disabled')],
    [Input('p804_0', 'value')])

def mostrar_preg_p18_4(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p805_1', 'disabled'),
     Output('p805_2', 'disabled'),
     Output('p805_3', 'disabled'),
     Output('p805_4', 'disabled')],
    [Input('p805_0', 'value')])

def mostrar_preg_p18_5(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False





# CALLBACKS PRODUCTOS: RUBRO OTROS

@app.callback(
    [Output('p901_1', 'disabled'),
     Output('p901_2', 'disabled'),
     Output('p901_3', 'disabled'),
     Output('p901_4', 'disabled')],
    [Input('p901_0', 'value')])

def mostrar_preg_p19_1(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p902_1', 'disabled'),
     Output('p902_2', 'disabled'),
     Output('p902_3', 'disabled'),
     Output('p902_4', 'disabled')],
    [Input('p902_0', 'value')])

def mostrar_preg_p19_2(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p903_1', 'disabled'),
     Output('p903_2', 'disabled'),
     Output('p903_3', 'disabled'),
     Output('p903_4', 'disabled')],
    [Input('p903_0', 'value')])

def mostrar_preg_p19_3(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p904_1', 'disabled'),
     Output('p904_2', 'disabled'),
     Output('p904_3', 'disabled'),
     Output('p904_4', 'disabled')],
    [Input('p904_0', 'value')])

def mostrar_preg_p19_4(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False


@app.callback(
    [Output('p905_1', 'disabled'),
     Output('p905_2', 'disabled'),
     Output('p905_3', 'disabled'),
     Output('p905_4', 'disabled')],
    [Input('p905_0', 'value')])

def mostrar_preg_p19_5(valor):
    if valor == 'no':
        return True, True, True, True
    else:
        return False, False, False, False



#################################################




# CALLBACK BOTONES
############################

# TAB DATOS GENERALES

@app.callback(Output('guardar_tab1', 'disabled'),
              Input('guardar_tab1', 'n_clicks'))

def disable_guardar1(on_off):
    return on_off

@app.callback(Output('guardar_tab1', 'n_clicks'),
              Input('corregir_tab1', 'n_clicks'))

def enable_guardar1(on_off):
    return 0



# TAB RUBROS CARNES

@app.callback(Output('guardar_tab2', 'disabled'),
              Input('guardar_tab2', 'n_clicks'))

def disable_guardar2(on_off):
    return on_off

@app.callback(Output('guardar_tab2', 'n_clicks'),
              Input('corregir_tab2', 'n_clicks'))

def enable_guardar2(on_off):
    return 0




# TAB RUBROS PESCADOS

@app.callback(Output('guardar_tab3', 'disabled'),
              Input('guardar_tab3', 'n_clicks'))

def disable_guardar3(on_off):
    return on_off

@app.callback(Output('guardar_tab3', 'n_clicks'),
              Input('corregir_tab3', 'n_clicks'))

def enable_guardar3(on_off):
    return 0




# TAB RUBROS AVES

@app.callback(Output('guardar_tab4', 'disabled'),
              Input('guardar_tab4', 'n_clicks'))

def disable_guardar4(on_off):
    return on_off

@app.callback(Output('guardar_tab4', 'n_clicks'),
              Input('corregir_tab4', 'n_clicks'))

def enable_guardar4(on_off):
    return 0



# TAB RUBROS EMBUTIDOS

@app.callback(Output('guardar_tab5', 'disabled'),
              Input('guardar_tab5', 'n_clicks'))

def disable_guardar5(on_off):
    return on_off

@app.callback(Output('guardar_tab5', 'n_clicks'),
              Input('corregir_tab5', 'n_clicks'))

def enable_guardar5(on_off):
    return 0



# TAB RUBROS VERDURAS

@app.callback(Output('guardar_tab6', 'disabled'),
              Input('guardar_tab6', 'n_clicks'))

def disable_guardar6(on_off):
    return on_off

@app.callback(Output('guardar_tab6', 'n_clicks'),
              Input('corregir_tab6', 'n_clicks'))

def enable_guardar6(on_off):
    return 0



# TAB RUBROS FRUTAS

@app.callback(Output('guardar_tab7', 'disabled'),
              Input('guardar_tab7', 'n_clicks'))

def disable_guardar7(on_off):
    return on_off

@app.callback(Output('guardar_tab7', 'n_clicks'),
              Input('corregir_tab7', 'n_clicks'))

def enable_guardar7(on_off):
    return 0



# TAB RUBROS ABARROTES

@app.callback(Output('guardar_tab8', 'disabled'),
              Input('guardar_tab8', 'n_clicks'))

def disable_guardar8(on_off):
    return on_off

@app.callback(Output('guardar_tab8', 'n_clicks'),
              Input('corregir_tab8', 'n_clicks'))

def enable_guardar8(on_off):
    return 0



# TAB RUBROS COMIDAS

@app.callback(Output('guardar_tab9', 'disabled'),
              Input('guardar_tab9', 'n_clicks'))

def disable_guardar9(on_off):
    return on_off

@app.callback(Output('guardar_tab9', 'n_clicks'),
              Input('corregir_tab9', 'n_clicks'))

def enable_guardar9(on_off):
    return 0


# TAB RUBROS OTROS

@app.callback(Output('guardar_tab10', 'disabled'),
              Input('guardar_tab10', 'n_clicks'))

def disable_guardar10(on_off):
    return on_off

@app.callback(Output('guardar_tab10', 'n_clicks'),
              Input('corregir_tab10', 'n_clicks'))

def enable_guardar10(on_off):
    return 0





@app.callback(
    Output(component_id='resultado', component_property='children'),
    Input(component_id='finalizar', component_property='n_clicks'),
    [State(component_id='lista_datos_store', component_property='data'),
     State(component_id='lista_datos_carne_store', component_property='data'),
     State(component_id='lista_datos_pescados_store', component_property='data'),
     State(component_id='lista_datos_aves_store', component_property='data'),
     State(component_id='lista_datos_embutidos_store', component_property='data'),
     State(component_id='lista_datos_verduras_store', component_property='data'),
     State(component_id='lista_datos_frutas_store', component_property='data'),
     State(component_id='lista_datos_abarrotes_store', component_property='data'),
     State(component_id='lista_datos_comidas_store', component_property='data'),
     State(component_id='lista_datos_otros_store', component_property='data')
     ]
)



def finalizar(n_clicks,data1,data2,data3,data4,data5,data6,data7,data8,data9,data10):
    
    lista_total = []
    
    if n_clicks > 0:
        if len(data10['lista_prod']) == 0:
            return dbc.Alert('Registre las pestañas anteriores.', color='danger')
        else:
            lista_total.append(data1['lista_prod'])
            lista_total.append(data2['lista_prod'])
            lista_total.append(data3['lista_prod'])
            lista_total.append(data4['lista_prod'])
            lista_total.append(data5['lista_prod'])
            lista_total.append(data6['lista_prod'])
            lista_total.append(data7['lista_prod'])
            lista_total.append(data8['lista_prod'])
            lista_total.append(data9['lista_prod'])
            lista_total.append(data10['lista_prod'])
            
            flat = flatten(lista_total)
            grabar_reg(lista_total=flat,cols=columnas,vals=val_num)
            #df1 = pd.DataFrame(flat)
            #df1.to_excel('lista_total.xlsx')
            return dbc.Alert('Registro Nº ' + str(data1['lista_prod'][0]) + ', finalizado con éxito.', color='info')



@app.callback(Output('finalizar', 'disabled'),
              Input('finalizar', 'n_clicks'))

def disable_finalizar(on_off):
    return on_off



'''                     
@app.callback(
	[Output(component_id='lista_datos_store', component_property='clear_data'),
     Output(component_id='lista_datos_carne_store', component_property='clear_data'),
     Output(component_id='lista_datos_pescados_store', component_property='clear_data'),
     Output(component_id='lista_datos_aves_store', component_property='clear_data'),
     Output(component_id='lista_datos_embutidos_store', component_property='clear_data'),
     Output(component_id='lista_datos_verduras_store', component_property='clear_data'),
     Output(component_id='lista_datos_frutas_store', component_property='clear_data'),
     Output(component_id='lista_datos_abarrotes_store', component_property='clear_data'),
     Output(component_id='lista_datos_comidas_store', component_property='clear_data'),
     Output(component_id='lista_datos_otros_store', component_property='clear_data')
     ],
    Input(component_id='reset_button', component_property='n_clicks') 
)

def clear(reset_clicks):
    #Clears memory
    if reset_clicks > 0:
        return True, True, True, True, True, True, True, True, True, True

'''  


@app.callback(Output('finalizar', 'n_clicks'),
              Input('corregir_finalizar', 'n_clicks'))

def enable_guardar_fin(on_off):
    return 0



# CORRER EL APLICATIVO

if __name__ == '__main__':
    app.run_server(debug=False)

    
#if __name__ == '__main__':
#    app.server(host='0.0.0.0', port=8080, debug=False)



























