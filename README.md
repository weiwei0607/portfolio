# 馬韡寧 WeiWei Ma｜AI 產品作品集

個人作品集網站，展示 21 個從 0 到 1 的 side projects、AI 產品經理的定位與聯絡方式。

🔗 **線上版本**：https://weining-ma.vercel.app

## 頁面

| 路徑 | 內容 |
|------|------|
| `/` | 主作品集：自我介紹、技術工具箱、21 個作品卡、聯絡方式 |
| `/cn/` | 簡體中文版 |
| `/growth/` | 海外增長／運營版履歷頁（中英文：`/growth/cn/`、`/growth/en/`） |
| `/automation/` | 自動化相關作品 |
| `/n8n/` | n8n 工作流作品（含 `gig-monitor.json`、`job-monitor.json`） |

## 結構

```
portfolio/                       # repo 根目錄
├── portfolio/                   # 網站根目錄（Vercel 部署的就是這一層）
│   ├── index.html               # 主頁（純靜態，無建置步驟）
│   ├── cn/ growth/ automation/ n8n/
│   ├── og-image.png             # 社群分享預覽圖
│   ├── Wei-Ning-Ma-Resume-AI-Product-Manager.pdf
│   ├── Wei-Ning-Ma-Resume-Growth-Operations.pdf
│   ├── robots.txt / sitemap.xml
│   └── .vercelignore            # 不對外部署的檔案（草稿、備份、本地預覽用圖片）
├── .github/workflows/deploy.yml # GitHub Pages 部署流程
└── .vercel/                     # Vercel 專案連結（不納入 git）
```

## 本地預覽

純靜態頁面，直接用任意靜態伺服器即可：

```bash
cd portfolio/portfolio
python3 -m http.server 8000
# 開啟 http://localhost:8000
```

## 部署

- **Vercel（正式網址）**：專案名稱 `portfolio`，使用 Vercel CLI 部署。網址 `weining-ma.vercel.app` 透過 `vercel alias set` 指向指定的 deployment。
- **GitHub Pages**：推送到 `master` 或 `main` 時，`.github/workflows/deploy.yml` 會把 `portfolio/` 目錄上傳部署（也可在 Actions 頁面手動觸發）。需在 repo Settings → Pages 將來源設為「GitHub Actions」。

## 更新內容

- **履歷**：替換 `portfolio/` 下對應的 PDF 檔案（AI 產品經理版、增長運營版）。
- **作品**：在 `portfolio/index.html` 的 `project-card` 區塊新增或修改作品卡，之後同步更新 `cn/` 與 `growth/` 中的對應內容。
- **圖片**：`portfolio/` 下的 `masters-*.jpg`、`digest-*.jpg` 只給本地預覽頁 `cover-previews.html` 使用，不會部署上線。
