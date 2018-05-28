import peewee

db = peewee.SqliteDatabase('pl_import.db')

class Log(peewee.Model):
    sync_date = peewee.DateTimeField()
    quantity = peewee.IntegerField()


    #creates a log event on database
    def createLogSyncPL(self, petitionSubmitDate,value):
        log = Log()
        log.quantity = value
        log.sync_date = petitionSubmitDate
        Log.save(log)
        
    #recover lastsync property to help in the next syncronization from where its stops
    def recoverLastSync(self):
        log = Log()
        log = Log.select().order_by(Log.sync_date.desc()).get()
        return log.sync_date
    
    class Meta:
        database = db
