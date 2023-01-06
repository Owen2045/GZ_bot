FROM python:3.10

# 設定環境變數
# ENV PYTHONDONTWRITEBYTECODE 1防止 Python 將 pyc 文件複製到容器中。
ENV PYTHONDONTWRITEBYTECODE 1

# ENV PYTHONUNBUFFERED 1確保將 Python 輸出記錄到終端，從而可以實時監控 Django 日誌。
ENV PYTHONUNBUFFERED 1

# 忽略PIP用su問題
ENV PIP_ROOT_USER_ACTION=ignore

# 在容器內/var/www/html 建立資料夾
RUN mkdir -p /var/www/html/GZ_bot

# 設定工作目錄
WORKDIR /var/www/html/GZ_bot

# 複製到當前工作目錄
COPY requirements.txt ./

# 安裝
RUN apt-get update && apt-get install -y \
    sqlite3 \
    python3-dev \
    libproj-dev

# 安裝pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# COPY . .
# CMD ["python3", "-OO", "-m", "carberretta"]
