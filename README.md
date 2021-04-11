# Portada

![](portada.png)

# Instalación de Dependencias

```bash
1. pip install virtualenv
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
4. pip install flask flask_mysql_connector shortuuid
```

## ó instalar Requerimientos

```bash
4.  pip3 install -r requirements.txt
```

## Script Base De Datos

```bash
CREATE TABLE
    `db_enlaces_cortos`.enlaces
    (
        id           INT AUTO_INCREMENT,
        url          VARCHAR(4000) NOT NULL,
        enlace_corto VARCHAR(45) NOT NULL,
        PRIMARY KEY (id)
    );
```
