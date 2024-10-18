from picrawler import Picrawler
from robot_hat import TTS, Music
from bleak import BleakScanner
import time

crawler = Picrawler()
tts = TTS()
music = Music()

# Bluetooth MAC address of your phone
phone_mac_address = "20:20:08:59:27:13"

def find_phone():
    devices = BleakScanner.discover()
    return any(device.address == phone_mac_address for device in devices)

def main():
    speed = 80
    while True:
        devices = BleakScanner.discover()
        phone_detected = any(device.address == phone_mac_address for device in devices)
        if phone_detected:
            print("Phone detected! Moving towards it.")
            tts.say("Phone detected! Moving towards it.")
            crawler.do_action('forward', 1, speed)
        else:
            print("Phone not detected. Scanning...")
            tts.say("Phone not detected. Scanning...")
            crawler.do_action('turn left', 1, speed)
        time.sleep(2)

if __name__ == "__main__":
    main()
