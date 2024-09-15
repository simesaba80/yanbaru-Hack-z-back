# 環境構築
python3.12.6とpoeetryを使用
Lintter、formatterにruff

## パッケージのインストール
```bash
poetry install
```

## SwaggerUIの確認
```bash
poetry run uvicorn 'backend.main:app' --host=0.0.0.0 --port=8000
```
して`http://localhost:8000/docs`にアクセス

## 開発用サーバー起動時
```bash
docker compose up -d
```

# commitする時は
フォーマットとリントをかけること
```
poetry run ruff format .

poetry run ruff check .
```
