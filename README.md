# 環境構築
python3.12.6とpoeetryを使用
Lintter、formatterにruff

## パッケージのインストール
```bash
poetry install
```

## 開発サーバーの起動
```bash
uvicorn 'backend.main:app' --host=0.0.0.0 --port=8000
```

## Dockerfile起動時
```bash
docker compose up -d
```

# commitする時は
フォーマットとリントをかけること
```
poetry run ruff format .

poetry run ruff check .
```
