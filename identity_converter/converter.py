#This program is designed to read in azure Managed Identity information, and produce YAML for aad-pod-identity usage

#Base Python Packages
import csv, logging, os, re

#from logzero
import logzero
from logzero import logger

##initialize logging
logzero.loglevel(logging.DEBUG)

#initialized dictionary containing dictionaries of MSI configuration information
msilist = {}

def read_input_csv(inputPath):
    """Reads in a CSV file and creates a dictionary of each line, adding it to a collection dictionary"""
    with open(inputPath, mode="r") as csvfile:
        reader = csv.DictReader(csvfile)
        line_count = 0
        for row in reader:
            if line_count == 0:
                logger.debug(f'Column names are {", ".join(row)}')
                line_count += 1
            logger.debug(f'\t{row["msi"]} as msi: {row["Client ID"]} as Client ID: {row["Object ID"]} as Object ID: {row["Resource ID"]} as Resource ID.')
            row["msi"] = row["msi"].lower()
            msilist[line_count]=row
            line_count += 1
    logger.debug(f'msi list: {msilist}')
    csvfile.close()
    return msilist

def write_azure_identity(identityList):
    """Takes in a nested dictionary of identities and creates azure identity yaml for each"""
    logger.debug(len(identityList))
    for identity_id, identity_info in identityList.items():
        logger.debug(f'processing msi #{identity_id} containing')

        # Convert the data in the dictionary item into variables
        filename = '../data/output/' + identity_info['msi'] + '.yaml'
        identityName = identity_info['msi']
        resourceId = identity_info['Resource ID']
        clientId = identity_info['Client ID']

        #Create a single YAML for the AzureIdentity for each item in identityList
        os.makedirs(os.path.dirname(filename), exist_ok=True)
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
        filename = '../data/output/' + identity_info['msi'] + '-binding.yaml'
        identityName = identity_info['msi']

        #Create a single YAML for the AzureIdentityBinding for each item in identityList
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open (filename, 'w') as identityfile:
            logger.debug(f'processing file:{filename}')
            identityfile.write(f'apiVersion: "aadpodidentity.k8s.io/v1"\n')
            identityfile.write(f'kind: AzureIdentityBinding\n')
            identityfile.write(f'metadata:\n')
            identityfile.write(f'  name: {identityName}-binding\n')
            identityfile.write(f'spec:\n')
            identityfile.write(f'  azureIdentity: {identityName}\n')
            identityfile.write(f'  selector: {identityName}')
            identityfile.close()

def full_conversion(inputPath):
    """Convert a single csv into identity and binding"""
    read_input_csv(inputPath)
    write_azure_identity(msilist)
    write_azure_identity_binding(msilist)
    msilist.clear

if __name__ == '__main__':
    full_conversion("../data/identities.csv")

