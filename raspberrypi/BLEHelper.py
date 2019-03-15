from pybleno import *
import sys
import signal
from SkateboardCharacteristic import *

class BLEHelper():

    def __init__(self, appState):
        self.appState = appState
        self.bleno = Bleno()
        self.bleno.on('stateChange', self.onStateChange)
        self.bleno.on('advertisingStart', self.onAdvertisingStart)
        self.bleno.start()

    def onStateChange(self, state):
        print('on -> stateChange: ' + state);

        if (state == 'poweredOn'):
            self.bleno.startAdvertising('echo', ['ec00'])
        else:
            self.bleno.stopAdvertising();

    def onAdvertisingStart(self, error):
        print('on -> advertisingStart: ' + ('error ' + error if error else 'success'));

        if not error:
            self.bleno.setServices([
                BlenoPrimaryService({
                    'uuid': 'ec00',
                    'characteristics': [ 
                        SkateboardCharacteristic('ec0F', self.appState)
                    ]
                })
            ])

    def start(self):
        self.bleno.start()

    def stop(self):
        self.bleno.stopAdvertising()
        self.bleno.disconnect()



