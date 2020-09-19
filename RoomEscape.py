from bangtal import *
import random

scene1 = Scene("Room1", "Images/배경-2.png")
scene2 = Scene("Room2", "Images/배경-2.png")
scene3 = Scene("Room3", "Images/배경-1.png")

doorTo2 = Object("Images/문-왼쪽-닫힘.png")
doorTo2.locate(scene1, 300,300)
doorTo2.show()
doorTo2_state = False

doorTo3 = Object("Images/문-오른쪽-닫힘.png")
doorTo3.locate(scene1, 800,300)
doorTo3.show()
doorTo3_state = False

doorTo1 = Object("Images/문-오른쪽-닫힘.png")
doorTo1.locate(scene2, 900,300)
doorTo1.show()
doorTo1_state = False

btn1 = Object("Images/redbtn.png")
btn1.locate(scene3, 80,470)
btn1.setScale(0.25)
btn1.show()
btn1_state = False

btn2 = Object("Images/redbtn.png")
btn2.locate(scene3, 200,480)
btn2.setScale(0.25)
btn2.show()
btn2_state = False

btn3 = Object("Images/redbtn.png")
btn3.locate(scene3, 320,490)
btn3.setScale(0.25)
btn3.show()
btn3_state = False

btn4 = Object("Images/redbtn.png")
btn4.locate(scene3, 440,500)
btn4.setScale(0.25)
btn4.show()
btn4_state = False

escape = Object("Images/escape.png")
escape.locate(scene3,800,300)
escape.hide()

board = Object("Images/board.png")
board.locate(scene3,700,300)
board.show()

board2 = Object("Images/rightboard.png")
board2.locate(scene2,100,300)
board2.setScale(0.6)
board2.show()

findKey = Object("Images/findkey.png")
findKey.locate(scene2,100,300)
findKey.setScale(0.6)
findKey.show()

music = Object("Images/music.png")
music.locate(scene3,1150,500)
music.setScale(0.05)
music.show()

title1 = Object("Images/guitar.png")
title1.locate(scene3,50,550)
title1.setScale(0.4)
title1.show()

title2 = Object("Images/piano.png")
title2.locate(scene3,170,560)
title2.setScale(0.4)
title2.show()

title3 = Object("Images/violin.png")
title3.locate(scene3,290,570)
title3.setScale(0.4)
title3.show()

title4 = Object("Images/marimba.png")
title4.locate(scene3,410,580)
title4.setScale(0.4)
title4.show()

expandBoard = Object("Images/bigboard.png")
expandBoard.locate(scene3,200,100)
expandBoard.hide()

key = Object("Images/key.png")
key.locate(scene2, 200,100)
key.setScale(0.05)
key.hide()
# 사용자가 key를 가지고 있는지 상태를 저장하는 변수
keyState = False

keyTimer = Timer(0.5)

def doorTo2_MouseAction(x,y,action):
    global doorTo2_state
    global doorTo1_state
    if doorTo2_state :
        # scene2으로 이동 시 scene1에서 2로 이동하는 문 닫기, scene2에서 1로 이동하는 문 닫기
        doorTo2.setImage("Images/문-왼쪽-닫힘.png")
        doorTo1.setImage("Images/문-오른쪽-닫힘.png")
        doorTo1_state = False
        doorto2_state = False
        scene2.enter()
    else:
        doorTo2.setImage("Images/문-왼쪽-열림.png")
        doorTo2_state = True
doorTo2.onMouseAction = doorTo2_MouseAction

def doorTo3_MouseAction(x,y,action):
    global doorTo3_state
    if doorTo3_state :
        scene3.enter()
    else:
        if keyState:
            doorTo3.setImage("Images/문-오른쪽-열림.png")
            doorTo3_state = True
        else:
            showMessage('문을 열기 위해서는 열쇠가 필요합니다')
doorTo3.onMouseAction = doorTo3_MouseAction

def doorTo1_MouseAction(x,y,action):
    global doorTo1_state
    global doorTo2_state
    if doorTo1_state :
        # scene1으로 이동 시 door state 변경
        doorTo1_state = False
        doorTo2_state = False
        scene1.enter()
    else:
        doorTo1.setImage("Images/문-오른쪽-열림.png")
        doorTo1_state = True
doorTo1.onMouseAction = doorTo1_MouseAction

def escape_MouseAction(x,y,action):
    endGame()
escape.onMouseAction = escape_MouseAction

def music_MouseAction(x,y,action):
    showAudioPlayer("bensound-sunny.mp3")
music.onMouseAction = music_MouseAction

def board_MouseAction(x,y,action):
    expandBoard.show()
board.onMouseAction = board_MouseAction

def expandBoard_MouseAction(x,y,action):
    expandBoard.hide()
expandBoard.onMouseAction = expandBoard_MouseAction

def btn1_MouseAction(x,y,action):
    global btn1_state
    if btn1_state:
        btn1.setImage("Images/redbtn.png")
        btn1_state = False
    else:
        btn1.setImage("Images/greenbtn.png")
        btn1_state = True
    checkAnswerState()
btn1.onMouseAction = btn1_MouseAction

def btn2_MouseAction(x,y,action):
    global btn2_state
    if btn2_state:
        btn2_state = False
        btn2.setImage("Images/redbtn.png")    
    else:
        btn2_state = True
        btn2.setImage("Images/greenbtn.png")
    checkAnswerState()
btn2.onMouseAction = btn2_MouseAction

def btn3_MouseAction(x,y,action):
    global btn3_state
    if btn3_state:
        btn3_state = False
        btn3.setImage("Images/redbtn.png")
    else:
        btn3_state = True
        btn3.setImage("Images/greenbtn.png")
    checkAnswerState()
btn3.onMouseAction = btn3_MouseAction

def btn4_MouseAction(x,y,action):
    global btn4_state
    if btn4_state:
        btn4_state = False
        btn4.setImage("Images/redbtn.png")
    else:
        btn4_state = True
        btn4.setImage("Images/greenbtn.png")
    checkAnswerState()
btn4.onMouseAction = btn4_MouseAction

# 정답 state를 확인하는 함수. 버튼 클릭 시마다 실행됨.
def checkAnswerState():
    if btn1_state == True and btn4_state == True and btn2_state == False and btn3_state == False:
        board.hide()
        escape.show()

# 키 찾기 버튼 클릭 상태를 저장하는 변수
findKeyState = False
def findKey_mouseAction(x,y,action):
    global findKeyState
    global keyState
    if findKeyState:
        # key를 찾았을 때
        key.hide()
        keyTimer.stop()
        key.pick()
        keyState = True
    else:
        # 키 찾기 버튼을 눌렀을 때 타이머를 작동시킴.
        findKeyState = True
        keyTimer.start()
findKey.onMouseAction = findKey_mouseAction

def keyTimer_timeout():
    key.show()
    key.locate(scene2,random.randint(0,1000),random.randint(0,500))
    keyTimer.start()
keyTimer.onTimeout = keyTimer_timeout

startGame(scene1)