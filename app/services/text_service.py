from app.utils.logger import get_logger
from app.models.schemas import TextRequest, TextResponse

class TextService:

    def __init__(self):
        self.logger = get_logger(__name__)

    def process(self, request: TextRequest) -> TextResponse:
        
        self.logger.info("Processing text")

        result = request.text.upper()

        return TextResponse(result=result)
