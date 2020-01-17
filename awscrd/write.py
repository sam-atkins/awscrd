"""
Write to output file
"""
from typing import Mapping

from awscrd.conf import AWS_DEFAULT_REGION


def creds_to_output_file(creds: Mapping, output_file_path: str, mode="w"):
    """
    Takes AWS CLI response and writes to the destination creds file

    Args:
        creds (Mapping): the AWS creds to be written to the creds file
        output_file_path (str): the path to where the creds are written
        mode (str, optional): the write mode, defaults to "w".
    """
    aws_access_key_id = creds.get("AccessKeyId")
    aws_secret_access_key = creds.get("SecretAccessKey")
    aws_session_token = creds.get("SessionToken")

    with open(output_file_path, mode) as text_file:
        print(f"export AWS_ACCESS_KEY_ID={aws_access_key_id}", file=text_file)
        print(f"export AWS_SECRET_ACCESS_KEY={aws_secret_access_key}", file=text_file)
        print(f"export AWS_SESSION_TOKEN={aws_session_token}", file=text_file)
        print(f"export AWS_DEFAULT_REGION={AWS_DEFAULT_REGION}", file=text_file)
