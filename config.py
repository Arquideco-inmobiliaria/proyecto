#esta llave sirve para manejar datos de sesion 
class Config:
    SECRET_KEY = "CIUJE10021%5KSXF"


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = "localhost"
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'arquideco'

config = {
    "development" : DevelopmentConfig
}