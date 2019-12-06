from win10toast import ToastNotifier
import sounddevice as sd
import numpy as np

# One-time initialization
toaster = ToastNotifier()

duration = 10  # seconds

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10

    # Set volume threshold here
    if int(volume_norm) > 165:         
        toaster.show_toast("Someone is calling!", "Check your phone! The microphone has detected a loud noise!", threaded=True,
        icon_path=None, duration=3)

        print("Loud sound detected: ")
        print(volume_norm)

while True:
    with sd.Stream(callback=print_sound):
        sd.sleep(duration * 1000)
    print("loop")