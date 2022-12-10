#################################### Project Description: 
# An interactive piece depicting a tree on a hill that goes through 4 seasons.
#################################### Expected Features:
# Program will pull the date and time from the computer and display differently depending on night/day and season.
# Currently debating on if I want it to be a real time comparison vs accelerated
# Tree will be animated
# Swaying branches, falling leaves, etc.
# Clicking on different parts of the image will cause different things to happen
# There will be three different areas (sky, tree, ground)
# If time allows, will also add some random events
#################################### Development Tasks:
# Code the tree trunk and branches.
# Complete the leaf particle system. 
# Movement when on tree vs falling
# Color and size of leaves
# Code the time system
# Split the months into seasons and times into day/night
# Link the seasons and time of day to the display.

season = 4
SPRING = 1
SUMMER = 2
FALL = 3
WINTER = 4
E = None
L = None
A = None
I = None
N = None
leaves = []
weight = 200
growth = 5

def setup():
    global E, L, A, I, N
    size(700, 800)
    background(255)

    E = Sky()
    L = Hill()
    A = Trunk()
    I = Branches()
    N = Leaves()

    
def draw():
    background(255)

    E.update()
    L.update()
    A.update()
    I.update()
    N.update()
    
    E.render()
    L.render()
    A.render()
    I.render()
    N.render()

# switch between seasons
def keyPressed():
    global season
    if key == "1" or key == "!":
        if season == SPRING:
            pass
        else:
            season = SPRING
    elif key == "2" or key == "@":
        if season == SUMMER:
            pass
        else:
            season = SUMMER
    elif key == "3" or key == "#":
        if season == FALL:
            pass
        else:
            season = FALL
    elif key == "4" or key == "$":
        if season == WINTER:
            pass
        else:
            season = WINTER
            
class Seasonal:
    def __init__(self, springColor, summerColor, fallColor, winterColor):
        self.springColor = springColor
        self.summerColor = summerColor
        self.fallColor = fallColor
        self.winterColor = winterColor
        self.update()
        
    def update(self):
        # change color by season
        if season == SPRING:
            self.col = self.springColor
        elif season == SUMMER:
            self.col = self.summerColor
        elif season == FALL:
            self.col = self.fallColor
        elif season == WINTER:
            self.col = self.winterColor
        
    def render(self):
        pass
        
class Sky(Seasonal):
    # set color
    springColor = color(135, 230, 255)
    summerColor = color(115, 220, 255)
    fallColor = color(150, 215, 255)
    winterColor = color(160, 200, 255)
    def __init__(self):
        self.update()
        
    def render(self):
        background(self.col)
        
class Trunk(Seasonal):
    # set bark color
    springColor = color(140, 90, 40)
    summerColor = color(150, 100, 50)
    fallColor = color(120, 80, 30)
    winterColor = color(130, 110, 90)
    def __init__(self):
        self.update()
        
    # draw tree trunk
    def render(self):
        fill(self.col)
        noStroke()
        x1 = width/2
        y1 = height/2
        x2 = x1 +10
        y2 = y1
        x3 = x2 +5
        y3 = (height/4)*3
        x4 = width/2 -10
        y4 = (height/4)*3 -5
        quad(x1, y1, x2, y2, x3, y3, x4, y4)
        
# branch shape
def branch(xOffset, yOffset):
    
    baseX = width/2
    baseY = height/2
    baseCurveX = baseX
    baseCurveY = baseY
    
    tipX = baseX + xOffset
    tipY = baseY - yOffset
    
    if xOffset > 0:
        tipCurveX = tipX + 300
    elif xOffset < 0:
        tipCurveX = tipX - 300
    tipCurveY = tipY + weight
    curve(baseCurveX, baseCurveY, baseX, baseY, tipX, tipY, tipCurveX, tipCurveY)
    
class Branches(Seasonal):
    # set color
    springColor = color(140, 90, 40)
    summerColor = color(150, 100, 50)
    fallColor = color(120, 80, 30)
    winterColor = color(130, 110, 90)
    
    def __init__(self):
        self.update()
        
    def render(self):
        noFill()
        strokeWeight(5)
        stroke(self.col)
        # draw 5 branches
        branch(-width/3, height/12)
        branch(width/3, height/12)
        branch(width/4, height/6)
        branch(-width/4, height/6)
        branch(-width/10, height/5)
        
# create leaf shape
def leaf():
    ginko = createShape()
    ginko.beginShape()
    ginko.vertex(5*growth, 0)
    ginko.vertex(0, 8*growth)
    ginko.vertex(4*growth, 10*growth)
    ginko.vertex(5*growth, 6*growth)
    ginko.vertex(6*growth, 10*growth)
    ginko.vertex(10*growth, 8*growth)
    ginko.vertex(5*growth, 0)
    ginko.endShape()
    shape(ginko, 0, 0)
    
class Leaves(Seasonal):
    global weight
    # set color
    springColor = color(180, 90, 115)
    summerColor = color(80, 200, 90)
    fallColor = color(230, 190, 130)
    winterColor = color(180, 160, 130)
    
    def __init__(self):
        self.update()
        
    # draw leaf
    def render(self):
        noStroke()
        fill(self.col)
        translate(100, 100)
        rotate(PI/3.0)
        leaf()

        
class Hill(Seasonal):
    # set color
    springColor = color(50, 200, 75)
    summerColor = color(205, 225, 75)
    fallColor = color(40, 200, 100)
    winterColor = color(115, 200, 140)
    
    def __init__(self):
        self.update()
        
    # draw Hill
    def render(self):
        fill(self.col)
        ellipseMode(CENTER)
        hillHeight = 4*height/5
        ellipse(width/2, height, 2*width, hillHeight)
        
        
