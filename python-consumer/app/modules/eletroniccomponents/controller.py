from fastapi import APIRouter, HTTPException, status
from . import service
from .schemas import MessageListResponse

router = APIRouter(prefix="/electronic-components", tags=["Electronic Components"])

@router.get(
    "/messages-event",
    response_model=MessageListResponse,
    summary="Listar todas as mensagens recebidas",
    responses={
        200: {"description": "Lista de mensagens obtida com sucesso"},
        404: {"description": "Nenhuma mensagem encontrada"}
    }
)
def list_messages():
    messages = service.EletronicComponents.get_all_messages()
    if not messages:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Nenhuma mensagem encontrada"
        )
    return {"messages": messages}
