import os
import sys
import pandas as pd 
import dataextract  

def main(blocksdatapath,transactionssavepath,block_number):

    dataextract.callapi(blocksdatapath,transactionssavepath,block_number)

if __name__ == "__main__":
    flatdatafilespath = './data/extracted_data/'

    try:
        block_number = sys.argv[1]
    except: 
        block_number = 20
    try:
        blocksdatapath = sys.argv[2]
    except:
        blocksdatapath = flatdatafilespath+'blocks'+str(block_number)+'_'.pickle
    try:
        transactionssavepath = sys.argv[3]
    except: 
        blocksdatapath = flatdatafilespath+'transactions'+str(block_number)+'_'.pickle

    # try:
    #     companyinfo = sys.argv[3]
    # except: 
    #     companyinfo = datapath+'companyinformation_Technology_.pickle'
    # try:
    #     financialinfo = sys.argv[4]
    # except: 
    #     financialinfo = datapath+'financialinformation_Technology_.pickle'


    main(blocksdatapath,transactionssavepath,block_number)

#def gettickers(tickerspath, sector, numberoftickers, updateData):