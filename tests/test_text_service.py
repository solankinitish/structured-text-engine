import pytest

from app.services.text_service import TextService
from app.models.schemas import TextRequest
from pydantic import ValidationError


def test_process_valid_text():
    service = TextService()
    request = TextRequest(text="hello")
    result = service.process(request)
    assert result.result == "HELLO"


def test_empty_string_raises_error():
    service = TextService()
    with pytest.raises(ValidationError):
        TextRequest(text="")


def test_non_string_raises_error():
    service = TextService()
    with pytest.raises(ValidationError):
        TextRequest(text=123)
