#surnuaed
import time
import random
import pickle
from os.path import exists
from threading import Timer








tutorial = 0
progression = 0
fighton = 0
hitchance = 0
enemybasemaxhealth = 2.0
enemymaxhealth = 2.0
enemyhealth = 0.0
enemydamage = 1
enemyattacks = ['löö']
yourattacks = ['löö']
yourmaxhealth = 5
yourhealth = 0
yourdamage = 1
yourattackchoice = ''
enemyattackchoice = ''
enemyskipping = 0
yourskipping = 0
bossfight = 0
difficulty = 'lühem'
hitdone = 1


STR = 1 #strenghte
DEF = 1 #defence
INT = 1 #intelligente
STRexp = 0
DEFexp = 0
INTexp = 0


def printend():
    print('märkad surnuaia väljapääsu, aga selle ees paikneb suur ümberkukkunud puu')
    a()
    print('mäletad, et said rootsi laevakaptenilt kirve, millega saad puu lõhkuda')
    a()
    print('lõhud ära ümberkukkunud puu')
    a()
    print('jõudsid elusalt surnuaiast välja ja sammud edasi Haapsalu poole')
    print('██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗')
    a()
    print('╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║████╗░██║')
    time.sleep(0.2)
    print('░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║')
    time.sleep(0.5)
    print('░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║██║╚████║')
    a()
    print('░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║')
    time.sleep(0.2)
    print('░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝')
    a()
    print('(1) alusta uuesti mängu')
    print('(2) lahku')
    choice = int(input('mida teed? '))
    while True:
        if choice == 1:
            break
            reset()
        elif choice == 2:
            exit()
        else:
            print('\n \n')
            print('Valik ei olnud õige, vali uuesti!')
    
def menu():
    fileexists = exists('save.dat')
    print('(1) hakka mängima')
    print('(2) lahku')
    print('(3) õpetus')
    if fileexists == True:
        print('(4) laadi salvestus')
    try:
        choice = int(input('mida teed? '))
    except:
        print('\n \n')
        print('Valik ei olnud õige, vali uuesti!')
        menu()
    if choice == 1:
        startgame()
    elif choice == 2:
        exit()
    elif choice == 3:
        learn()
    elif choice == 4 and fileexists == True:
        load()
    else:
        print('\n \n')
        print('Valik ei olnud õige, vali uuesti!')
        menu()
def learn():
    print('\n Pikem tee == 10 levelit Level 11 on lõpuboss\n Lühem tee == 8 levelit (vastastel 25% rohkem elusid) Level 11 on lõpuboss\n Legaalsed liigutused:\n Jalaga, rohkem dmg (2)  väiksem löögi võimalus 80% \n Millal saab lahti: STR 2\n Müksamine, lükkab vastase 2 käiguks ümber võimalus 60%\n Millal saab lahti:i DEF 2\n Peaga ründamine, teeb vastase kahjutuks 3-meks käiguks, kui ei saa pihta siis jääd ise 1 käigu vahele\n Millal saab lahti: STR 4\n lollitamine võimaldab sul loolitada ja kuidagi moodi vastasele dmg(15) extreemselt väike võimalus 1%\n Millal saab lahti: INT 3\n Kui palju exp saab lühemal teel: 0 - 20\n Kui palju exp saab pikal teel: 0 -10\n Kui palju et level uppida: 30 \n')
    menu()
def startgame():
    global tutorial
    global progression
    global enemybasemaxhealth
    global difficulty
    if tutorial == 0:
        print('liigud haapsalu poole')
        a()
        print('poole tee peale jääb surnuaed')
        a()
        print('ainuke viis haapsalusse minna on läbi surnuaia')
        a()
        print('tee läheb kaheks')
        a()
        while True:
            difficulty = input('vali kas lühem tee või pikem tee: ')
            if difficulty == 'lühem' or difficulty == 'pikem':
                if difficulty == 'lühem':
                    enemybasemaxhealth *= 1.25
                break
            else:
                print('\n \n')
                print('Valik ei olnud õige, vali uuesti!')
        print('sinu poole jalutab imeliku väljanägemisega tegelane')
        a()
        print('järsku ta ründab sind')
        a()
        print('enda kaitseks pead ta nüüd ära võitma')
        a()
        tutorial = 1
    fightstart()
    while True:
        if fighton == 1:
            yourturnexe()
        if fighton == 1:
            enemyturnexe()
        if fighton == 0:
            if progression == 7 and difficulty == 'lühem':
                enemyboss()
                break
            elif progression == 12 and difficulty == 'pikem' :
                enemyboss()
                break
            else:
                walking()
def hit():
    global yourhealth
    global hitdone
    print('said ta kirvega pihta -2 elud')
    yourhealth -=2
    hitdone = 1
    if yourhealth < 1:
        hitdone = 0
        lost()
    print('vajuta Enter et edasi minna')
    
    
def enemyboss():
    global bossfight
    global enemyhealth
    global yourhealth
    global enemymaxhealth
    global yourmaxhealth
    global fighton
    bossfight = 1
    enemymaxhealth = 20
    enemyhealth = enemymaxhealth
    yourhealth = yourmaxhealth
    print('oled jõudnud viimase vastaseni, ROOTSI LAEVA KAPTEN!!!')
    a()
    while True:
        if hitdone == 1 and bossfight == 1:
            yourturnexe()
    
def enemybossattack():
    global hitdone
    t = Timer(2, hit)
    t.start()
    hitdone = 0
    answer = input('ta viskas sind kirvega \nkirjuta "liigu" et tema löök tõrjuda\n\n')
    if answer == 'liigu' and hitdone == 0:
        t.cancel()
        print('tõrjusid ta kirve \n ')
        hitdone = 1
        yourturnexe()


def a():
    time.sleep(1.5)
    
def reset():
    global STR
    global DEF
    global INT
    global tutorial
    global progression
    global fighton
    global hitchance
    global enemybasemaxhealth
    global enemymaxhealth
    global enemyhealth
    global enemydamage
    global enemyattacks
    global yourattacks
    global yourmaxhealth
    global yourhealth
    global yourdamage
    global yourattackchoice
    global enemyattackchoice
    global enemyskipping
    global yourskipping
    global bossfight
    global difficulty
    global hitdone
    
    tutorial = 0
    progression = 0
    fighton = 0
    hitchance = 0
    enemybasemaxhealth = 2.0
    enemymaxhealth = 2.0
    enemyhealth = 0.0
    enemydamage = 1
    enemyattacks = ['löö']
    yourattacks = ['löö']
    yourmaxhealth = 5
    yourhealth = 0
    yourdamage = 1
    yourattackchoice = ''
    enemyattackchoice = ''
    enemyskipping = 0
    yourskipping = 0
    bossfight = 0
    difficulty = 'lühem'
    hitdone = 1
    
    menu()
    
def save():
    global yourattacks
    global yourmaxhealth
    global progression
    global tutorial
    global STR
    global DEF
    global INT
    global difficulty
    with open('save.dat', 'wb') as write:
        pickle.dump(yourattacks, write)
        pickle.dump(yourmaxhealth, write)
        pickle.dump(progression, write)
        pickle.dump(tutorial, write)
        pickle.dump(STR, write)
        pickle.dump(DEF, write)
        pickle.dump(INT, write)
        pickle.dump(difficulty, write)

def load():
    global yourattacks
    global yourmaxhealth
    global progression
    global tutorial
    global STR
    global DEF
    global INT
    global difficulty
    with open('save.dat', 'rb') as read:
        yourattacks = pickle.load(read)
        yourmaxhealth = pickle.load(read)
        progression = pickle.load(read)
        tutorial = pickle.load(read)
        STR = pickle.load(read)
        DEf = pickle.load(read)
        INT = pickle.load(read)
        difficulty = pickle.load(read)
    print('laaditud \n')
    menu()

def fightstart():
    global enemyhealth
    global yourhealth
    global enemymaxhealth
    global yourmaxhealth
    global fighton
    global enemybasemaxhealth
    enemymaxhealth = enemybasemaxhealth * (1+ (float(progression) * 0.1))
    print('\nvastane: ', end = '')
    enemies = ['surnud kurjategija', 'surnud õpetaja']
    print(random.choice(enemies))
    fighton = 1
    enemyhealth = enemymaxhealth
    yourhealth = yourmaxhealth
    
def endfight():
    global fighton
    global progression
    global STRexp
    global DEFexp
    global INTexp
    global STR
    global DEF
    global INT
    global yourattacks
    global yourmaxhealth
    global difficulty
    if difficulty == 'lühem':
        STRexpc = random.randint(0,20)
        DEFexpc = random.randint(0,20)
        INTexpc = random.randint(0,20)
    else:
        STRexpc = random.randint(0,10)
        DEFexpc = random.randint(0,10)
        INTexpc = random.randint(0,10)
    STRexp += STRexpc
    DEFexp += DEFexpc
    INTexp += INTexpc
    present = 1
    fighton = 0
    progression += 1
    print('võitsid vastase')
    print(f'said {STRexpc} STR exp')
    print(f'{STRexp}/30 STR exp')
    print(f'said {DEFexpc} DEF exp')
    print(f'{DEFexp}/30 STR exp')
    print(f'said {INTexpc} INT exp')
    print(f'{INTexp}/30 STR exp')
    if STRexp >= 30:
        STR += 1
        STRexp = 0
        yourmaxhealth += 1
    elif DEFexp >= 30:
        DEF += 1
        DEFexp = 0
    elif INTexp >= 30:
        INT += 1
        INTexp = 0
    print(f'STR level {STR}')
    print(f'DEF level {DEF}')
    print(f'INT level {INT}')
    if STR == 2:
        for attack in yourattacks:
            if attack == 'jalalöök':
                present = 1
                break
            else:
                present = 0
        if present == 0:
            yourattacks.append('jalalöök')
    if DEF == 2:
        for attack in yourattacks:
            if attack == 'müksa':
                present = 1
                break
            else:
                present = 0
        if present == 0:
            yourattacks.append('müksa')
    if STR == 4:
        for attack in yourattacks:
            if attack == 'peaga':
                present = 1
                break
            else:
                present = 0
        if present == 0:
            yourattacks.append('peaga')
    if INT == 3:
        for attack in yourattacks:
            if attack == 'lollita':
                present = 1
                break
            else:
                present = 0
        if present == 0:
            yourattacks.append('lollita')
    

    
    
def lost():
    global fighton
    fighton = 0
    print('██╗░░░██╗░█████╗░██╗░░░██╗  ██████╗░██╗███████╗██████╗░')
    time.sleep(0.1)
    print('╚██╗░██╔╝██╔══██╗██║░░░██║  ██╔══██╗██║██╔════╝██╔══██╗')
    time.sleep(0.2)
    print('░╚████╔╝░██║░░██║██║░░░██║  ██║░░██║██║█████╗░░██║░░██║')
    time.sleep(0.3)
    print('░░╚██╔╝░░██║░░██║██║░░░██║  ██║░░██║██║██╔══╝░░██║░░██║')
    time.sleep(0.2)
    print('░░░██║░░░╚█████╔╝╚██████╔╝  ██████╔╝██║███████╗██████╔╝')
    time.sleep(0.1)
    print('░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚═════╝░╚═╝╚══════╝╚═════╝░')
    print('(1) laadi viimane salvestus')
    print('(2) alusta algusest')
    lostchoice = input('Mille valid? ')
    if lostchoice == '1':
        load()
    elif lostchoice == '2':
        reset()
    else:
        print('\n \n')
        print('Valik ei olnud õige, vali uuesti!')
        lost()
        
def walking():
    global progression
    print(f'kaugus {progression}')
    print()
    print('liigud edasi')
    save()
    fightstart()
    
    
def turnend():
    global enemyhealth
    global yourhealth
    global enemymaxhealth
    global yourmaxhealth
    print(f'vastase elud {enemyhealth}/{enemymaxhealth}')
    print(f'sinu elud {yourhealth}/{yourmaxhealth} \n')
    
def yourturnexe():
    global enemyskipping
    global yourattackchoice
    global yourattacks
    enemyskipping -= 1
    valid = 0
    text = 'ründamisvalikud: '
    for yourattackstr in yourattacks:
        if yourattackstr == yourattacks[0]:
            text += f'{yourattackstr}'
        else:
            text += f', {yourattackstr}'
    print(text)
    yourattackchoice = input('vali kuidas teda ründad: ')
    for attack in yourattacks:
        if yourattackchoice == attack:
            valid = 1
            break
    if valid == 1:
        yourattack(yourattackchoice)
    else:
        print('\n \n')
        print('Valik ei olnud õige, vali uuesti!')
        yourturnexe()
        
    
def yourattack(yourattackchoicestr):
    global enemyhealth
    global yourdamage
    global hitchance
    global yourskipping
    global enemyskipping
    global bossfight
    hitchance = random.randint(0, 10000)
    if yourattackchoicestr == 'löö':
        yourdamage = 1
        if hitchance > 9500:
            print('sa lõid mööda \n')
        else:
            enemyhealth -= yourdamage
            print(f'vastase elud -{yourdamage} \n')
        if enemyhealth <= 0:
            if bossfight == 1:
                bossfight = 0
                printend()
            else:
                endfight()
        else:
            turnend()
    elif yourattackchoicestr == 'lollita':
        yourdamage = 15
        if hitchance > 100:
            print('HAHA sa ei saanud lollitamisega hakkama \n')
        else:
            enemyhealth -= yourdamage
            print(f'vastase elud -{yourdamage} \n')
        if enemyhealth <= 0:
            if bossfight == 1:
                bossfight = 0
                printend()
            else:
                endfight()
        else:
            turnend()
    elif yourattackchoicestr == 'jalalöök':
        yourdamage = 2
        if hitchance > 8000:
            print('sa lõid mööda \n')
        else:
            enemyhealth -= yourdamage
            print(f'vastase elud -{yourdamage} \n')
        if enemyhealth <= 0:
            if bossfight == 1:
                bossfight = 0
                printend()
            else:
                endfight()
        else:
            turnend()
    elif yourattackchoicestr == 'müksa':
        yourdamage = 2
        if hitchance > 6000:
            print('müksasid mööda \n')
        else:
            enemyskipping = 2
            print('vastane ei saa käia kaks korda \n')
        if enemyhealth <= 0:
            if bossfight == 1:
                bossfight = 0
                printend()
            else:
                endfight()
        else:
            turnend()
    elif yourattackchoicestr == 'peaga':
        yourdamage = 2
        if hitchance > 4000:
            print('lõid peaga mööda oled uimane jääd korra vahele \n')
            yourskipping = 2
        else:
            enemyskipping = 3
            print('vastane ei saa käia 3 korda \n')
        if enemyhealth <= 0:
            if bossfight == 1:
                bossfight = 0
                printend()
            else:
                endfight()
        else:
            turnend()
    if bossfight == 1:
        enemybossattack()
    
    

def enemyturnexe():
    global enemyattackchoice
    global yourskipping
    yourskipping -= 1
    enemyattackchoice = random.choice(enemyattacks)
    
    enemyattack(enemyattackchoice)
    
def enemyattack(enemyattackchoicestr):
    global yourhealth
    global enemydamage
    print(f'vastane kasutab {enemyattackchoicestr}')
    if enemyattackchoicestr == 'löö':
        print('vastane sai pihta')
        yourhealth -= enemydamage
        print(f'sinu elud -{enemydamage} \n')
        if yourhealth == 0:
            print('sa kaotasid')
            lost()
        else:
            turnend()
    
        
        
    
    
    
lost()


