#!/usr/bin/env python
# -*- coding: utf-8 -*-
from control.integrationController import IntegrationController
from model.petition import Petition
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
if __name__ == '__main__':
    #loop = True
    ITController = IntegrationController()    
    #print(ITController.trello.getBoard())
    def menu_functions(option):
        if option == '1':
            print('=================================================')
            print('########### (1) DOWNLOAD PLIP FILES   ###########')
            print('=================================================')
            ITController.downloadPLIPFile()
            ITController.store()

        elif option == '2':
            lastSyncDate = ITController.log.recoverLastSync()
            print('=================================================')
            print('######### (2) PLIP SYNC DATE  ########')
            print("Last sync was in: " + str(lastSyncDate))
            print('=================================================')
        elif option == '3':
            print('=================================================')
            print('######### (3) PUSH PLIP TO TRELLO BOARD  ########')
            ITController.pushPlipToTrelloBoard()
            print('=================================================')
        elif option == '4':
            print('=================================================')
            print('######### (4) RECOVER LAST PLIP SYNCED  ########')
            for petition in ITController.petition.select().order_by(Petition.submitDate.desc()).limit(1):
                print("Última Petição salva: " + str(petition.plip_name))
                print("Sincronizada em: " + str(petition.submitDate) )
            print('=================================================')

    def isSure(choise):
        is_sure = raw_input("You have selected option [" + str(choise) + "], are you sure, press Y (Yes) or N (No):")
        if is_sure == 'Y' or is_sure == 'y':
            print("Cool, lets proceed")
            return True
        else:
            return False
    
    def askValue():
        choise  = raw_input("Select a Menu option: ")
        return choise 


    def displayMenuOptions():
        print(' ---==== MENU ====--- ')
        print('(1) - Begin a PLIP Sync')
        print('(2) - Recover Last PLIP Sync Date')
        print('(3) - PUSH PLIP TO TRELLO BOARD')
        print('(4) - List PLIPs from database')
        #print('(0) - Quit')

        choise = askValue()
        is_sure = isSure(choise)

        if is_sure:
            # call menu  functions and execute code
            menu_functions(choise)
        else:
            displayMenuOptions()
    
    print('=================================================')
    print('########### WELLCOME TO PLIP SYNC APP ###########')
    print('=================================================')
    
    while (True):
        #displayMenuOptions()
        print(ITController.trello.getListFromBoard())
        break


        



        
    

