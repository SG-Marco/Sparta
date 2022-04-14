import pygame
from random import *

# 레벨에 맞게 설정하기
def setup(level):
    global display_time
    # 얼마동안 숫자를 보여줄지?
    display_time = 5 - (level - 1) * 0.3
    display_time = max(display_time, 1)

    # How many numbers?
    number_count = (level // 3) + 5
    number_count = min(number_count, 20)

    shuffle_grid(number_count)

# 숫자섞기
def shuffle_grid(number_count):
    rows = 5
    columns = 9

    cell_size = 130
    button_size = 110
    screen_left_margin = 50
    screen_top_margin = 20

    grid = [[0 for col in range(columns)] for row in range(rows)]

    number = 1
    while number <= number_count:
        row_idx = randrange(0, rows)
        col_idx = randrange(0, columns)

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number
            number += 1


            # 현재 gird cell 위치 기준으로 x, y 위치 구하기
            center_x = screen_left_margin + (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) + (cell_size / 2)
    
            # 숫자 버튼 만들기
            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)

            number_buttons.append(button)


# 잘 되는지 확인용
    print(grid)




def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    msg = game_font.render(f"{curr_level}", True, WHITE)
    msg_rect = msg.get_rect(center=start_button.center)
    screen.blit(msg, msg_rect)


def display_game_screen():
    global hidden
    if not hidden:
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        if elapsed_time > display_time:
            hidden = True

    for idx, rect in enumerate(number_buttons, start=1):
        if hidden:
            pygame.draw.rect(screen, WHITE, rect)
        else:
        # 실제 숫자 텍스트
            cell_text = game_font.render(str(idx), True, WHITE)
            text_rect = cell_text.get_rect(center=rect.center)
            screen.blit(cell_text, text_rect)


def check_buttons(pos):
    global start, start_ticks

    if start:
        check_number_buttons(pos)
    elif start_button.collidepoint(pos):
        start = True
        start_ticks = pygame.time.get_ticks()


def check_number_buttons(pos):
    global hidden, start, curr_level
    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]: # right num
                del number_buttons[0]
                if not hidden:
                    hidden = True
            else:
                game_over()
            break

    if len(number_buttons) == 0:
        start = False
        hidden = False
        curr_level += 1
        setup(curr_level)

# 게임 종료 처리
def game_over():
    global running
    running = False
    msg = game_font.render(f"Your level is {curr_level}", True, WHITE)
    msg_rect = msg.get_rect(center=(screen_width / 2, screen_height / 2))
    screen.fill(BLACK)
    screen.blit(msg, msg_rect)


pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(("Memory Game"))
game_font = pygame.font.Font(None, 120)

# Start button
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height-120)


# Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (50, 50, 50)

number_buttons = []
curr_level = 1
display_time = None # 숫자를 처음에 보여주는 시간
start_ticks = None # 현재 시간 정보?


# 게임 시작 여부
start = False
hidden = False # 숫자 가림 여부

setup(curr_level)

# Game loop
running = True
while running:
    click_pos = None

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
            print(click_pos)

    screen.fill(BLACK)

    if start:
        display_game_screen()
    else:
        display_start_screen()


# 사용자가 클릭 했다면
    if click_pos:
        check_buttons(click_pos)

    pygame.display.update()


pygame.time.delay(5000)

pygame.QUIT()



















