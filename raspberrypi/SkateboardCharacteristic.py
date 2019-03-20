from pybleno import Characteristic
import array
import struct
import sys
import traceback
import json
from builtins import str

class SkateboardCharacteristic(Characteristic):
    
    def __init__(self, uuid, appState):
        Characteristic.__init__(self, {
            'uuid': uuid,
            'properties': ['read', 'write', 'notify'],
            'value': None
          })
        self.appState = appState
        self._value = array.array('B', [0] * 0)
        self._updateValueCallback = None
          
    def onReadRequest(self, offset, callback):
        print('SkateboardCharacteristic - %s - onReadRequest: value = %s' % (self['uuid'], [hex(c) for c in self._value]))
        # TODO send back the app state
        sensorData = {"acceleration": self.appState.acceleration, 
            "pressure": self.appState.pressure}
        callback(Characteristic.RESULT_SUCCESS, json.dumps(sensorData).encode())

    def onWriteRequest(self, data, offset, withoutResponse, callback):
        self._value = data
        
        # hardcoded
        print('SkateboardCharacteristic - %s - onWriteRequest: value = %s' % (self['uuid'], [hex(c) for c in self._value]))
        print('data:', data)
        command = data.decode().split()
        
        if len(command) >= 2:
            if command[0] in ['display', 'displayMode']:
                self.appState.displayMode = command[1]
            if command[0] == 'set':
                if command[1] == 'sensorTrigger':
                    if command[2] == 'on':
                        self.appState.useSensorTriggers = True
                    else command[2] == 'off':
                        self.appState.useSensorTriggers = False
 
        # if self._updateValueCallback:
        #     print('SkateboardCharacteristic - onWriteRequest: notifying');
            
        #     self._updateValueCallback(self._value)
        
        callback(Characteristic.RESULT_SUCCESS)
        
    def onSubscribe(self, maxValueSize, updateValueCallback):
        print('SkateboardCharacteristic - onSubscribe')
        
        self._updateValueCallback = updateValueCallback

    def onUnsubscribe(self):
        print('SkateboardCharacteristic - onUnsubscribe');
        
        self._updateValueCallback = None
