#!/usr/bin/env python



import argparse
import io
import time
import picamera
import datetime
import os



def main(*argv):
   """
       Defines arguments: time before and after, and mouse/trial to be tested

   """
   
   
   parser = argparse.ArgumentParser(description='seconds before and after lever is pressed.')
   parser.add_argument('before', type=int, help='seconds to record before.')
   parser.add_argument('after', type=int, help='seconds to record after.')
   parser.add_argument('folder', type=str, default=".", help = 'mouse to be tested')
   args = parser.parse_args(argv[1:])
   folder = args.folder
   x = args.before
   y = args.after
   z = x + y
   import RPi.GPIO as GPIO
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(27, GPIO.IN, GPIO.PUD_UP)

   with picamera.PiCamera(framerate=90) as camera:
      try:
         if not os.path.exists(folder):
            os.makedirs(folder)
         stream = picamera.PiCameraCircularIO(camera, seconds = z)
         while True:
            stream.seek(0)
            camera.start_recording(stream, format= 'h264', splitter_port=1)
            GPIO.wait_for_edge(27, GPIO.FALLING)
            camera.wait_recording(y, splitter_port=1)
            camera.stop_recording()
            '''stream.seek(z*90)'''
            for frame in stream.frames:
               if frame.frame_type == picamera.PiVideoFrameType.sps_header:
                  stream.seek(frame.position)
                  break
               # Gives the time specifications that you want, in
               # year-month-day_hour:minute:second:microsecond
            j = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f')
            with io.open(os.path.join(folder, 'mouse_press' + str(j).replace(
                  ' ', '_') + '.h264'), 'wb') as output:
               data = stream.read()
               if not data:
                  break
               output.write(data)
      except KeyboardInterrupt:
         print("Program is now ending session.")
                 


   return 0
