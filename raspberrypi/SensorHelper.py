from pyfirmata import Arduino, util

class SensorHelper():

  def __init__(self, appState):
    self.appState = appState

    self.board = Arduino('/dev/ttyACM0')

    it = util.Iterator(self.board)
    it.start()
    self.board.analog[0].enable_reporting()
    self.board.analog[1].enable_reporting()
    self.board.analog[2].enable_reporting()
    self.board.analog[3].enable_reporting()
    self.board.analog[4].enable_reporting()
    self.acceleration = (0.0, 0.0, 0.0)
    self.pressure = (0.0, 0.0)

  def tick(self, seconds):
    xr = self.board.analog[2].read()
    yr = self.board.analog[3].read()
    zr = self.board.analog[4].read()
    f1 = self.board.analog[0].read()
    f2 = self.board.analog[1].read()
    if (xr is not None) and (yr is not None) and (zr is not None):
      xg = (xr - 0.5) * 3.0
      yg = (yr - 0.5) * 3.0
      zg = (zr - 0.5) * 3.0
      self.appState.acceleration = self.acceleration = (xg, yg, zg)
      self.appState.pressure = self.pressure = (f1, f2)
    # self.board.pass_time(seconds)

    # Also read sensor




