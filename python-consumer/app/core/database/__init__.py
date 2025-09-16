from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Cria o mecanismo do SQLAlchemy
if settings.DATABASE_URL:
    engine = create_engine(settings.DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
else:
    # Se não tiver conexão com o banco, usar configurações mínimas
    Base = declarative_base()
    SessionLocal = None
    engine = None

# Função para obter uma sessão do banco de dados
def get_db():
    if SessionLocal:
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
    else:
        yield None
