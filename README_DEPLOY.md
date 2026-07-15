# linzihyang 多頁作品集網站

## 🌐 網站功能

- **5個頁面**: 首頁、關於我、作品集、課程、聯繫
- **互動式設計**: 粒子動畫、篩選功能、響應式布局
- **多語言**: 繁體中文
- **配色**: 深綠 + 金色高級感設計

## 📁 專案結構

```
linzihyang-multisite/
├── app.py              # Flask 後端
├── templates/          # HTML 模板
│   ├── base.html       # 基礎模板
│   ├── home.html       # 首頁
│   ├── about.html      # 關於我
│   ├── portfolio.html  # 作品集
│   ├── courses.html    # 課程
│   └── contact.html    # 聯繫
├── static/             # 靜態資源
│   ├── css/style.css   # 樣式表
│   ├── js/main.js      # JavaScript
│   └── images/         # 圖片
├── Dockerfile          # Docker 設定
├── docker-compose.yml  # Docker Compose
├── requirements.txt    # Python 依賴
└── htpasswd            # 密碼保護
```

## 🚀 本地運行

```bash
cd /Users/linzihyang/linzihyang-multisite
source venv/bin/activate
python3 app.py
```

訪問: http://localhost:8080

## 🐳 NAS 部署 (QNAP)

### 步驟 1: 開啟 NAS SSH
1. 登入 QNAP Web UI (http://192.168.68.100)
2. 控制面板 → 終端機與 SNMP → 開啟 SSH 功能

### 步驟 2: 安裝 Docker
1. QNAP App Center → 搜尋 "Docker" → 安裝

### 步驟 3: 上傳專案
```bash
# 在 Mac 上執行
scp -r /Users/linzihyang/linzihyang-multisite admin@192.168.68.100:/share/Home/
```

### 步驟 4: SSH 登入 NAS
```bash
ssh admin@192.168.68.100
cd /share/Home/linzihyang-multisite
```

### 步驟 5: 建立密碼
```bash
printf "admin:$(openssl passwd -apr1 your_secure_password)\n" > htpasswd
```

### 步驟 6: 啟動 Docker
```bash
docker-compose up -d --build
```

### 步驟 7: 驗證
```bash
docker ps  # 應該看到 linzihyang-site 運行中
curl http://localhost:8080
```

## 🌍 外網存取

### 路由器設定
1. 登入路由器 (通常是 192.168.68.1)
2. 設定端口轉發:
   - 外部端口: 8080 → 內部 IP: 192.168.68.100, 端口: 8080

### 訪問網址
- 內網: http://192.168.68.100:8080
- 外網: http://[你的公网IP]:8080

## 🔐 安全防護

### 密碼保護
- 訪問網站時需要輸入帳密
- 預設: admin / your_secure_password
- 修改密碼: 編輯 htpasswd 檔案

### 防火牆建議
- 只開啟必要端口 (8080)
- 限制來源 IP 範圍 (如果可以)
- 定期更新系統

## 📊 頁面說明

### 首頁 (/)
- Hero 區域與粒子動畫
- 快速統計數字
- 精選作品集預覽
- 服務介紹

### 關於我 (/about)
- 個人介紹
- 經歷與認證時間軸
- 專業技能展示

### 作品集 (/portfolio)
- 可篩選的作品格
- 分類: 全部/婚紗/人像/品牌/建築
- 懸停動畫效果

### 課程 (/courses)
- 4種課程時數與內容
- 迷你班/進階班/企業版
- 報名連結

### 聯繫 (/contact)
- 社群媒體連結
- 聯絡表單
- 電子郵件與電話

## 🔄 更新網站

### 修改內容
1. 編輯對應的 HTML 模板
2. 重新啟動 Flask:
   ```bash
   pkill -f "python3 app.py"
   python3 app.py
   ```

### Docker 部署更新
```bash
docker-compose down
docker-compose up -d --build
```

## 📝 維護日誌

- 2025-07-15: 初始版本建立
- 2025-07-15: 多頁架構完成
- 2025-07-15: Docker 部署設定完成

## 🆘 故障排除

### 網站無法訪問
1. 檢查 Flask 是否在運行: `ps aux | grep python3`
2. 檢查端口是否被佔用: `lsof -i:8080`
3. 查看錯誤日誌: `cat /tmp/flask.log`

### Docker 問題
1. 檢查 Docker 狀態: `docker ps`
2. 查看容器日誌: `docker logs linzihyang-site`
3. 重啟容器: `docker-compose restart`

### 密碼忘記
1. 重新產生 htpasswd:
   ```bash
   printf "admin:$(openssl passwd -apr1 new_password)\n" > htpasswd
   docker-compose restart
   ```
