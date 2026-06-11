# 馬韡寧 WeiWei Ma — AI 產品經理作品集

個人作品集網站，展示 13 個從 0 到 1 的 AI side projects、技術工具箱與聯絡方式。

🔗 **線上版本**：透過 GitHub Pages 自動部署（見下方）

## 內容

- **不只會想，還能動手做** — 自我介紹與定位
- **技術與產品工具箱** — 使用的技術與工具
- **13 個從 0 到 1 的 Side Projects** — 作品列表
- **讓我們聊聊 AI 產品** — 聯絡方式

## 結構

```
portfolio/
├── portfolio/
│   ├── index.html              # 單頁作品集（純靜態，無建置步驟）
│   └── Resume_WeiWei_Ma.pdf    # 履歷 PDF
└── .github/workflows/deploy.yml # GitHub Pages 自動部署
```

## 本地預覽

純靜態頁面，直接開檔或用任意靜態伺服器：

```bash
cd portfolio
python3 -m http.server 8000
# 開啟 http://localhost:8000
```

## 部署

推送到 `master` 或 `main` 分支時，GitHub Actions 會自動把 `portfolio/` 目錄部署到 GitHub Pages。
也可在 Actions 頁面手動觸發（workflow_dispatch）。

> 需在 repo Settings → Pages 將來源設為「GitHub Actions」。

## 更新履歷

直接替換 `portfolio/Resume_WeiWei_Ma.pdf`，並同步更新 `index.html` 中的作品內容。
