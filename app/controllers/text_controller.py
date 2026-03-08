from app.services.text_service import TextService
from app.models.schemas import TextRequest, TextResponse
from app.utils.logger import get_logger


class TextController:

    def __init__(self, text_service: TextService):

        self.service = text_service
        self.logger = get_logger(__name__)
    
    def process_text(self, request: TextRequest) -> TextResponse:

        self.logger.info("Controller received request")

        return self.service.process(request)
