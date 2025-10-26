# ---- ベースイメージ ----
FROM python:3.12-slim

# ---- 作業ディレクトリ ----
WORKDIR /app

# ---- 依存関係コピーとインストール ----
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- ソースコードコピー ----
COPY . .

# ---- Flask起動設定 ----
ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# ---- ポート開放 ----
EXPOSE 10000

# ---- 実行コマンド ----
CMD ["flask", "run", "--port=10000"]
