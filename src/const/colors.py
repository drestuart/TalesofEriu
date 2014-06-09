# A constants module for holding color tuples

# Helper class for objects with color
class withColor(object):
    def __init__(self, **kwargs):
        super(withColor, self).__init__()

    def getColor(self):        
        return self.__class__.color
    
    def setColor(self, value):
        self.__class__.color = value

# Helper class for objects with a background color
class withBackgroundColor(withColor):
    def __init__(self, **kwargs):
        super(withBackgroundColor, self).__init__(**kwargs)

    def getBackgroundColor(self):        
        return self.__class__.backgroundColor
    
    def setBackgroundColor(self, value):
        self.__class__.backgroundColor = value

# Common colors
black = (0,0,0)
white = (255,255,255)
grey = (128,128,128)
lightGrey = (192,192,192)
lighterGrey = (211,211,211)

blue = (0,0,255)
lightSkyBlue = (135,206,250)
lightBlue = (173,216,230)
darkBlue = (0,0,139)
deepSkyBlue = (0,191,255)

red = (255,0,0)
lightRed = (205,92,92)
darkRed = (139,0,0)
darkMagenta = (139,0,139)

green = (0,255,0)
darkerGreen = (0,100,0)
forestGreen = (34,139,34)

goldenrod = (218,165,32)
gold = (255,215,0)
brown = (165,42,42)
darkBrown = (139,69,19)
sienna = (160,82,45)

orange = (255, 165, 0)

yellow = (255, 255, 0)

# UI Colors
blankBackground = black

colorDefaultFG = white
colorDefaultBG = black

colorMapPanelFG = white
colorMapPanelBG = black

colorMessagePanelFG = white
colorMessagePanelBG = black

colorCharPanelFG = white
colorCharPanelBG = black

# Level tile and feature colors
colorNotInFOV = grey
colorWallNotInFOV = (105,105,105)
colorLightWall = (130, 110, 50)
colorDarkGround = (50, 50, 150)
colorLightGround = (200, 180, 50)

colorWood = sienna 
colorRock = darkBrown
colorStone = lighterGrey
colorGrass = darkerGreen
colorTree = forestGreen

# World map colors
colorOcean = darkBlue
colorRiver = deepSkyBlue
colorMountain = colorStone
colorField = colorGrass
colorForest = colorTree
colorPlain = goldenrod

# Material colors
colorSteel = lightSkyBlue
colorGold = gold
colorMeat = brown
colorLeather = darkBrown