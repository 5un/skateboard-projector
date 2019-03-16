from pyfirmata import Arduino, util
board = Arduino('/dev/ttyACM0')

it = util.Iterator(board)
it.start()
board.analog[0].enable_reporting()
value = board.analog[0].read()
print(value)