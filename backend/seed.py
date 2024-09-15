from sqlalchemy.orm import sessionmaker

from backend.db import engine
from backend.models.color import Base, Eisafile, User

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
    user_id="testuser",
    mail="kizuku@example.com",
    hashed_password="testpassword",
    name="kizuku",
)

test_eisafile = Eisafile(
    id="testuser",
    file_path="hoge.ogg",
    created_at="2021-01-01",
    updated_at="2021-01-01",
)

session.add(test_user)
session.add(test_eisafile)
session.commit()

# セッションのクローズ
session.close()
