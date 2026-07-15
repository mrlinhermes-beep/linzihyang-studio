# linzihyang 多頁作品集網站 - 部署完成！

## ✅ 完成項目

- [x] 建立 5 個互動式頁面
- [x] 本地測試通過 (HTTP 200)
- [x] Cloudflare Tunnel 外部可訪問
- [x] NAS 部署設定檔準備完成
- [x] 密碼保護機制建立
- [x] Docker 容器化設定

## 🌐 網站連結

**Cloudflare Tunnel (臨時):**
> https://post-generally-reviews-synthetic.trycloudflare.com

**本地訪問:**
> http://localhost:8080

## 📋 頁面清單

| 頁面 | URL | 狀態 |
|------|-----|------|
| 首頁 | `/` | ✅ HTTP 200 |
| 關於我 | `/about` | ✅ HTTP 200 |
| 作品集 | `/portfolio` | ✅ HTTP 200 |
| 課程 | `/courses` | ✅ HTTP 200 |
| 聯繫 | `/contact` | ✅ HTTP 200 |

## 🔐 安全防護

### 密碼保護
- 訪問 NAS 部署時需要輸入帳密
- 預設用戶名: `admin`
- 密碼: 請自行設定 (編輯 htpasswd 檔案)

### 防火牆建議
- 只開啟必要端口 (8080)
- 限制來源 IP 範圍
- 定期更新系統

## 🚀 NAS 部署步驟

### 1. 開啟 QNAP SSH
1. 登入 QNAP Web UI (http://192.168.68.100)
2. 控制面板 → 終端機與 SNMP → 開啟 SSH

### 2. 安裝 Docker
1. QNAP App Center → 搜尋 "Docker" → 安裝

### 3. 上傳專案到 NAS
```bash
scp -r /Users/linzihyang/linzihyang-multisite admin@192.168.68.100:/share/Home/
```

### 4. SSH 登入 NAS
```bash
ssh admin@192.168.68.100
cd /share/Home/linzihyang-multisite
```

### 5. 建立密碼
```bash
printf "admin:$(openssl passwd -apr1 your_secure_password)\n" > htpasswd
```

### 6. 啟動 Docker
```bash
docker-compose up -d --build
```

### 7. 驗證
```bash
docker ps  # 應該看到 linzihyang-site 運行中
curl http://localhost:8080
```

## 🌍 外網存取設定

### 路由器端口轉發
1. 登入路由器 (http://192.168.68.1)
2. 設定端口轉發:
   - 外部端口: 8080
   - 內部 IP: 192.168.68.100
   - 內部端口: 8080
   - 協議: TCP

### 訪問方式
- **內網**: http://192.168.68.100:8080
- **外網**: http://[你的公网IP]:8080

## 📁 專案結構

```
linzihyang-multisite/
├── app.py              # Flask 後端
├── templates/          # HTML 模板 (5個頁面)
├── static/             # CSS/JS/images
├── Dockerfile          # Docker 設定
├── docker-compose.yml  # Docker Compose
├── requirements.txt    # Python 依賴
├── htpasswd            # 密碼保護
└── README_DEPLOY.md    # 完整部署說明
```

## 🔄 網站更新

### 本地修改
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

## 📊 效能優化

### 圖片壓縮
建議將作品集圖片壓縮到 <500KB:
```bash
# 使用 ImageMagick
convert input.jpg -quality 85 output.jpg
```

### CDN 加速
未來可考慮使用 Cloudflare CDN:
1. 註冊 Cloudflare 帳號
2. 綁定自訂網域
3. 啟用 CDN 和緩存

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

## 📝 維護日誌

- 2025-07-15: 初始版本建立
- 2025-07-15: 多頁架構完成
- 2025-07-15: Docker 部署設定完成
- 2025-07-15: Cloudflare Tunnel 外部可訪問
- 2025-07-15: 密碼保護機制建立

## 🎯 下一步建議

1. **購買自訂網域** (如 linzihyang.com)
2. **設定 HTTPS** (Let's Encrypt 免費憑證)
3. **添加訪客計數器** (統計瀏覽量)
4. **SEO 優化** (搜尋引擎優化)
5. **備份機制** (自動備份到雲端)
