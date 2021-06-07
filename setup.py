import os
from setuptools import setup
from nvpy import nvpy

setup(
	name="estegano",
	version="1.0.0",
	author="The Eagle Team",
	author_email="devjames79@gmail.com",
	description="Aplicação para esconder uma mensagem dentro de uma imagem usando a tecnica da Esteganografia.",
	license="BSD",
	url="https://github.com/cpbotha/nvpy",
	packages=['estegano'],
	entry_points={
		'gui_scripts': ['estegano = estegano.app:main']
	},
	classifiers=[
		"License :: OSI Approved :: BSD License",
	],
)
