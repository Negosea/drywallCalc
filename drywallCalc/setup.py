from setuptools import setup, find_packages

setup(
    name='drywallCalc',
    version='0.1',
    packages=find_packages(),  # Encontra todos os pacotes e subpacotes
    install_requires=[
        # Liste as dependências aqui, se houver
    ],
    entry_points={
        'console_scripts': [
            'drywallcalc=drywallCalc.main:main',  # Altere para o ponto de entrada correto
        ],
    },
    include_package_data=True,
    description='Calculadora para cálculos de drywall',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Marcos Sea',
    author_email='tecnosteelframe@gmail.com',
    url='https://github.com/Negosea/drywallCalc',
    license='MIT',  # Ou a licença que você escolher
)
