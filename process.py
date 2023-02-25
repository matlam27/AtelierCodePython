### ====================================================================================================
### IMPORTS
### ====================================================================================================
import arcade
from utils import *
import math

class Process:
    ### ====================================================================================================
    ### PARAMETERS
    ### ====================================================================================================
    SCREEN_WIDTH = int(1920 * 0.75)
    SCREEN_HEIGHT = int(1080 * 0.75)

    ### ====================================================================================================
    ### CONSTRUCTOR

    def createItem(self):
        x = randint(0,self.SCREEN_WIDTH)
        y =  self.SCREEN_HEIGHT + 150
        params = {
            "filePath": "images/items/star.png",
            "size": (self.SCREEN_WIDTH / 15, self.SCREEN_HEIGHT / 15),
            "position": (x, y),
            "spriteBox": (1 , 1, 128, 128),
            "startIndex": 0,
            "endIndex" : 0,
            "frameDuration" : 1/10

        }
        star = createAnimatedSprite(params)
        self.itemList.append(star)

    def collisionCircle(self,x1,y1,r1,x2,y2,r2):
        dx = x1 - x2
        dy = y1 - y2
        d = math.sqrt(dx*dx + dy*dy)
        return (d < r1 + r2)
    ### ====================================================================================================
    def __init__(self):
        pass

    ### ====================================================================================================
    ### INIT
    ### ====================================================================================================
    def setup(self):
        params = {
            "filePath":"images/characters/penguin_fix.png",
            "size" : (200,200),
            "position": (self.SCREEN_WIDTH//2, self.SCREEN_HEIGHT//3,5),

        }
        self.penguin = createFixedSprite(params)

        params = {
            "filePath": "images/backgrounds/winter.png",
            "size": (self.SCREEN_WIDTH,self.SCREEN_WIDTH),
            "position": (self.SCREEN_WIDTH//2, self.SCREEN_HEIGHT//2),
        }
        self.winter = createFixedSprite(params)

        self.moveL = False
        self.moveR = False
        self.sprint = False
        self.time = 0

        params = {
            "filePath": "images/characters/penguin.png",
            "size": (200, 200),
            "position": (self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 3, 5),
            "spriteBox": (5, 1, 250, 250),
            "startIndex": 0,
            "endIndex": 3,
            "frameDuration": 1 / 10
        }
        self.penguin_runR = createAnimatedSprite(params)

        params = {
            "filePath": "images/characters/penguin.png",
            "size": (200,200),
            "position": (self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 3, 5),
            "spriteBox": (5, 1, 250, 250),
            "startIndex": 0,
            "endIndex": 3,
            "frameDuration": 1/10,
            "flipH": True
        }
        self.penguin_runL = createAnimatedSprite(params)

        params = {
            "filePath": "images/characters/penguin.png",
            "size": (200, 200),
            "position": (self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 3, 5),
            "spriteBox": (5, 1, 250, 250),
            "startIndex": 4,
            "endIndex": 4,
            "frameDuration": 1 / 10,

        }
        self.penguin_sprintR = createAnimatedSprite(params)

        params = {
            "filePath": "images/characters/penguin.png",
            "size": (200, 200),
            "position": (self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 3, 5),
            "spriteBox": (5, 1, 250, 250),
            "startIndex": 4,
            "endIndex": 4,
            "frameDuration": 1 / 10,
            "flipH": True
        }
        self.penguin_sprintL = createAnimatedSprite(params)

        self.itemList = []
    ### ====================================================================================================
    ### UPDATE
    ### ====================================================================================================
    def update(self, deltaTime):
        self.time += deltaTime
        if self.time >= 0.2:
            self.time = 0
            self.createItem()



        self.penguin_runL.update_animation()
        self.penguin_runR.update_animation()
        self.penguin_sprintL.update_animation()
        self.penguin_sprintR.update_animation()



        speed = 2 if self.sprint else 1

        if self.moveL:
            self.penguin.center_x -= 10 * speed
        if self.moveR:
            self.penguin.center_x += 10 * speed

        if self.penguin.center_x < 0 :
            self.penguin.center_x = self.SCREEN_WIDTH
        if self.penguin.center_x > self.SCREEN_WIDTH :
            self.penguin.center_x = self.penguin.width





        self.penguin_runR.center_x = self.penguin.center_x
        self.penguin_runL.center_x = self.penguin.center_x
        self.penguin_sprintR.center_x = self.penguin.center_x
        self.penguin_sprintL.center_x = self.penguin.center_x

        for star in self.itemList:
            star.update_animation()
            star.angle += 5
            star.center_y -= 10
            if star.center_y < -300:
                self.itemList.remove(star)
            elif self.collisionCircle(
                star.center_x,
                star.center_y,
                star.width/2,
                self.penguin.center_x,
                self.penguin.center_y + self.penguin.height/5,
                self.penguin.width/5):
                    self.itemList.remove(star)
    ### ====================================================================================================
    ### RENDERING
    ### ====================================================================================================
    def draw(self):

        self.winter.draw()
        if self.moveL == self.moveR:
            self.penguin.draw()
        elif self.moveR:
            if self.sprint:
                self.penguin_sprintR.draw()
            else:
                self.penguin_runR.draw()
        else:
            if self.sprint:
                self.penguin_sprintL.draw()
            else:
                self.penguin_runL.draw()



        for star in self.itemList:
            star.draw()


    ### ====================================================================================================
    ### KEYBOARD EVENTS
    ### key is taken from : arcade.key.xxx
    ### ====================================================================================================
    def onKeyEvent(self, key, isPressed):
        if key == arcade.key.Q:

                self.moveL = isPressed
        if key == arcade.key.D:

                self.moveR = isPressed

        if key == arcade.key.LSHIFT:
            self.sprint = isPressed

        if key == arcade.key.C and isPressed:
            self.createItem()



    ### ====================================================================================================
    ### GAMEPAD BUTTON EVENTS
    ### buttonName can be "A", "B", "X", "Y", "LB", "RB", "VIEW", "MENU", "LSTICK", "RSTICK"
    ### ====================================================================================================
    def onButtonEvent(self, gamepadNum, buttonName, isPressed):
        print(f"GamePad={gamepadNum} - ButtonNum={buttonName} - isPressed={isPressed}")

    ### ====================================================================================================
    ### GAMEPAD AXIS EVENTS
    ### axisName can be "X", "Y", "RX", "RY", "Z"
    ### ====================================================================================================
    def onAxisEvent(self, gamepadNum, axisName, analogValue):
        print(f"GamePad={gamepadNum} - AxisName={axisName} - Value={analogValue}")

    ### ====================================================================================================
    ### MOUSE MOTION EVENTS
    ### ====================================================================================================
    def onMouseMotionEvent(self, x, y, dx, dy):
        print(f"MOUSE MOTION : x={x}/y={y} dx={dx}/dy={dy}")

    ### ====================================================================================================
    ### MOUSE BUTTON EVENTS
    ### ====================================================================================================
    def onMouseButtonEvent(self, x, y, buttonNum, isPressed):
        # print(f"MOUSE BUTTON : x={x}/y={y} buttonNum={buttonNum} isPressed={isPressed}")
        if abs(self.logo.center_x - x) < self.logo.width // 2.2:
            if abs(self.logo.center_y - y) < self.logo.height // 2.2:
                if isPressed:
                    if abs(self.speedX) < 1 and abs(self.speedY) < 1:
                        self.speedX *= 20
                        self.speedY *= 20
                    else:
                        self.speedX /= 20
                        self.speedY /= 20
