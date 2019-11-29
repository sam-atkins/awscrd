# AWS Get Creds

CLI script to get security credentials as part of using MFA to protect programmatic calls to specific AWS API operations.

[![CircleCI](https://circleci.com/gh/sam-atkins/awscrd-cli.svg?style=svg)](https://circleci.com/gh/sam-atkins/awscrd-cli)
<a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

- [AWS Get Creds](#aws-get-creds)
  - [Usage](#usage)
  - [Install](#install)
  - [Documentation Links](#documentation-links)

## Usage

```bash
awscrd -p {profile name} -t {MFA token}
```

## Install

AWS credentials are assumed to be in `~./aws/credentials` per standard guidance from AWS. Refer to the [docs](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) for info.

Session token and other security credentials are written to `~/.creds` which suits my workflow at Big Health.

These file locations can be changed in `./awscrd/conf.py`.

```bash
# create a venv
virtualenv -p python3.7 venv

# activate the venv
source venv/bin/activate

# install dependencies
poetry install
```

To bundle your script with setuptools for dev purposes run:

```bash
pip3 install --editable .
```

To setup the script to run from any directory, run this in your home directory:

```
pip3 install --editable /Users/{username}/path/to/awscrd
```

## Documentation Links

- [boto STS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.get_session_token)
- [Python config parser](https://docs.python.org/3/library/configparser.html)
- [Click docs re setuptools integration](https://click.palletsprojects.com/en/7.x/setuptools/#setuptools-integration)
