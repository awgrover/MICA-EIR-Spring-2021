import board
import time
from analogio import AnalogIn

vbat_voltage_pin = AnalogIn(board.VOLTAGE_MONITOR)


def get_voltage( pin ):
    return ( pin.value * 3.3 ) / 65536 * 2

while True:
    battery_voltage = round( get_voltage( vbat_voltage_pin ), 2 )

    #check clock battery OK
    clock_battery_status = "NA"

    print( "Main Battery voltage: {}   Clock Battery status: {}".format( battery_voltage, clock_battery_status ) )

    time.sleep( 1 )
