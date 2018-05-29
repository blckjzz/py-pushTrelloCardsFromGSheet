#!/usr/bin/env python
# -*- coding: utf-8 -*-
from control.integrationController import IntegrationController
from collections import Counter
import settings
import dotenv 
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')
if __name__ == '__main__':
    ITController = IntegrationController()    
    #download PL file from Google Sheet
    #ITController.trello.debug()
    #ITController.downloadPLIPFile()
    #ITController.store()
    #print("LastSync: ", ITController.log.recoverLastSync())
    ITController.pushPlipToTrelloBoard()