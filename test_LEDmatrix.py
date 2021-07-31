import board
import busio as io
import adafruit_ht16k33.matrix
import time

i2c = io.I2C(board.SCL, board.SDA)
matrix = adafruit_ht16k33.matrix.Matrix16x8(i2c)

def ledsoff():
    matrix.fill(0)

def neutralexp():
    matrix.fill(0)
    
    matrix[2, 1] = 1
    matrix[3, 1] = 1
    matrix[4, 1] = 1
    matrix[11, 1] = 1
    matrix[12, 1] = 1
    matrix[13, 1] = 1
    matrix[1, 2] = 1
    matrix[2, 2] = 1
    matrix[3, 2] = 1
    matrix[4, 2] = 1
    matrix[5, 2] = 1
    matrix[10, 2] = 1
    matrix[11, 2] = 1
    matrix[12, 2] = 1
    matrix[13, 2] = 1
    matrix[14, 2] = 1
    matrix[1, 3] = 1
    matrix[2, 3] = 1
    matrix[3, 3] = 1
    matrix[4, 3] = 1
    matrix[5, 3] = 1
    matrix[10, 3] = 1
    matrix[11, 3] = 1
    matrix[12, 3] = 1
    matrix[13, 3] = 1
    matrix[14, 3] = 1
    matrix[1, 4] = 1
    matrix[2, 4] = 1
    matrix[3, 4] = 1
    matrix[4, 4] = 1
    matrix[5, 4] = 1
    matrix[10, 4] = 1
    matrix[11, 4] = 1
    matrix[12, 4] = 1
    matrix[13, 4] = 1
    matrix[14, 4] = 1
    matrix[1, 5] = 1
    matrix[2, 5] = 1
    matrix[3, 5] = 1
    matrix[4, 5] = 1
    matrix[5, 5] = 1
    matrix[10, 5] = 1
    matrix[11, 5] = 1
    matrix[12, 5] = 1
    matrix[13, 5] = 1
    matrix[14, 5] = 1
    matrix[2, 6] = 1
    matrix[3, 6] = 1
    matrix[4, 6] = 1
    matrix[11, 6] = 1
    matrix[12, 6] = 1
    matrix[13, 6] = 1
    
def surpriseexp():
    matrix.fill(0)
    
    matrix[1, 0] = 1
    matrix[2, 0] = 1
    matrix[3, 0] = 1
    matrix[4, 0] = 1
    matrix[5, 0] = 1
    matrix[10, 0] = 1
    matrix[11, 0] = 1
    matrix[12, 0] = 1
    matrix[13, 0] = 1
    matrix[14, 0] = 1
    matrix[0, 1] = 1
    matrix[1, 1] = 1
    matrix[2, 1] = 1
    matrix[3, 1] = 1
    matrix[4, 1] = 1
    matrix[5, 1] = 1
    matrix[6, 1] = 1
    matrix[9, 1] = 1
    matrix[10, 1] = 1
    matrix[11, 1] = 1
    matrix[12, 1] = 1
    matrix[13, 1] = 1
    matrix[14, 1] = 1
    matrix[15, 1] = 1
    matrix[0, 2] = 1
    matrix[1, 2] = 1
    matrix[2, 2] = 1
    matrix[3, 2] = 1
    matrix[4, 2] = 1
    matrix[5, 2] = 1
    matrix[6, 2] = 1
    matrix[9, 2] = 1
    matrix[10, 2] = 1
    matrix[11, 2] = 1
    matrix[12, 2] = 1
    matrix[13, 2] = 1
    matrix[14, 2] = 1
    matrix[15, 2] = 1
    matrix[0, 3] = 1
    matrix[1, 3] = 1
    matrix[2, 3] = 1
    matrix[3, 3] = 1
    matrix[4, 3] = 1
    matrix[5, 3] = 1
    matrix[6, 3] = 1
    matrix[9, 3] = 1
    matrix[10, 3] = 1
    matrix[11, 3] = 1
    matrix[12, 3] = 1
    matrix[13, 3] = 1
    matrix[14, 3] = 1
    matrix[15, 3] = 1
    matrix[0, 4] = 1
    matrix[1, 4] = 1
    matrix[2, 4] = 1
    matrix[3, 4] = 1
    matrix[4, 4] = 1
    matrix[5, 4] = 1
    matrix[6, 4] = 1
    matrix[9, 4] = 1
    matrix[10, 4] = 1
    matrix[11, 4] = 1
    matrix[12, 4] = 1
    matrix[13, 4] = 1
    matrix[14, 4] = 1
    matrix[15, 4] = 1
    matrix[0, 5] = 1
    matrix[1, 5] = 1
    matrix[2, 5] = 1
    matrix[3, 5] = 1
    matrix[4, 5] = 1
    matrix[5, 5] = 1
    matrix[6, 5] = 1
    matrix[9, 5] = 1
    matrix[10, 5] = 1
    matrix[11, 5] = 1
    matrix[12, 5] = 1
    matrix[13, 5] = 1
    matrix[14, 5] = 1
    matrix[15, 5] = 1
    matrix[0, 6] = 1
    matrix[1, 6] = 1
    matrix[2, 6] = 1
    matrix[3, 6] = 1
    matrix[4, 6] = 1
    matrix[5, 6] = 1
    matrix[6, 6] = 1
    matrix[9, 6] = 1
    matrix[10, 6] = 1
    matrix[11, 6] = 1
    matrix[12, 6] = 1
    matrix[13, 6] = 1
    matrix[14, 6] = 1
    matrix[15, 6] = 1
    matrix[1, 7] = 1
    matrix[2, 7] = 1
    matrix[3, 7] = 1
    matrix[4, 7] = 1
    matrix[5, 7] = 1
    matrix[10, 7] = 1
    matrix[11, 7] = 1
    matrix[12, 7] = 1
    matrix[13, 7] = 1
    matrix[14, 7] = 1

    
def joyexp():
    matrix.fill(0)
    
    matrix[1, 4] = 1
    matrix[5, 4] = 1
    matrix[10, 4] = 1
    matrix[14, 4] = 1
    matrix[1, 5] = 1
    matrix[2, 5] = 1
    matrix[3, 5] = 1
    matrix[4, 5] = 1
    matrix[5, 5] = 1
    matrix[10, 5] = 1
    matrix[11, 5] = 1
    matrix[12, 5] = 1
    matrix[13, 5] = 1
    matrix[14, 5] = 1
    matrix[2, 6] = 1
    matrix[3, 6] = 1
    matrix[4, 6] = 1
    matrix[11, 6] = 1
    matrix[12, 6] = 1
    matrix[13, 6] = 1
    
def angerexp():
    matrix.fill(0)
    
    matrix[2, 1] = 1
    matrix[3, 1] = 1
    matrix[4, 1] = 1
    matrix[5, 1] = 1
    matrix[10, 1] = 1
    matrix[11, 1] = 1
    matrix[12, 1] = 1
    matrix[13, 1] = 1
    matrix[1, 2] = 1
    matrix[2, 2] = 1
    matrix[3, 2] = 1
    matrix[4, 2] = 1
    matrix[5, 2] = 1
    matrix[10, 2] = 1
    matrix[11, 2] = 1
    matrix[12, 2] = 1
    matrix[13, 2] = 1
    matrix[14, 2] = 1
    matrix[1, 3] = 1
    matrix[2, 3] = 1
    matrix[3, 3] = 1
    matrix[4, 3] = 1
    matrix[11, 3] = 1
    matrix[12, 3] = 1
    matrix[13, 3] = 1
    matrix[14, 3] = 1
    matrix[1, 4] = 1
    matrix[2, 4] = 1
    matrix[3, 4] = 1
    matrix[12, 4] = 1
    matrix[13, 4] = 1
    matrix[14, 4] = 1
    matrix[1, 5] = 1
    matrix[2, 5] = 1
    matrix[13, 5] = 1
    matrix[14, 5] = 1
    matrix[1, 6] = 1
    matrix[14, 6] = 1
    
def tiredexp():
    matrix.fill(0)
    
    # left eye
    matrix[1, 4] = 1
    matrix[2, 4] = 1
    matrix[3, 4] = 1
    matrix[4, 4] = 1
    matrix[5, 4] = 1
    
    # right eye
    matrix[10, 4] = 1
    matrix[11, 4] = 1
    matrix[12, 4] = 1
    matrix[13, 4] = 1
    matrix[14, 4] = 1
    
matrix.fill(1)
time.sleep(1)
matrix.fill(0)
time.sleep(1)
neutralexp()
time.sleep(1)
surpriseexp()
time.sleep(1)
joyexp()
time.sleep(1)
angerexp()
time.sleep(1)
tiredexp()
time.sleep(1)
matrix.fill(0)
