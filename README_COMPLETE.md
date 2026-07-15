# linzihyang 高互動性作品集網站 - 完整部署指南

## 🎉 網站特點

### 高互動性功能
- ✅ **Three.js 粒子系統** - 3D 金色粒子動畫，回應滑鼠移動
- ✅ **GSAP 動畫** - 專業級滾動動畫和過場效果
- ✅ **打字機效果** - 首頁標語逐字顯示
- ✅ **自定義游標** - 金色圓圈游標 + 懸停放大效果
- ✅ **磁吸按鈕** - 按鈕跟隨游標微微移動
- ✅ **3D 傾斜卡片** - About 區塊照片跟隨滑鼠 3D 旋轉
- ✅ **數字滾動動畫** - 統計數字從 0 滾動到目標值
- ✅ **滾動揭示動畫** - 各區塊元素隨滾動漸入
- ✅ **視差滾動** - Hero 區域視差效果
- ✅ **Lightbox** - 作品集全屏查看，支援鍵盤操作
- ✅ **課程彈窗** - 點擊課程展開詳細大綱
- ✅ **篩選功能** - 作品集可按類別篩選
- ✅ **載入動畫** - 品牌名稱 + 進度條預載入畫面

### 完整內容對齊
- ✅ **首頁** - Hero、快速統計、精選作品、服務介紹
- ✅ **關於我** - 完整履歷、經歷時間軸、獎項榮譽
- ✅ **作品集** - 12 件作品，可篩選（全部/婚紗/人像/品牌/建築）
- ✅ **課程** - 7 種課程，完整時數與內容
- ✅ **聯繫** - 社群連結、聯絡表單

### 原始 Canva 網站資料對齊
- ✅ 所有文字內容完整移植
- ✅ 14 項經歷認證完整列出
- ✅ 16 家合作品牌完整列出
- ✅ 2 項獎項完整列出
- ✅ 7 種課程完整列出（含詳細說明）
- ✅ 所有社群連結完整
- ✅ 聯絡資訊完整（Email、電話）

## 🌐 網站連結

**本地訪問:**
> http://localhost:8080

**Cloudflare Tunnel (外部可訪問):**
> https://post-generally-reviews-synthetic.trycloudflare.com

## 📋 5個頁面完整清單

| 頁面 | URL | 功能 |
|------|-----|------|
| 首頁 | `/` | Hero動畫、快速統計、精選作品、服務介紹 |
| 關於我 | `/about` | 個人介紹、經歷時間軸、獎項榮譽 |
| 作品集 | `/portfolio` | 12件作品、分類篩選、Lightbox |
| 課程 | `/courses` | 7種課程、詳細大綱彈窗 |
| 聯繫 | `/contact` | 社群連結、聯絡表單 |

## 🚀 NAS 部署步驟 (QNAP)

### 步驟 1: 開啟 QNAP SSH
1. 登入 QNAP Web UI (http://192.168.68.100)
2. 控制面板 → 終端機與 SNMP → 開啟 SSH 功能
3. 記住端口（預設 22）

### 步驟 2: 安裝 Docker
1. QNAP App Center → 搜尋 "Docker" → 安裝
2. 等待安裝完成

### 步驟 3: 上傳專案到 NAS
```bash
# 在 Mac 上執行
scp -r /Users/linzihyang/linzihyang-multisite admin@192.168.68.100:/share/Home/
```

### 步驟 4: SSH 登入 NAS
```bash
ssh admin@192.168.68.100
cd /share/Home/linzihyang-multisite
```

### 步驟 5: 建立密碼保護
```bash
# 產生密碼檔案
printf "admin:$(openssl passwd -apr1 your_secure_password)\n" > htpasswd
```

### 步驟 6: 啟動 Docker
```bash
# 建立 Docker 映像
docker build -t linzihyang-site .

# 啟動容器
docker-compose up -d

# 驗證
docker ps  # 應該看到 linzihyang-interactive 運行中
curl http://localhost:8080
```

### 步驟 7: 驗證網站
```bash
# 測試所有頁面
curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/
curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/about
curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/portfolio
curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/courses
curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/contact
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

## 🔐 安全防護

### 密碼保護
- 訪問網站時需要輸入帳密
- 預設: admin / your_secure_password
- 修改密碼: 編輯 htpasswd 檔案

### 防火牆建議
- 只開啟必要端口 (8080)
- 限制來源 IP 範圍 (如果可以)
- 定期更新系統

## 📁 專案結構

```
linzihyang-multisite/
├── app_v2.py              # Flask 後端（高互動性版本）
├── templates/             # HTML 模板
│   ├── home.html          # 首頁（Three.js + GSAP）
│   ├── about.html         # 關於我
│   ├── portfolio.html     # 作品集（篩選 + Lightbox）
│   ├── courses.html       # 課程（彈窗）
│   └── contact.html       # 聯繫
├── static/                # 靜態資源
│   ├── css/
│   │   └── interactive.css  # 互動式樣式
│   └── js/
│       └── interactive.js   # 互動式腳本
├── assets/                # 圖片資源
│   ├── images/
│   │   ├── portfolio/     # 作品集圖片
│   │   ├── about/         # About 圖片
│   │   └── courses/       # 課程圖片
│   └── images/            # 原始 Canva 圖片（50張）
├── Dockerfile             # Docker 設定
├── docker-compose.yml     # Docker Compose
├── requirements.txt       # Python 依賴
├── htpasswd               # 密碼保護
└── README_DEPLOY.md       # 本文件
```

## 🔄 網站更新

### 本地修改
1. 編輯對應的 HTML 模板
2. 重新啟動 Flask:
   ```bash
   pkill -f "python3 app_v2.py"
   cd /Users/linzihyang/linzihyang-multisite
   source venv/bin/activate
   python3 app_v2.py
   ```

### Docker 部署更新
```bash
docker-compose down
docker build -t linzihyang-site .
docker-compose up -d
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
3. 查看錯誤日誌: `cat /tmp/flask_v2.log`

### Docker 問題
1. 檢查 Docker 狀態: `docker ps`
2. 查看容器日誌: `docker logs linzihyang-interactive`
3. 重啟容器: `docker-compose restart`

### 密碼忘記
1. 重新產生 htpasswd:
   ```bash
   printf "admin:$(openssl passwd -apr1 new_password)\n" > htpasswd
   docker-compose restart
   ```

### 圖片無法顯示
1. 檢查圖片路徑是否正確
2. 確認圖片檔案存在於 assets/images/
3. 檢查 Flask 靜態檔案路由

## 📝 維護日誌

- 2025-07-15: 初始版本建立
- 2025-07-15: 高互動性功能完成
- 2025-07-15: 原始 Canva 網站內容完整對齊
- 2025-07-15: Docker 部署設定完成
- 2025-07-15: 密碼保護機制建立

## 🎯 下一步建議

1. **購買自訂網域** (如 linzihyang.com)
2. **設定 HTTPS** (Let's Encrypt 免費憑證)
3. **添加訪客計數器** (統計瀏覽量)
4. **SEO 優化** (搜尋引擎優化)
5. **備份機制** (自動備份到雲端)
6. **添加部落格功能** (未來擴充)

## 💡 技術棧

- **前端**: HTML5, CSS3, JavaScript (ES6+)
- **動畫**: Three.js (3D粒子), GSAP (滾動動畫)
- **後端**: Python Flask
- **部署**: Docker, Cloudflare Tunnel
- **字體**: Noto Sans TC, Noto Serif TC
- **配色**: 深綠 (#00170b) + 金色 (#ad803b, #e1a64c)
