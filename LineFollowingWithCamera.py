import cv2
import numpy as np
import RPi.GPIO as GPIO
import time


def Preprocessing(Img):
    img = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    ret, thr = cv2.threshold(blur, 0, 255, cv2.THRESH_OTSU)
    return thr


def takePictureFromVideo():
    video = cv2.VideoCapture(0)
    while True:
        check,frame = video.read()
        cv2.imshow("Capturing",frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()
    return frame


def FindRouteofLine():
    Image = takePictureFromVideo()
    Image = Preprocessing(Image)
    cv2.imshow('Image', Image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    lengthofImage = len(Image[1,:])
    HeightofImage = len(Image[:,1])
    zeroMatrix,middleofLength=Returnonezero(Image,HeightofImage,lengthofImage)
    centerofBlackline = FindMiddleofBlackLine(zeroMatrix)
    return middleofLength, centerofBlackline


def Returnonezero(Image,HeightofImage,lengthofImage):
    middleofLength = int(lengthofImage/2)
    middleofHeight = int(HeightofImage/2)
    zeroMatrix = np.zeros(lengthofImage-1)
    for i in range(lengthofImage-1):
        if (Image[middleofHeight,i]==Image[middleofHeight,i+1]):
            zeroMatrix[i]=0
        else:
            zeroMatrix[i]=1
    return zeroMatrix,middleofLength




def FindMiddleofBlackLine(zeroMatrix):
    print(zeroMatrix)
    print(len(zeroMatrix))
    begin=0
    end=0
    bool = True
    for i in range(len(zeroMatrix)):
        if ((zeroMatrix[i]==1) and bool):
            begin = i
            bool = False
        elif (zeroMatrix[i]==1):
            end = i
            break)
    pwm2..ChangeDutyCycle(int(rightmotorspeed*100))
    time.sleep((delay))


def main():
    kp = 0.135/300
    ki = 0.03/900
    kd = 0.135/300
    I = 0
    previousError = 0
    initialPower = 0.7
    delay = 0.01
    leftmotorspeed = initialPower
    rightmotorspeed = initialPower
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12,GPIO.OUT)
    GPIO.setmode(13,GPIO.OUT)
    pwm1 = GPIO.PWM(12, 100)
    pwm2 = GPIO.PWM(13, 100)
    while True:
        I,leftmotorspeed,rightmotorspeed,previousError = movement(kp,ki,kd,I,previousError,initialPower,leftmotorspeed,rightmotorspeed)
        motorAction(leftmotorspeed,rightmotorspeed,delay,pwm1,pwm2)


main()