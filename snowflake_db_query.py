import snowflake.connector
import logging
def db_get(current1,current2):
    ctx = snowflake.connector.connect(
    user='xxxxxx',
    password='xxxxxxx',
    account='xxxxxxx.ap-southeast-2',
    warehouse='COMPUTE_WH',
    database='TEST',
    schema='public'
    )
    cs = ctx.cursor()
    try:
        #cs.execute("SELECT current_version()")
        #one_row = cs.fetchone()
        #print(one_row[0])
        #cs.execute("""Use database test ;""")
        cs.execute("""CREATE OR REPLACE TABLE foreign_exchange (
                        current1 VARCHAR(3),
                        current2 VARCHAR(3),                       
                        exchange_rate FLOAT);"""
                        )
        cs.execute ("""insert into foreign_exchange values('USD','GBP',0.67);""")
        cs.execute ("""insert into foreign_exchange values('GBP','EUR',1.14);""")
        
        sql_statement = "select exchange_rate from foreign_exchange where current1='{}' and current2='{}'".format(current1,current2)
        print(sql_statement)
        try:
            cs.execute (sql_statement)
            one_row = cs.fetchone()
            print(one_row[0])
        except:
            sql_statement = "select exchange_rate from foreign_exchange where current1='{}' and current2='{}'".format(current2,current1)
            try:
                cs.execute (sql_statement)
                one_row = cs.fetchone()
                
                print(round(1/one_row[0],2))
            except:
                print ("Are you sure we have the record?")    
        #print ("Are you sure we have the record?")

    ### When successful, displays message 'Table TRANSACTIONS successfully created'
    #logging.info(cs)
    finally:
        cs.close()
        ctx.close()

db_get('GBP','USD')
