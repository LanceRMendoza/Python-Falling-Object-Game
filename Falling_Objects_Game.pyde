# Falling Objects

ballRandomX = random(255)
ballX = [ballRandomX, ballRandomX + 50, ballRandomX + 100, ballRandomX + 200, ballRandomX + 400]
ballY = [60, 90, 120, 150, 180]
ballRadius = 12
ballFallSpeed = 5

# Different points system for each ball.
ballColor = [color(50, 50, 250), color(50, 250,250), color(250, 50, 50), color(50), color (250)] #r,g,b
ballColorpoints = [1, 2, -3, 2*4, -4]
highScore = 0
score = 0

visualScore = 0
visualScoreUpdateCount = 0

# Paddle catcher
paddlePosX = 320
paddlePosY = 450
paddleWidth = 50
paddleHeight = 15

def setup ():
    size (640, 480)
    textSize(12)
    rectMode(CENTER)
                
def draw ():
    global score, highScore, ballFallSpeed, ballY, life, visualScoreUpdateCount, visualScore
    # -- Logic
    if mousePressed:
        print ("Mouse Pressed")
        ballX.append(random(width))
        ballY.append(random(-10))
        ballColor.append(color(random(255), random(255), random(255)))
    #else:
        #print ("not pressed")
    
    # paddle movement
    paddlePosX = mouseX

    for i in range (len(ballX)):
        #Ball Movement
        ballX[i] += random(-2,2) #
        ballY[i] += ballFallSpeed
        
        #Collision detection
        if (ballX[i] > paddlePosX - paddleWidth/2 and ballX[i] < paddlePosX + paddleWidth/2 and ballY[i] > paddlePosY - paddleWidth/2 and ballY[i] < paddlePosY + paddleWidth/2):
            score = score + ballColorpoints[i]
            highScore = score
            highScore = max (highScore, score)
            ballX[i] = random(width)
            ballY[i] = - ballRadius
            print("catch")

        # Randomize position on X axis
        if ballY[i] > height + ballRadius:
            ballX[i] = random(width) 
            ballY[i] = - ballRadius
            # life = life - 1
    
    # Counts up/down score.
    visualScoreUpdateCount -= 1
    if (visualScoreUpdateCount <= 0):
        visualScoreUpdateCount = 10
        if (visualScore < score):
            visualScore = visualScore + 1
        if (visualScore > score):
            visualScore = visualScore - 1

        #if the visual score is less than the actual score, increase the visualScore by one
        #if the visual score is greater than the actual score, subtract the visualScore by one
    
    # -- Draw
    background (54, 81, 94)
    
    for i in range(len(ballX)): 
        fill (ballColor[i])
        circle (ballX[i], ballY[i], ballRadius*2)
        fill (255)
    
    # bumper rectangle
    rect (paddlePosX, paddlePosY, paddleWidth, paddleHeight)
    
    # All texts in game
    text("BallCount: " + str(len(ballX)), 10, 15) # print text, print string of lenth of ballX
    text ("Score: "+ str(visualScore), 10, 30) # str() returns the value as a string
    # text ("High Score:"+ str(highScore), 10, 45)
    text ("Key inputted:"+ str(key), 10, 45)
    text ("Press s to exit game.", 10, 60)
    
    text("D/Blue balls give you:" + str(1), width - 140, 15)
    text("L/Blue balls give you:" + str(2), width - 140, 30)
    text("Red balls give you:" + str(-3), width - 140, 45)
    text("Black balls give you:" + str(2*4), width - 140, 60)
    text("White balls give you:" + str(-4), width - 140, 75)

    # Exit the game if key pressed.
    if keyPressed:
        if key == 's':
            exit()
