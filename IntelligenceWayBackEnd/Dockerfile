# Usa una imagen base de Python
FROM python
 
# Establece el directorio de trabajo en el contenedor
WORKDIR /app
 
# Copia los archivos de requisitos
COPY requirements.txt /app/

# Instala los requisitos
RUN pip install --no-cache-dir -r requirements.txt
 
# Copia el resto de los archivos de la aplicación al contenedor
COPY . /app/
 
# Expone el puerto
EXPOSE 8000
 
# Comando para correr la aplicación Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]