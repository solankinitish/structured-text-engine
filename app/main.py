from app.config import settings
from app.utils.logger import get_logger
from app.services.text_service import TextService
from app.exceptions import InvalidInputError

def main():
    logger = get_logger(__name__)
    logger.info(f"Starting {settings.app_name}")

    service = TextService()
    
    try:
        result = service.process("hello world")
        logger.info(f"Processed result: {result}")
    
    except InvalidInputError as e:
        logger.error(f"Invalid input: {e}")
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
