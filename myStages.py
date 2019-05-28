import pandas as pd
import numpy as np
import requests
import json
import myFunctions as mf
import base64

def stageOne(df_A, tmpFolderLocation, Divide_set, C_seed, C_min, C_max): # endpointUrl

    # myData = pd.read_csv(endpointUrl)
    myData = df_A # myData.drop('Unnamed: 0', axis=1)
    
    #Do the actual magic
    myResult = mf.start_at_A(myData, Divide_set, C_seed, C_min, C_max)

    f = open(tmpFolderLocation + '/randomBytes', 'w')
    f.write(json.dumps(myResult["randomBytes"]))
    f.close()

    del myResult["randomBytes"]

    return myResult

def stageTwo(df_B, tmpFolderLocation, inputArgs, Divide_set, C_seed, C_min, C_max): # endpointUrl
    # myData=pd.read_csv(endpointUrl)
    # colB = myData.columns
    Y = df_B.iloc[:,-1]
    myData = df_B # myData[colB[0:6]].drop(['Unnamed: 0'], axis=1) # we only use first 5 columns here because the values
    
    myResult = mf.start_at_B(myData, C_seed, C_min, C_max, inputArgs["sumNoiseBytes"], Divide_set)
    
    f = open(tmpFolderLocation + '/randomBytes', 'w')
    f.write(json.dumps(myResult["randomBytes"]))
    f.close()

    del myResult["randomBytes"]
    
    return myResult

def stageThree(df_A, tmpFolderLocation, inputArgs, Divide_set): # endpointUrl
    myData = df_A # pd.read_csv(endpointUrl)
    # myData = myData.drop('Unnamed: 0', axis=1)
    
    with open(tmpFolderLocation + '/randomBytes') as binary_file:
        A_randoms = json.loads(binary_file.read())
    
    myResult = mf.communication_at_A(myData, A_randoms, inputArgs["sumNoisesAB"], inputArgs["sumNoisesB"], Divide_set)
    
    return myResult

def stageFour(df_B, tmpFolderLocation, inputArgs, Divide_set): # endpointUrl
    # myData=pd.read_csv(endpointUrl)
    # colB = myData.columns
    Y = df_B.iloc[:,-1]
    myData = df_B # myData[colB[0:6]].drop(['Unnamed: 0'], axis=1) # we only use first 5 columns here because the values
    
    with open(tmpFolderLocation + '/randomBytes') as binary_file:
        B_randoms = json.loads(binary_file.read())
        
    myResult = mf.Final_at_B(myData, inputArgs["randomsSumSet"], inputArgs["sumNoisesBARand"], inputArgs["XaTXa"], B_randoms, Divide_set)
    
    return myResult