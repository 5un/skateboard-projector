from pyfirmata import Arduino, util
import time
board = Arduino('/dev/ttyACM0')

it = util.Iterator(board)
it.start()
board.analog[0].enable_reporting()
while True:
	value = board.analog[0].read()
	print(value)
	board.pass_time(0.5)
	time.sleep(0.5)
