#!/bin/bash

if [[ -z "$1" ]]; then
    echo -e "Tenés que especificar el método: pipenv o venv"
    echo "Ejemplo: ./setup.sh pipenv"
    exit 1
fi

METHOD="$1"

echo "Actualizando paquetes ..."
sudo apt update

echo "Instalando Python ..."
sudo apt install python3 -y

code .

if [[ "$METHOD" == "pipenv" ]]; then
    echo "Instalando pipenv ... "
    sudo apt install pipenv -y --ignore-missing
    
    echo "Instalando Flask ..."
    pipenv install flask flask_mail
    
    echo "¡Entorno virtual con pipenv creado exitosamente! Usá 'pipenv shell' para activarlo."
    elif [[ "$METHOD" == "venv" ]]; then
    echo "Instalando pip y venv ..."
    sudo apt install python3-pip python3-venv -y
    
    echo "Creando entorno virtual ..."
    python3 -m venv .venv
    
    echo "Activando el entorno ..."
    source .venv/bin/activate
    
    echo "Instalando Flask ..."
    pip install flask flask_mail
    echo "¡Entorno virtual con venv creado exitosamente! Usá 'source .venv/bin/activate' para activarlo."
else
    echo -e "Método no reconocido: $METHOD. Tenés que usar 'pipenv' o 'venv'."
    exit 1
fi