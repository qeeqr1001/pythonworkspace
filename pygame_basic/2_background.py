import pygame

pygame.init()  #초기화 (반드시 필요)

#화면 크기 설정

screen_width=480 #가로 크기
screen_height=640 #세로 크기
pygame.display.set_mode((screen_width,screen_height))



#화면 타이틀 설정
screen = pygame.display.set_mode((screen_width, screen_height)) # screen 변수에 할당
pygame.display.set_caption("PyGame") #게임 이름

#배경 이미지 불러오기
background=pygame.image.load("C:/Users/wldus/OneDrive/바탕 화면/pythonworkspace/pygame_basic/background.png")


#이벤트 루프
running=True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type==pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            running=False #게임이 진행중이 아님
    
    screen.blit(background,(0,0))   #배경 그리기  
    pygame.display.update() #게임화면을 다시 그리기(파이게임은 화면을 계속 그려줘야함.필수)

# 배경을 설정하는 다른 방법으로 배경이미지 불러오지 않고 그냥 색을 채워줄 수도있음
# screen.fill((0,0,255)) RGB값으로 파란색에 해당하는 값.




#pygame 종료
pygame.quit()
