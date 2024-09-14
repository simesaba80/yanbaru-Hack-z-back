from sqlalchemy import create_engine

from backend.utils import config

# 接続文字列を定義
db_url = config.config.DB_URL

# SQLAlchemyエンジンを作成
engine = create_engine(db_url)

# 接続テスト
try:
    connection = engine.connect()
    print("データベースへの接続に成功しました！")
except Exception as e:
    print(f"データベースへの接続エラー: {e}")
finally:
    connection.close()
