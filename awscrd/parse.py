"""
Parses user profile info from a config file
"""
import configparser
import sys
from typing import Tuple


def profile_from_config(profile: str, input_file_path: str) -> Tuple[str, str]:
    """
    Parses a file using configparser

    Args:
        profile (str): the profile name which must match the section title
        input_file_path (str): the absolute file path to the creds file

    Returns:
        Tuple[str, str]: AWS IAM account number and AWS user name
    """
    config = configparser.ConfigParser()
    config.read(input_file_path)

    try:
        profile_section = config[profile]
    except KeyError:
        print(f"Unable to find profile {profile} in AWS credentials file")
        sys.exit(1)

    aws_iam_account_number = profile_section.get("aws_iam_account_number")
    username = profile_section.get("username")

    return aws_iam_account_number, username
