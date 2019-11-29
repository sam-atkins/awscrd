from unittest.mock import patch

import pytest

from awscrd.sts import get_token


MOCK_STS_RESPONSE_HAPPY_PATH = {
    "Credentials": {
        "AccessKeyId": "AAAAAAAAAA",
        "SecretAccessKey": "BBBBBBB",
        "SessionToken": "CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC",
    },
    "ResponseMetadata": {
        "RequestId": "b046e0f2-0ef6-11ea-af31-XXXXXXXXXX",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "XXXXXXX-XXXX-XXXX-XXX-XXXXXX",
            "content-type": "text/xml",
            "content-length": "804",
            "date": "Thu, 28 Nov 2019 21:12:06 GMT",
        },
        "RetryAttempts": 0,
    },
}

MOCK_STS_RESPONSE_4XX = {
    "ResponseMetadata": {
        "RequestId": "b046e0f2-0ef6-11ea-af31-XXXXXXXXXX",
        "HTTPStatusCode": 400,
        "HTTPHeaders": {
            "x-amzn-requestid": "XXXXXXX-XXXX-XXXX-XXX-XXXXXX",
            "content-type": "text/xml",
            "content-length": "804",
            "date": "Thu, 28 Nov 2019 21:12:06 GMT",
        },
        "RetryAttempts": 0,
    }
}


@patch("awscrd.sts._get_security_creds", return_value=MOCK_STS_RESPONSE_HAPPY_PATH)
def test_get_sts_returns_creds_dict(mock_boto):
    token = "123456"
    account_number = "222222"
    username = "test.sam"
    response = get_token(
        token=token, aws_iam_account_number=account_number, username=username
    )

    assert response == {
        "AccessKeyId": "AAAAAAAAAA",
        "SecretAccessKey": "BBBBBBB",
        "SessionToken": "CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC",
    }


@patch("awscrd.sts._get_security_creds", side_effect=Exception)
def test_get_sts_exception_causes_sys_exit(mock_boto):
    with pytest.raises(SystemExit):
        token = "123456"
        account_number = "222222"
        username = "test.sam"
        get_token(token=token, aws_iam_account_number=account_number, username=username)


@patch("awscrd.sts._get_security_creds", return_value=MOCK_STS_RESPONSE_4XX)
def test_get_sts_4xx_causes_sys_exit(mock_boto):
    with pytest.raises(SystemExit):
        token = "123456"
        account_number = "222222"
        username = "test.sam"
        get_token(token=token, aws_iam_account_number=account_number, username=username)
