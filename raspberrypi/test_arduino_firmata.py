from pyfirmata import Arduino, util
import time
board = Arduino('/dev/ttyACM0')

it = util.Iterator(board)
it.start()
board.analog[0].enable_reporting()
board.analog[1].enable_reporting()
board.analog[2].enable_reporting()
while True:
	xr = board.analog[0].read()
	yr = board.analog[1].read()
	zr = board.analog[2].read()
	if (xr is not None) and (yr is not None) and (zr is not None):
		xg = (xr - 0.5) * 3.0
		yg = (yr - 0.5) * 3.0
		zg = (zr - 0.5) * 3.0
		print(xg, yg, zg)
	board.pass_time(0.5)
	time.sleep(0.5)
