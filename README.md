# cdktf_examples


# CDKTF_APP1:
This consisting example of aws dynamodb and opensearch domain creation via cdk teraform using python language.

# Pre-requisites for CDKTF:
- npm
- terraform 1.0+
- python3
- aws cli v2

# Commands to get started:
- npm install -g cdktf-cli -> This command will help in installing cdk tf package
- pip install pipenv -> PIPEVN helps in installing depending packages in a particular virtual environmnent for a specific project.

# To initialize a cdktf project, following command can be used here --local is used to avoid terraform cloud usage( by default terraform cloud is used to store all the metadata files and token )

cdktf init --template="python" --local
Note: cdktf_app1 dir is a pre-initialized dir, therefore on usage of the same above command wont be needed.

source .venv/bin/activate -> command to activate pipenv

# Once the project is initialized, we need to install aws provider library for this project, following commands will help installing the same:

cdktf provider add "aws@~>4.0”

pipenv run pip install cdktf-cdktf-provider-aws

cdktf get

# To deploy the application following command can be used:

cdktf deploy

# To delete the deployed application stack:

cdktf destroy




# Repository Description
- cdktf_app/ -> Entry point of the project
- cdktf.json -> Placeholder for all the metadata of the project
- help -> lists of frequently used pip libraries and useful pipeve commands
- main.py -> main boiler plate script where all the resources defined

