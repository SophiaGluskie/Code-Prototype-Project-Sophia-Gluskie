# Ocean Artwork FINAL: 'Infinite Current' 

# BEGINNING OF ADDITIVE WAVE SET UP 

# Additive wave set up - setting up the specific functions and measurements for the wave
# NOTE additive wave will appear differently each time the code is run

# Defining the wave parameters
xspacing = 8   # How far apart should each horizontal location is spaced
w = 0          # Width of entire wave length
maxwaves = 4   # Total number of waves to add together

theta = 0.0
amplitude = [0] * maxwaves   # Height of wave
dx = [0] * maxwaves          # Value for incrementing X, to be calculated as a function of period and xspacing
yvalues = []                 # Using an array to store height values for the wave within the code

# Stating a global variable to store the selected background ocean image 
bg_image = None

# Setup of background ocean image and size of the image (standard 15inch macbook pro screen-size)
def setup():
    global w, bg_image
    size(1500, 850)
    frameRate(30)
    colorMode(RGB, 255, 255, 255, 100)
    w = width + 16

    # Load the background ocean image onto screen
    bg_image = loadImage("ocean4.jpeg")  

    for i in range(maxwaves):
        amplitude[i] = random(10, 30)
        period = random(100, 300)  # Number of pixels before the wave repeats
        dx[i] = (TWO_PI / period) * xspacing

    global yvalues
    yvalues = [0] * (w // xspacing)

# Utilising the def draw function to display the background image - I discovered that this is a necessary function for ensuring both the image and wave shows up on screen
def draw():
    # Display the background image
    image(bg_image, 0, 0, width, height)  # Stretch the image to fit the screen-size already implemented

    calcWave()
    renderWave()

# Calculate the additive wave requirements
def calcWave():
    global theta, yvalues

    # Increment theta that defines that the speed that the wave repeats
    theta += 0.03

    # Set all height values to zero
    for i in range(len(yvalues)):
        yvalues[i] = 0

    # Accumulate wave height values
    for j in range(maxwaves):
        x = theta
        for i in range(len(yvalues)):
            # Every other wave is cosine instead of sine
            if j % 2 == 0:
                yvalues[i] += sin(x) * amplitude[j]
            else:
                yvalues[i] += cos(x) * amplitude[j]
            x += dx[j]

# Draw the wave on screen by using an ellipse at each location on the wave
def renderWave():
    noStroke()
    fill(107, 183, 152, 50) #Colour the ellipses on the wave green
    ellipseMode(CENTER)
    for x in range(len(yvalues)):
        ellipse(x * xspacing, height / 2 + yvalues[x], 16, 16)

# END OF ADDITIVE WAVE CODE

# START OF BLUE CIRCULAR DESIGN

    # Blue circle design to be repeated with increasing Y values 
    # and alternate increasing X values
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(10, 10, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(70, 50, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(70, 100, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(100, 150, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(100, 200, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(150, 250, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(150, 300, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(200, 350, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(200, 400, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(250, 450, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(250, 500, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(300, 550, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(300, 600, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(350, 650, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(350, 700, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(400, 750, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(400, 800, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(450, 850, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(20, 80, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(30, 150, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(50, 200, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(20, 250, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(80, 260, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(50, 300, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(20, 350, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(100, 340, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(100, 340, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(60, 390, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(140, 400, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(15, 420, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(55, 460, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(120, 450, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(185, 470, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(10, 500, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(40, 550, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(90, 520, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(150, 520, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(200, 560, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(250, 600, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(80, 600, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(140, 590, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(8, 610, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(200, 630, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(280, 660, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(30, 670, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(90, 660, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(200, 690, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(160, 660, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(6, 730, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(70, 720, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(140, 730, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(230, 745, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(280, 720, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(300, 780, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(340, 750, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(350, 820, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(20, 790, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(4, 850, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(80, 780, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(60, 850, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(140, 800, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(200, 790, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(170, 850, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(250, 830, 80)
    
    noFill()
    stroke(112,181,252)
    strokeWeight(2.5)
    circle(290, 870, 80)
    
# END OF CIRCULAR DESIGN WRITTEN CODE

# END OF OCEAN ARTWORK CODE
