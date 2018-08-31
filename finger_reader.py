# try:
#     import hashlib
#     from pyfingerprint.pyfingerprint import PyFingerprint
# except:
#     pass

import sqlite3

# try:
#     f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
#
#     if (f.verifyPassword() == False):
#         raise ValueError('The given fingerprint sensor password is wrong!')
#
#     ##Ya que ya inicializo el sensor
#     ##Intentamos leer el dedo
#     try:
#
#         ##Esperamos a que el usuario ponga el dedo
#         while(f.readImage() == False):
#             pass
#
#         ##Convertimos la imagen del dedo a caracteristicas para poder leerlo
#         f.convertImage(0x01)
#
#         ##Buscamos si ya existe el dedo en la base de datos
#         result = f.searchTemplate()
#
#         positionNumber = result[0]
#         accuracyScore = result[1]
#
#         ##En caso que el dedo no exista indicarlo
#         print('Usuario: ' + positionNumber)
#
#
# except Exception as e:
#     print('The fingerprint sensor could not be initialized!')
#     print('Exception message: ' + str(e))
#     #exit(1)

class CheckUser:

    def __init__(self):
        self.conn = sqlite3.connect('./DB/reloj_checador.db')
        self.c = self.conn.cursor()

        # try:
        #     f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
        #     if (f.verifyPassword() == False):
        #         raise ValueError('The given fingerprint sensor password is wrong!')
        # except Exception as e:
        #     print('The fingerprint sensor could not be initialized!')
        #     print('Exception message: ' + str(e))

    def check_name(self, name):
        self.c.execute('SELECT * FROM Users WHERE name=?', (name,))
        user = self.c.fetchone()

        if user is not None:
            return user[1]
        else:
            return 'error'

    def check_user(self, tk):
        pass

    def close_connection(self):
        self.c.close()
        self.conn.close()
