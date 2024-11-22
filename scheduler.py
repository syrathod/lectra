import time
import keyboard

class scheduler:
    def schedule():
        print("\n[*] Sleeping...")    

        start_time = time.time()
        timeout = 60*10

        while time.time() - start_time < timeout:
            if keyboard.is_pressed("ctrl+shift"):
                break
            time.sleep(0.1) 

        return