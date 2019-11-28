import pytest

from awscrd.parse import profile_from_config


def test_parse_profile_from_config_returns_creds_tuple():
    profile = "test"
    input_test_creds_file = "./test/data/test_creds"
    account_number, username = profile_from_config(
        profile=profile, input_file_path=input_test_creds_file
    )
    assert account_number == "123456"
    assert username == "test.sam"


def test_parse_profile_from_config_raises_if_no_profile_in_file():
    profile = "qa"
    input_test_creds_file = "./tests/data/test_creds"
    with pytest.raises(KeyError):
        profile_from_config(profile=profile, input_file_path=input_test_creds_file)
