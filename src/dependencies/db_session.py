from sqlalchemy.orm import Session

from src.configs.postgresql import database


def get_db() -> Session:
    db = database.get_session()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.commit()
        db.close()
