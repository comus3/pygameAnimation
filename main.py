#question : pq import random marche pas( aller voir où il est appelé)
#comment changer la police du texte? comment rentrer texte dans boutons?
#comment implementer reset button? Il faut faire une finctuin qui va tout remettre aux vals? non. Je pref redemarrer le prog si possible

# initialisation de pygame
from msilib import text
import pygame
import pygame_gui
from pygame_gui.elements import UIButton, UITextEntryLine, UILabel, UIHorizontalSlider
import sys
import math
import random
pygame.init()





#init
screen = pygame.display.set_mode((1000,900))
clock = pygame.time.Clock()
manager = pygame_gui.UIManager((1000, 900))

j = 46   #radius augmment
timmm = 0  #time var
tres = True  #minte ou descend?
rotation = 0  #rien osef
nombreDeCercles = 0 #osef
nombreDeCerclesMax = 50 #nombre de cerlces dessines
rotDiv = 300 #a quel pt la rotation est lente
randomRotVar = False #est ce que on ajoute du random a la rot
maxDiameterVar = 400
minDiameterVar = 126
#textRandomRotationVar = 'Random rotation speed:False'  #osef
formationAngle = 18 #angle de formation dees cercles
sensDeRotation = 1 #sens de rotation
backgroundBool = False
special_mode = False
belek = 1
augmentationDist = 10 #augmentatino de distance au centre
augmentationDesRayons = 3 #diff de rayon des cercles entre eux
colorMultiOne = 30   # changements de couleur
colorMultiTwo = 10      #changements de couleur
colorMultiThree = 1     #changements de couleur
################   initialisation des bouttons




####### #     BOUTONS
random_Bouton = UIButton(
	relative_rect=pygame.Rect(900, 000, 100, 30),
	text='Random\nrotation',
	manager=manager
)
radius_Bouton = UIButton(
	relative_rect=pygame.Rect(790, 000, 100, 30),
	text='radius toggle',
	manager=manager
)
background_Bouton = UIButton(
	relative_rect=pygame.Rect(0, 400, 100, 70),
	text='background',
	manager=manager
)
special_Bouton = UIButton(
	relative_rect=pygame.Rect(0, 300, 100, 70),
	text='spécial',
	manager=manager
)
rreverse_Bouton = UIButton(
	relative_rect=pygame.Rect(0, 200, 100, 70),
	text='reverse',
	manager=manager
)

######### SLIDERS
sliderMaxD = UIHorizontalSlider(
    pygame.Rect((750,
    30),(240, 25)), 400, (2, 1000),
    manager = manager
)
sliderMinD = UIHorizontalSlider(
    pygame.Rect((750,
    80),(240, 25)), 126, (1, 120),
    manager = manager
)
circlesDrawnMax = UIHorizontalSlider(
    pygame.Rect((750,
    130),(240, 25)), 80, (1, 300),
    manager = manager
)
angleChange = UIHorizontalSlider(
    pygame.Rect((750,
    180),(240, 25)), 18, (1, 150),
    manager = manager
)
distanceChange = UIHorizontalSlider(
    pygame.Rect((750,
    230),(240, 25)), 10, (1, 25),
    manager = manager
)
colorChange1 = UIHorizontalSlider(
    pygame.Rect((750,
    530),(240, 25)), 30, (1, 70),
    manager = manager
)
colorChange2 = UIHorizontalSlider(
    pygame.Rect((750,
    580),(240, 25)), 10, (1, 25),
    manager = manager
)
colorChange3 = UIHorizontalSlider(
    pygame.Rect((750,
    630),(240, 25)), 1, (1, 60),
    manager = manager
)

########### infos


displayOfRot = UILabel(
	    relative_rect=pygame.Rect(750, 620, 250, 100),
	    text=str("Couleurs"),
	    manager=manager
    )
displayof = UILabel(
	    relative_rect=pygame.Rect(750, 53, 250, 20),
	    text=("max d"),
	    manager=manager
    )
displayof = UILabel(
	    relative_rect=pygame.Rect(750, 103, 250, 20),
	    text=("mindy"),
	    manager=manager
    )
displayof = UILabel(
	    relative_rect=pygame.Rect(750, 153, 250, 20),
	    text=("Max Circles"),
	    manager=manager
    )
displayof = UILabel(
	    relative_rect=pygame.Rect(750, 203, 250, 20),
	    text=("Angle change"),
	    manager=manager
    )
displayof = UILabel(
	    relative_rect=pygame.Rect(750, 253, 250, 20),
	    text=("distance change"),
	    manager=manager
    )




#run
while True:
    time_delta = clock.tick(60)

    ######################    partie bouttons(réactions)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == random_Bouton:
                if randomRotVar:randomRotVar = False
                else:randomRotVar = True
            if event.ui_element == background_Bouton:
                if backgroundBool:backgroundBool = False
                else: backgroundBool = True
            if event.ui_element == special_Bouton:
                if special_mode:
                    special_mode = False
                    if backgroundBool:backgroundBool = False
                else: special_mode = True
            if event.ui_element == rreverse_Bouton:
                if sensDeRotation == 1:sensDeRotation = -1 
                else:sensDeRotation = 1
            if event.ui_element == radius_Bouton:
                minDiameterVar = maxDiameterVar-1
                tres = True
        if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_element == sliderMaxD:
                maxDiameterVar = event.value
                tres = True
                j = minDiameterVar
            if event.ui_element == sliderMinD:
                minDiameterVar = event.value
            if event.ui_element == circlesDrawnMax:
                nombreDeCerclesMax = event.value
                nombreDeCercles = 0
            if event.ui_element == angleChange:
                formationAngle = event.value
            if event.ui_element == distanceChange:
                augmentationDist = event.value
            if event.ui_element == colorChange1:
                colorMultiOne = event.value
            if event.ui_element == colorChange2:
                colorMultiTwo = event.value
            if event.ui_element == colorChange3:
                colorMultiThree = event.value
            
        manager.process_events(event)
    manager.update(time_delta/1)
    def pos(ordonee):
        x = 40
        y  = ordonee*10
    
    target = (3,2)
    listedetuple = [(2,3),(4,0)]



    ######################    partie dessins et update des vars
    if not(special_mode):
        for i in range(nombreDeCercles):
            pygame.draw.circle(screen,(((colorMultiOne*i)+timmm)%255,((colorMultiTwo*i)-timmm)%255,((colorMultiThree*3)+timmm)%255),(450+(augmentationDist*i*math.cos((sensDeRotation*rotation)+(i*math.pi)/formationAngle)),450+(augmentationDist*i*math.sin((sensDeRotation*rotation)+(i*math.pi)/formationAngle))),i*augmentationDesRayons+ j)
    else:
        if belek == nombreDeCerclesMax: belek = 1
        for i in [belek,belek+1,belek+2,belek+3]:
            pygame.draw.circle(screen,(((colorMultiOne*i)+timmm)%255,((colorMultiTwo*i)-timmm)%255,((colorMultiThree*3)+timmm)%255),(450+(augmentationDist*i*math.cos((sensDeRotation*rotation)+(i*math.pi)/formationAngle)),450+(augmentationDist*i*math.sin((sensDeRotation*rotation)+(i*math.pi)/formationAngle))),i*augmentationDesRayons+ j)
        belek = belek+1



    inctn = (math.pi)/rotDiv  #incrementation de rotation
    if randomRotVar:
        leNombreFou = random.randrange(10)
        leNombreFou = leNombreFou - 5               #comment for no random rotation
        if 100<rotDiv: rotDiv = rotDiv + leNombreFou
        else: rotDiv = rotDiv + 5
    timmm = timmm + 1     
    if tres:
        j = j + 1
    else: j = j-1
    if j == maxDiameterVar: tres = False
    elif j == minDiameterVar: tres = True
    rotation = rotation + inctn
    if nombreDeCercles<nombreDeCerclesMax: nombreDeCercles = nombreDeCercles + 1

    # if randomRotVar:textRandomRotationVar = 'Random rotation speed:True'
    # else: textRandomRotationVar = 'Random rotation speed:False'
    

    ###############################  affichage 
    manager.draw_ui(screen)
    pygame.display.flip()
    if backgroundBool: pygame.draw.rect(screen, (125, 123, 15), pygame.Rect(0, 0, 1000, 900))
    


#      /\  ___\   /\  __ \   /\ "-./  \   
#      \ \ \____  \ \ \/\ \  \ \ \-./\ \  
# 	\ \_____\  \ \_____\  \ \_\ \ \_\ 
# 	 \/_____/   \/_____/   \/_/  \/_/ 
