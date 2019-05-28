import os
import json
import pandas as pd
import myStages as ms

endpointType = os.environ.get("endpointType")
endpointUrl = os.environ.get("endpointUrl")
inputFileLocation = "/input.txt"
outputFileLocation = "/output.txt"
logFileLocation = "/log.txt"
tempFolder = "/temp/"

#Read input file
with open(inputFileLocation) as f:  
    inputArgs = json.load(f)

#############################################
#do whatever you want from here
#############################################
currentStage = inputArgs["stage"]
print("Stage: %s" % currentStage)

##### Common Knowledge #####
Divide_set = 10
C_seed = 2
C_min = 0
C_max = 5

if currentStage == 1:
    df_A = pd.DataFrame.from_records(inputArgs["dataA"]).transpose()
    outputJson = ms.stageOne(df_A, tempFolder, Divide_set, C_seed, C_min, C_max) # endpointUrl
if currentStage == 2:
    df_B = pd.DataFrame.from_records(inputArgs["dataB"]).transpose()
    outputJson = ms.stageTwo(df_B, tempFolder, inputArgs, Divide_set, C_seed, C_min, C_max) # endpointUrl
if currentStage == 3:
    df_A = pd.DataFrame.from_records(inputArgs["dataA"]).transpose()
    outputJson = ms.stageThree(df_A, tempFolder, inputArgs, Divide_set) # endpointUrl
if currentStage == 4:
    df_B = pd.DataFrame.from_records(inputArgs["dataB"]).transpose()
    outputJson = ms.stageFour(df_B, tempFolder, inputArgs, Divide_set) # endpointUrl

# Write output to file
with open(outputFileLocation, 'w') as f:
    f.write(json.dumps(outputJson))