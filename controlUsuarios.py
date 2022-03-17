from pymongo import MongoClient
import cryptocode

user = 'userusers'
password = 'Users123456'
port = '27017'
key = 'keyroot'

client = MongoClient(f'mongodb://{user}:{password}@localhost:{port}')

database = client['users']
collection = database['registro']


def CreateNewUser():
    name = input('Escribe tu Nombre: ')
    email = input('Escribe tu Email: ')
    contra = input('Escribe tu contrasena: ')
    return {'name': name, 'email': email, 'password': cryptocode.encrypt(contra, key)}

data=CreateNewUser()
collection.insert_one(data)

print('Quieres consulta si un usuario existe')

mailTosend=input('ingresa un correo: ')
doc=collection.find_one({"email":mailTosend})
if doc==None:
    print('Ese usuario no existe')
else:
    #print(doc)
    persona=doc['name']
    print(f'la persona con el email de {mailTosend} se llama: {persona}')