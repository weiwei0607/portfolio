import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add CSS for language toggle
css_toggle = """
        html[lang="zh-TW"] .en-only { display: none !important; }
        html[lang="en"] .zh-only { display: none !important; }
"""
html = html.replace('</style>', css_toggle + '    </style>')

# Replace Nav Links with Toggle Button
nav_original = """        <ul class="nav-links">
            <li><a href="#about">關於我</a></li>
            <li><a href="#skills">技能</a></li>
            <li><a href="#projects">作品</a></li>
            <li><a href="#contact">聯繫</a></li>
        </ul>"""
nav_new = """        <ul class="nav-links">
            <li><a href="#about"><span class="zh-only">關於我</span><span class="en-only">About</span></a></li>
            <li><a href="#skills"><span class="zh-only">技能</span><span class="en-only">Skills</span></a></li>
            <li><a href="#projects"><span class="zh-only">作品</span><span class="en-only">Projects</span></a></li>
            <li><a href="#contact"><span class="zh-only">聯繫</span><span class="en-only">Contact</span></a></li>
            <li><button id="lang-toggle" style="background:none; border:1px solid var(--border); color:var(--text); padding:0.2rem 0.6rem; border-radius:4px; cursor:pointer; font-family:inherit; font-size:0.85rem; margin-left:1rem; transition:color 0.3s;">EN</button></li>
        </ul>"""
html = html.replace(nav_original, nav_new)

# Add JS for Language Toggle at the bottom
js_toggle = """
    <script>
        document.getElementById('lang-toggle').addEventListener('click', function() {
            const html = document.documentElement;
            if (html.getAttribute('lang') === 'zh-TW') {
                html.setAttribute('lang', 'en');
                this.textContent = '中';
                document.title = 'WeiWei Ma — AI Product Manager Portfolio';
            } else {
                html.setAttribute('lang', 'zh-TW');
                this.textContent = 'EN';
                document.title = '馬韡寧 WeiWei Ma — AI 產品經理作品集';
            }
        });
    </script>
</body>"""
html = html.replace('</body>', js_toggle)

def swap(zh, en, text=html):
    return text.replace(zh, f'<span class="zh-only">{zh}</span><span class="en-only">{en}</span>')

# Hero section replacements
html = swap("正在尋找 AI 產品經理機會", "Open to AI Product Manager opportunities", html)
hero_h1_zh = """馬韡寧 <span class="gradient">WeiWei Ma</span><br>
                AI 產品經理"""
hero_h1_en = """WeiWei Ma<br>
                <span class="gradient">AI Product Manager</span>"""
html = html.replace(hero_h1_zh, f'<span class="zh-only">{hero_h1_zh}</span>\n                <span class="en-only">{hero_h1_en}</span>')

hero_desc_zh = """從發現用戶痛點到設計 AI 解決方案，從寫 PRD 到動手寫 Code。<br>
                能橋接技術與商業，讓 AI 真正落地產生價值。"""
hero_desc_en = """From spotting user pain points to designing AI solutions — and from writing PRDs to shipping code.<br>
                I bridge product and engineering to turn AI into real business value."""
html = html.replace(hero_desc_zh, f'<span class="zh-only">{hero_desc_zh}</span>\n                <span class="en-only">{hero_desc_en}</span>')

html = swap("AI 整合專案", "AI-integrated projects", html)
html = swap("跨平台經驗", "Cross-platform experience", html)
html = swap("查看作品集 →", "View Projects →", html)
html = swap("📄 下載履歷", "📄 Download Resume", html)
html = swap("📧 聯繫我", "📧 Contact Me", html)

# About section replacements
html = swap("關於我", "About", html)
html = swap("不只會想，還能動手做", "I don't just strategize — I ship.", html)

about_desc_zh = """台大生醫工程研究所，具備 AI 產品運營與數據驅動決策思維。<br>
                從教育科技到心理健康，從 B2B SaaS 到 AI 原生應用，用產品解決真實問題。"""
about_desc_en = """M.S. in Biomedical Engineering from National Taiwan University. Product thinker with a data-driven, AI-first mindset.<br>
                From EdTech to mental health, B2B SaaS to AI-native apps — I build products that solve real problems."""
html = html.replace(about_desc_zh, f'<span class="zh-only">{about_desc_zh}</span>\n                <span class="en-only">{about_desc_en}</span>')

html = swap("我認為好的 AI PM 不只是「提需求的人」，而是要能深入理解技術邊界、設計可行的 AI 交互流程、並用數據驗證假設。", "A great AI PM isn't just someone who files requirements. They understand technical constraints, design usable AI interactions, and validate assumptions with data.", html)
html = swap("在炫圖 AI 實習期間，我定義北美市場短視頻內容策略，分析 TikTok/Instagram/YouTube 用戶行為模式，建立可量化的每日內容決策框架。", "At Xuantu AI, I defined short-form content strategy for the North American market, analyzed user behavior across TikTok, Instagram, and YouTube, and built a measurable daily content decision framework.", html)
html = swap("私下開發了 11 個 Side Projects，從 Flutter 到 FastAPI 到 Next.js，技術棧橫跨 Mobile、Web、Backend。這讓我能和工程師用同一種語言溝通。", "I've built 13 side projects spanning Flutter, FastAPI, and Next.js — across mobile, web, and backend. That hands-on fluency lets me speak the same language as engineers.", html)

html = swap("產品思維", "Product Thinking", html)
html = swap("從用戶研究、競品分析到產品定位，完整產品生命周期經驗", "End-to-end product lifecycle experience: user research, competitive analysis, and positioning", html)
html = swap("AI 落地能力", "AI Execution", html)
html = swap("整合 OpenAI、Gemini、Moonshot 等多 LLM，設計 Prompt 與 AI 交互流程", "Integrated OpenAI, Gemini, Moonshot, and other LLMs; designed prompts and AI interaction flows", html)
html = swap("全端開發", "Full-Stack Building", html)
html = swap("Flutter、React、React Native、FastAPI、Next.js 都能動手做", "Hands-on with Flutter, React, React Native, FastAPI, and Next.js", html)
html = swap("數據驅動", "Data-Driven", html)
html = swap("設計數據儀表板、A/B 測試、用戶行為分析", "Built dashboards, ran A/B tests, and analyzed user behavior", html)

# Skills section replacements
html = swap("技能", "Skills", html)
html = swap("技術與產品工具箱", "Product & Engineering Toolkit", html)
# Skill tags
html = swap(">用戶研究<", ">User Research<", html)
html = swap(">競品分析<", ">Competitive Analysis<", html)
html = swap(">產品路線圖<", ">Product Roadmapping<", html)
html = swap(">數據分析<", ">Data Analytics<", html)
html = swap(">A/B Test<", ">A/B Testing<", html)
html = swap(">LLM 產品化<", ">LLM Productization<", html)
html = swap(">跨平台<", ">Cross-Platform<", html)
html = swap(">API 設計<", ">API Design<", html)
html = swap(">隱私設計<", ">Privacy by Design<", html)
html = swap(">正念設計<", ">Mindful Design<", html)
html = swap(">教育遊戲<", ">Educational Games<", html)
html = swap(">掃碼加好友<", ">QR Friend Connect<", html)
html = swap(">BFS 演算法<", ">BFS Algorithm<", html)
html = swap(">AI 任務分解<", ">AI Task Decomposition<", html)
html = swap(">語音輸入<", ">Voice Input<", html)
html = swap(">多 LLM<", ">Multi-LLM<", html)
html = html.replace('><span class="zh-only">', '><span class="zh-only">').replace('</span><span class="en-only">', '</span><span class="en-only">')

# Projects section replacements
html = swap("作品集", "Projects", html)
html = swap("13 個從 0 到 1 的 Side Projects", "13 Side Projects, 0 → 1", html)
html = swap("每個專案都是從真實痛點出發，設計產品方案，動手實作，迭代優化。", "Every project starts from a real pain point: design the solution, build it, and iterate.", html)

html = swap("🤖 AI 原生應用", "🤖 AI-Native Apps", html)
html = swap("🛠️ 生活工具 / Utility", "🛠️ Life Utilities", html)
html = swap("📚 教育科技", "📚 EdTech", html)
html = swap("🎮 遊戲化 / Gamification", "🎮 Gamification", html)
html = swap("🛠️ 生產力工具", "🛠️ Productivity Tools", html)
html = swap("⚙️ 自動化", "⚙️ Automation", html)

html = swap(">負能量吸收器<", ">Negativity Absorber<", html)
html = swap("AI 情緒夥伴。三階段對話設計（情感驗證→認知重構→行動建議），支援 OpenAI/Moonshot/自訂 API，離線情緒檢測引擎。", "An AI emotional companion. Three-stage chat design (validation → cognitive reframing → actionable advice). Supports OpenAI, Moonshot, and custom APIs, with an offline emotion-detection engine.", html)

html = swap("回憶小說家 Memoir Novelist", "Memoir Novelist", html)
html = swap("把日記變成小說。用戶寫日記 → Gemini AI 生成連貫小說，可選風格（愛情/懸疑/療癒）和角色。Flutter + FastAPI + React 三端架構。", "Turns journal entries into novels. Users write diary posts → Gemini AI generates a coherent story with selectable genres (romance / mystery / healing) and characters. Flutter + FastAPI + React architecture.", html)

html = swap(">Task Shredder<", ">Task Shredder<", html)
html = swap("AI 任務斷捨離。Brain Dump 模糊目標 → AI 生成澄清問題 → 結構化任務輸出。React Native + Next.js API。", "AI-powered task decluttering. Brain-dump vague goals → AI asks clarifying questions → outputs structured tasks. React Native + Next.js API.", html)

html = swap(">新<", ">New<", html)
html = swap(">戀愛對話分析師<", ">Relationship Chat Analyst<", html)
html = swap("貼上對話截圖 → AI 計算「敷衍指數」、識別紅旗行為、找出逃避模式、給出可操作建議。Gemini JSON mode 確保輸出結構。", "Paste a chat screenshot → AI calculates a \"blow-off score,\" flags red flags, spots avoidance patterns, and gives actionable advice. Gemini JSON mode guarantees structured output.", html)

html = swap(">🟢 已上線<", ">🟢 Live<", html)
html = swap("互動推理小說《霧中真相》", "Interactive Mystery Novel: Truth in the Mist", html)
html = swap("設定角色與場景，Gemini 實時生成互動式推理劇情。每段提供多選支線讓玩家主導敘事，水墨風開場動畫，PWA 可加入主畫面。玩家自帶 API key（前端零金鑰外洩）。", "Set characters and scenes; Gemini generates interactive mystery plots in real time. Each segment offers branching choices so players drive the story. Ink-wash intro animation, PWA installable, and BYO API key for zero frontend key exposure.", html)

html = swap("FairMeet 最公平的相聚地", "FairMeet — The Fairest Meetup Spot", html)
html = swap("幫一群人找出最公平的「目的地」。等時圈 × 相聚的設計理念，結果只到行政區層級、不洩漏個人出發位置（隱私優先）。後端 proxy 加 CORS 白名單與配額保護，前端零金鑰。", "Finds the fairest destination for a group. Built on isochrones × meetup design philosophy; results stop at district level to protect starting locations (privacy-first). Backend proxy with CORS allowlist and quota protection; no keys exposed on the frontend.", html)

html = swap(">我的美食地圖<", ">My Food Map<", html)
html = swap("記錄每道菜在每間店的愛與恨，下次不再踩雷。Google Maps 探索附近餐廳、隨機選餐、Firebase 帳號登入後各自雲端同步（每人資料隔離）。", "Track what you loved or hated at every restaurant so you never order wrong again. Explore nearby spots on Google Maps, get a random pick, and sync per-user data to the cloud after Firebase login (data isolation enforced).", html)

html = swap(">Tutoring Bot<", ">Tutoring Bot<", html)
html = swap("B2B 教育 SaaS。學生用 LINE 回報成績 → 老師在 Web Dashboard 看成績折線圖 → 機構管理者看全盤數據。FastAPI + Chart.js + LINE Bot。", "B2B EdTech SaaS. Students report scores via LINE → teachers view trend charts on a web dashboard → admins see the full picture. FastAPI + Chart.js + LINE Bot.", html)

html = swap(">History Bridge<", ">History Bridge<", html)
html = swap("歷史人物六度分隔。輸入兩位歷史人物，用 BFS 演算法找出最短路徑。附帶限時答題和猜猜我是誰遊戲模式。", "Six degrees of separation for historical figures. Enter two people and a BFS algorithm finds the shortest link. Includes timed quizzes and a \"guess who\" game mode.", html)

html = swap("B-Battle 意志力記帳遊戲", "B-Battle — Willpower Budget RPG", html)
html = swap("把記帳變成 RPG。三層預算池 HP 視覺化、人格系統（好友/導師/宿敵）、Gemini AI 即時戰場評論、成就與裝備系統。羅馬大理石風格＋多人雲端同步。", "Turns budgeting into an RPG. Three-tier budget HP visualization, personality system (friend / mentor / rival), live Gemini AI battle commentary, plus achievements and gear. Roman marble aesthetic with multiplayer cloud sync.", html)

html = swap(">Budget Battle<", ">Budget Battle<", html)
html = swap("B-Battle 的 Flutter 跨平台版本。意志力系統、冷靜模式、願望清單、AI 隊友對話。和 React 版資料互通。", "The cross-platform Flutter version of B-Battle. Willpower system, cooldown mode, wishlist, and AI teammate chat. Data syncs with the React version.", html)

html = swap("Break the Loop 生活破圈器", "Break the Loop", html)
html = swap("微習慣挑戰。每天抽一個「身體覺察」小任務，用 2 分鐘打破無意識的行為循環。「呼吸」設計理念：暖奶油＋鼠尾草的平靜介面，去除催促感的 gamification。", "Micro-habit challenges. Draw one daily \"body-awareness\" mini-task and spend two minutes breaking unconscious behavior loops. \"Breathe\" design philosophy: warm cream + sage palette for a calm, non-urgent gamification experience.", html)

html = swap(">職場生存工具<", ">Office Survival Toolkit<", html)
html = swap("上班摸魚不被發現的 PWA 工具箱。AI 加密聊天（6 主題）、變臉 UI（Excel/Outlook/Terminal 偽裝）、下班結界、假通知。", "A PWA toolkit for discreet office downtime. AI encrypted chat with 6 themes, disguise UI (Excel / Outlook / Terminal), end-of-day boundary, and fake notifications.", html)

html = swap(">Declutter Challenge<", ">Declutter Challenge<", html)
html = swap("30 天斷捨離挑戰。每天丟一件，結構化引導 + 進度追蹤 + 分類系統（保留/丟棄/捐贈/猶豫）。", "A 30-day decluttering challenge. One item per day with structured guidance, progress tracking, and sorting buckets (keep / discard / donate / maybe).", html)

html = swap(">WeiWei Reminders<", ">WeiWei Reminders<", html)
html = swap("自動化生活助手。Gmail 消費通知自動解析記帳、Google Sheets 預算自動更新、Telegram 週報推送。", "A personal automation assistant. Parses Gmail purchase receipts for bookkeeping, auto-updates a Google Sheets budget, and pushes weekly Telegram reports.", html)

# Contact & Footer
html = swap("聯繫", "Contact", html)
html = swap("讓我們聊聊 AI 產品", "Let's talk AI products", html)
html = swap("正在尋找 AI 產品經理的機會，歡迎聯繫！", "I'm open to AI Product Manager roles — let's connect!", html)

html = swap("作品", "Projects", html)

html = swap("© 2026 馬韡寧 WeiWei Ma. Built with curiosity and code.", "© 2026 WeiWei Ma. Built with curiosity and code.", html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done translating")
