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
    
<<<<<<< HEAD
    def getCardsUrl(self, *filter):
        cards = self.getBoardUrl + "cards?" + filter
        return cards
    
    def getListsUrl(self, *filter):
        cards = self.TRELLO_URL + "/lists/?" + filter
        return cards
=======
    def getCardsUrl(self):
        cards = self.TRELLO_URL + self.BOARD_ID +"/cards" + "?&key=" + self.TRELLO_KEY + "&token=" + self.TRELLO_TOKEN
        return cards
    
    def getListsUrl(self):
        cards = self.TRELLO_URL + self.BOARD_ID +"/lists/?&key=" + self.TRELLO_KEY + "&token=" + self.TRELLO_TOKEN
        return cards

    def getListFromBoard(self):

        try:
            url = "https://api.trello.com/1/boards/" + self.BOARD_ID + "/lists"

            querystring = {"key": self.TRELLO_KEY ,"token": self.TRELLO_TOKEN}

            r = requests.request("GET", url, params=querystring)
            print(r.content)
        except requests.exceptions.RequestException as e:
            print("no, something went wrog, must check.")
            print("Status code: " + str(r.status_code))
            print e
            sys.exit(1)


>>>>>>> development
    
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
<<<<<<< HEAD
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
=======
        count = 0
        try:
            url = "https://api.trello.com/1/cards"
            #print(petition.plip_name)
            #for petition in petitionList:
            querystring = { "name": petition.plip_name ,
                            "desc":                             "Id do Projeto: " + str(petition.id) +
                                                                " \nDATA DE SUBMISSÃO DO PL: \n "
                                                                + str(petition.submitDate)
                                                                + "\n Texto do Projeto de Lei: \n " 
                                                                + str(petition.plip_text)
                                                                + " Dados do Proponente "
                                                                + "\n ================= \n"
                                                                + "\n Nome: "
                                                                + str(petition.sender_name)
                                                                + "\n E-mail: " 
                                                                + str(petition.sender_email)
                                                                + "\n Abrangencia: " 
                                                                + str(petition.plip_wide)
                                                                + "\n Estado/Cidade/Município:" 
                                                                + "\n Estado: "
                                                                + str(petition.plip_state)
                                                                + "\n Cidade: "
                                                                + str(petition.plip_municipality)
                                                                + "\n Links: "
                                                                + str(petition.plip_links)
                                                                ,
                            "pos" : "bottom",
                            "idList": self.TRELLO_LIST_ID,
                            "urlSource" : "",
                            "due" : petition.submitDate,
                            "keepFromSource" : "all",
                            "due" : petition.submitDate,
                            "key" : self.TRELLO_KEY,
                            "token" : self.TRELLO_TOKEN
                            }
            r = requests.request("POST", url, params=querystring)
            return 1
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print e
            #print("no, something went wrog, must check.")
            #print("Status code: " + str(r.status_code))
            sys.exit(1)
            
 
>>>>>>> development
