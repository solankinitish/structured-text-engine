from fastapi import APIRouter
from app.controllers.text_controller import TextController
from app.models.schemas import TextRequest, TextResponse

router = APIRouter()

controller = TextController()


@router.post("/process", response_model=TextResponse)
def process_text(request: TextRequest):
    return controller.process_text(request)
