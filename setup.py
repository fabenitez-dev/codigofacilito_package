from pathlib import Path # > 3.6
from setuptools import setup
"""
Este archivo es para que PyPi pueda clasificar la libreria correctamente y para que 
pip pueda instalarla de forma apropiada
"""

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text() #lee archivo README.md

VERSION = '0.0.1' # versionar como se desee 
DESCRIPTION = 'Consume API de codigofacilito.com'
PACKAGE_NAME = 'pack_cfacilito'
AUTHOR = 'Francisco Alejandro Benitez'
EMAIL = 'fabenitez.dev@hotmail.com'
GITHUB_URL = 'https://github.com/fabenitez-dev/codigofacilito_package' #URL de github del paquete creado

setup(
    name = PACKAGE_NAME,
    packages = [DESCRIPTION],
    version = VERSION,
    license='MIT',
    description = DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    author = AUTHOR,
    author_email = EMAIL,
    url = GITHUB_URL,
    keywords = [],
    install_requires=[ 
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)