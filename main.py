#This program is designed to read in azure Managed Identity information, and produce YAML for aad-pod-identity usage

#Base Python Packages
import csv
import logging

#from PyYAML
import yaml

#from logzero
import logzero
from logzero import logger

##initialize logging
logzero.loglevel(logging.DEBUG)

#initialized dictionary containing dictionaries of MSI configuration information
msilist = {}

class AzureManagedIdentity:
    def ___init___(self, msi, clientId, objectId, resourceId):
        self.msi = msi
        self.clientId = clientId
        self.objectId = objectId
        self.resourceId = resourceId

def read_input_csv(filePath):
    """Reads in a CSV file and creates a dictionary of each line, adding it to a collection dictionary"""
    with open(filePath, mode="r") as csvfile:
        reader = csv.DictReader(csvfile)
        line_count = 0
        for row in reader:
            if line_count == 0:
                logger.debug(f'Column names are {", ".join(row)}')
                line_count += 1
            logger.debug(f'\t{row["msi"]} as msi: {row["Client ID"]} as Client ID: {row["Object ID"]} as Object ID: {row["Resource ID"]} as Resource ID.')
            msilist[line_count]=row
            line_count += 1
    logger.debug(f'msi list: {msilist}')
    csvfile.close()

def write_azure_identity(identityList):
    """Takes in a nested dictionary of identities and creates azure identity yaml for each"""
    logger.debug(len(identityList))
    for identity_id, identity_info in identityList.items():
        logger.debug(f'processing msi #{identity_id} containing')

        # Convert the data in the dictionary item into variables
        filename = identity_info['msi'] + '.yaml'
        identityName = identity_info['msi']
        resourceId = identity_info['Resource ID']
        clientId = identity_info['Client ID']

        #Create a single YAML for the AzureIdentity for each item in identityList
        with open (filename, 'w') as identityfile:
            logger.debug(f'processing file:{filename}')
            identityfile.write(f'apiVersion: "aadpodidentity.k8s.io/v1"\n')
            identityfile.write(f'kind: AzureIdentity\n')
            identityfile.write(f'metadata:\n')
            identityfile.write(f'  name: {identityName}\n')
            identityfile.write(f'spec:\n')
            identityfile.write(f'  type: 0\n')
            identityfile.write(f'  resourceID: {resourceId}\n')
            identityfile.write(f'  clientID: {clientId}')
            identityfile.write(f'')
            identityfile.close()

def write_azure_identity_binding(identityList):
    """Takes in a nested dictionary of identities and creates azure identity binding yaml for each"""
    logger.debug(len(identityList))
    for identity_id, identity_info in identityList.items():
        logger.debug(f'processing msi #{identity_id} containing')

        # Convert the data in the dictionary item into variables
        filename = identity_info['msi'] + '.yaml'
        identityName = identity_info['msi']
        resourceId = identity_info['Resource ID']
        clientId = identity_info['Client ID']

        #Create a single YAML for the AzureIdentityBinding for each item in identityList
        with open (filename, 'w') as identityfile:
            logger.debug(f'processing file:{filename}')
            identityfile.write(f'apiVersion: "aadpodidentity.k8s.io/v1"\n')
            identityfile.write(f'kind: AzureIdentity\n')
            identityfile.write(f'metadata:\n')
            identityfile.write(f'  name: {identityName}\n')
            identityfile.write(f'spec:\n')
            identityfile.write(f'  type: 0\n')
            identityfile.write(f'  resourceID: {resourceId}\n')
            identityfile.write(f'  clientID: {clientId}')
            identityfile.close()


#read_input("single-line.csv")
read_input_csv("example-identities.csv")
write_azure_identity(msilist)

