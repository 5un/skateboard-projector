from pyfirmata import Arduino, util

class SensorHelper():

  def __init__(self, appState):
    self.appState = appState

    self.board = Arduino('/dev/ttyACM0')

    it = util.Iterator(board)
    it.start()
    self.board.analog[0].enable_reporting()
    self.board.analog[1].enable_reporting()
    self.board.analog[2].enable_reporting()
    self.acceleration = (0.0, 0.0, 0.0)
    self.pressure = (0.0, 0.0)

  def tick(self, seconds):
    xr = board.analog[0].read()
    yr = board.analog[1].read()
    zr = board.analog[2].read()
    if (xr is not None) and (yr is not None) and (zr is not None):
      self.acceleration[0] = (xr - 0.5) * 3.0
      self.acceleration[1] = (yr - 0.5) * 3.0
      self.acceleration[2] = (zr - 0.5) * 3.0
      appState.acceleration = self.acceleration
    
    board.pass_time(seconds)

    # Also read sensor




