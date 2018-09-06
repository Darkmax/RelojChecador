try:
    import hashlib
    from pyfingerprint.pyfingerprint import PyFingerprint
except:
    pass

import sqlite3

class CheckUser:

    def __init__(self):
        self.conn = sqlite3.connect('./DB/reloj_checador.db')
        self.c = self.conn.cursor()

        try:
            self.f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
            if (self.f.verifyPassword() == False):
                raise ValueError('The given fingerprint sensor password is wrong!')
        except Exception as e:
            print('The fingerprint sensor could not be initialized!')
            print('Exception message: ' + str(e))

    def __del__(self):
        self.close_connection()

    def getTimeRead(self):
        self.c.execute('SELECT finger_read_time FROM Configuration WHERE idConfig = 1')
        return self.c.fetchone()[0]

    def get_user(self, finger_id):
        self.c.execute('SELECT * FROM Users WHERE index_finger=?', (finger_id,))
        user = self.c.fetchone()
        if user is not None:
            return [user[0], user[1], user[2], user[3]]
        else:
            return 'error'

    def check_user(self):

        ##si no leyo imagen regresar
        if self.f.readImage() == False:
            return [False, -1]
        else:
            self.f.convertImage(0x01)
            result = self.f.searchTemplate()
            positionNumber = result[0]
            accuracyScore = result[1]
            
            ##Si encontro el usuario
            if accuracyScore >= 50:
                user = self.get_user(positionNumber)
                return [True] + user
            ##No encontro el usuario
            else:
                return [True, -1]

    def addFinger(self, state):
        print(state)

    def close_connection(self):
        self.c.close()
        self.conn.close()
