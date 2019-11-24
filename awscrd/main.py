import click

from awscrd import parse
from awscrd import conf
from awscrd import sts
from awscrd import write


@click.command()
@click.option("-p", "--profile")
@click.option("-t", "--token")
def main(profile, token):
    """
    CLI script to get AWS security credentials

    Args:
        profile (str): the user's AWS profile name e.g. dev, qa, production. Must match
                       a profile section header in the input credentials file
        token (str): MFA token
    """
    aws_iam_account_number, username = parse.profile_from_config(
        profile=profile, input_file_path=conf.AWS_CREDS_FILE
    )
    print("✅ Parsed AWS credentials from file")

    creds_dict = sts.get_token(
        token=token, aws_iam_account_number=aws_iam_account_number, username=username
    )
    print("✅ Token received from STS")

    write.creds_to_output_file(
        creds=creds_dict, output_file_path=conf.DESTINATION_CREDS_FILE, mode="w"
    )
    print(f"✅ Credentials written to {conf.DESTINATION_CREDS_FILE}")
