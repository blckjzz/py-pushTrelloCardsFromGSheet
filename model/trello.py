#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import requests
import sys
import os, errno
reload(sys)
sys.setdefaultencoding('utf-8')

class Trello:
    def __init__(self):
        self.TRELLO_KEY =  os.getenv("TRELLO_KEY")
        self.TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")
        self.TRELLO_URL = os.getenv("TRELLO_URL")
        self.BOARD_ID = os.getenv("TRELLO_BOARD_ID")
        self.TRELLO_LIST_ID = os.getenv("TRELLO_LIST_ID")  
        
    def debug(self):
        print("DEBUG OF TRELLO MODEL PARAMS")
        print("TrelloKey:" , os.getenv("TRELLO_KEY"))
        print("TRELLO_TOKEN:" , self.TRELLO_TOKEN)
        print("TRELLO_URL:" , self.TRELLO_URL)
        print("BOARD_ID:" , self.BOARD_ID)
        print("TRELLO_LIST_ID:" , self.TRELLO_LIST_ID)

    def getBoardUrl(self):
        return self.TRELLO_URL + self.BOARD_ID + "?&key=" + self.TRELLO_KEY + "&token=" + self.TRELLO_TOKEN
    
    def getCardsUrl(self, *filter):
        cards = self.getBoardUrl + "cards?" + filter
        return cards
    
    def getListsUrl(self, *filter):
        cards = self.TRELLO_URL + "/lists/?" + filter
        return cards
    
    ## transferd methods needs to fix

    #retrieve all data from a trello board by it's boardkey
    def getBoard(self):
        url = self.getBoardUrl()
        result = requests.get(url)
        return result.text

    #retrieve all data from a trello board by it's boardkey
    def getCards(self):
        url = self.getCardsUrl()
        result = requests.get(url)
        return result.text
    
    #create a card into trello board
    def createCard(self, petition):
        url = "https://api.trello.com/1/cards"
        #for petition in petitionList:
        querystring = { "name": petition.petition_name ,
                        "desc": "Texto do Projeto de Lei: " + petition.petition_text 
                        + "\nDados do Proponente: \n Nome: " 
                                                            + petition.sender_name 
                                                            + "\nE-mail:" 
                                                            + petition.sender_mail
                                                            + "\nPetição nacional?" 
                                                            + petition.petition_is_nationWide 
                                                            + "\nEstado/Cidade/Município:" 
                                                            + petition.petition_municipality
                                                            + datetime.datetime.fromtimestamp(petition.submitDate).strftime('%d/%m/%Y')
,
                        "pos" : "bottom",
                        "idList": self.TRELLO_LIST_ID,
                        "urlSource" : "",
                        "keepFromSource" : "all",
                        "key" : self.TRELLO_KEY,
                        "token" : self.TRELLO_TOKEN
                        }
        #print(url + '' + str(querystring))
        r = requests.request("POST", url, params=querystring)
        print("is the plip a card on trello ?: " + str(r.content))
