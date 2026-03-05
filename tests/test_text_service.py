from app.services.text_service import TextService
from app.exceptions import InvalidInputError
import pytest

def test_process_valid_text():
    service = TextService()
    result = service.process("hello")
    assert result == "HELLO"


def test_empty_string_raises_error():
    service = TextService()
    with pytest.raises(InvalidInputError):
        service.process("")


def test_non_string_raises_error():
    service = TextService()
    with pytest.raises(InvalidInputError):
        service.process(123)