#!/usr/bin/env python
# -*- coding: utf-8 -*-
from control.integrationController import IntegrationController
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
if __name__ == '__main__':
    ITController = IntegrationController()    

    #ITController.log.createLogSyncPL('2018-03-01 00:00:00', 0)

    #download PL file from Google Sheet
    #ITController.downloadPLIPFile()
    #ITController.store()
    #print(ITController.log.recoverLastSync())
    #ITController.pushPlipToTrelloBoard()
    #print(ITController.trello.getBoard())
    def menu_functions(option):
            return {
                '1' : ITController.downloadPLIPFile(),
                '2' : ITController.log.recoverLastSync(),
                '0' : False
            }.get(option, 0)    # 9 is default if x not found
    

    def displayMenuOptions():
        print('=================================================')
        print('########### WELLCOME TO PLIP SYNC APP ###########')
        print('=================================================')
        print('')
        print('(1) - Begin a PLIP Sync')
        print('(2) - Recover Last PLIP Sync Date')
        print('(3) - List PLIPs from database')
        print('(4) - Get Infos about your Trello Board')
        print('(0) - Quit')

        choise  = raw_input("Select a Menu option: ")
        is_sure = raw_input("You have selected option [" + choise + "], are you sure, press Y (Yes) or N (No):")
        if is_sure == 'Y' or is_sure == 'y':
            print("Cool, lets proceed")
            # call menu  functions and execute code
            menu_functions(choise)
        else:
            displayMenuOptions()
        
    op = True
    while not (False):
        displayMenuOptions()


        



        
    

