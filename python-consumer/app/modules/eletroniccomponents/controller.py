from fastapi import APIRouter, HTTPException, status
from . import service
from .schemas import MessageEventResponse

router = APIRouter(prefix="/electronic-components", tags=["Electronic Components"])

@router.get(
    "/message-event",
    response_model=MessageEventResponse,
    summary="Obter último evento de mensagem",
    responses={
        200: {"description": "Mensagem encontrada com sucesso"},
        404: {"description": "Nenhuma mensagem encontrada"}
    }
)
def get_message_event():
    result = service.EletronicComponents.get_message_event()
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Nenhuma mensagem encontrada"
        )
    return result
