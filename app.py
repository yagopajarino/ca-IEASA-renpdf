import pandas as pd
import tabula
import numpy as np
from unidecode import unidecode
import re
import os
pd.options.display.float_format = '{:,.2f}'.format
import warnings
warnings.simplefilter("ignore")
import shutil

def extraccion(pdf,medidas):
    df = tabula.read_pdf(pdf,pages=1,multiple_tables=False,pandas_options={"header":None,"decimal":","},\
                       area=[medidas[0],medidas[1],medidas[2],medidas[3]],relative_area=False)
    return df[0]

def datos_descripcion(ruta,medidas_descripcion):
    df = extraccion(ruta,med_descripcion)
    reemplazos = {"(tierra.*del.*fuego)":"TDF",
                  "(santa.*cruz)":"SCR",
                  "(neuquen)":"NQN",
                  "(chubut)":"CHU",
                  "nan":""}
    texto = ""
    for y in range(df.shape[0]):
        for x in range(df.shape[1]):
            texto += str(df.loc[y,x]) + " "
        texto = texto.lower()
    for x in list(reemplazos.keys()):
        texto = re.sub(x,reemplazos[x],texto)
    rex = [".*(enero).*",
       ".*(febrero).*",
       ".*(marzo).*",
       ".*(abril).*",
       ".*(mayo).*",
       ".*(junio).*",
       ".*(julio).*",
       ".*(agosto).*",
       ".*(septiembre).*",
       ".*(octubre).*",
       ".*(noviembre).*",
       ".*(diciembre).*"]
    
    for x in range(len(rex)):
        busqueda = re.findall(rex[x],texto)
        if len(busqueda)>0:
            mes = x+1
    rex_año = "(20\d{2})[^A]"
    año = re.findall(rex_año,texto)[0]
    rex_cuenca_1p = "cuenca:\s*(\w{2,})"
    cuenca = re.findall(rex_cuenca_1p,texto)[0]
    if len(re.findall("(f\w*do.*fid)",texto))>0:
        concepto = 1
    else: concepto = 0
    return mes, int(año), cuenca.upper(), concepto


med_descripcion = [230,123,420,362]

root = input("Ingrese directorio de archivos: ")
des_root = root + '\\' + "output" + "\\"
docs = os.listdir(path=root)
os.makedirs(des_root, exist_ok = True)


rex = re.compile("(\d{4}A\d*)")
rextd = re.compile("^(\w{2})")

if ".DS_Store" in docs:
    docs.remove(".DS_Store")
        

n = 0
urls = []
for x in docs:
    n += 1
    url = str(root + "\\" + x)
    try:
        mes, año, cca, concepto = datos_descripcion(url, med_descripcion)
        nro_doc = re.findall(rex,x)[0]
        tipo_doc = re.findall(rextd,x)[0]
        nombre = "{}.{} {} {} {}".format(año,str(mes).zfill(2),cca,tipo_doc,nro_doc)
        new_url = "{}{}.pdf".format(des_root,nombre)
        shutil.copy(url,new_url)
        print("{} OK".format(n))
    except:
        new_url = "{}{}.pdf".format(des_root,x)
        shutil.copy(url,new_url)
        print("{} error".format(n))