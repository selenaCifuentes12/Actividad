# -*- coding: utf-8 -*-
"""Actividad_n°2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V8Xnl1CetmEmYHXyl7s_cwgBahMW1oT4
"""

import pandas as pd

from google.colab import files
files.upload()

df=pd.read_excel("BaseD.xlsx")

df

OrdenColumnas= pd.DataFrame(df,columns= ["Nombre","Apellido","Departamento","Sección","Matrícula","Salario","Fecha Ingreso"])
OrdenColumnas

Copiadoras=df[df.Sección == "Copiadoras"]
Copiadoras

Impresoras=df[df.Sección == "Impresoras"]
Impresoras

Fax=df[df.Sección == "Fax"]
Fax

SumaSalario=df.Salario.sum()
SumaSalario