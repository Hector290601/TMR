from RPi_GPIO_Rotary import rotary

def cwTurn():
    print("CW")

def ccwTurn():
    print("CCW")

def buttonPushed():
    print("Button")

def valueChanged(count):
    print("Change")

rot = rotary.Rotary(23, 24, 25, 2)

rot.register(increment=cwTurn, decrement=ccwTurn)

rot.register(pressed=buttonPushed, onchange=valueChanged)

rot.start()

while True:
    try:
        pass
    except KeyBoardInterrupt:
        break

rot.stop()
