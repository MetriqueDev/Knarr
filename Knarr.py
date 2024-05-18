import pygame
from classes.card import Card
from classes.board import Board
from classes.boat import Boat
from classes.player import Player
from classes.destination import Card_bateau
from classes.package import Package
from classes.hand import Hand
from classes.package_destination import Package_Destination
from classes.game import Game
from classes.input import Button , Input

import sqlite3


#PyGame setup
pygame.init()
screen = pygame.display.set_mode((1920,1080),pygame.RESIZABLE) #(1280, 720))

pygame.display.set_caption("Knarr")

running=True
clock = pygame.time.Clock()
step="main"
font = pygame.font.SysFont("arialblack", 40)
TEXT_COL = (255, 255, 255)

#Musique
#pygame.mixer.music.load(".\\musique\\Dragonborn.mp3")
#pygame.mixer.music.play()
#musique=True

#Background
background_load = pygame.image.load(".\\images\\fond.jpg").convert()
background= pygame.transform.scale(background_load, (1920,1080))
main_menu_bgload=pygame.image.load(".\\images\\gui\\pxArt.png").convert()
main_menu_bg = pygame.transform.scale(main_menu_bgload,(1920,1080))

#Fermeture
fermeture_size=30
fermeture_load = pygame.image.load(".\\images\\gui\\stop.png").convert_alpha()
fermeture= pygame.transform.scale(fermeture_load, (fermeture_size,fermeture_size))
fermeture_boutton= Button(screen.get_width()-40,10,fermeture,1)

btn_unselect_image_load=pygame.image.load(f".\\images\\gui\\btn_unselect.png").convert_alpha() 
btn_select_image_load=pygame.image.load(f".\\images\\gui\\btn_select.png").convert_alpha() 

connexion_boutton= Button(200,200,[btn_unselect_image_load,btn_select_image_load],5,font,"Connexion")

inscription_button= Button(200,350,[btn_unselect_image_load,btn_select_image_load],5,font,"inscription")

option_boutton= Button(200,500,[btn_unselect_image_load,btn_select_image_load],5,font,"Option")

#retour_image_load=pygame.image.load(f".\\images\\gui\\empty.png").convert_alpha() 
#retour_boutton= Button(750,500,retour_image_load,0.2)
#Initialisation propre
nbr_player=1
players=[]


liste=[]

active_card=None
mouse_pos=[0,0]



while running:
    #screen.fill((0,0,0))

    #Menu du début !!!!
    if step == "main":
        screen.blit(main_menu_bg,(0,0))

        
        if connexion_boutton.draw(screen):
            step="connexion"#Je déplace vers le menu de connexion 

            #J'initialise le nécessaire pour le menu de connexion
            connexion_title=font.render("Menu connexion",True,TEXT_COL)
            name_label=font.render("Votre nom:",True,TEXT_COL)
            input_name_image_load=pygame.image.load(f".\\images\\gui\\input.png").convert_alpha() 
            input_name_boutton= Input(200,250,input_name_image_load,2,font,TEXT_COL)
            mdp_label=font.render("Votre mot de passe:",True,TEXT_COL)
            input_mdp_image_load=pygame.image.load(f".\\images\\gui\\input.png").convert_alpha() 
            input_mdp_boutton= Input(200,450,input_name_image_load,2,font,TEXT_COL)
            valider_boutton= Button(200,700,[btn_unselect_image_load,btn_select_image_load],5,font,"Valider")
            retour_boutton= Button(200+20+5*96,700,[btn_unselect_image_load,btn_select_image_load],5,font,"Retour")

        if inscription_button.draw(screen):
            step="inscription"#Je déplace vers le menu d'inscription 

            #J'initialise le nécessaire pour le menu d'inscription
            inscription_title=font.render("Menu inscription",True,TEXT_COL)
            name_label=font.render("Votre nom:",True,TEXT_COL)
            input_name_image_load=pygame.image.load(f".\\images\\gui\\input.png").convert_alpha() 
            input_name_boutton= Input(200,250,input_name_image_load,2,font,TEXT_COL)
            mdp_label=font.render("Votre mot de passe:",True,TEXT_COL)
            input_mdp_image_load=pygame.image.load(f".\\images\\gui\\input.png").convert_alpha() 
            input_mdp_boutton= Input(200,450,input_name_image_load,2,font,TEXT_COL)

            valider_boutton= Button(200,700,[btn_unselect_image_load,btn_select_image_load],5,font,"Valider")
            retour_boutton= Button(200+20+5*96,700,[btn_unselect_image_load,btn_select_image_load],5,font,"Retour")

        if option_boutton.draw(screen):
            step="option"#Je déplace vers le menu d'option 

            #J'initialise le nécessaire pour le menu d'option
            valider_boutton= Button(200,700,[btn_unselect_image_load,btn_select_image_load],5,font,"Valider")
            retour_boutton= Button(200+20+5*96,700,[btn_unselect_image_load,btn_select_image_load],5,font,"Retour")

    #jeu boucle exécuté pour jouer !!!!
    if step == "play":
        jeu.update(screen,liste,font,name)#J'update le jeu

        #gestion du drag and drop (je vérifie si c'est le bon joeur qui essaie)
        for event in pygame.event.get():
            if jeu.players[jeu.turn%len(jeu.players)].name==name:
                jeu.event_handler(event,screen)

        #je le laisse icic car c'est personnel au joueur le déplacmeent de la carte pendnat le drag and drop
        if jeu.destination.active_card_e != None:
            jeu.destination.echange[jeu.destination.active_card_e].print(screen,(event.pos[0]-jeu.destination.offset_x,event.pos[1]-jeu.destination.offset_y))
        if jeu.destination.active_card_i != None:
            jeu.destination.influence[jeu.destination.active_card_i].print(screen,(event.pos[0]-jeu.destination.offset_x,event.pos[1]-jeu.destination.offset_y))
        if jeu.board.active_card_b !=None:
            jeu.board.pioche[jeu.board.active_card_b].print(screen,(event.pos[0]-jeu.board.offset_x,event.pos[1]-jeu.board.offset_y))
        

        #J'affiche la main du bon joueur...
        for player in jeu.players:
                if player.name==name:
                    player.hand.afficher_main(screen)
                    player.boat.print(screen)
                    player.boat.print_object(screen,liste)
                    player.boat.print_object(screen,jeu.destination.liste)
                    player.print_equipage(screen)

        if retour_boutton.draw(screen):
            print(step)
            step="main"
            option_boutton= Button(200,500,[btn_unselect_image_load,btn_select_image_load],5,font,"Option")

    #Menu pour jouer
    if step=="menu_play":
        screen.blit(main_menu_bg,(0,0))

        user_icone_btn.draw(screen)

        if jouer_boutton.draw(screen):
            
            screen.blit(main_menu_bg,(0,0))
            chargement_label=font.render("Chargement...",True,TEXT_COL)
            screen.blit(chargement_label,(int(screen.get_width()/2-chargement_label.get_width()/2),int(screen.get_height()/2-chargement_label.get_height())))
            pygame.display.update()
            pygame.mixer.music.load(".\\musique\\gui_sound\\start.wav")
            pygame.mixer.music.play()

            step="play"
            players=[]
            players.append(Player(name,niveau))
            players[0].game_init()
            
            players.append(Player("RobertoLeRobotRigolo",1,True))#Robot
            players[1].game_init()
            
            #for i in range(nbr_player):
            #    players.append(Player("Vladimir Ilitch",niveau))
            #    players[i].game_init()
            #    players[i].info()
            jeu=Game(players)
            jeu.init_image(screen)
            jeu.init_game(screen)

            



            retour_boutton= Button(screen.get_width()-5*96-10,screen.get_height()-32*5-10,[btn_unselect_image_load,btn_select_image_load],5,font,"Retour")

        if option_boutton.draw(screen):
            step="option"
            retour_boutton= Button(200+20+5*96,700,[btn_unselect_image_load,btn_select_image_load],5,font,"Retour")

        if retour_boutton.draw(screen):
            step="main"
            option_boutton= Button(200,500,[btn_unselect_image_load,btn_select_image_load],5,font,"Option")

    #Menu connexion
    if step == "connexion":
        screen.blit(main_menu_bg,(0,0))

        screen.blit(connexion_title,(200,100))
        screen.blit(name_label,(200,200))
        input_name_boutton.draw(screen)

        screen.blit(mdp_label,(200,400))
        input_mdp_boutton.draw(screen)

        if valider_boutton.draw(screen):
            #print("Valider")
            #print("name:",input_name_boutton.get_input())
            #print("mdp:",input_mdp_boutton.get_input())
            name=input_name_boutton.get_input()
            mdp=input_mdp_boutton.get_input()


            con = sqlite3.connect("data.db")
            cur = con.cursor()
            data_connect=cur.execute("SELECT * FROM comptes WHERE nom = '{}'".format(name))
            data=data_connect.fetchone()
            cur.close()
            con.close()
            if data==None:
                #print("connais pas")
                pygame.mixer.music.load(".\\musique\\gui_sound\\non.wav")
                pygame.mixer.music.play()
                step="main"
            else:
                if data[5] == mdp:
                    step="menu_play"
                    jouer_boutton= Button(200,100,[btn_unselect_image_load,btn_select_image_load],5,font,"Jouer")
                    option_boutton= Button(200,250,[btn_unselect_image_load,btn_select_image_load],5,font,"Option")
                    retour_boutton= Button(200,400,[btn_unselect_image_load,btn_select_image_load],5,font,"Retour")
                    user_icone_image=pygame.image.load(f".\\images\\gui\\player_ship\\ship{len(name)%6}.png").convert_alpha() 
                    user_icone_btn=Button(10,10,user_icone_image,3)
                    niveau=data[4]
                    defaites=data[3]
                    victoires=data[2]
                    pygame.mixer.music.load(".\\musique\\gui_sound\\bienvenue.wav")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load(".\\musique\\gui_sound\\non.wav")
                    pygame.mixer.music.play()
                    #print("pas le bon mdp")
                    step="main"

        if retour_boutton.draw(screen):
            pygame.mixer.music.load(".\\musique\\gui_sound\\retour.wav")
            pygame.mixer.music.play()
            #print(step)
            step="main"

    if step == "inscription":
        screen.blit(main_menu_bg,(0,0))

        screen.blit(inscription_title,(200,100))
        screen.blit(name_label,(200,200))
        input_name_boutton.draw(screen)

        screen.blit(mdp_label,(200,400))
        input_mdp_boutton.draw(screen)

        if valider_boutton.draw(screen):
            #print("Valider")
            #print("name:",input_name_boutton.get_input())
            #print("mdp:",input_mdp_boutton.get_input())

            name=input_name_boutton.get_input()
            mdp=input_mdp_boutton.get_input()

            con = sqlite3.connect("data.db")
            cur = con.cursor()
            existe=cur.execute("SELECT nom FROM comptes WHERE NOM = '{}'".format(name))
            print(existe.fetchone())
            if existe.fetchone()==None:
                print("save")
                cur.execute("INSERT INTO 'comptes' ('nom','victoires','défaites','niveau','mdp') VALUES (?,?,?,?,?)",(name,0,0,0,mdp))
                con.commit()
                pygame.mixer.music.load(".\\musique\\gui_sound\\oui.wav")
            else:
                pygame.mixer.music.load(".\\musique\\gui_sound\\non.wav")
            pygame.mixer.music.play()
            cur.close()
            con.close()


            step="main"#il est inscrit mais il doit se connecter donc retour au premier écran
        if retour_boutton.draw(screen):
            pygame.mixer.music.load(".\\musique\\gui_sound\\retour.wav")
            pygame.mixer.music.play()
            #print(step)
            step="main"

    if step == "option":
        screen.blit(main_menu_bg,(0,0))
        img = font.render("Menu d'option",True,TEXT_COL)
        screen.blit(img,(200,500))
        if valider_boutton.draw(screen):
            pygame.mixer.music.load(".\\musique\\gui_sound\\oui.wav")
            pygame.mixer.music.play()
        if retour_boutton.draw(screen):
            #print(step)
            step="main"
            option_boutton= Button(200,500,[btn_unselect_image_load,btn_select_image_load],5,font,"Option")
            pygame.mixer.music.load(".\\musique\\gui_sound\\retour.wav")
            pygame.mixer.music.play()

    if fermeture_boutton.draw(screen):
        break

    for event in pygame.event.get():
        if step == "inscription" or step=="connexion":
            input_name_boutton.write(event)
            input_mdp_boutton.write(event)


        background= pygame.transform.scale(background_load, (screen.get_width(),screen.get_height()))
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)
pygame.quit()