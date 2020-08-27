#This program is designed to read in azure Managed Identity information, and produce YAML for aad-pod-identity usage
import PyYaml
import csv

azuremanagedidentitylist = {}

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
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\t{row["msi"]} as msi: {row["Client ID"]} as Client ID: {row["Object ID"]} as Object ID: {row["Resource ID"]} as Resource ID.')
            azuremanagedidentitylist[line_count]=row
            line_count += 1
    print("LINE BREAK")
    print(azuremanagedidentitylist)
    csvfile.close()

def write_azure_identity(identityList):
    """Takes in a nested dictionary of identities and creates azure identity yaml for each"""



#read_input("single-line.csv")
read_input_csv("azure-identities.csv")

