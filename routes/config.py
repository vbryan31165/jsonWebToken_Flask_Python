from distutils.debug import DEBUG


class Developmentconfig():
    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    MYSQL_PASSWORD=''
    MYSQL_DB='jsonWebToken_Flask_python'

config={
    'development': Developmentconfig
}