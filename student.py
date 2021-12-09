#!/usr/bin python3
from teacher import PiggyParent
import sys
import time

class Piggy(PiggyParent):

    '''
    *************
    SYSTEM SETUP
    *************
    '''

    def __init__(self, addr=8, detect=True):
        PiggyParent.__init__(self) # run the parent constructor

        ''' 
        MAGIC NUMBERS <-- where we hard-code our settings
        '''
        self.LEFT_DEFAULT = 71
        self.RIGHT_DEFAULT = 80
        self.MIDPOINT = 1525  # what servo command (1000-2000) is straight forward for your bot?
        self.set_motor_power(self.MOTOR_LEFT + self.MOTOR_RIGHT, 0)
        self.load_defaults()
        
    def load_defaults(self):
        """Implements the magic numbers defined in constructor"""
        self.set_motor_limits(self.MOTOR_LEFT, self.LEFT_DEFAULT)
        self.set_motor_limits(self.MOTOR_RIGHT, self.RIGHT_DEFAULT)
        self.set_servo(self.SERVO_1, self.MIDPOINT)

    def menu(self):
        """Displays menu dictionary, takes key-input and calls method"""
        ## This is a DICTIONARY, it's a list with custom index values. Python is cool.
        # Please feel free to change the menu and add options.
        print("\n *** MENU ***") 
        menu = {"n": ("Navigate", self.nav),
                "d": ("Dance", self.dance),
                "o": ("Obstacle count", self.obstacle_count),
                "s": ("Shy", self.shy),
                "f": ("Follow", self.follow),
                "c": ("Calibrate", self.calibrate),
                "q": ("Quit", self.quit),
                "s": ("square", self.square),
                "x": ("distance", self.liam),
                "e": ("intermediate movement", self.fwd_w_scan),
                "m": ("maze navigation", self.maze)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = str.lower(input("Your selection: "))
        # activate the item selected
        menu.get(ans, [None, self.quit])[1]()

    '''
    ****************
    STUDENT PROJECTS
    ****************
    '''

    def maze(self):
      stopping_distance = 100
      check_distance = 150
      while True:
        self.fwd()
        time.sleep(0.5)
        if (self.read_distance() >= stopping_distance):
          self.left()
          time.sleep(.75)
          left = self.read_distance()
          self.right()
          time.sleep(1.5)
          right = self.read_distance()

          if (right > left):
            self.fwd()
          
          if (left > right):
            self.left()
            time.sleep(1.5)
            self.fwd()


    def swerve_left(self):
      print ("left")
      self.left(primary = 100, counter = 70)
      time.sleep(1)
      self.right(primary =100, counter = 70)
      time.sleep(1)


    def swerve_right(self):
      print ("right")
      self.right(primary = 100, counter = 70)
      time.sleep(1)
      self.left(primary =100, counter = 70)
      time.sleep(1)

    def fwd_w_scan(self):
      stopping_distance = 100
      check_distance = 150
      
      while True:
        self.fwd()

        self.servo(1000)
        time.sleep(.1)
        left = self.read_distance()
        
        self.servo(2000)
        time.sleep(.1)
        right = self.read_distance()
        
        self.servo(1500)
        time.sleep(.1)
        center = self.read_distance()

        if (left <= stopping_distance):
          self.swerve_left()
        
        elif (right <= stopping_distance):
          self.swerve_right()
        
        elif (center <= stopping_distance):
          self.stop()
          time.sleep(1.5)
          self.liam()

        

    def swerve(self):
      stopping_distance = 200
      check_distance = 300
      right = self.read_distance()
      center = self.read_distance()
      left = self.read_distance()

      while True:
        if self.read_distance() >= stopping_distance:
          self.fwd_w_scan()

        elif self.read_distance() < stopping_distance:
          self.read_distance()
          if (right > left):
            self.right(primary =100, counter = 80)
            time.sleep(1)
            self.left(primary =100, counter = 80)
            time.sleep(1)

          if (right < left):
            self.left(primary =100, counter = 80)
            time.sleep(1)
            self.right(primary =100, counter = 80)
            time.sleep(1)

    def liam(self):
        stopping_distance = 200
        check_distance = 400
      
        if self.read_distance() >= stopping_distance:
          self.fwd()
        elif self.read_distance() < stopping_distance:
          self.stop()
          self.servo(1000)
          time.sleep(.5)
          right = self.read_distance()
          self.servo(2000)
          time.sleep(.5)
          left = self.read_distance()

          if (right > left): 
            self.stop()
            self.right()
            time.sleep(.75)
            self.fwd()
            time.sleep(1.5)
            self.left()
            time.sleep(.75)
            self.fwd()
            time.sleep(2)
            self.left()
            time.sleep(.75)
            self.fwd()
            time.sleep(1.5)
            self.right()
            time.sleep(.75)
            self.servo(self.MIDPOINT)

          elif (right < left): 
            self.stop()
            self.left()
            time.sleep(.75)
            self.fwd()
            time.sleep(1.5)
            self.right()
            time.sleep(.75)
            self.fwd()
            time.sleep(2)
            self.right()
            time.sleep(.75)
            self.fwd()
            time.sleep(1.5)
            self.left()
            time.sleep(.75)
            self.servo(self.MIDPOINT)
            


    
      
      





    def square(self):
      for i in range(4):
        self.fwd()
        time.sleep(3)
        self.stop()
        self.right(primary = 38, counter = -38)
        time.sleep(.75)
        self.stop()

    
    def dance(self):
        """A higher-ordered algorithm to make your robot dance"""
        # TODO: check to see if it's safe before dancing
        if safe_to_dance():
          pass
        # lower-ordered example...
        for i in range (3):
          self.right(primary=100, counter=100)
          time.sleep(1)
          self.stop()
          self.right(primary = 100, counter = -100)
          time.sleep(1)
          self.left(primary = 100, counter = -100)
          time.sleep(1)
          self.back()
          time.sleep(1)
          self.fwd()
          self.right(primary = 100, counter = -1100)
          time.sleep(1)
          self.left(primary = 100, counter = -1100)
          time.sleep(1)
          self.stop()

        

    def safe_to_dance(self):
        """ Does a 360 distance check and returns true if safe """
        pass
        return True

    def shake(self):
        """ Another example move """
        self.deg_fwd(720)
        self.stop()

    def example_move(self):
        """this is an example dance move that should be replaced by student-created content"""
        self.right() # start rotating right
        time.sleep(1) # turn for a second
        self.stop() # stop
        self.servo(1000) # look right
        time.sleep(.15) # give your head time to move
        self.servo(2000) # look left

    def scan(self):
        """Sweep the servo and populate the scan_data dictionary"""
        for angle in range(self.MIDPOINT-350, self.MIDPOINT+350, 3):
            self.servo(angle)
            self.scan_data[angle] = self.read_distance()

    def obstacle_count(self):
        """Does a 360 scan and returns the number of obstacles it sees"""
        pass

    def nav(self):
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("-------- [ Press CTRL + C to stop me ] --------\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        
        # TODO: build self.quick_check() that does a fast, 3-part check instead of read_distance
        while self.read_distance() > 250:  # TODO: fix this magic number
            self.fwd()
            time.sleep(.01)
        self.stop()
        # TODO: scan so we can decide left or right
        # TODO: average the right side of the scan dict
        # TODO: average the left side of the scan dict
        


###########
## MAIN APP
if __name__ == "__main__":  # only run this loop if this is the main file

    p = Piggy()

    if sys.version_info < (3, 0):
        sys.stdout.write("Sorry, requires Python 3.x\n")
        p.quit()

    try:
        while True:  # app loop
            p.menu()

    except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
        p.quit()  
