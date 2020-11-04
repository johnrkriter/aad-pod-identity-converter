# Notice
**This repo is currently under construction**

# aad-pod-identity-converter
Read in a list of azure managed identity and convert them to YAML for use with aad-pod-identity

# Local environment setup
standard python setup
1. create a ```venv``` folder in your root locally.
2. setup a local venv ```virtualenv -p `which python3` venv```
3. activate local environment either in editor(like vsCode) or in terminal ```source venv/bin/activate```
4. install your requirements ```pip install -r requirements.txt```

# Running tests
1.Run ```python3 -m unittest  tests/test_converter.py```

# Building Docker Image
1. from the root directory execute the build ```docker build -t identity_converter:latest```
2. Default data will be kept inside the container when you run ```docker run identity_converter:latest```

It is recommended to run this with an attached host volume, so you can provide input and recieve output.
to do this, run with the following 
```docker run -v /path/to/input/file/directory:/usr/src/app/data:rw jkriter/identity_converter:latest```
*note*make sure the input file is called identities.csv or code will fail


# Additional Information
For more information about about using Azure Identity on AKS, refer to [Azure/aad-pod-identity](https://github.com/Azure/aad-pod-identity) run 
https://www.tutorialspoint.com/python3/python_command_line_arguments.htm
