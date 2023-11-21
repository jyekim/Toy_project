import pygame
import math
import random

from hangman_words import word_list

#게임창 설정
pygame.init()
WIDTH, HEIGHT = 1000, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

#button variables 버튼변수
RADIUS = 20
GAP = 15
letters = []
#화면 가로 중앙에 모든 버튼이 고르게 배치
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
  x = startx + GAP * 2 + (RADIUS * 2 + GAP) * (i % 13)
  y = starty + (i // 13) * (GAP + RADIUS * 2)
  letters.append([x, y, chr(A + i), False])

# 글자 폰트
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 50)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

# load image 이미지띄우기
images = []
for i in range(7):
  image = pygame.image.load("hangman" + str(i) + ".png")
  images.append(image)

#game varibales 게임변수
hangman_status = 0
word = random.choice(word_list)
#word = "APPLE"
guessed = []

# 게임창 배경 colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)

# setup game loop
# FPS(Frames Per Second) 설정
FPS = 60
clock = pygame.time.Clock()
run = True


def draw():
  win.fill(WHITE)

  #행맨 타이틀 그리기
  text = TITLE_FONT.render("HANGMAN GAME", 1, BLACK)
  win.blit(text, (WIDTH / 2 - text.get_width() / 2, 10))

  # 글자 그리기
  display_word = ""
  for letter in word:
    if letter in guessed:
      display_word += letter + " "
    else:
      display_word += "_ "

  text = WORD_FONT.render(display_word, 1, BLACK)
  win.blit(text, (400, 200))

  # 버튼 그리기
  for letter in letters:
    x, y, ltr, clicked = letter
    if clicked:
      pygame.draw.circle(win, YELLOW, (x, y), RADIUS, 3 if clicked else 1)
    else:
      pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
      text = LETTER_FONT.render(ltr, 1, BLACK)
      win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

  #전체 그림을 어디쯤에 띄울것인지
  win.blit(images[hangman_status], (150, 100))
  pygame.display.update()


while run:
  clock.tick(FPS)
  draw()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      #버튼 눌렀을 때 어떤 알파벳이 뜨는지 알려줌
      m_x, m_y = pygame.mouse.get_pos()
      for letter in letters:
        x, y, ltr, clicked = letter
        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
        if dis < RADIUS and not clicked:
          print(ltr)
          guessed.append(ltr)
          if ltr not in word:
            hangman_status += 1
          letter[3] = True

  won = True
  for letter in word:
    if letter not in guessed:
      won = False
      break
    draw()

  if won:
    text = WORD_FONT.render("You WON!", 1, ORANGE)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 + 50))
    pygame.display.update()
    pygame.time.delay(5000)  #5초동안
    break

  if hangman_status == 6:
    text_word = WORD_FONT.render(f"{word}", 1, (255, 0, 0))
    text_rest = WORD_FONT.render("You lose! The answer is", 1, BLACK)
    # 텍스트를 화면에 그릴 위치 계산
    x_word = WIDTH / 2 - (text_word.get_width() + text_rest.get_width()) / 2
    y_word = HEIGHT / 2 + 50

    # 렌더링된 텍스트를 화면에 그림
    win.blit(text_rest, (x_word, y_word))
    win.blit(text_word, (x_word + text_rest.get_width() + 10, y_word))
    #win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 + 80))
    pygame.display.update()
    pygame.time.delay(5000)  #5초동안
    break

pygame.quit()
