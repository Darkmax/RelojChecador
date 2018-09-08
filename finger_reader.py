try:
    import hashlib
    from pyfingerprint.pyfingerprint import PyFingerprint
except:
    pass

import sqlite3

class Backend:

    def __init__(self):
        '''Start the connection to the DB and init the drivers with the finger reader'''
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

    def getConfigurationTimeRange(self):
        '''Returns the range of time where is considered checkin'''

        self.c.execute('SELECT rango_entrada FROM Configuration WHERE idConfig = 1')
        time_string = self.c.fetchone()[0]
        return time_string.split(';')

    def getExportPath(self):
        '''Method to get path to save the csv files'''

        try:
            self.c.execute('SELECT path_export FROM Configuration WHERE idConfig = 1')
            return self.c.fetchone()[0]
        except Exception as e:
            print('getExportPath method')
            print('Exception message: ' + str(e))

    def getTimeRead(self):
        '''Get from the configuration the time that needs to be on the finger reader sensor'''
        self.c.execute('SELECT finger_read_time FROM Configuration WHERE idConfig = 1')
        return self.c.fetchone()[0]

    def get_user(self, finger_id):
        '''Get user values of the DB'''
        self.c.execute('SELECT * FROM Users WHERE index_finger=? or index_finger2=?',
                       (finger_id, finger_id,))
        user = self.c.fetchone()
        if user is not None:
            return [user[0], user[1], user[2], user[3]]
        else:
            return 'error'

    def addPerson(self, values):
        '''Method to insert person on to the DB'''
        try:
            name = values[0]
            last_name = values[1]
            index_finger = values[2]
            index_finger2 = values[3]
            query = 'INSERT INTO Users (name, last_name, index_finger, index_finger2) VALUES (?, ?, ?, ?)'
            self.c.execute(query, (name, last_name, index_finger, index_finger2))
            self.conn.commit() #insert values

            return True
        except Exception as e:
            print('Exception message: ' + str(e))
            return False

    def check_user(self):
        '''Method to check user finger print on the stored templates'''
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
                print(user)
                return [True,] + user
            ##No encontro el usuario
            else:
                return [True, -1]

    def addFinger(self, state):
        '''Method to add finger print to the store templates'''
        try:
            if self.f.readImage() == False:
                return [False, 1]
            else:
                if state == 1:
                    self.f.convertImage(0x01)
                    result=self.f.searchTemplate()
                    positionNumber = result[0]

                    if positionNumber >= 0:
                        print('Template already exists')
                        return [False, -1] ##return already exist
                    else:
                        print('primera captura bien')
                        return [True, 1] ##ok capture first time
                else:

                    self.f.convertImage(0x02)

                    if self.f.compareCharacteristics() == 0:
                        print('no es el mismo dedo')
                        return [False, 0] ##is not the same finger
                    else:
                        self.f.createTemplate()
                        positionNumber = self.f.storeTemplate()
                        print('Dado en la posicion: ' + str(positionNumber))
                        return [True, positionNumber]

        except Exception as e:
            print('Exception message: ' + str(e))

    def deleteFinger(self, index):
        try:
            return self.f.deleteTemplate(index)
        except Exception as e:
            print('Exception message: ' + str(e))

    def close_connection(self):
        '''Close connection to the DB'''
        self.c.close()
        self.conn.close()
