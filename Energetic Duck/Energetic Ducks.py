###########################
#Title: Energetic Ducks   #
#Last Updated: Jan.26.2018#
#Programmer Jonathan Li   #
###########################


from tkinter import *
from math import *
from time import *
from random import *


root = Tk()
screen = Canvas(root, width=800, height=800, background="grey50")



global backon
backon=False




def setInitialValues():     #all the initial values
    global xBall, yBall, ballRadius, ballColour, xMouse, yMouse, xSpeed, ySpeed, maxSpeed, ball, Qpressed, penestrate, hit
    global rockets, rocketspeed, xrockets, yrockets, posx, posy, foodImage, nugget, nugx, nugy, bullet, instruct, back
    global foodposx, foodposy, initialimage, duckx, ducky, FEGELEIN, tbag, fishies, spd, playButton, xr, yr, rc,count, stored, hunt, duckslid, cnugget, ult, tp


    ult=False
    if mlg==False:   #image of ducks
        foodImage = PhotoImage( file = "source.gif" )
    else:  #image of shreks
        foodImage = PhotoImage( file = "shrek.gif" )                       
    back=Button(root, text = "Play", font = "Times 30", command = play, anchor=CENTER )
    nugget=PhotoImage(file="62b817ced2917aef3fc27401635e31c6.gif")


    FEGELEIN=[]
    cnugget="KEVIN"


    xBall = 400
    yBall = 400
    foodposx=[]
    foodposy=[]
    ballRadius = 20
    ballColour = "black"
    spd=10
    xMouse = 0
    yMouse = 0
    tbag=False
    
    xSpeed = 0
    ySpeed = 0
    xr=[]
    yr=[]
    rockets = []
    xrockets = []
    yrockets = []
    rocketspeed = 20
    rc=[]
    maxSpeed = 10

    
    playButton=Button(root, text = "Play", font = "Times 30", command = play, anchor=CENTER )
    
    ball = 0
    fishies=[]
    Qpressed = False
    posx=0
    posy=0
    initialimage=[]
    nugx=0
    nugy=0
    duckx=[]
    ducky=[]
    hunt=0
    tp=90000
    hit=False


    for i in range (count):
        duckx.append(0)
        ducky.append(0)
        FEGELEIN.append(0)
    
    stored=0
    bullet=5

    
def spnugget():                              #spawns a chicken nugget
    global nugx, nugy, nugget, cnugget
    nugx=randint(250, 550)
    nugy=randint(250, 550)
    cnugget=screen.create_image(nugx, nugy, image=nugget)

    
def resetUserValues(x):         #lol this doesn't actually reset it just gets the amoount of ducks from the slider
    global count
    count=duckslid.get()

    
def penes():                 #when you click penestration, if it is on, it turns it off, if it is off, it turns it on
    global penestrate,l, test
    penestrate=test.get()
    if penestrate:

        screen.delete(l)
        l=screen.create_text(11400, 570, text="OFF", font="Times 15")

    else:

        screen.delete(l)
        l=screen.create_text(11400, 570, text="ON", font="Times 15")

        
def shrek():   #turns images into shrek             
    global mlg, s, test2
    mlg=test2.get()
    if mlg:
        screen.delete(s)
        s=screen.create_text(11400, 270, text="OFF", font="Times 15")

    else:
        screen.delete(s)
        s=screen.create_text(11400, 270, text="ON", font="Times 15")

        
def intro():        #all the buttons and crap  ALSO IF YOU GO TO INSTRUCTION THEN GO BACK, IT RESETS THE SETTING. THAT IS NOT A BUG
    global playButton, duckslid, ducklab, peneButton, penestrate,l, instruct, backon, back,insa, insb, insc, insd, inse, insf, shreked, mlg, s, logoi
    global logo, test, test2
    test = BooleanVar()    #checkbox for penestrate
    test.set(True)
    test2 = BooleanVar()   #checkbox for shrek mode
    test2.set(False)
    mlg=False
    penestrate=True
    screen.create_rectangle(0, 0, 800, 800, fill="lightblue")
    l=screen.create_text(11400, 570, text="ON", font="Times 15")       #honestly, I don't need those but I'm too lazy to find all the screen.remove and all so i left this here, but i moved this off screen, same for next line
    s=screen.create_text(11400, 270, text="OFF", font="Times 15")    
    logo = PhotoImage( file = "coollogo_com-212585678.gif" )
    logoi=screen.create_image(400, 400, image=logo)
    playButton = Button(root, text = "Play", font = "Times 30", command = play, anchor=CENTER )
    playButton.pack()
    #playButton.place( x = 150, y = 700, width=100, height = 50 )
    playButton.place( x = 250, y = 600, width=100, height = 50 )
    peneButton = Checkbutton(root, text = "Penetration: ", variable = test, font = "Times 20", command = penes, anchor=CENTER )      #penestration button
    peneButton.pack()
    peneButton.place( x = 150, y = 550, width=200, height = 50 )
    ducklab=Label(root, text = "Amount of duck", font = "fixedsys 15", foreground="yellow", background="slate grey")        #just a label for amount of duck
    ducklab.place(x=150, y=600)
    duckslid = Scale( root, from_ = 2, to=30, orient=HORIZONTAL, command = resetUserValues, length=150, width = 10, resolution = 1  )  #duck slider for amount of ducks
    duckslid.pack()
    #x=150 originally, y=630
    duckslid.place( x = 350, y = 600 )
    duckslid.set( 3 )
    screen.update()
    instruct=Button(root, text = "Instruction", font = "Times 20", command = instruction, anchor=CENTER )    #instruction button
    instruct.pack()
    instruct.place( x = 150, y = 150, width=200, height = 50 )
    shreked=Checkbutton(root, text = "Shrek mode", variable=test2, font = "Times 20", command = shrek, anchor=CENTER )    #instruction button
    shreked.pack()
    shreked.place( x = 150, y = 250, width=200, height = 50 )
    if backon==False:                                                                      #creates back button when it is supposed to
        back=Button(root, text = "Play", font = "Times 30", command = play, anchor=CENTER )
    if backon==True:                                                      #deletes back button when it clicks back
        back.destroy()
        screen.delete(insa, insb, insc, insd, inse, insf)
        backon==False

    


def instruction():                                        #shows instruction and deletes the intro button
    global instruct, playButton, duckslid, ducklab, peneButton, l, back, backon, insa, insb, insc, insd, inse, insf, shreked, s, logoi
    duckslid.destroy()
    ducklab.destroy()
    playButton.destroy()
    peneButton.destroy()
    shreked.destroy()
    screen.delete(l,s, logoi)
    instruct.destroy()
    back=Button(root, text = "back", font = "Times 20", command = intro, anchor=CENTER )
    back.pack()
    back.place( x = 100, y = 150, width=200, height = 50 )
    insa=screen.create_text(0, 100, text="Use wasd keys to move", font="Times 18", anchor=W)
    insb=screen.create_text(0, 300, text="Shift to boost speed (first shift then press w/a/s/d while pressing shift", font="Times 18", anchor=W)
    insc=screen.create_text(0, 400, text="left click to shoot, t for t-bag(t-bag doesn't do anything meaningful)", font="Times 18", anchor=W)
    insd=screen.create_text(0, 500, text="Right click to shoot multiple bullets, beware you only have 5 shots here", font="Times 18", anchor=W)
    inse=screen.create_text(0, 600, text="Don't let the duck touch you,shoot as much ducks as possible", font="Times 18", anchor=W)
    insf=screen.create_text(0, 700, text="Eat chicken nugget, you will only need to move the mouse to shoot for 3 secnods", font="Times 18", anchor=W)
    backon=True


def play():            #delete the buttons and starts the game
    global playButton, duckslid, ducklab, instruct, back, logoi, l, s
    duckslid.destroy()
    ducklab.destroy()
    playButton.destroy()
    peneButton.destroy()
    screen.delete(l, logoi, s)
    instruct.destroy()
    back.destroy()
    shreked.destroy()
    runGame()


def duckmove():          #make the ducksmove
    global duckx, ducky, foodposx, foodposy, FEGELEIN, count
    for i in range (count):
        if foodposx[i]>=800 or foodposx[i]<=0:                #if the ducks go to the left/right edge, it goes to the other direction, Fegelein indicates the direction, 0 for right, 1 for left
            FEGELEIN[i]=1-FEGELEIN[i]

        if FEGELEIN[i]==0:             #move to right
            duckx[i]=(randint(0, 2))
        else:
            duckx[i]=(randint(-2,0))        #move to left
        if foodposy[i]+ducky[i]<800 and foodposy[i]+ducky[i]>0:           #randomize up and down movement when not at edge
            ducky[i]=(randint(-30, 30))
        elif foodposy[i]+ducky[i]<800:                   #when at top move down
            ducky[i]=(randint(0, 30))
        else:
            ducky[i]=(randint(-30, 0))             #when at bottom move up
        foodposx[i]=foodposx[i]+duckx[i]
        foodposy[i]=foodposy[i]+ducky[i]
        
#click to shoot
def mouseClickHandler( event ):
    global xMouse, yMouse, ballColour, Qpressed, xr, yr, rc
    
    global posx, posy
    posx=event.x
    posy=event.y
    if posx==xBall and posy==yBall:                   #if somehow someway the guy clicked in the exact center of the ball, this prevents crash
        xr.append(1)
        yr.append(1)

    else:
        xr.append((posx-xBall)/(abs(posy-yBall)+abs(posx-xBall)))      #ratio of x to y comparing to total distance
        yr.append((posy-yBall)/(abs(posy-yBall)+abs(posx-xBall)))
    rc.append(False)
    spawnNewRocket()


def mccree( event ):     #right click shoots 360 bullets
    global xMouse, yMouse, ballColour, Qpressed, xr, yr, rc, bullet
    
    
    if bullet>0:      #if bullet nom>0
  

        for bull in range (12):          #360 spam
            xr.append(cos(bull*pi/6)/2)
            yr.append(sin(bull*pi/6)/2)
            spawnNewRocket()
            
            rc.append(True)          #records that these bullet comes from right click

        bullet=bullet-1    #decrease count every time
#when key is pressed


def keyDownHandler( event ):
    global xSpeed, ySpeed, Qpressed, xBall, yBall, tbag, spd
    #the capital letter boost speed
    if event.keysym =="A" and spd>0:
        spd=spd-1
        xSpeed=-maxSpeed*3        
    elif event.keysym =="D" and spd>0:
        spd=spd-1
        xSpeed=maxSpeed*3
    elif event.keysym =="W" and spd>0:
        spd=spd-1
        ySpeed=-maxSpeed*3
    elif event.keysym =="S" and spd>0:
        spd=spd-1
        ySpeed=maxSpeed*3

        
    #left, right, up, down
    elif event.keysym =="a":   
        xSpeed = -maxSpeed
        
    elif event.keysym == "d":   
        xSpeed = maxSpeed

    elif event.keysym == "w":   
        ySpeed = -maxSpeed

    elif event.keysym == "s":   
        ySpeed = maxSpeed


    #quit
    elif event.keysym == "q" or event.keysym == "Q":    #Quit does not work in intro screen, also the user quits instead of restarting the game. 
        Qpressed = True
    #tbag, records if the guy has tbag on, when on and pressed t, it goes off and vice versa
    elif event.keysym =="t" or event.keysym == "T":
        if tbag:
            tbag=False
        else:
            tbag=True
        
    


def spawnNewRocket():            #adding the rockets to the list
    global rockets, xrockets, yrockets, foodposx, foodposy
    xrockets.append( xBall )
    yrockets.append( yBall )
    rockets.append(0)
    
    


def keyUpHandler( event ):
    global xSpeed, ySpeed
    
    xSpeed = 0  #stop the ball motion
    ySpeed = 0


#update the ball's position
def updateBallPosition():
    global mlg,s, ult, xBall, yBall, foodposx, foodposy, xSpeed, ySpeed, count, nugx, nugy, ult, tp, cnugget, backon,a, bullett, timeline, fkc, tbag, fishies, times
    
    if xBall+xSpeed>200 and yBall+ySpeed>200 and xBall+xSpeed<600 and yBall+ySpeed<600:    #if in bound, it moves, if the ball is out of bounds, then it doesn't move    
        xBall = xBall + xSpeed
        yBall = yBall + ySpeed

        
    for i in range (count):     #if the ball runs into a duck, the game goes back tointro
        if foodposx[i]-49.5<=xBall+xSpeed<=foodposx[i]+49.5 and foodposy[i]-80<=yBall+ySpeed<=foodposy[i]+80:         #if ball runs into a duck
            if mlg:
                rekt=screen.create_text(400, 400, text="GET SHREKT", font="Arial 89")
            else:
                rekt=screen.create_text(400, 400, text="GET REKT", font="Arial 89")    #the get rekt message
            screen.update()
            sleep(2)
            for k in range (len(fishies)):           
                screen.delete(fishies[k])


            screen.delete(rekt, bound,a, bullett, timeline, fkc, s)       #deletes everything
            for a in range (count):
                screen.delete(initialimage[a])                #deletes all duck
           
            backon=False
            setInitialValues()                   #reset the value of everything
            ult=False
            screen.unbind("<Motion>")           #if the game ends up  power upped
            screen.bind("<Button-1>", mouseClickHandler)
            intro()    #reset to intro screen
            break

    if nugx-60<=xBall<=nugx+60 and nugy-60<=yBall<=nugy+60:          #if the ball eats the chicken nugget
        ult=True
        tp=time()-times             #records the time when the character eats the chicken nugget

        screen.delete(cnugget)
        nugx=9000               #reset the nugget value to something you can't touch in case it causes bug
        nugy=9000

def updateRocketPositions():
    global rockets, xrockets, yrockets, xBall, yBall, fish, posx, posy, foodposx, foodposy, xr, yr, count, stored, hunt, penestrate, hit
    
    for i in range(0,len(yrockets)):
                    
        yrockets[i] = yrockets[i] + rocketspeed*yr[i]
        xrockets[i] = xrockets[i] + rocketspeed*xr[i]           #shoots the place it does depending on ratio
        for cancer in range (count):                       #when rocket his duck
            if foodposx[cancer]-44.5<=xrockets[i]<=foodposx[cancer]+44.5 and foodposy[cancer]-71.5<=yrockets[i]<=foodposy[cancer]+71.5:
                stored=cancer        #stores the number wherethe duck is hit
                drawFood()
                hunt=hunt+1
                hit=True
                #break                      
    deleteArrayItemsThatAreOffScreen()
            

def deleteArrayItemsThatAreOffScreen():
    global penestrate, hit
    i = 0
    
    if penestrate==False and hit:       #if penestration is off and the bullet hit, delete the rocket
            yrockets.pop(i)
            xrockets.pop(i)
            rockets.pop(i)
            xr.pop(i)
            yr.pop(i)
            rc.pop(i)
            hit=False
            
    while i < len(yrockets)-1:
        if yrockets[i]<0 or yrockets[i]>800 or xrockets[i]<0 or xrockets[i]>800:        #delete the rocket off screen, as well as any value along with it
            yrockets.pop(i)
            xrockets.pop(i)
            rockets.pop(i)
            xr.pop(i)
            yr.pop(i)
            rc.pop(i)
        else:
            i = i + 1


#draw the ball
def drawBall():
    global ball, tbag, fishies, rc
    
    ball = screen.create_oval(xBall-ballRadius, yBall-ballRadius, xBall + ballRadius, yBall+ballRadius, fill= "red")
    if tbag:
        fishies.append(screen.create_text(xBall, yBall, text="T-BAG", fill="white"))    #tbag when it is on
    else:
        for av in range (len(fishies)):
            screen.delete(fishies[av])                            #delete the tbag text when it is turned off

def drawrockets():
    for i in range(0,len(yrockets)):
        if rc[i]==True:
            color="blue"     #right click bullet is blue
        else:
            color="red"     #left click is left
        rockets[i] = screen.create_oval( xrockets[i] - 5, yrockets[i] - 5,xrockets[i] + 5,yrockets[i] + 5,fill=color)

def deleterockets():                 #delete rockets when called
    for i in range(0,len(max(xrockets, yrockets))):
       screen.delete(rockets[i])



def gameOver():
    if Qpressed == True:
        return True

    else:
        return False
    


#when q is pressed, it stops the game and destroy everything
def stopGame():
    screen.delete(ball)
    screen.create_text( 400, 400, text="Thanks for playing...Nub", anchor=CENTER, font="Times 35")
    screen.update()
    sleep(2)
    root.destroy()

def drawFood():     #draw the duck
    global foodImage, foodposx, foodposy, initialimage, xBall, yBall, ballRadius, count, stored
    i=stored
    a=randint(0, 800)
    b=randint(0, 800)
    ran=7.5+0.5*count    #measures minimum distance to you when duck is spawned (it is ran x 20)
    if ran>12:
        ran=12    #maximum 10 so duck can actually spawn in screen and not too far
    while xBall-ballRadius*ran<=a<=xBall+ballRadius*ran and yBall-ballRadius*ran<=b<=yBall+ballRadius*ran:        #if it spawns on or too close to you, it spawns in another position
        a=randint(0, 800)
        b=randint(0, 800)

    foodposx[i]=a
    foodposy[i]=b    

    screen.delete(initialimage[i])
    

    initialimage[i]=screen.create_image(foodposx[i], foodposy[i], image=foodImage)    #puts the duck in that place
    screen.update()

def runGame():   #runs the game
    
    global times,xBall, yBall, ballColour, foodposy, initialimage, foodposx, foodposy,spd, count, hunt, cnugget, nugx, nugy, ult, times, tp, bullet, ballRadius, bound, a, bullett, timeline, fkc

    fkc=0    #records number of boost
    bullett=0   #number of blue bullet
    setInitialValues()
    
    
    screen.update()
    for i in range (count):              #make them start at top left corner
            foodposx.append(randint(50, 100))
            foodposy.append(randint(50,100))
    times=time()       #records the time when it starts
    screen.update()
    a=screen.create_text(500, 500, text="Ducks hunted: "+str(hunt))

    ult=False     #when character eats chicken nugget, this turns on
    chicken=True    #this was for testing...
    temp=0       #stores the time after eating the nugget
    tp=0    #stores how long since character eats nugget
    spawningnugget=True
    
    bound=screen.create_rectangle(200-ballRadius/2, 200-ballRadius/2, 600+ballRadius/2, 600+ballRadius/2, fill="white")   #boundry for the character
    while Qpressed ==False:

        screen.delete(a)
        a=screen.create_text(500, 500, text="Ducks hunted: "+str(hunt))
        
        for i in range (count):
            initialimage.append(screen.create_image(foodposx[i], foodposy[i], image=foodImage))
        rn=round((time()-times),2)
        timeline=screen.create_text(80, 30, text="Time:"+str(rn), font="Arial 20", anchor=W)     #time message
        
        if int(rn)%15==10 and rn !=0 and chicken:     #spawns chicken nugget every 15 seconds            
            chicken=False
            if spawningnugget==True:
                spnugget()
                temp=time()-times
                spawningnugget=False

        if rn-temp>5:        #after eating chicken nuggets and the power up is over, it sets the value back
            chicken=True
            spawningnugget=True
        if ult==True:
            screen.bind("<Motion>", mouseClickHandler)      #under powerup, the user only has to move the mouse to shoot
            if rn-tp>=3:   #power up for three second                
                screen.unbind("<Motion>")           #after powerup, returns to normal
                screen.bind("<Button-1>", mouseClickHandler)
                ult=False

        if rn-temp>10:       #after 10 seconds, chicken nugget disappears
            screen.delete(cnugget)
            nugx=9000
            nugy=9000

            
        screen.delete(fkc)
        fkc=screen.create_text(500, 20, text="Boost left: "+str(spd))
        screen.delete(bullett)
        bullett=screen.create_text(350, 20, text="Blue Bullet left: "+str(bullet))         #the messages on top


        duckmove()        
        updateBallPosition()
        updateRocketPositions()
        drawBall()
        drawrockets()
        screen.update()
        sleep(0.01)
        screen.delete(ball)
        screen.delete(timeline)
        deleterockets()

        for i in range (count):
            screen.delete(initialimage[i])
        initialimage=[]
    stopGame()    #stops the game when q is pressed

   

root.after(0, intro)


screen.bind("<Button-1>", mouseClickHandler)
screen.bind("<Button-3>", mccree)
screen.bind("<Key>", keyDownHandler)
screen.bind("<KeyRelease>", keyUpHandler)


screen.pack()
screen.focus_set()
root.mainloop()
