import pygame
import random
import os

###1. 게임 스크린 만들기

pygame.init()  #모든 파이게임라이브러리 초기화시작

#Global Constants 전역상수들 생성
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#running이라는 container에 사진 두개 넣어서 뛰는 모습 만든것/이미지가 복수일 경우 리스트형태로 넣어야함
RUNNING = [
    pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
    pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))
]

JUMPING = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))

DUCKING = [
    pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
    pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
    pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
    pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))
]

LARGE_CATCUS = [
    pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
    pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
    pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))
]

BIRD = [
    pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
    pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))
]

CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))

BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))

#공룡 클래스
class Dinosaur():
  X_POSITION = 80
  Y_POSITION = 310
  Y_POSITION_DUCK = 340
  JUMP_VEL = 8.5

  def __init__(self):
    self.duck_img = DUCKING
    self.run_img = RUNNING
    self.jump_img = JUMPING


    self.dino_duck = False 
    self.dino_run = True #출발할때 자세
    self.dino_jump = False #특정키를 입력해서 점프할 때 true로 바꿔주면 됨

    self.step_index = 0
    self.jump_vel = self.JUMP_VEL
    self.image = self.run_img[0] #위에 리스트 넣어진 것을 0,1과 반복하여 구현할 것임
    self.dino_rect = self.image.get_rect() #피격범위를 넣어서 공룡이 장애물 피할때 움직임 감지
    self.dino_rect.x = self.X_POSITION
    self.dino_rect.y = self.Y_POSITION

def update(self,userInput):
    if self.dino_duck:
      self.duck()
    if self.dino_run:
      self.run()
    if self.dino_jump:
      self.jump()
    
    if self.step_index >= 10:
        self.step_index = 0
    
    #공룡이 동작됨을 테스트할 때 조건문 
    #키보드의 입력과 공룡의 현상태에 따른 동작을 제어하는 코드 
    if userInput[pygame.K_UP] and not self.dino_jump: #업키를 누르고 점프 상태가 아닐때 2단 점프를 방지하기 위함
       self.dino_duck = False
       self.dino_jump = True
       self.dino_run = False
    elif userInput[pygame.K_DOWN] and not self.dino_jump:  #키보드 다운 버튼과 공중에서 ducking 하지 않도록 and notjump 넣은 'ducking상태' 
       self.dino_duck = True
       self.dino_jump = False
       self.dino_run = False
    elif not (self.dino_jump or userInput[pygame.K_DOWN]):  #점프상태 또는 아래키를 입력하지 않았을때 '달리는 상태'를 뜻함
       self.dino_duck = False
       self.dino_jump = False
       self.dino_run = True

def duck(self):
   self.duck= self.duck_img
   self.dino_rect = self.image.get_rect()
   self.dino_rect.x = self.X_POSITION
   self.dino_rect.y = self.Y_POSITION
   self.step_index += 1


def run(self):
   self.image = self.run_img[self.step_index//5] #self.step_index는 0~9까지인데 5로나눈 몫을 사용하기때문에, //는 나눈 몫을 구하는 연산자 
   self.dino_rect = self.image.get_rect()
   self.dino_rect.x = self.X_POSITION
   self.dino_rect.y = self.Y_POSITION
   self.step_index += 1 

def jump(self):
   #제어 
   self.image = self.jump.img
   if self.dino_jump:
      self.dino_rect.y -= self.jump_vel * 4  #빼주는 이유가 y좌표가 적을수록 위로 가기에 y값이 적을수록 공룡이 높은 것
      self.jump_vel -= 0.8
   if self.jump_vel < -self.JUMP_VEL: #떨어지는 값이 처음 최초의 8.5점프값보다 낮아지면 점프를 중지함
      self.dino_jump = False
      self.jump_vel = self.JUMP_VEL

def draw(self, SCREEN):
   SCREEN.blit(self.image,(self.dino_rect.x, self.dino_rect.y))

#구름 클래스
class Cloud():
   def __init__(self):
      self.x = SCREEN_WIDTH + random.randint(800,1000)
      self.y = random.randint(50,100)
      self.image = CLOUD
      self.width = self.image.get_width() #너비를 가져오는 이유는 업데이트에 있음!
   
   def update(self):
      self.x -= game_speed
      if self.x <-self.width:
          self.x = SCREEN_WIDTH + random.randint(2600, 3000)
          self.y = random.randint(50,100)
    
   def draw(self,SCREEN):
      SCREEN.blit(self.image,(self.x, self.y))


#### 2. 메인함수 만들기
def main():
  global game_speed
  run = True
  clock = pygame.time.Clock()
  player = Dinosaur()
  game_speed = 14

  while run:
    for event in pygame.event.get():  #사용자가 활동을 하는 동안에
      if event.type == pygame.QUIT:
        run = False

    SCREEN.fill(255, 255, 255)
    userInput = pygame.key.get_pressed()

    player.draw(SCREEN)
    player.update(userInput)

    clock.tick(30)  #이미지 업데이트 할 때 초당 30장 로드


### 3. 점수기능과 배경, 구름, 트랙 
#구름이 게임에서 오른쪽에서 왼쪽으로 지나감 
#
main()
