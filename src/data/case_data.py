from nanoid import generate

name = "python_api_"+generate()


# this is the project example values to be used
# you can change the version if you like (5.x)
project_data = {
    "name": name, "version": "5.x", "simulationSoftware": "OpenFoam"
}


# this is the case values example to create the case
# you can change the runScript, solverName and decomposeParDict
case_data = {
    "name": "API Case",
    "parallel": True,
    "runScript":
    './Allrun &>> $ROOT_DIRECTORY/log.txt\n pvpython U_ParaView_LocalFolder_V0.py &>> $ROOT_DIRECTORY/log.txt',
    "solverName": "simpleFoam",
        "decomposeParDict":
        'echo "\nFoamFile\n        {\n          version 2.0;\n          format ascii;\n          class dictionary;\n          object decomposeParDict;\n        }\n        numberOfSubdomains 1;\n        method scotch;\n" > system/decomposeParDict',
        "emailNotification": False,
        "machineType": "5d441a30e10af60008ec01f8",
        "inputFileId": ""
}


experiment_data = {
    "name": name,
    "version": "2.4.0",
    "simulationSoftware": "OpenFoam",
    "caseDetails": {
        "runScript": "simpleFoam &> $ROOT_DIRECTORY/log.txt",
        "decomposeParDict": "echo \"\nFoamFile\n        {\n          version 2.0;\n          format ascii;\n          class dictionary;\n          object decomposeParDict;\n        }\n        numberOfSubdomains 1;\n        method scotch;\n\" > system/decomposeParDict",
        "solverName": "simpleFoam",
        "emailNotification": True,
        "machineType": "5c6556721d4ebf0a98155411",
        "parallel": True
    },
    "isExperiment": True,
    "iterateParams": True,
    "inputParameters": [
        {
            "path": "0/K",
            "variableName": "K",
            "progressionType": "arithmetic",
            "startValue": 10,
            "endRatio": 30,
            "steps": 3,
            "values": [
                "10",
                "20",
                "30"
            ]
        },
        {
            "path": "0/epsilon",
            "variableName": "epsilon",
            "progressionType": "arithmetic",
            "startValue": 100,
            "endRatio": 300,
            "steps": 3,
            "values": [
                "100",
                "200",
                "300"
            ]
        }
    ],
    "inputFileId": ""
}

# this is the name for your input file
# make sure it has the same name as the file located on /test_files folder
input_data = {
    "fileName": "quickcase1"
}
