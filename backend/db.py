from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.utils import config

# 接続文字列を定義
db_url = config.config.DB_URL

# SQLAlchemyエンジンを作成
engine = create_engine(db_url)

# セッションローカルクラスを作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# データベースセッションを取得する関数を定義
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
