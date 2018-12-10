import pygame
import time

pygame.init()
HP = 100
DEF = 5
ATK = 10
gold = 100
gold1 = 0
width = 1800
height = 900
Edamage = 5
ally = 0
info = 0
gameDisplay = pygame.display.set_mode((width, height),pygame.RESIZABLE)
pygame.display.set_caption('PROJECT:EUREKA')
gameIcon = pygame.image.load('ey.png').convert()
pygame.display.set_icon(gameIcon)

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (34,177,76)
lightgreen = (0, 255, 0)
blue = (255,239,213)
lightblue = (238,213,183)

smallfont = pygame.font.SysFont("unispacebold", 15)
medfont = pygame.font.SysFont("unispacebold", 50)
largefont = pygame.font.SysFont("unispacebold", 85)
clock = pygame.time.Clock()

print(pygame.font.get_fonts())
def loadimage(image, pos_x, pos_y):
    gameDisplay.blit(image, (pos_x, pos_y))

def getgold():
    return gold1

def getgold2():
    return gold

def getATK():
    return ATK

def getDEF():
    return DEF

def getHP():
    return HP

def getALLY():
    return ally

def getINFO():
    return info

def textbutton(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx + (buttonwidth / 2)), buttony + (buttonheight / 2))
    gameDisplay.blit(textSurf, textRect)

def text_objects(text, color,size = "small"):

    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def button(text, x, y, width, height, inactive_color, active_color,action = None,part = 27):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1:
            if action == "start":
                starting()
            elif action == "next":
                screen1()
            elif action =="next1":
                screen2()
            elif action =="next2":
                screen3()
            elif action =="next3":
                screen4()
            elif action =="next4":
                screen5()
            elif action =="next5":
                screen6()
            elif action =="next6":
                screen7()
            elif action =="next7":
                screen8()
            elif action =="next8":
                screen9()
            elif action =="next9":
                screen10()
            elif action =="next10":
                screen11()
            elif action =="next11":
                screen12()
            elif action =="next12":
                battle1()
            elif action =="next13":
                screen14()
            elif action =="next14":
                screen15()
            elif action =="next15":
                screen16()
            elif action =="next16":
                screen17()
            elif action =="next17":
                screen18()
            elif action =="next18":
                screen19()
            elif action =="next19":
                screen20()
            elif action =="next20":
                screen21()
            elif action =="next21":
                screen22()
            elif action =="next22":
                screen23()
            elif action =="next23":
                screen24()
            elif action =="next24":
                screen25()
            elif action =="next25":
                screen26()
            elif action =="next26":
                screen27()
            elif action =="next27":
                screen28()
            elif action =="next28":
                screen29()
            elif action =="next29":
                screen30()
            elif action =="next30":
                screen31()
            elif action =="next31":
                screen32()
            elif action =="next32":
                screen33()
            elif action =="next33":
                screen34()
            elif action =="next341":
                screen35()
            elif action =="next342":
                global ally
                ally = 1
                screen35()
            elif action =="next35":
                screen36()
            elif action =="next36":
                screen37()
            elif action =="next37":
                screen38()
            elif action =="next38":
                screen39()
            elif action =="next39":
                screen40()
            elif action =="next40":
                screen41()
            elif action =="next41":
                screen42()
            elif action =="next42":
                screen43()
            elif action =="next43":
                screen44()
            elif action =="next44":
                screen45()
            elif action =="next45":
                screen46()
            elif action =="next46":
                screen47()
            elif action =="next47":
                screen48()
            elif action =="next48":
                screen49()
            elif action =="next49":
                screen50()
            elif action =="next50":
                screen51()
            elif action =="next51":
                screen52()
            elif action =="next52":
                screen53()
            elif action =="next53":
                screen54()
            elif action =="next54":
                screen55()
            elif action =="next55":
                screen56()
            elif action =="next56":
                screen57()
            elif action =="next57":
                screen58()
            elif action =="next58":
                screen59()
            elif action =="next59":
                screen60()
            elif action =="next60":
                screen61()
            elif action =="next61":
                screen62()
            elif action =="next62":
                screen63()
            elif action =="next63":
                screen64()
            elif action =="next64":
                screen65()
            elif action =="next65":
                screen66()
            elif action =="next66":
                screen67()

            elif action =="next167":
                screen167()
            elif action =="next1681":
                global info
                info = 1
                screen169()
            elif action =="next1682":
                global gold
                gold = getgold2() + 200
                screen169()
            elif action =="next169":
                screen170()
            elif action =="next170":
                screen171()
            elif action =="next171":
                screen172()
            elif action =="next172":
                screen173()
            elif action =="next173":
                screen174()
            elif action =="next174":
                screen175()
            elif action =="next175":
                screen176()
            elif action =="next176":
                screen177()
            elif action =="next177":
                screen178()
            elif action =="next178":
                screen179()
            elif action =="next179":
                screen180()
            elif action =="next180":
                screen181()
            elif action =="next181":
                screen182()
            elif action =="next182":
                screen183()
            elif action =="next183":
                screen184()
            elif action =="next184":
                screen185()
            elif action =="next185":
                screen186()
            elif action =="next1861":
                screen187()
            elif action == "next1862":
            elif action =="next187":
                screen188()
            elif action =="next188":
                screen189()
            elif action =="next189":
                screen190()
            elif action =="next190":
                screen191()
            elif action =="next191":
                screen192()

            elif action =="next266":
                screen267()
            elif action =="next267":
                screen268()
            elif action =="next268":
                screen269()
            elif action =="next269":
                screen270()
            elif action =="next270":
                screen271()
            elif action =="next271":
                screen272()
            elif action =="next272":
                screen273()
            elif action =="next273":
                screen274()
            elif action =="next274":
                screen275()
            elif action =="next273":
                screen274()
            elif action =="next274":
                screen275()
            elif action =="next275":
                screen276()
            elif action =="next276":
                screen277()
            elif action =="next277":
                screen278()
            elif action =="next278":
                screen279()
            elif action =="next279":
                screen280()
            elif action =="next280":
                screen281()
            elif action =="next281":
                screen282()
            elif action =="next282":
                screen283()
            elif action =="next283":
                screen284()

            elif action =="shop":
                screen27(part-1)
            elif action =="ATK1":
                damage = getATK()
                return damage
            elif action =="DEF1":
                defd = getDEF()*2
                return defd
            elif action =="PAS1":
                damage = getATK()
                return damage

            elif action =="ATK":
                lvl2()
            elif action =="DEF":
                lvl3()
            elif action =="HP":
                lvl1()

            elif action =="mommy":
                mommy()

            elif action =="ATK2":
                lvl22()
            elif action =="DEF2":
                lvl33()
            elif action =="HP2":
                lvl11()

            elif action =="ATK+":
                return 1
            elif action =="DEF+":
                return 1
            elif action =="HP+":
                return 2

            elif action =="choice1":
                choice1()
            elif action =="choice2":
                choice2()
            elif action =="choice3":
                choice3()

            elif action =="battle2":
                battle2()
            elif action =="battle3":
                rescue()
            elif action =="train":
                train()
            elif action =="pay":
                pay1()

            elif action =="battle4":
                battle4()
            elif action =="battle5":
                rescue1()
            elif action =="train1":
                train1()
            elif action =="pay1":
                pay11()

            elif action =="battlebad1":
                battlebad1()
            elif action =="battlebad2":
                battlebad2()
            elif action =="battlebad3":
                battlebad3()
            elif action == "battlebad4":
                battlebad4()
            elif action == "battlebad5":
                battlebad5()
            elif action =="rescue2":
                rescue2()
            elif action =="train2":
                train2()
            elif action =="pay2":
                pay12()
            elif action =="battle6":
                battle6()

            elif action =="yes":
                return "yes"
            elif action =="no":
                return "no"

            elif action =="battlegood1":
                battlegood1()
            elif action =="battlegood2":
                battlegood2()
            elif action =="battlegood3":
                battlegood3()
            elif action =="battlegood4":
                battlegood4()
            elif action =="battlegood5":
                battlegood5()
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))
    textbutton(text,black,x,y,width,height)

def messagescreen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(1800 / 2), int(900 / 2) + y_displace)
    gameDisplay.blit(textSurf, textRect)

def intro():
    intro = True
    gameDisplay.fill(white)
    bg = pygame.image.load('ProjectEureka.jpg')
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("NEW GAME", 800, 425, 200, 50, blue, lightblue, "start")
        button("LOAD GAME", 800, 500, 200, 50, blue, lightblue, "start")
        pygame.display.update()

def starting():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Father: well One day Ericka, you are gonna do great things.You will have a greater impact in today’s society!", 300, 700, 1200, 50,blue,lightblue )
        button("next", 1600, 800, 100, 50, blue, lightblue,"next")
        pygame.display.update()

def screen1():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Mother: Calm down, don’t pressure her. Just let her grow up at her once pace.", 300, 700, 1200, 50,blue,lightblue )
        button("next", 1600, 800, 100, 50, blue, lightblue,"next1")
        pygame.display.update()
def screen2():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Father: Okay, Honey. We love you, Ericka.", 300, 700, 1200, 50,blue,lightblue )
        button("next", 1600, 800, 100, 50, blue, lightblue,"next2")
        pygame.display.update()
def screen3():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Father: Okay, Honey. We love you, Ericka.", 300, 700, 1200, 50,blue,lightblue )
        button("next", 1600, 800, 100, 50, blue, lightblue,"next3")
        pygame.display.update()
def screen4():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Eureka: What a weird dream….. Who were those people? Nevermind, I’ll just go to breakfast.", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next4")
        pygame.display.update()
def screen5():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("113: Oh, hey Eureka, how was your sleep? We got a long day ahead of us.", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next5")
        pygame.display.update()
def screen6():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Eureka: Yeah, I know. I had this weird dream about two people, and they were like, talking to me. I can’t remember much anymore though.", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next6")
        pygame.display.update()
def screen7():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("113: Huh, that is weird. Maybe you have met them somewhere in the past before?", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next7")
        pygame.display.update()
def screen8():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Eureka: That’s impossible. For as long as I remember, I have grown up in this organization. Training day-by-day to become the best assassin to make my father proud.", 100, 700, 1500, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next8")
        pygame.display.update()
def screen9():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("113: It must be hard to live up to your father, the head of the enterprise.", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next9")
        pygame.display.update()
def screen10():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Eureka: Yeah, but I won’t give up.  *ALARM RINGS*", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next10")
        pygame.display.update()
def screen11():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("113: It’s time for training. Good luck out there.", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next11")
        pygame.display.update()
def screen12():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("BOSS: Hello Eureka you know the drill (100HP,5 DEF, 10ATK)", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next12")
        pygame.display.update()
def battle1():
    HP=100
    EHP=75
    Edamage = 10
    DEF = 5
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2-1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:"+str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:"+str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50,blue, lightblue,"ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            screen13()
        pygame.display.update()
def screen13():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2.jpg')
    gold = 100
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("BOSS: You did well here is your reward(100g)", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next13")
        button(str(gold)+"g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()
def screen14():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("BOSS: Now head over to the armory to get suited up", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next14")
        pygame.display.update()
def screen15():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.jpg')
    gold = 100
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Blacksmith: I got 3 fine weapons for you take your pick", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next15")
        button(str(gold) + "g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()
def screen16():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene6Shop.jpg')
    gold = 100
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        damage = button("Electric Sword (60g)", 300, 600, 1200, 50, blue, lightblue, "choice1")
        damage2 = button("Dagger (50g)", 300, 700, 1200, 50, blue, lightblue, "choice2")
        damage3 = button("Electric Warhammer (75g)", 300, 800, 1200, 50, blue, lightblue, "choice3")
        button(str(gold) + "g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()
def choice1():
    global gold1
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Blacksmith: Great choice! Your ATK is now at 12", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next16")
        button(str(gold-60) + "g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()
        gold1 = gold-60
        global ATK
        ATK = 12
def choice2():
    global gold1
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Blacksmith: Great choice! Your ATK is now at 9", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next16")
        button(str(gold-50) + "g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()
        gold1 = gold-50
        global ATK
        ATK = 9
def choice3():
    global gold1
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Blacksmith: Great choice! Your ATK is now at 15", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next16")
        button(str(gold-75) + "g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()
        gold1 = gold-75
        global ATK
        ATK = 15
def screen17():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("BOSS: Great youre back! time to choose the next mission", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next17")
        button(str(getgold()) + "g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()
def screen18():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Battle enemies (2 enemies with stats: Health: 60, Defense: 0, Damage: 15. Gold reward: 200)", 300, 600, 1200, 50, blue, lightblue, "battle2")
        button("Rescue. Gold reward(100g)", 300, 700, 1200, 50, blue, lightblue, "battle3")
        button("or training (After may choose to upgrade Health by 10, Damage by 5, or Defense by 5)", 300, 800, 1200, 50, blue, lightblue, "train")
        pygame.display.update()
def battle2():
    global HP
    HP=100
    EHP=60
    Edamage = 10
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene4Battle.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:"+str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:"+str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50,blue, lightblue,"ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            battle21()
        pygame.display.update()
def battle21():
    HP=getHP()
    EHP=60
    Edamage = 10
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene4Battle2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:"+str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:"+str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50,blue, lightblue,"ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            screen19()
        pygame.display.update()
def screen19():
    global gold1,HP
    HP = 100
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2.jpg')
    gold = getgold()
    gold1 = gold + 200
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("BOSS: You did well here is your reward(200g)", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next19")
        button(str(gold1)+"g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()
def train():
    HP = 100
    EHP = 70
    Edamage = 0
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2-1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            level()
        pygame.display.update()
def level():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("ADD 10 TO MAX HP", 300, 600, 1200, 50, blue, lightblue, "HP")
        button("ADD 5 TO MAX DAMAGE", 300, 700, 1200, 50, blue, lightblue, "ATK")
        button("ADD 5 TO MAX DEFENSE", 300, 800, 1200, 50, blue, lightblue, "DEF")
        pygame.display.update()
def lvl1():
    global HP
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    HP = 110
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("God: Great choice! Your HP is now at 110 ", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next19")
        pygame.display.update()
def lvl2():
    global ATK,HP
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    ATK = getATK() + 5
    HP = 100
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("God: Great choice! Your ATK is now at "+str(ATK), 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next19")
        pygame.display.update()
def lvl3():
    global DEF,HP
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    DEF = getDEF()+5
    HP = 100
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("GOD: Great choice! Your DEF is now at "+str(DEF), 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next19")
        pygame.display.update()
def rescue():
    global HP
    HP = 100
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene4Saving.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("You found her goodjob! now head back to the boss", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "pay")
        pygame.display.update()
def pay1():
    global gold1
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2.jpg')
    gold = getgold()
    gold1 = gold + 100
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("BOSS: You did well here is your reward(100g)", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next19")
        button(str(gold1) + "g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()
def screen20():
    global gold1
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Welcome back. Your next mission is to gather information on a possibly threatening corporation.", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next20")
        pygame.display.update()
def screen21():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene5final.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Eureka: There seems to be an important conversation ongoing, moving in to eavesdrop", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next21")
        pygame.display.update()
def screen22():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene5final.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Eureka: *that man seems familiar who could he be*", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next22")
        pygame.display.update()
def screen23():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene5final.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Familiar man: WE ARE ABOUT TO MAKE A BREAKTHROUGH THAT CAN CHANGE THE FUTURE FOR HUMANS", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next23")
        pygame.display.update()
def screen24():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene5final.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Eureka: Id better report this to the boss", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next24")
        pygame.display.update()
def screen25():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Eureka: *relays information*", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next25")
        pygame.display.update()
def screen26():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("BOSS: this is quite the situation we have on our hands. Head over to the shop to gear up", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next26")
        pygame.display.update()
def screen27(part = 28):
    global HP,ATK,DEF,gold1
    goldminus = 0
    part = part
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Stats.jpg')
    HP = getHP()
    ATK = getATK()
    DEF = getDEF()
    DEF1 = getDEF()
    HP1 = getHP()
    ATK1 = getATK()
    gold = getgold()
    gold2 = getgold2()
    ans = "ey"
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("HP" + str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ATK" + str(ATK), 1500, 200, 150, 50, blue, lightblue)
        button("DEF" + str(DEF), 1500, 300, 150, 50, blue, lightblue)
        button(str(gold) + "g", 1200, 100, 150, 50, blue, lightblue)
        HPadd = button("ADD 2 TO MAX HP(5g)", 300, 600, 1200, 50, blue, lightblue, "HP+")
        ATKadd = button("ADD 1 TO MAX DAMAGE(5g)", 300, 700, 1200, 50, blue, lightblue, "ATK+")
        DEFadd = button("ADD 1 TO MAX DEFENSE(5g)", 300, 800, 1200, 50, blue, lightblue, "DEF+")
        button("next", 1600, 800, 100, 50, blue, lightblue, "next"+str(part))
        if HPadd == None:
            HPadd = 0
        if ATKadd == None:
            ATKadd = 0
        if DEFadd == None:
            DEFadd = 0
        if gold <=0:
            button("NO MORE GOLD TO SPEND!!", 600, 350, 300, 50, blue, lightblue)
            button("next", 1600, 800, 100, 50, blue, lightblue, "next"+str(part))
        else:
            HP = getHP() + HPadd
            ATK = getATK() + ATKadd
            DEF = getDEF() + DEFadd
            goldminus = (HPadd/2)*5 + ATKadd*5 + DEFadd*5
            gold = gold - goldminus
        if DEF1 != DEF:
            button("are you happy with your selection of this number of points to DEF:" + str(DEF - DEF1), 600, 300, 600, 50, blue, lightblue)
            ans = button("Yes", 600, 400, 150, 50, blue, lightblue, "yes")
            ans2 = button("No", 800, 400, 150, 50, blue, lightblue, "no")
            if ans == "yes":
                button("UPGRADE SUCCESSFUL", 600, 350, 300, 50, blue, lightblue)
            elif ans2 == "no":
                HP = HP1
                ATK = ATK1
                DEF = DEF1
                screen27(part)
        if ATK1 != ATK:
            button("are you happy with your selection of this number of points to ATK:" + str(ATK - ATK1), 600, 250, 600, 50, blue, lightblue)
            ans = button("Yes", 600, 400, 150, 50, blue, lightblue, "yes")
            ans2 = button("No", 800, 400, 150, 50, blue, lightblue, "no")
            if ans == "yes":
                button("UPGRADE SUCCESSFUL", 600, 350, 300, 50, blue, lightblue)
            elif ans2 == "no":
                HP = HP1
                ATK = ATK1
                DEF = DEF1
                screen27(part)
        if HP1 != HP:
            button("are you happy with your selection of this number of points to HP:" + str(HP - HP1), 600, 200, 600, 50, blue, lightblue)
            ans = button("Yes", 600, 400, 150, 50, blue, lightblue, "yes")
            ans2 = button("No", 800, 400, 150, 50, blue, lightblue, "no")
            if ans == "yes":
                button("UPGRADE SUCCESSFUL", 600, 350, 300, 50, blue, lightblue)
            elif ans2 == "no":
                HP = HP1
                ATK = ATK1
                DEF = DEF1
                screen27(part)
        pygame.display.update()


def screen28():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("BOSS: While plans are being made i have other tasks for you", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next28")
        button(str(getgold2()) + "g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()
def screen29():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Battle enemies (2 enemies with stats: Health: 60, Defense: 0, Damage: 15. Gold reward: 200)", 300, 600, 1200, 50, blue, lightblue, "battle4")
        button("Rescue. Gold reward(100g)", 300, 700, 1200, 50, blue, lightblue, "battle5")
        button("or training (After may choose to upgrade Health by 10, Damage by 5, or Defense by 5)", 300, 800, 1200, 50, blue, lightblue, "train1")
        pygame.display.update()
def battle4():
    global HP
    HP=getHP()
    EHP=60
    Edamage = 12
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene4Battle.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:"+str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:"+str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50,blue, lightblue,"ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            battle41()
        pygame.display.update()
def battle41():
    HP=getHP()
    EHP=60
    Edamage = 12
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene4Battle2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:"+str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:"+str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50,blue, lightblue,"ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            screen30()
        pygame.display.update()
def screen30():
    global gold,HP
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2.jpg')
    gold = getgold2()
    gold = gold + 200
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("BOSS: You did well here is your reward(200g)", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next30")
        button(str(gold)+"g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()
def train1():
    global HP
    Edamage = 12
    EHP = 60
    HP = getHP()
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2-1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            level1()
        pygame.display.update()
def level1():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("ADD 10 TO MAX HP", 300, 600, 1200, 50, blue, lightblue, "HP2")
        button("ADD 5 TO MAX DAMAGE", 300, 700, 1200, 50, blue, lightblue, "ATK2")
        button("ADD 5 TO MAX DEFENSE", 300, 800, 1200, 50, blue, lightblue, "DEF2")
        pygame.display.update()
def lvl11():
    global HP
    HP = getHP() + 10
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("God: Great choice! Your HP is now at " + str(HP), 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next30")
        pygame.display.update()
def lvl22():
    global ATK,HP
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    ATK = getATK() + 5
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("God: Great choice! Your ATK is now at "+str(ATK), 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next30")
        pygame.display.update()
def lvl33():
    global DEF,HP
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    DEF = getDEF()+5
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("GOD: Great choice! Your DEF is now at "+str(DEF), 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next30")
        pygame.display.update()
def rescue1():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene4Saving.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("You found her goodjob! now head back to the boss", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "pay1")
        pygame.display.update()
def pay11():
    global gold
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2.jpg')
    gold = getgold2()
    gold = gold + 100
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("BOSS: You did well here is your reward(100g)", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next30")
        button(str(gold) + "g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()
def screen31():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene8.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Eureka: *HUH AM I DREAMING AGAIN?? WHAT IS THIS!??*", 300, 700, 1200, 50,blue,lightblue )
        button("next", 1600, 800, 100, 50, blue, lightblue,"next31")
        pygame.display.update()
def screen32():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene8.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("SUPER HUMAN ARMY AND CHAOS REIGNS", 300, 700, 1200, 50,blue,lightblue )
        button("next", 1600, 800, 100, 50, blue, lightblue,"next32")
        pygame.display.update()
def screen33():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("113: Hey you dont look so good?", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next33")
        pygame.display.update()
def screen34():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Its nothing dont mind me", 300, 600, 1200, 50, blue, lightblue, "next341")
        button("I had this dream... (explain)", 300, 700, 1200, 50, blue, lightblue, "next342")
        pygame.display.update()
def screen35():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("*EUREKA PLEASE HEAD TO THE HEAD OFFICE IMMEDIATELY*", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next35")
        pygame.display.update()
def screen36():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop",36)
        button("BOSS: Your next mission is to infiltrate the corporation and kidnap an important asset", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next36")
        pygame.display.update()
def screen37():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('EEE.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 37)
        button("EUREKA: looks like i can fight the guards or simply sneak through the ventilation shaft", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next37")
        pygame.display.update()
def screen38():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('EEE.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 38)
        button("FIGHT GUARDS (earn 200g)", 300, 600, 1200, 50, blue, lightblue, "battle6")
        button("Sneak in", 300, 700, 1200, 50, blue, lightblue, "next38")
        pygame.display.update()
def battle6():
    global HP
    HP=getHP()
    EHP=150
    Edamage = 10
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene10guards.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop",)
        button("EUREKA:"+str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:"+str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50,blue, lightblue,"ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        HP -= (damage/getATK())*10 - damage2 + damage3
        EHP -= damage
        if HP <= 0:
            fail()
        if EHP <= 0:
            screen39()
        pygame.display.update()
def screen39():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene10guards.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 39)
        button("Eureka: id better head to the ventilation room", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next39")
        pygame.display.update()
def screen40():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene10Vent.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 40)
        button("Eureka: I made it in alive", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next40")
        pygame.display.update()
def screen41():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene10Vent.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 41)
        button("Eureka: Am i really doing the right thing right now?", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next41")
        pygame.display.update()
def screen42():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene10Vent.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 42)
        button("Eureka: why am i suddenly thinking about this i should complete the mission", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next42")
        pygame.display.update()
def screen43():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene11.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 43)
        button("Eureka: *there he is, i should capture him immediately*", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next43")
        pygame.display.update()
def screen44():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene11.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 44)
        button("Familiar man: Ive been expecting you", 300, 700, 1200, 50, blue, lightblue, )
        button("next", 1600, 800, 100, 50, blue, lightblue, "next44")
        pygame.display.update()
def screen45():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene11.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 45)
        button("Eureka: how did you know i was coming", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next45")
        pygame.display.update()
def screen46():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene11.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 46)
        button("Familiar man: Its because you need my expertise to complete VENOM", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next46")
        pygame.display.update()
def screen47():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene11.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 47)
        button("Familiar man: Youre not taking me alive if thats what you are thinking because VENOM will lead to the end of the Human race", 300, 700, 1200, 50, blue, lightblue, )
        button("next", 1600, 800, 100, 50, blue, lightblue, "next47")
        pygame.display.update()
def screen48():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene12.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 48)
        button("Familiar man: ERICKA IS THAT YOU??", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next48")
        pygame.display.update()
def screen49():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene12.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 49)
        button("Ericka: *where have i heard that name before*", 300, 700, 1200, 50, blue, lightblue, )
        button("next", 1600, 800, 100, 50, blue, lightblue, "next49")
        pygame.display.update()
def screen50():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 50)
        button("Father: well One day Ericka, you are gonna do great things.You will have a greater impact in today’s society!",300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next50")
        pygame.display.update()
def screen51():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene12.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 51)
        button("Ericka: WHO THE HELL ARE YOU AND WHY DID YOU CALL ME THAT NAME", 300, 700, 1200, 50, blue, lightblue, )
        button("next", 1600, 800, 100, 50, blue, lightblue, "next51")
        pygame.display.update()
def screen52():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene12.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 52)
        button("Familiar man: because i am your father...", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next52")
        pygame.display.update()
def screen53():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene12.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 53)
        button("Ericka: THATS IMPOSSIBLE MY FATHER IS THE BOSS OF EEE NOT YOU!", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next53")
        pygame.display.update()
def screen54():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene12.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 54)
        button("Familiar man: Let me explain what happened", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next54")
        pygame.display.update()
def screen55():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene13.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 55)
        button("Familiar man: Your mother and i were the leading experts in human genetics at our prime", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next55")
        pygame.display.update()
def screen56():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene13.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 56)
        button("Familiar man: Then we got an offer from EEE but it seemed shady at the time so we declined", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next56")
        pygame.display.update()
def screen57():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene13.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 57)
        button("Familiar man: we never heard from them since that time", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next57")
        pygame.display.update()
def screen58():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene13.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 58)
        button("Familiar man: A few years later we had you", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next58")
        pygame.display.update()
def screen59():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene13.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 59)
        button("Familiar man: however your mother had complications with your birth and she became weak", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next59")
        pygame.display.update()
def screen60():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene13.2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 60)
        button("Familiar man: after a few more years we had a picnic when we got ambushed", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next60")
        pygame.display.update()
def screen61():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene13.2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 61)
        button("Familiar man: we were tranquilized and when we woke up you were gone", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next61")
        pygame.display.update()
def screen62():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene13.3.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 62)
        button("Familiar man: your mother became weaker and that motivated me to create a serum to keep her alive", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next62")
        pygame.display.update()
def screen63():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene13.3.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 63)
        button("Father: because i perfected the serum EEE wants to use me to create an army of superhumans", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next63")
        pygame.display.update()
def screen64():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('SCENE14superfinal.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 64)
        button("Eureka: *what do i do now, do i go back to the boss or betray them*", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next64")
        pygame.display.update()
def screen65():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('SCENE14superfinal.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 65)
        button("Father: Ericka do you want to see your mother", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next65")
        pygame.display.update()
def screen66():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('SCENE14superfinal.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 66)
        button("go and see her", 300, 600, 1200, 50, blue, lightblue, "mommy")
        button("decline", 300, 700, 1200, 50, blue, lightblue, "next66")
        pygame.display.update()
def mommy():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene15.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Father: There is your mother, she cant even move at all that is why i created the serum for her", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next66")
        pygame.display.update()
def screen67():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene16-repeated.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 67)
        button("side with my father to stop EEE", 300, 600, 1200, 50, blue, lightblue, "next167")
        button("continue on with my mission", 300, 700, 1200, 50, blue, lightblue, "next266")
        pygame.display.update()
def screen167():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene16-repeated.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 167)
        button("Father: we need to start by taking out the rat thats in our company", 300, 600, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "battlegood1")
        pygame.display.update()
def battlegood1():
    global HP
    HP = getHP()
    EHP = 70
    Edamage = 13
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene16.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            screen168()
        pygame.display.update()
def screen168():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene16.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 168)
        button("Let him go in exchange for entrance info to EEE", 300, 600, 1200, 50, blue, lightblue, "next1681")
        button("Kill him(200g)", 300, 700, 1200, 50, blue, lightblue, "next1682")
        pygame.display.update()
def screen169():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene16-repeated.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 169)
        button("Good job now lets head to EEE", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next169")
        pygame.display.update()
def screen170():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene17good.jpg')
    if info == 1 and ally == 1:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 170)
            button("Eureka: 113 you remember my dream? well now i have proof, lets take this company down", 300, 600, 1200, 50, blue, lightblue)
            button("next", 1600, 800, 100, 50, blue, lightblue, "next170")
            pygame.display.update()
    elif info == 1 and ally == 0:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 170)
            button("Eureka: 113 i need you to help me destroy this company", 300, 600, 1200, 50, blue, lightblue, "next170")
            button("Eureka: 113 either you get out of my way or die", 300, 800, 1200, 50, blue, lightblue, "battlegood2")
            pygame.display.update()
    else:
        battlegood2()
def battlegood2():
    global HP
    HP = getHP()
    EHP = 90
    Edamage = 14
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene17good.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            screen1711()
        pygame.display.update()
def screen1711():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene17bad.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 171)
        button("Eureka: im sorry my friend it had to be done", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next170")
        pygame.display.update()
def screen171():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene18.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 171)
        button("Eureka: Why isnt the boss here?", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next171")
        pygame.display.update()
def screen172():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene18miniboss.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 172)
        button("Eureka: looks like he left one of his lackeys here. Time to take you out", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "battlegood3")
        pygame.display.update()
def battlegood3():
    global HP
    HP = getHP()
    EHP = 120
    Edamage = 15
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene18miniboss.jpg')
    if getALLY() == 1:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("113 bonus(2x ATK)", 100, 100, 200, 50, blue, lightblue)
            button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
            button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
            damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
            damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
            damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
            if damage == None:
                damage = 0
            if damage2 == None:
                damage2 = 0
            if damage3 == None:
                damage3 = 0
            if damage != 0:
                HP -= Edamage
                EHP -= damage*2
            if damage2 != 0:
                HP += damage2 - Edamage
            if damage3 != 0:
                HP -= damage3
            if HP <= 0:
                fail()
            if EHP <= 0:
                screen173()
            pygame.display.update()
    else:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
            button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
            damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
            damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
            damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
            if damage == None:
                damage = 0
            if damage2 == None:
                damage2 = 0
            if damage3 == None:
                damage3 = 0
            if damage != 0:
                HP -= Edamage
                EHP -= damage
            if damage2 != 0:
                HP += damage2 - Edamage
            if damage3 != 0:
                HP -= damage3
            if HP <= 0:
                fail()
            if EHP <= 0:
                screen173()
            pygame.display.update()
def screen173():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene18dead.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 173)
        button("Eureka: now that he is taken care of time to search for clues", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next173")
        pygame.display.update()
def screen174():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene18video.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 174)
        button("Boss: well hello there Eureka, you must be wondering why i am not in my office right now", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next174")
        pygame.display.update()
def screen175():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene18video.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 175)
        button("Boss: Thats because i anticipated that you would betray me so i sent a different agent in your stead", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next175")
        pygame.display.update()
def screen176():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene18video.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 176)
        button("Boss: i now have the ability to create a superhuman army within 48 hours", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next176")
        pygame.display.update()
def screen177():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene18video.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 177)
        button("Boss: I guess this will serve as our goodbye because i placed a time bomb within the building :)", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next177")
        pygame.display.update()
def screen178():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene18video.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 178)
        button("Boss: Goodbye Eureka it was fun while it lasted", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next178")
        pygame.display.update()
def screen179():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene17good.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 179)
        button("Eureka: 113 TELL EVERYBODY TO EVACUATE THE BUILDING RIGHT NOW", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next179")
        pygame.display.update()
def screen180():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene19.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 180)
        button("Eureka: Everybody got out safe, goodjob everyone", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next180")
        pygame.display.update()
def screen180():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene19.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 180)
        button("Eureka: Everybody got out safe, goodjob everyone", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next180")
        pygame.display.update()
def screen181():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene20.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 181)
        button("Eureka: Father the boss has escaped, what do we do now", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next181")
        pygame.display.update()
def screen182():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene20.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 182)
        button("Father: i think we could target one of his old associates", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next182")
        pygame.display.update()
def screen183():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene21.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 183)
        button("Eureka: you must be the old associate, so are you gonna tell me where he is or do we have to make this complicated", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next183")
        pygame.display.update()
def screen184():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene21.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 184)
        button("Associate: i dont even know what youre talking about", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next184")
        pygame.display.update()
def screen185():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene21.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 185)
        button("Eureka: looks like this is going to be complicated", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "battlegood4")
        pygame.display.update()
def battlegood4():
    global HP
    HP = getHP()
    EHP = 120
    Edamage = 15
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene21fightscene.jpg')
    if getALLY() == 1:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("113 bonus(2x ATK)", 100, 100, 200, 50, blue, lightblue)
            button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
            button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
            damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
            damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
            damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
            if damage == None:
                damage = 0
            if damage2 == None:
                damage2 = 0
            if damage3 == None:
                damage3 = 0
            if damage != 0:
                HP -= Edamage
                EHP -= damage*2
            if damage2 != 0:
                HP += damage2 - Edamage
            if damage3 != 0:
                HP -= damage3
            if HP <= 0:
                fail()
            if EHP <= 0:
                screen186()
            pygame.display.update()
def screen186():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene21.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 186)
        button("kill him", 300, 600, 1200, 50, blue, lightblue, "next1861")
        button("let him go (gain berserk ability)", 300, 700, 1200, 50, blue, lightblue, "next1862")
        pygame.display.update()
def screen187():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene21.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 187)
        button("Eureka: well i got what i needed time to head back", 300, 600, 1200, 50, blue, lightblue)
        button("next", 300, 700, 1200, 50, blue, lightblue, "next187")
        pygame.display.update()
def screen188():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene20.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 188)
        button("Eureka: he is at the basement of EEE lets head out", 300, 600, 1200, 50, blue, lightblue)
        button("next", 300, 700, 1200, 50, blue, lightblue, "next188")
        pygame.display.update()
def battlegood5():
    global HP
    HP = getHP()
    EHP = 150
    Edamage = 15
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene22.jpg')
    if getALLY() == 1:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("113 bonus(2x ATK)", 100, 100, 200, 50, blue, lightblue)
            button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
            button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
            damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
            damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
            damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
            if damage == None:
                damage = 0
            if damage2 == None:
                damage2 = 0
            if damage3 == None:
                damage3 = 0
            if damage != 0:
                HP -= Edamage
                EHP -= damage * 2
            if damage2 != 0:
                HP += damage2 - Edamage
            if damage3 != 0:
                HP -= damage3
            if HP <= 0:
                fail()
            if EHP <= 0:
                screen173()
            pygame.display.update()
    else:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
            button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
            damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
            damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
            damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
            if damage == None:
                damage = 0
            if damage2 == None:
                damage2 = 0
            if damage3 == None:
                damage3 = 0
            if damage != 0:
                HP -= Edamage
                EHP -= damage
            if damage2 != 0:
                HP += damage2 - Edamage
            if damage3 != 0:
                HP -= damage3
            if HP <= 0:
                fail()
            if EHP <= 0:
                battlegood51()
            pygame.display.update()
def battlegood51():
    global HP
    HP = getHP()
    EHP = 120
    Edamage = 15
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene22.1.jpg')
    if getALLY() == 1:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("113 bonus(2x ATK)", 100, 100, 200, 50, blue, lightblue)
            button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
            button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
            damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
            damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
            damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
            if damage == None:
                damage = 0
            if damage2 == None:
                damage2 = 0
            if damage3 == None:
                damage3 = 0
            if damage != 0:
                HP -= Edamage
                EHP -= damage * 2
            if damage2 != 0:
                HP += damage2 - Edamage
            if damage3 != 0:
                HP -= damage3
            if HP <= 0:
                fail()
            if EHP <= 0:
                screen173()
            pygame.display.update()
    else:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
            button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
            damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
            damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
            damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
            if damage == None:
                damage = 0
            if damage2 == None:
                damage2 = 0
            if damage3 == None:
                damage3 = 0
            if damage != 0:
                HP -= Edamage
                EHP -= damage
            if damage2 != 0:
                HP += damage2 - Edamage
            if damage3 != 0:
                HP -= damage3
            if HP <= 0:
                fail()
            if EHP <= 0:
                screen189()
            pygame.display.update()
def screen189():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene23.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 189)
        button("Eureka: Father its finished we did it", 300, 600, 1200, 50, blue, lightblue)
        button("next", 300, 700, 1200, 50, blue, lightblue, "next189")
        pygame.display.update()
def screen190():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene23.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 189)
        button("Eureka: Father its finished we did it", 300, 600, 1200, 50, blue, lightblue)
        button("next", 300, 700, 1200, 50, blue, lightblue, "next189")
        pygame.display.update()

def screen267():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene16kidnap.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 267)
        button("Eureka: im sorry father but i have to finish my job", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next267")
        pygame.display.update()
def screen268():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene16meetup.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 268)
        button("Eureka: you must be the rat, i got the asset lets head back to the boss", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next268")
        pygame.display.update()
def screen269():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene16meetup.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 269)
        button("Rat: sure i was getting tired of this place anyway", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next269")
        pygame.display.update()
def screen270():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 270)
        button("Boss: well done eureka, now we just need time to perfect VENOM, you can go on other missions while you wait", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next270")
        pygame.display.update()
def screen271():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 271)
        button("Battle enemies (2 enemies with stats: Health: 60, Defense: 0, Damage: 15. Gold reward: 200)", 300, 600, 1200, 50, blue, lightblue, "battlebad1")
        button("Rescue. Gold reward(100g)", 300, 700, 1200, 50, blue, lightblue, "rescue2")
        button("or training (After may choose to upgrade Health by 10, Damage by 5, or Defense by 5)", 300, 800, 1200, 50, blue, lightblue, "train2")
        pygame.display.update()
def battlebad1():
    global HP
    HP=getHP()
    EHP=60
    Edamage = 12
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene4Battle.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:"+str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:"+str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50,blue, lightblue,"ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            battlebad12()
        pygame.display.update()
def battlebad12():
    HP=getHP()
    EHP=60
    Edamage = 12
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene4Battle2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:"+str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:"+str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50,blue, lightblue,"ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            screen272()
        pygame.display.update()
def screen272():
    global gold,HP
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2.jpg')
    gold = getgold2()
    gold = gold + 200
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 272)
        button("BOSS: You did well here is your reward(200g)", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next272")
        button(str(gold)+"g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()
def train2():
    global HP
    Edamage = 12
    EHP = 60
    HP = getHP()
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2-1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            level2()
        pygame.display.update()
def level2():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("ADD 10 TO MAX HP", 300, 600, 1200, 50, blue, lightblue, "HP2")
        button("ADD 5 TO MAX DAMAGE", 300, 700, 1200, 50, blue, lightblue, "ATK2")
        button("ADD 5 TO MAX DEFENSE", 300, 800, 1200, 50, blue, lightblue, "DEF2")
        pygame.display.update()
def lvl41():
    global HP
    HP = getHP() + 10
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("God: Great choice! Your HP is now at " + str(HP), 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next272")
        pygame.display.update()
def lvl42():
    global ATK,HP
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    ATK = getATK() + 5
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("God: Great choice! Your ATK is now at "+str(ATK), 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next272")
        pygame.display.update()
def lvl43():
    global DEF,HP
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    DEF = getDEF()+5
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("GOD: Great choice! Your DEF is now at "+str(DEF), 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next272")
        pygame.display.update()
def rescue2():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene4Saving.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("You found her goodjob! now head back to the boss", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "pay2")
        pygame.display.update()
def pay12():
    global gold
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2.jpg')
    gold = getgold2()
    gold = gold + 100
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("BOSS: You did well here is your reward(100g)", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next272")
        button(str(gold) + "g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()

def screen273():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene1.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 273)
        button("Eureka: A lot of things happened today, i didnt expect to meet my real father", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next273")
        pygame.display.update()
def screen274():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene1.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 274)
        button("*ATTENTION ALL AGENTS PLEASE HEAD TO THE HEAD OFFICE, THERE HAS BEEN AN ESCAPE*", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next274")
        pygame.display.update()
def screen275():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 275)
        button("Boss: YOUR FATHER JUST TOOK THE PERFECTED SERUM AND ESCAPED! I WANT HIM BACK DEAD OR ALIVE", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next275")
        pygame.display.update()
def screen276():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 276)
        button("Eureka: I'll head to the company immediately", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next276")
        pygame.display.update()
def screen277():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene10Guards.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 277)
        button("Eureka: Looks like i have to force myself in", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "battlebad2")
        pygame.display.update()
def battlebad2():
    global HP
    HP=getHP()
    EHP=200
    Edamage = 14
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene10Guards.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:"+str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:"+str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50,blue, lightblue,"ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            screen278()
        pygame.display.update()
def screen278():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene20.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 278)
        button("Eureka: Father youre going to have to come with me, if you resist you die", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next278")
        pygame.display.update()
def screen279():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene20.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 279)
        button("Father: Eureka please think about what youre doing. The entire human race is in danger", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next279")
        pygame.display.update()
def screen280():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene20.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 280)
        button("Eureka: I dont care im just here to do what the boss ordered me to do", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next280")
        pygame.display.update()
def screen281():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene21fight.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 281)
        button("Disguised113: EUREKA IM HERE TO STOP YOU BECAUSE I BELIEVE IN THE DOCTORS VISIONS SO I HELPED HIM ESCAPE", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "battlebad3")
        pygame.display.update()
def battlebad3():
    global HP
    HP = getHP()
    EHP = 200
    Edamage = 14
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene21fight.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            screen282()
        pygame.display.update()
def screen282():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene21fight.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 282)
        button("Eureka: im sorry my friend it had to be done", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "screen282")
        pygame.display.update()
def screen283():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene22.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 283)
        button("Eureka: looks like they hired more henchmen to stop me", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "battlebad4")
        pygame.display.update()
def battlebad4():
    global HP
    HP = getHP()
    EHP = 150
    Edamage = 14
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene22.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            battlebad41()
        pygame.display.update()
def battlebad41():
    global HP
    HP = getHP()
    EHP = 200
    Edamage = 14
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene22.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            screen284()
        pygame.display.update()
def screen284():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene23decision.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 284)
        button("Eureka: well hello there father", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next284")
        pygame.display.update()
def screen285():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene23decision.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 285)
        button("Father: i always wonder what could have happened if you were not kidnapped", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next285")
        pygame.display.update()
def screen286():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene23decision.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 286)
        button("Father: we could have changed the world for the better ericka please think this through", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next286")
        pygame.display.update()
def screen287():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene23decision.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 286)
        button("Bring them back to EEE", 300, 600, 1200, 50, blue, lightblue, "screenbad")
        button("Kill both of them", 300, 700, 1200, 50, blue, lightblue, "screenbadd")
        button("Change of heart and go fight EEE", 300, 800, 1200, 50, blue, lightblue, "screenbaddd")
        pygame.display.update()
def screenbad():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene24bad1.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop")
        button("Boss: good job eureka, now lets start this off by making your parents our first test subjects", 300, 600,1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "credits")
        pygame.display.update()
def screenbadd():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene24bad1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop")
        button("Boss: good job eureka, i can now appoint you as leader of the new superhuman army we are about to create", 300, 600,1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "credits")
        pygame.display.update()
def screenbadd2():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene25bad.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop")
        button("Eureka went on to become the leader of an army to take down any resistance as EEE took over the world", 300, 600,1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "screenbadd2")
        pygame.display.update()
def screenbaddd():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene24bad3.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 286)
        button("Father: we could have changed the world for the better ericka please think this through", 300, 600,1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next286")
        pygame.display.update()
def fail():
    gameDisplay.fill(black)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        messagescreen("YOU HAVE FAILED", white, 0, "large")
        messagescreen("THERE IS NO GOING BACK NOW", white, 100, "medium")
        button("NEW GAME", 800, 600, 200, 50, blue, lightblue, "start")
        pygame.display.update()
intro()
pygame.quit()
quit()
