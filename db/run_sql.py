import psycopg2  
import psycopg2.extras as ext

def run_sql(sql, values = None): # helper function can pass one or two arguments. 
    conn = None                    # always sql but sometimes maybe other values
    results = [] # empty list variable
    
    try: 
        conn=psycopg2.connect("dbname='music_collection'")
        cur = conn.cursor(cursor_factory=ext.DictCursor)   
        cur.execute(sql, values) #executes sql request
        conn.commit() # executes but not saved until commit
        results = cur.fetchall() # results will be returned info
        cur.close()           #closes down connection 
    except (Exception, psycopg2.DatabaseError) as error: # if it has an error print error
        print(error)
    finally:
        if conn is not None: # if the connection is not closed
            conn.close() # makes sure connection gets closed
    return results # gives back things you want

  