import time
import threading

class FingerReader:

    def ReadFinger(self):
        time_out = 2
        timer = 0

        while(timer < time_out):
            timer += 1
            time.sleep(1)

        return True