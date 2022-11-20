import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    even_key = encrypt_message("ABBCCA", 2)
    odd_key = encrypt_message("AABBCC", 1)

    invalid_key = encrypt_message("AABBCC", -1)

    assert even_key == "ACCB_BA"
    assert odd_key == "A_CCBBA"

    assert invalid_key == "CCBBAA"

    with pytest.raises(TypeError) as error:
        encrypt_message(98, 2)

    assert str(error.value) == "tipo inválido para message"
