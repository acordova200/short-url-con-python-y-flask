

# Portada

![](portada.png)

# Docker

```bash
Primera vez:
docker-compose up --build -d

Parar contenedores:
docker-compose down

Iniciar contenedores:
docker-compose up -d
```

# Python 3.9.2 requerido

## Instalación de Python con Version Manager

```bash
Mac:
https://github.com/pyenv/pyenv

Windows:
https://github.com/pyenv-win/pyenv-win

pyenv install 3.9.2

pyenv global 3.9.2
```

## ALTERNATIVA: conda

```bash
https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html

conda create -n env python=3.9.2

conda activate env

```


# Instalación de Dependencias

```bash
python -m ensurepip --upgrade
pip3 install --upgrade pip
```

```bash
1. pip3 install virtualenv
```

```bash
2. py -m venv env
```

```bash
Windows
3. .\env\Scripts\activate
Mac
3. source env/bin/activate
```

```bash
4. pip install Flask==1.1.2 flask-mysql-connector==1.1.0 shortuuid==1.0.1
```

## ó instalar Requerimientos

```bash
4.  pip3 install -r requirements.txt
```

    
## Script Base De Datos

```bash
CREATE DATABASE db_enlaces_cortos;


CREATE TABLE
    `db_enlaces_cortos`.ENLACES
    (
        id           INT AUTO_INCREMENT,
        url          VARCHAR(4000) NOT NULL,
        enlace_corto VARCHAR(45) NOT NULL,
        PRIMARY KEY (id)
    );
```
