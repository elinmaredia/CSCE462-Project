from gpiozero import MotionSensor
from picamera import PiCamera
import requests
from signal import pause
from filestack import Client
from time import sleep

sleep(3)
pir = MotionSensor(4)
camera = PiCamera()
client = Client("AQJWfxpMTQgWW677VUPKTz")


while True:       
    def send_alert():
        camera.capture('motionImage.jpg')
        new_filelink = client.upload(filepath="motionImage.jpg")
        print(new_filelink.url)
        r = requests.post("https://maker.ifttt.com/trigger/motionDetect/with/key/e3An1mZ_PLo9i78j5NwUqs2XfDz-kUyvFRZ47Ta9ORr", json={"value1" : new_filelink.url})
        if r.status_code == 200:
            print('Alert Sent!')
        else:
            print("ERROR")

    while True:
        if pir.motion_detected:
            print('Motion detected!')
            send_alert()
            camera.capture('motionImage.jpg')
            break
    sleep(7)
