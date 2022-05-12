import os

count = 0

while (True):
  with open('output.txt') as f:
    lines = f.readlines()
    lines = lines

    if (lines[-1] == 'Stopping...\n'):
      print("Stopped")
      break

    if (lines[-1] == "Detected 'porcupine'\n" and lines.count("Detected 'porcupine'\n") > count):
      print("Wakeword Detected")
      count += 1
      print(count)
      print("Calling Requstangle Service")
      os.system('rosservice call /request_angle true')

  f.close()
