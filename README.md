# 進虛擬環境
win10
F:\site_project\GZ_bot\venv_GZ_bot_win\Scripts\Activate.ps1
WSL
source /mnt/f/site_project/GZ_bot/venv_GZ_bot/bin/activate
# win選擇自動進入虛擬環境
ctrl + shift + p 輸入：Python: Select Interpreter 
# 建立虛擬環境
pip install virtualenv
python -m venv project_name


# 資料表更新
python manage.py makemigrations
python manage.py migrate


# 虛擬環境安裝chrome
sudo apt update
sudo apt install wget
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get install -f
google-chrome --version

# future plan
## GZ_info
### 資訊指令
```txt
1. info > 活動資訊 
2. note > 更新資訊    
```




