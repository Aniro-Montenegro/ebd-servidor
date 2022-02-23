# ebd-servidor

## Projeto em Python para servidor de Escola Dominical

### Projeto em Python para servidor de Escola Dominical

Este projeto tem o intuito de criar um servidor que servirá o aplicativo para administração da Escola Dominical

### Requimerents

pip freeze > requirements.txt

### Virtual Env

py -3 -m venv .venv

.venv\Scripts\activate

.venv\Scripts\deactivate.bat

### Pip Gerenciamento de pacotes

pip install requests- cria o arquivo requeriments

pip install -r requirements.txt - instala as bibliotecas do projeto

### Flake8

pip install flake8

pip freeze > requirements-dev.txt

pip install -r requirements-dev.txt

flake8 - avalia o codigo

## Para Inatalar

````commandline
py -3 -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
````

### Para Conferir qualidade do código

````commandline
flake8
````

# Upgrade de Dependencias

pip uninstall [requests] - Desistala biblioteca especifica(usas sem conchetes)

pip freeze

pip install requests==2.27.1 - Instala biblioteca especifica