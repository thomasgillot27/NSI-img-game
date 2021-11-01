"""
Programme réalisé par Gillot Thomas, 1G7
"""
import pygame

#initialisation graphique
pygame.init()
fenetre = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("jeu d'aventure")
font = pygame.font.Font('freesansbold.ttf', 25)

image0 = pygame.image.load("plan.png")

image1 = pygame.image.load("entree.png")
text1 = font.render("Vous êtes à l'entrée", True, (0, 0, 0))

image2 = pygame.image.load("salle-a-manger.png")
text2 = font.render("Vous êtes dans la salle à manger", True, (0, 0, 0))

image3 = pygame.image.load("salon.png")
text3 = font.render("Vous êtes dans le salon", True, (0, 0, 0))

image4 = pygame.image.load("couloir.png")
text4 = font.render("Vous êtes dans le couloir", True, (0, 0, 0))

image5 = pygame.image.load("cuisine.png")
text5 = font.render("Vous êtes dans la cuisine", True, (0, 0, 0))

image6 = pygame.image.load("chambre.png")
text6 = font.render("Vous êtes dans la chambre", True, (0, 0, 0))

image7 = pygame.image.load("garage.png")
text7 = font.render("Vous êtes dans le garage", True, (0, 0, 0))

image8 = pygame.image.load("cabane.png")
text8 = font.render("Vous êtes dans le cabanon", True, (0, 0, 0))
text88 = font.render("Vous avez trouvé la clé du grenier", True, (0, 0, 0))

image9 = pygame.image.load("grenier.png")
text9 = font.render("Vous êtes dans le grenier", True, (255, 255, 255))


Personnage=1
clé=0

def decrireLaPiece(piece):
    if piece==1:
        fenetre.blit(image1,(0,0))  #afficher l'image à la prochaine actualisation
        fenetre.blit(text1,(10,690)) #afficher le texte à la prochaine actualisation
        fenetre.blit(image0,(0,0))
    elif piece==2:
        fenetre.blit(image2,(0,0))
        fenetre.blit(text2,(10,690))
        fenetre.blit(image0,(0,0))
    elif piece==3:
        fenetre.blit(image3,(0,0))
        fenetre.blit(text3,(10,690))
        fenetre.blit(image0,(0,0))
    elif piece==4:
        fenetre.blit(image4,(0,0))
        fenetre.blit(text4,(10,690))
        fenetre.blit(image0,(0,0))
    elif piece==5:
        fenetre.blit(image5,(0,0))
        fenetre.blit(text5,(10,690))
        fenetre.blit(image0,(0,0))
    elif piece==6:
        fenetre.blit(image6,(0,0))
        fenetre.blit(text6,(10,690))
        fenetre.blit(image0,(0,0))
    elif piece==7:
        fenetre.blit(image7,(0,0))
        fenetre.blit(text7,(10,690))
        fenetre.blit(image0,(0,0))
    elif piece==8:
        fenetre.blit(image8,(0,0))
        fenetre.blit(text8,(10,690))
        fenetre.blit(image0,(0,0))
    elif piece==9:
        fenetre.blit(image9,(0,0))
        fenetre.blit(text9,(10,690))
        fenetre.blit(image0,(0,0))


def decision(direction,piece):    #la fonction decision permet de se déplacer
    memorisePiece=piece
    global clé

    if direction=='z':    #Z : le personnage désire aller au nord
        if piece==1:
            piece=4
        elif piece==4:
            piece=7
        elif piece==7:
            piece=8
            if clé==0:
                print("Vous avez trouvé la clé du grenier")
                clé=1

    elif direction=='s':    #S : le personnage désire aller au sud
        if piece==4:
            piece=1
        elif piece==7:
            piece=4
        elif piece==8:
            piece=7

    elif direction=='d':    #D : le personnage désire aller à l'est
        if piece==1:
            piece=2
        elif piece==3:
            piece=1
        elif piece==4:
            piece=5
        elif piece==6:
            piece=4
        elif piece==7 and clé==1:
            piece=9
        else:
            print("Vous devez trouvez le clé pour accédez au grenier")

    elif direction=='q':    #Q : le personnage désire aller à l'ouest
        if piece==1:
            piece=3
        elif piece==2:
            piece=1
        elif piece==5:
            piece=4
        elif piece==4:
            piece=6
        elif piece==9:
            piece=7

    if memorisePiece==piece:
        print("Deplacement impossible")
    return piece



loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN:  #lecture du clavier
            Personnage=decision(event.unicode,Personnage)
            if event.key == pygame.K_ESCAPE or event.unicode == 'l': #touche l pour quitter
                loop = False
    decrireLaPiece(Personnage)
    # Actualisation de l'affichage
    pygame.display.flip()
pygame.quit()

