import os
from dotenv import load_dotenv
from pathlib import Path


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

upload_folder = Path('.') / 'uploads'

db = os.getenv('DATABASE_NAME')
user = os.getenv('DATABASE_USER')
password = os.getenv('DATABASE_PASS')
host = os.getenv('DATABASE_HOST')
port = os.getenv('DATABASE_PORT')





# Flask-Mail
servidor_email = os.getenv('MAIL_SERVER')
puerto_email = os.getenv('MAIL_PORT')
tls_mail = os.getenv('MAIL_USE_TLS')
ssl_mail = os.getenv('MAIL_USE_SSL')
mail_username = os.getenv('MAIL_USERNAME')
mail_password = os.getenv('MAIL_PASSWORD')
correo_envio_automatico = os.getenv('MAIL_DEFAULT_SENDER')

nombre_app = os.getenv('USER_APP_NAME')
habiliar_validacion_correo = os.getenv('USER_ENABLE_EMAIL')
usuario_nombre = os.getenv('USER_ENABLE_USERNAME')
correo_usuario = os.getenv('USER_EMAIL_SENDER_EMAIL')
nombre_usuario_envia = os.getenv('USER_EMAIL_SENDER_NAME')

print(servidor_email)
print (puerto_email)
apiKey=os.getenv('SENDGRID_API_KEY')
print(apiKey)

class Config(object):
    SQLALCHEMY_DATABASE_URI = f'postgres://{user}:{password}@{host}:{port}/{db}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED = True
    SECRET_KEY = 'JoseAlonsoArangurenmartinez12345678912345678912345625'

    #UPLOAD_FOLDER = upload_folder
    MAIL_SERVER = servidor_email
    MAIL_PORT = puerto_email
    MAIL_USE_SSL = ssl_mail
    MAIL_USE_TLS = tls_mail
    MAIL_USERNAME = mail_username
    MAIL_PASSWORD = mail_password
    MAIL_DEFAULT_SENDER=correo_envio_automatico

    USER_APP_NAME=nombre_app
    USER_ENABLE_EMAIL=habiliar_validacion_correo
    USER_ENABLE_USERNAME=usuario_nombre
    USER_EMAIL_SENDER_EMAIL=correo_usuario
    USER_EMAIL_SENDER_NAME=nombre_usuario_envia

#

