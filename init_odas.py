import os
import time

os.system("./matrix-odas &")
time.sleep(5)
os.system("./odaslive -vc ../config/matrix-demo/matrix_creator.cfg")
