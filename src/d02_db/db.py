import psycopg2
import pandas as pd

def setconnection(username,password):

    param_dic = {
        "host"      : "localhost",
        "database"  : "mev_inspect",
        "user"      : username,
        "password"  : password,
        "port"      : "5432"
    }

    conn = psycopg2.connect(
        database    =param_dic['database'], 
        user        =param_dic['user'], 
        password    =param_dic['password'], 
        host        =param_dic['host'], 
        port        =param_dic['port']
    )

    print('Connection succesfully set up!')
    
    return conn.cursor()