##librerias Importadas
import minimalmodbus
import time
########## END ######

## Funcion para cargar lista meterlist() y pollear datos
def modbusCall(meterlist):
    for Items in meterlist:
        Values = dict()
        device = minimalmodbus.Instrument('/dev/ttyUSB0',Items['id'],Items['protocol'])
        device.serial.timeout = 1
        device.serial.baudrate = Items['baud']
        Values['meter'] = Items['MeterName']
        Values['timestamp'] = time.strftime("%m-%d-%Y %H:%M:%S")
        for vars in Items['Variables']:
            if vars[2] == 16:
                Values[vars[0]]= 0
            elif vars[2] == 32:
                Values[vars[0]] = device.read_long(vars[1],vars[3],vars[4])/vars[5]
    return Values
############## END ##############

###### Ensamble lista meterlist ###############################
meterlist = list()
serialMeter = dict()
ipath = '/home/pi/Desktop/'
serialMeter = {'MeterName': 'Escritorio', 'id':8, 'baud': 19200, 'protocol':'rtu', 'Variables':list()}
serialMeter['Variables'].append(('Voltage',0,32,3,False,10.0,0))
serialMeter['Variables'].append(('Current',2,32,3,False,100.0,0))
serialMeter['Variables'].append(('Power',4,32,3,False,100.0,0))
serialMeter['Variables'].append(('Power',18,32,3,False,100.0,0))
meterlist.append(serialMeter)
############################### END ###############################

print modbusCall(meterlist)
