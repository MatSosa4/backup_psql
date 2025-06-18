# Backup Script

## Uso
1. Edita las variables de entorno:

```py
container_name = "nombre_contenedor"
db_user = "usuario"
db_name = "nombre_base_datos"
backup_dir = "./backups"  # Por si deseas cambiar la carpeta
```

2. Revisa si existe python

```bash
which python3
```

3. Edita la tabla de cronología en Linux (crontab)

```bash
crontab -e
```

4. Asigna el tiempo en el que se ejecutará el script:

```txt
0 2 * * * /usr/bin/python3 /path/backup_postgres.py >> /path/backup.log 2>&1
```

## Restauración
Ya que se utilizará Docker:

1. Crea la base de datos, el nombre no importa.

2. Ejecuta el .sql en el contenedor:

```bash
docker exec -i nombre_de_tu_contenedor_postgres psql -U postgres -d nombre_de_tu_base_de_datos < /path/backup.sql
```
