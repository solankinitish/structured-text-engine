from app.utils.logger import get_logger
from app.models.schemas import TextRequest
from app.controllers.text_controller import TextController

logger = get_logger(__name__)


def main():
    logger.info("Starting StructuredTextEngine")

    controller = TextController()

    request = TextRequest(text="hello world")

    response = controller.process_text(request)

    logger.info(f"Processed result: {response.result}")


if __name__ == "__main__":
    main()
