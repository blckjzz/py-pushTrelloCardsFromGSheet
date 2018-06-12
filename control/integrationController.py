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
        log = Log()
        #recover date from last Sync and displays it before accually syncs
        lastSyncDate = self.log.recoverLastSync('TRELLO_SYNC')
        #for p in Petition.where(Petition.submitDate >= lastSyncDate).get():
        count = 0
        print("Last sync: " + str(lastSyncDate))

        for petition in Petition.select().where(Petition.submitDate >= lastSyncDate):
            print(petition.plip_name)
            count += self.trello.createCard(petition)
        print("Tototal of [" + str(count) +"] roposes pushed to Trello board")
            
        #if plip finishes now will create a log for it
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.motive = "TRELLO_SYNC"
        log.quantity = count
        log.sync_date = now
        self.log.createLogSyncPL(log.sync_date, log.quantity, log.motive)


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
            #pt = Petition.select().where(Petition.submitDate > '2018-02-29 00:00:00').order_by(Petition.submitDate.desc()).limit(1)
            lastSync = self.log.recoverLastSync('PLIP_SYNC')
            #print(lastSync)
            #test = datetime.datetime.strptime(str(lastSync), '%Y-%m-%d %H:%M:%S')
            print("Last sync was in: ", lastSync)
            for row in plips:
                if(row[0] != 'status'):
                    timestamp = datetime.datetime.strptime(row[15],'%Y-%m-%d %H:%M:%S')
                    #print("debug timestamp:")
                    #print(type(timestamp))
                    #print("debug lastsync")
                    #print(type(lastSync))
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
                self.log.createLogSyncPL(petition.submitDate,len(petitionList), "PLIP_SYNC")
        else:
            #logs in case there is any new petition
            self.log.createLogSyncPL(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),len(petitionList), "PLIP_SYNC")

#TODO
#create method that pushes every entrie from database to trello boards






