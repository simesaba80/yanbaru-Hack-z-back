from sqlalchemy.orm import sessionmaker

from backend.db import engine
from backend.models.voice import Base, Record, User

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

# セッションの作成
Session = sessionmaker(bind=engine)
session = Session()

# テストデータの挿入
test_user = User(
    username="testuser",
    password="testpassword",
    email="kizuku@example.com",
    eisafile="testfile",
)
test_record = Record(id=1, color1="#000000", color2="#FFFFFF")

session.add(test_user)
session.add(test_record)
session.commit()

# セッションのクローズ
session.close()
