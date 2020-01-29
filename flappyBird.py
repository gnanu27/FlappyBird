import pygame, sys


class Bird(object):
    def __init__(self):
        self.birdRect = pygame.Rect(40, 250, 40, 30) 
        self.birdStatus = [
            pygame.image.load('./img/bird0_0.png'),
            pygame.image.load('./img/bird0_1.png'),
            pygame.image.load('./img/bird0_2.png'),
            pygame.image.load('./img/dead.png'),
        ]

        self.status = 0
        self.birdX = 50
        self.birdY = 250
        self.jump = False
        self.jumpHeight = 10
        self.downHeight = 1
        self.dead= False

    #move Bird
    def moveBird(self):
        if self.jump:
            self.jumpHeight = self.jumpHeight - 1
            self.birdY -= self.jumpHeight

        else:
            self.downHeight += 0.1
            self.birdY += self.downHeight
        self.birdRect[1] = int(self.birdY)



class Pipe(object):
    def __init__(self):
        self.wallX = 120
        self.pipeUp = pygame.image.load('./img/pipe_down.png')
        self.pipeDown = pygame.image.load('./img/pipe_up.png')


    #move Pipe
    def movePipe(self):
        self.wallX -= 2
        if self.wallX < -42:
            global score
            score += 10
            self.wallX = 300


def checkDead():
    rectUp = pygame.Rect(Pipe.wallX, 362, Pipe.pipeUp.get_width(),Pipe.pipeUp.get_height())
    rectDown = pygame.Rect(Pipe.wallX, -150, Pipe.pipeDown.get_width(),Pipe.pipeDown.get_height())
    if rectUp.colliderect(Bird.birdRect) or rectDown.colliderect(Bird.birdRect):
        Bird.dead = True

    if not 0 < Bird.birdRect[1] < 512:
        Bird.dead = True
        return Bird.dead

    else: 
        return False
def getResult():
    text1 = 'Game Over'
    text2 = ' Your final Score is: '+ str(score)
    fontText1 = pygame.font.SysFont(None, 70)
    fontText2 = pygame.font.SysFont(None, 30)
    renderText1 = font.render(text1, -1, (242, 3, 36))
    renderText2 = font.render(text2, -1, (253, 177, 6))
    screen.blit(renderText1, [60, 100])
    screen.blit(renderText2, [20, 1500])

    pygame.display.update()



def createMap():
    screen.blit(background, (0, 0))
    #show Pipe 
    screen.blit(Pipe.pipeDown, (int(Pipe.wallX), -150))
    screen.blit(Pipe.pipeUp, (int(Pipe.wallX), 362))
    Pipe.movePipe()
    #show Bird
    if Bird.dead:
        Bird.status = 3
    elif Bird.jump:
        Bird.status = 0
    else:
        Bird.status = 2
    screen.blit(Bird.birdStatus[Bird.status], (int(Bird.birdX), int(Bird.birdY)))
    Bird.moveBird()
    #Show Font  
    screen.blit(font.render('Score: '+str(score), 1, (255, 255, 255)), (60, 20))
    pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont(None, 40)


    size = (288, 512)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    Bird = Bird()
    Pipe = Pipe()
    score = 0

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Bird.jump = True
                    Bird.jumpHeight = 10
                    Bird.downHeight = 1

        background = pygame.image.load("./img/bg_day.png")

        if checkDead():
            getResult()
        else:
            createMap()

    pygame.quit()