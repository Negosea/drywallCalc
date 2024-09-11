from setuptools import setup, find_packages

setup(
    name='drywallCalc',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Liste as dependências aqui, se houver
    ],
    entry_points={
        'console_scripts': [
            'drywallcalc=main:main',  # Altere para o ponto de entrada correto
        ],
    },
)
