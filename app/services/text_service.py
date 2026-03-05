from app.utils.logger import get_logger
from app.exceptions import InvalidInputError

class TextService:

    def __init__(self):
        self.logger = get_logger(__name__)

    def process(self, text: str) -> str:
        if not isinstance(text, str):
            raise InvalidInputError("Input must be a string.")
        
        if text.strip() == "":
            raise InvalidInputError("Input text cannot be empty.")
        
        self.logger.info("Processing text")

        return text.upper()