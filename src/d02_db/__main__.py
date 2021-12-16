import os
import sys
import pandas as pd 
import db  

def main(username,password):

    conn = db.setconnection(username,password)

if __name__ == "__main__":

    try:
        username = sys.argv[1]
    except: 
        username = "postgres"
    try:
        password = sys.argv[2]
    except:
        password = "password"

    #     companyinfo = sys.argv[3]
    # except: 
    #     companyinfo = datapath+'companyinformation_Technology_.pickle'
    # try:
    #     financialinfo = sys.argv[4]
    # except: 
    #     financialinfo = datapath+'financialinformation_Technology_.pickle'

    main(username,password)
