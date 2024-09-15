from backend.db import engine
from backend.models.voice import Base

# 接続テスト
try:
    connection = engine.connect()
    print("データベースへの接続に成功しました！")
except Exception as e:
    print(f"データベースへの接続エラー: {e}")
finally:
    connection.close()

# データベースのテーブルを削除
Base.metadata.drop_all(bind=engine)
# データベースのテーブルを作成
Base.metadata.create_all(bind=engine)
