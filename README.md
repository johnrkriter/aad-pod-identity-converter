# Notice
**This repo is currently under construction**

# aad-pod-identity-converter
Read in a list of azure managed identity and convert them to YAML for use with aad-pod-identity

# Requirements
Current version of this app uses python3 and pip3. Python 2 is not supported.

# Local environment setup
standard python setup
1. create a ```venv``` folder in your root locally.
2. setup a local venv ```virtualenv -p `which python3` venv```
3. activate local environment either in editor(like vsCode) or in terminal ```source venv/bin/activate```
4. install your requirements ```pip install -r requirements.txt```

# Additional Information
For more information about about using Azure Identity on AKS, refer to [Azure/aad-pod-identity](https://github.com/Azure/aad-pod-identity)