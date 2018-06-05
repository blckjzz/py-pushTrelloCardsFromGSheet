#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Models import
from model.trello import Trello
from model.petition import Petition
from model.log import Log
import settings
# libs import
import datetime
import sqlite3
import sys
import os, errno
import urllib2
import csv
reload(sys)
sys.setdefaultencoding('utf-8')



class IntegrationController:
    def __init__(self):   
        self.trello = Trello()
        self.log = Log()    
        self.petitionsList = []
        self.petition = Petition()

    def pushPlipToTrelloBoard(self):
        #recover date from last Sync and displays it before accually syncs
        lastSyncDate = self.log.recoverLastSync()
        #for p in Petition.where(Petition.submitDate >= lastSyncDate).get():
        petitions = Petition.select().where(Petition.submitDate >= lastSyncDate)
        #print(len(petitions))
        for petition in petitions:
            #print(petition.plip_name)
            self.trello.createCard(petition)

    # downloads and store plips from google sheets on local repositoty
    def downloadPLIPFile(self):
        plipSheet = os.getenv("GOOGLE_SHEET_URL")
        fileName = 'plip.csv'
       
        #tries to create plip repo file in case not exists
        self.petition.createPlipRepo()
        print('Baixando PLIPs')

        filedata = urllib2.urlopen(plipSheet)  
        datatowrite = filedata.read()

        try:
            with open('plip-repo/plip.csv', 'wb') as f:  
                f.write(datatowrite)
            print("Arquivo baixado com sucesso!")
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        
    # read lines from csv file
    # and transform then into petition's objects
    # then store each plip in the database
    # creates a log of when and how many plips were synced

    def store(self):
        petitionList = []
        with open('plip-repo/plip.csv', 'rb') as csvfile:
            plips = csv.reader(csvfile)
    
            lastSync = self.log.recoverLastSync()        
            print("Last sync was in: " + str(lastSync))
            for row in plips:
                if(row[0] != 'status'):
                    timestamp = datetime.datetime.strptime(row[15],'%Y-%m-%d %H:%M:%S')
    
                    if timestamp > lastSync:
                        print("última sincronização: "+ str(lastSync))
                        print("Timestamp de envio da petição:" + str(timestamp))
                        print("Timestamp de envio maior que a ultima sincronização.. salvando no banco:")
                        petition = Petition(
                            plip_status = row[0],
                            plip_template = row[1],
                            plip_fantasy_name = row[2],
                            plip_name = row[3],
                            plip_text = row[4],
                            plip_wide = row[5],
                            plip_state = row[6],
                            plip_municipality = row[7],
                            plip_video = row[8],
                            plip_references = row[9],
                            plip_links = row[10],
                            sender_name = row[11],
                            sender_email =row[12],
                            sender_telephone =row[13],
                            submitDate = row[15]
                        )
                        is_save = petition.save()
                        petitionList.append(is_save)
                    else:
                        print("Timestamp:")
                        print(timestamp)
                        print("petition send date lower then lastSync")
            print("Total of:[" + str(len(petitionList))+ "] was synced during this task.")
        #create a log of the last petition Date that was synced
        if 'petition' in locals():
            if hasattr(petition, 'submitDate'):
                self.log.createLogSyncPL(petition.submitDate,len(petitionList))
        else:
            #logs in case there is any new petition
            self.log.createLogSyncPL(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),len(petitionList))

#TODO
#create method that pushes every entrie from database to trello boards






