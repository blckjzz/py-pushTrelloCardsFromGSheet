import peewee

# TODO 
# REMOVE DATABASE CALL THAT IS HARDCODED AND PLACE IN .ENV FILE
db = peewee.SqliteDatabase('pl_import.db')

class Log(peewee.Model):
    sync_date = peewee.DateTimeField()
    quantity = peewee.IntegerField()
    motive = peewee.TextField()


    #creates a log event on database
    def createLogSyncPL(self, date, quantity, motive):
        log = Log()
        log.quantity = quantity
        log.sync_date = date
        log.motive = motive
        Log.save(log)
        
    #recover lastsync property to help in the next syncronization from where its stops
    def recoverLastSync(self, motive):
        log = Log()
        print(motive)
        print type(motive)
        #for log in Log.select().where(Log.motive == 'PLIP_SYNC'):
        log = Log.select().order_by(Log.sync_date.desc()).where(Log.motive == motive).get()
        return log.sync_date
    class Meta:
        database = db
