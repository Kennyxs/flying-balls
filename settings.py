import menu 
from basecommand import *
WHITE = [255,255,255]
YELLOW = [255,209,0]
GREEN = [93,255,0]
BLUE = [0,35,255]
RED = [255,0,46]
GREY = [167,171,173]
COLOURS =[WHITE,YELLOW,GREEN,BLUE,RED,GREY]
HEIGHT = 500
WEIDTH = 500
DIFERENT = [[WEIDTH//2, HEIGHT//8],[WEIDTH//2, HEIGHT//8*7],[HEIGHT//2, WEIDTH//8],[HEIGHT//2,WEIDTH//8*7] ]
COLOR = menu.slovar.get('chosec')
NAME =  menu.slovar.get('name')
MANYENEMY = int(menu.slovar.get('puter'))
TRYES = ifs(NAME)
if TRYES == False:
    tables(NAME)
RECORD = player(NAME)
TOP = top()