#!/usr/bin/env python
# -*- coding: utf-8 -*-
import peewee
import os, errno
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


<<<<<<< HEAD

=======
# TODO 
# REMOVE DATABASE CALL THAT IS HARDCODED AND PLACE IN .ENV FILE
>>>>>>> development
db = peewee.SqliteDatabase('pl_import.db')

class Petition(peewee.Model):
    plip_status = peewee.CharField()
    plip_template = peewee.CharField()
    plip_fantasy_name = peewee.CharField()
    plip_name = peewee.CharField()
    plip_text = peewee.CharField()
    plip_wide = peewee.CharField() 
    plip_state = peewee.CharField()
    plip_municipality = peewee.CharField()
    plip_video =  peewee.CharField()
    plip_references = peewee.CharField()
    plip_links = peewee.CharField()
    sender_name = peewee.CharField()
    sender_email = peewee.CharField()
    sender_telephone = peewee.CharField()
    submitDate = peewee.DateTimeField()

    class Meta:
        database = db

    def createPlipRepo(self):
        try:
            return os.makedirs('plip-repo')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
<<<<<<< HEAD

=======
>>>>>>> development
