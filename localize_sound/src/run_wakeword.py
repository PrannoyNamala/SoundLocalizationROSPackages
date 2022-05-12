import subprocess, shlex, os
command = 'ppn-mic-demo --access_key "ZhJ7+UU+KNS+QjZypA5/m3vcNuJZ9KUwnkt3mztOu/LVzAe7RUsPpg==" --keywords porcupine --audio_device_index 5'
workingdirectory = "/home/pi"

os.system(command + ' > output.txt')
