from pathlib import Path


home = str(Path.home())

AWS_CREDS_FILE = f"{home}/.aws/credentials"
DESTINATION_CREDS_FILE = f"{home}/.creds"
# TODO(sam) hard coded for now, make dynamic so can use different "default" regions
AWS_DEFAULT_REGION = "us-east-1"
