# Python FastAPI backend

## セットアップ

1. 必要なパッケージをインストール

```
pip install fastapi uvicorn
```

2. サーバー起動

```
uvicorn main:app --reload
```

## API エンドポイント例

- `/` : Hello World
- `/api/hello` : JSON レスポンス

---

# Astro frontend

## セットアップ

1. 依存パッケージのインストール

```
cd frontend
npm install
```

2. サーバー起動

```
npm run dev
```

---

# 全体構成

- `frontend/` : Astro フロントエンド
- `backend/` : Python FastAPI バックエンド

# 起動方法

1. 2 つのターミナルでそれぞれサーバーを起動してください。
2. ブラウザで `http://localhost:4321`（Astro）と `http://localhost:8000`（FastAPI）にアクセスできます。
