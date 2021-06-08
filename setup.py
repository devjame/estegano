import os
from setuptools import setup, find_packages

setup(
	name="estegano",
	version="1.0.0",
	author="The Eagle Team",
	author_email="devjames79@gmail.com",
	description="Aplicação com base na tecnica de Esteganografia.",
	license="BSD",
	url="https://github.com/devjame/estegano",
	packages=find_packages(where='estegano'),
	entry_points={
		'gui_scripts': ['estegano = estegano.app:main']
	},
	classifiers=[
		"Development Status :: 3 - Alpha",
		"License :: OSI Approved :: BSD License",
	],
	install_requires=["numpy==1.20.1", "opencv-contrib-python==4.5.1.48", "opencv-python==4.5.1.48", "Pillow==8.1.2"],
)
