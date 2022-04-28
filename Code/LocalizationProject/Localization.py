from tuning import Tuning
import usb.core
import usb.util
import time
import calculateLocation


def localization():
    x = 0
    y = 0

    dev = tuple(usb.core.find(find_all=True, idVendor=0x2886, idProduct=0x0018))
    print(len(dev))

    if dev:

        Mic_tuning_0 = Tuning(dev[0]) #Long Cable
        Mic_tuning_1 = Tuning(dev[2]) #Short Cable
        #print (Mic_tuning_0.direction)
        #print (Mic_tuning_1.direction)
        x, y = calculateLocation.calculate_distance(6, Mic_tuning_0.direction, Mic_tuning_1.direction)
        #print(x,y)
        return (x, y)

"""
        while True:
            try:

                print(Mic_tuning_0.direction)
                print(Mic_tuning_1.direction)
                x, y = calculateLocation.calculate_distance(6, Mic_tuning_0.direction, Mic_tuning_1.direction)
                print(x, y)
                time.sleep(1)

            except KeyboardInterrupt:
                break
"""
#localization()