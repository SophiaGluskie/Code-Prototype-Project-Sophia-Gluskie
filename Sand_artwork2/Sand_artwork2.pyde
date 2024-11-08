# Sand Artwork FINAL: 'Shifting Sand'

# BEGINNING OF SINE WAVE SET UP

# Sine wave setup - setting up the specific functions and measurements for the wave

# Defining the wave parameters
xspacing = 10  # Distance between each horizontal location
theta = 0.0    # Start angle at 0
amplitude = 75.0  # Height of wave
period = 500.0  # How many pixels before the wave repeats
dx = 0         # Value for incrementing X
yvalues = []   # List to store height values for the wave

# Set image variable to none so sand background image is able to be set
img = None

# Setup of background sand image and size of the image (standard 15inch macbook pro screen-size)
def setup():
    global yvalues, img, dx
    size(1500, 850)
    img = loadImage("sand2.jpeg") # load up the image that I took # Setting up background sand image
    img.resize(width, height)  # Resize image to fit canvas - # set the size of the window (my standard mac window size)
    dx = (TWO_PI / period) * xspacing
    yvalues = [0] * (width // xspacing)

# Utilising the def draw function to display the background image - I discovered that this is a necessary function for ensuring both the image and wave shows up on screen
def draw():
    global theta, yvalues
    
    # Display the image (which is actually nothing due to the custom background image being used)
    image(img, 0, 0)
    
    # Increment theta that defines the speed of the wave
    theta += 0.02

    # Calculate y values for the wave
    x = theta
    for i in range(len(yvalues)):
        yvalues[i] = sin(x) * amplitude
        x += dx

    # Draw the wave with an ellipse at each location
    noStroke()
    fill(247,241,175)  # Colour the ellipses on the wave yellow
    for x in range(len(yvalues)):
        ellipse(x * xspacing, height / 2 + yvalues[x], 10, 10)
        
# END OF SINE WAVE CODE

# START OF YELLOW CURVATURE DESIGN

# Set the colour and fill of the the first curve (this has to be set each time due to differing strokeweights)
    noFill()
    stroke(247,241,175) # Yellow colour selected
    strokeWeight(2)

# Initial bezier design - to be repeated with differing Y coordinates to produce a repeated curvature design down the length of the sand image
    bezier(0, 0, 100, 15, 200, 0.2, 400, 3)
    bezier(400, 3, 150, 300, 500, 0.2, 750, 3)
    bezier(750, 3, 800, 300, 1125, 0.2, 1312, 3)
    bezier(1312, 3, 1200, 300, 1500, 0, 1500, 0)

    noFill()
    stroke(247,241,175)
    strokeWeight(3)

    bezier(0, 0, 100, 15, 200, 0.5, 400, 6)
    bezier(400, 6, 150, 300, 500, 0.5, 750, 6)
    bezier(750, 6, 800, 300, 1125, 0.5, 1312, 6)
    bezier(1312, 6, 1200, 300, 1500, 0, 1500, 0)
    
    noFill()
    stroke(247,241,175)
    strokeWeight(4)
    
    bezier(0, 0, 100, 15, 200, 2, 400, 15)
    bezier(400, 15, 150, 300, 500, 2, 750, 15)
    bezier(750, 15, 800, 300, 1125, 2, 1312, 15)
    bezier(1312, 15, 1200, 300, 1500, 0, 1500, 0)
    
    noFill()
    stroke(247,241,175)
    strokeWeight(5)
    
    bezier(0, 0, 100, 25, 200, 5, 400, 25)
    bezier(400, 25, 150, 300, 500, 5, 750, 25)
    bezier(750, 25, 800, 300, 1125, 5, 1312, 25)
    bezier(1312, 25, 1200, 300, 1500, 0, 1500, 0)
    
    noFill()
    stroke(247,241,175)
    strokeWeight(12)
    
    bezier(0, 0, 100, 50, 200, 10, 400, 50)
    bezier(400, 50, 150, 300, 500, 10, 750, 50)
    bezier(750, 50, 800, 300, 1125, 10, 1312, 50)
    bezier(1312, 50, 1200, 300, 1500, 0, 1500, 0)
    
    noFill()
    stroke(247,241,175)
    strokeWeight(12)
    
    bezier(0, 0, 100, 100, 200, 15, 400, 100)
    bezier(400, 100, 300, 300, 500, 15, 750, 100)
    bezier(750, 100, 900, 300, 1125, 15, 1312, 100)
    bezier(1312, 100, 1300, 300, 1500, 0, 1500, 0)
    
    noFill()
    stroke(247,241,175)
    strokeWeight(10)
    
    bezier(0, 20, 100, 300, 200, 20, 400, 100)
    bezier(400, 100, 375, 300, 500, 20, 750, 100)
    bezier(750, 100, 937, 300, 1125, 20, 1312, 100)
    bezier(1312, 100, 1400, 300, 1500, 0, 1500, 0)
    
    noFill()
    stroke(247,241,175)
    strokeWeight(8)
    
    bezier(0, 106, 150, 300, 200, 180, 400, 106)
    bezier(400, 106, 325, 300, 500, 180, 750, 106)
    bezier(750, 106, 987, 300, 1125, 180, 1312, 106)
    bezier(1312, 106, 1450, 300, 1500, 212, 1500, 106)
    
    noFill()
    stroke(247,241,175)
    strokeWeight(6)
    
    bezier(0, 206, 150, 300, 200, 150, 400, 206)
    bezier(400, 206, 325, 300, 500, 150, 750, 206)
    bezier(750, 206, 987, 300, 1125, 150, 1312, 206)
    bezier(1312, 206, 1450, 300, 1500, 212, 1500, 206)
    
    noFill()
    stroke(247,241,175)
    strokeWeight(4)
    
    bezier(0, 306, 150, 300, 200, 150, 400, 306)
    bezier(400, 306, 325, 300, 500, 150, 750, 306)
    bezier(750, 306, 987, 300, 1125, 150, 1312, 306)
    bezier(1312, 306, 1450, 300, 1500, 212, 1500, 306)
    
    noFill()
    stroke(247,241,175)
    strokeWeight(3)
    
    bezier(0, 406, 150, 300, 200, 150, 400, 406)
    bezier(400, 406, 325, 300, 500, 150, 750, 406)
    bezier(750, 406, 987, 300, 1125, 150, 1312, 406)
    bezier(1312, 406, 1450, 300, 1500, 212, 1500, 406)
    
    noFill()
    stroke(247,241,175)
    strokeWeight(2)
    
    bezier(0, 506, 150, 300, 200, 150, 400, 506)
    bezier(400, 506, 325, 300, 500, 150, 750, 506)
    bezier(750, 506, 987, 300, 1125, 150, 1312, 506)
    bezier(1312, 506, 1450, 300, 1500, 212, 1500, 506)

# END OF YELLOW CURVATURE DESIGN

# END OF SAND ARTWORK CODE
