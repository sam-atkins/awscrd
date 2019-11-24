from pathlib import Path


home = str(Path.home())

AWS_CREDS_FILE = f"{home}/.aws/credentials"
DESTINATION_CREDS_FILE = f"{home}/.creds"
