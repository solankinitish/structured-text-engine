from fastapi import APIRouter
from app.controllers.text_controller import TextController
from app.models.schemas import TextRequest, TextResponse
from app.core.container import Container

router = APIRouter()

container = Container()
controller = TextController(container.text_service)


@router.post("/process", response_model=TextResponse)
def process_text(request: TextRequest):
    return controller.process_text(request)
