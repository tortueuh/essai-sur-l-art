
import pygame
import math
import numpy
import random
pygame.mixer.init()
pygame.font.init()

class graphic():
    def __init__(self):
        self.running = True 
        self.surface = pygame.display.set_mode((1200,650))
        blank = pygame.Surface((8,8))
        blank.fill((255,255,255))
        pygame.display.set_icon(blank)
        pygame.display.set_caption("")
        self.window = 0
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("good_font.ttf",32)
        self.font2 = pygame.font.Font("good_font.ttf",64)


        self.ds = 0
        self.vs =[0,0]
        self.esc_rect = pygame.rect.Rect(600-175,150,350,200)
        self.dx_y = [0,0]
        self.vt = [0,0]
        self.color = 0

        self.count = 0
        self.count2 = 0
        self.percent = 100
        self.images = [pygame.transform.scale(pygame.image.load("im/i1.png").convert_alpha(),(252,288)),pygame.image.load("im/i2.png").convert_alpha(),pygame.image.load("im/i3.png").convert_alpha(),pygame.image.load("im/i4.png").convert_alpha(),pygame.transform.scale(pygame.image.load("im/i5.png").convert_alpha(),(133*2,168*2))]
        self.poses = [(30,130),(780,400),(950,20),(-1000,0),(350,230),]
        self.px = 0
        self.toppers = []
        for i in range(265):
            self.toppers.append(0)


        self.eye = pygame.transform.scale(pygame.image.load('im/eye.png').convert_alpha(),(342,256))
        self.huge_eye = pygame.transform.scale(pygame.image.load('im/169.png').convert_alpha(),(1200,650))
        self.eyes = [] 
        self.count3 = 0
        self.circle_diameter = 1
        self.center = [int(804/(1712/1200)),int(530/(1712/1200))]
    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False 
            if self.window == 0:
                if event.type == pygame.MOUSEMOTION:
                    self.vs = [(pygame.mouse.get_pos()[0]-self.esc_rect.centerx),(pygame.mouse.get_pos()[1]-self.esc_rect.centery)]
                    self.vt = math.sqrt((self.esc_rect.centerx-(600-175+175))**2+(self.esc_rect.centery-250)**2)
                    

                    self.color = max(0,int((200-self.vt)/200 * 255))
                    
                    self.ds = math.sqrt(self.vs[0]**2+self.vs[1]**2)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.esc_rect.collidepoint(pygame.mouse.get_pos()):
                            self.window = 1

    def draw(self):
        if self.window == 0:
            self.surface.fill((255,255,255))
            self.surface.blit(self.font.render("Vous voulez penser l'Art ? Suivez moi !",False,(0,0,0)),(600-self.font.size("Vous voulez penser l'Art ? Suivez moi !")[0]/2,30))
            pygame.draw.rect(self.surface,(0,0,0),self.esc_rect)
            self.surface.blit(self.font.render("Clique moi.",False,(self.color,self.color,self.color)),(self.esc_rect[0]+350/2-self.font.size("Clique moi.")[0]/2,self.esc_rect[1]+200/2-self.font.size("Clique moi.")[1]/2))
            
            if self.ds < 202:
                if self.esc_rect.x > 0 and self.esc_rect.right < 1200:
                    self.dx_y[0] -= self.vs[0]/self.ds*1.5
                if self.esc_rect.bottom < 675 and self.esc_rect.y > 0:
                    self.dx_y[1] -= self.vs[1]/self.ds*1.5
                self.esc_rect.x = 600-175 + int(self.dx_y[0])
                self.esc_rect.y = 150 + int(self.dx_y[1])
                self.vs = [(pygame.mouse.get_pos()[0]-self.esc_rect.centerx),(pygame.mouse.get_pos()[1]-self.esc_rect.centery)]
                self.ds = math.sqrt(self.vs[0]**2+self.vs[1]**2)
        if self.window == 1:
            self.surface.fill((255,255,255))
            self.surface.blit(self.font.render("Quand l'oeuvre sera-t-elle dénaturée ?",False,(0,0,0)),(600-self.font.size("Quand l'oeuvre sera-t-elle dénaturée ?")[0]/2,60))
            self.surface.blit(self.font2.render(str(self.percent)+"%",False,(0,0,0)),(600-self.font2.size(str(self.percent)+"%")[0]/2,120))
            self.count += 1
            if self.percent > -1:
                if self.count == 20 and self.percent > 0:
                    self.count = 0 
                    self.percent -= 1
                
                for i in range(len(self.images)):
                    self.surface.blit(self.images[i],self.poses[i])
                    if self.percent > 0:
                        if i == 0:
                            for s in range(18):
                                r1 = random.randint(0,251)
                                r12 = random.randint(0,251)
                                r2 = random.randint(0,287)
                                r22 = random.randint(0,287)
                                c1 = self.images[i].get_at((r1,r2))
                                c2 = self.images[i].get_at((r12,r22))
                                pygame.draw.rect(self.images[i],(c1),(r12,r22,1,1))
                                pygame.draw.rect(self.images[i],(c2),(r1,r2,1,1))
                        if i == 2:
                            for s in range(26):
                                x = self.px % 180 
                                y = (self.px // 180)
                                if y < 280:
                                    dx = 255 - self.images[i].get_at((x,y))[0]
                                    pygame.draw.rect(self.images[i],(dx,dx,dx),(x,y,1,1))
                                    self.px += 1
                        if i == 1:
                            for s in range(25):
                                top = random.randint(0,264)
                                
                                if self.toppers[top] != 263:
                                    self.toppers[top] += 1 
                                pygame.draw.rect(self.images[i],(self.images[i].get_at((top,0))[0],self.images[i].get_at((top,0))[0],self.images[i].get_at((top,0))[0]),(top,self.toppers[top],1,1))
                        if i == 4:
                            for s in range(45):
                                x = random.randint(0,133*2-1)
                                y = random.randint(0,168*2-1)
                                if self.images[i].get_at((x,y))[0] > 255/2:
                                    color = (255,255,255)
                                else:
                                    color  = (0,0,0)
                                pygame.draw.rect(self.images[i],color,(x,y,1,1))
            if self.percent ==0:
                self.count2 += 1
                
                if self.count2 == 60:
                    self.window = 2
        elif self.window == 2:
            self.count3 += 1
            if self.count3  < 40*120:
                for eye in self.eyes:
                    self.surface.blit(self.eye,eye)
                    eye[1] += random.randint(1,2)
                    if eye[1] > 675:
                        self.eyes.remove(eye)
                if random.randint(0,90) == 9 and self.count3 < 120*35:
                    self.eyes.append([random.randint(-100,1200),random.randint(-100,475)])
            elif self.count3 == 40*120:
                self.surface.blit(self.huge_eye,(0,0))
            else:
                self.circle_diameter += 1
                pygame.draw.circle(self.surface,(4,4,4),self.center,self.circle_diameter)
        pygame.display.flip()

pygame.mixer.music.load('im/bald_night.ogg')
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play()
graph = graphic()
while graph.running:
    graph.event()
    graph.draw()
    graph.clock.tick(120)
    
