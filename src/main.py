import pygame #line:1
import random #line:2
pygame .init ()#line:5
WIDTH ,HEIGHT =800 ,600 #line:8
CELL_SIZE =20 #line:9
WHITE =(255 ,255 ,255 )#line:12
GREEN =(0 ,255 ,0 )#line:13
RED =(255 ,0 ,0 )#line:14
BLACK =(0 ,0 ,0 )#line:15
screen =pygame .display .set_mode ((WIDTH ,HEIGHT ))#line:18
pygame .display .set_caption ("Snake Game")#line:19
clock =pygame .time .Clock ()#line:22
font =pygame .font .Font (None ,36 )#line:25
snake =[(100 ,100 ),(90 ,100 ),(80 ,100 )]#line:28
snake_dir =(CELL_SIZE ,0 )#line:29
food =(random .randint (0 ,(WIDTH //CELL_SIZE )-1 )*CELL_SIZE ,random .randint (0 ,(HEIGHT //CELL_SIZE )-1 )*CELL_SIZE )#line:31
running =True #line:34
score =0 #line:35
def draw_snake (O00OOO0O0OOO0OO0O ):#line:37
    for O00000000OOO0O000 in O00OOO0O0OOO0OO0O :#line:38
        pygame .draw .rect (screen ,GREEN ,pygame .Rect (O00000000OOO0O000 [0 ],O00000000OOO0O000 [1 ],CELL_SIZE ,CELL_SIZE ))#line:39
def draw_food (OOO00OOO0O0OOO000 ):#line:41
    pygame .draw .rect (screen ,RED ,pygame .Rect (OOO00OOO0O0OOO000 [0 ],OOO00OOO0O0OOO000 [1 ],CELL_SIZE ,CELL_SIZE ))#line:42
def move_snake (OOOO0OO0OOO0OO000 ,OOOOO0OO0OOOO0OO0 ):#line:44
    OO000O0OOO0OOO0OO =(OOOO0OO0OOO0OO000 [0 ][0 ]+OOOOO0OO0OOOO0OO0 [0 ],OOOO0OO0OOO0OO000 [0 ][1 ]+OOOOO0OO0OOOO0OO0 [1 ])#line:45
    OOOO0OO0OOO0OO000 =[OO000O0OOO0OOO0OO ]+OOOO0OO0OOO0OO000 [:-1 ]#line:46
    return OOOO0OO0OOO0OO000 #line:47
def check_collision (OOO0O00OOOO000000 ):#line:49
    OO0O0OOOOO000O0O0 =OOO0O00OOOO000000 [0 ]#line:50
    if OO0O0OOOOO000O0O0 [0 ]<0 or OO0O0OOOOO000O0O0 [0 ]>=WIDTH or OO0O0OOOOO000O0O0 [1 ]<0 or OO0O0OOOOO000O0O0 [1 ]>=HEIGHT :#line:52
        return True #line:53
    if OO0O0OOOOO000O0O0 in OOO0O00OOOO000000 [1 :]:#line:55
        return True #line:56
    return False #line:57
def grow_snake (O00OOO0OOOOO0O0O0 ):#line:59
    O0OO0O0000O0000OO =O00OOO0OOOOO0O0O0 [-1 ]#line:60
    O00OOO0OOOOO0O0O0 .append (O0OO0O0000O0000OO )#line:61
def show_start_menu ():#line:63
    screen .fill (BLACK )#line:64
    OOOO000OO00OOOO0O =font .render ("Snake Game",True ,WHITE )#line:65
    O0OOO000OOOOO0000 =font .render ("Press SPACE to Start",True ,WHITE )#line:66
    screen .blit (OOOO000OO00OOOO0O ,(WIDTH //2 -OOOO000OO00OOOO0O .get_width ()//2 ,HEIGHT //3 ))#line:67
    screen .blit (O0OOO000OOOOO0000 ,(WIDTH //2 -O0OOO000OOOOO0000 .get_width ()//2 ,HEIGHT //2 ))#line:68
    pygame .display .flip ()#line:69
    OOOO0000O000O0O00 =True #line:71
    while OOOO0000O000O0O00 :#line:72
        for O0000000OO00O0OOO in pygame .event .get ():#line:73
            if O0000000OO00O0OOO .type ==pygame .QUIT :#line:74
                pygame .quit ()#line:75
                exit ()#line:76
            if O0000000OO00O0OOO .type ==pygame .KEYDOWN and O0000000OO00O0OOO .key ==pygame .K_SPACE :#line:77
                OOOO0000O000O0O00 =False #line:78
def show_score (O0OOO0OO0O0O0OO0O ):#line:80
    OO00OO0O000OO00OO =font .render (f"Score: {O0OOO0OO0O0O0OO0O}",True ,WHITE )#line:81
    screen .blit (OO00OO0O000OO00OO ,(10 ,10 ))#line:82
show_start_menu ()#line:85
while running :#line:88
    for event in pygame .event .get ():#line:89
        if event .type ==pygame .QUIT :#line:90
            running =False #line:91
    keys =pygame .key .get_pressed ()#line:94
    if keys [pygame .K_UP ]and snake_dir !=(0 ,CELL_SIZE ):#line:95
        snake_dir =(0 ,-CELL_SIZE )#line:96
    if keys [pygame .K_DOWN ]and snake_dir !=(0 ,-CELL_SIZE ):#line:97
        snake_dir =(0 ,CELL_SIZE )#line:98
    if keys [pygame .K_LEFT ]and snake_dir !=(CELL_SIZE ,0 ):#line:99
        snake_dir =(-CELL_SIZE ,0 )#line:100
    if keys [pygame .K_RIGHT ]and snake_dir !=(-CELL_SIZE ,0 ):#line:101
        snake_dir =(CELL_SIZE ,0 )#line:102
    snake =move_snake (snake ,snake_dir )#line:105
    if check_collision (snake ):#line:108
        print (f"Game Over! Your score: {score}")#line:109
        running =False #line:110
    if snake [0 ]==food :#line:113
        grow_snake (snake )#line:114
        food =(random .randint (0 ,(WIDTH //CELL_SIZE )-1 )*CELL_SIZE ,random .randint (0 ,(HEIGHT //CELL_SIZE )-1 )*CELL_SIZE )#line:116
        score +=1 #line:117
    screen .fill (BLACK )#line:120
    draw_snake (snake )#line:121
    draw_food (food )#line:122
    show_score (score )#line:123
    pygame .display .flip ()#line:124
    clock .tick (10 )#line:127
pygame .quit ()
