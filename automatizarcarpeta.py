import os 
import sys
import shutil
import time
from random import randint

ruta_descargas = "C:\\CarpetaParaOrdenar\\"
ext_texto = ['.docx','.txt','.doc','.pdf','.pptx']
ext_foto = ['.png','.jpg','.jpeg','.gif']
ext_video = ['.mov','.mp4']


def ordenar(archivo, ext):
	for i in ext_texto:
		if ext == i:
			shutil.move(ruta_descargas + archivo, ruta_descargas + 'Texto')
	
	for i in ext_foto:
		if ext == i:
			shutil.move(ruta_descargas + archivo, ruta_descargas + 'Fotos')

	for i in ext_video:
		if ext == i:
			shutil.move(ruta_descargas + archivo, ruta_descargas + 'Video')

	if ext != '':
		shutil.move(ruta_descargas + archivo, ruta_descargas + 'Otros')

def main():
	for archivo in os.listdir(ruta_descargas):
		nombre_archivo, ext = os.path.splitext(archivo)
		ordenar(archivo, ext)
main()
