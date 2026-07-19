#!/usr/bin/env python3
"""Generate iOS-style app icons for portfolio projects.

Style: vibrant vertical gradient background, bold white glyph with a
subtle drop shadow, soft top sheen — like modern Apple app icons.
"""

# name -> (gradient_top, gradient_bottom, glyph_svg)
ICONS = {
    # 吸收負能量 → 平靜的笑臉 + 火花
    "negativity-absorber": ("#2dd4bf", "#0f766e", """
        <circle cx="60" cy="62" r="26" fill="none" stroke-width="6"/>
        <path d="M44 57 q6 -7 12 0" fill="none" stroke-width="5"/>
        <path d="M64 57 q6 -7 12 0" fill="none" stroke-width="5"/>
        <path d="M48 70 q12 10 24 0" fill="none" stroke-width="5.5"/>
        <path d="M90 22 C91.2 27 92.5 28.3 97.5 29.5 C92.5 30.7 91.2 32 90 37 C88.8 32 87.5 30.7 82.5 29.5 C87.5 28.3 88.8 27 90 22 Z" class="fill"/>
        <circle cx="27" cy="33" r="3" class="fill"/>
    """),
    # 回憶錄小說 → 攤開的書
    "memoir-novelist": ("#fbbf24", "#d97706", """
        <path d="M60 42 C53 35 43 33 32 36 V84 C43 81 53 83 60 89 C67 83 77 81 88 84 V36 C77 33 67 35 60 42 Z" fill="none" stroke-width="6"/>
        <path d="M60 42 V89" fill="none" stroke-width="5"/>
        <path d="M40 50 h11 M40 60 h11 M69 50 h11 M69 60 h11" fill="none" stroke-width="4"/>
    """),
    # 任務粉碎機 → 紙進碎紙機
    "task-shredder": ("#f87171", "#dc2626", """
        <path d="M44 52 V30 a5 5 0 0 1 5 -5 h22 a5 5 0 0 1 5 5 V52" fill="none" stroke-width="6"/>
        <path d="M52 36 h16 M52 44 h16" fill="none" stroke-width="4"/>
        <rect x="28" y="52" width="64" height="16" rx="8" fill="none" stroke-width="6"/>
        <path d="M42 75 v12 M54 75 v17 M66 75 v10 M78 75 v14" fill="none" stroke-width="5"/>
    """),
    # 聊天關係分析 → 對話框 + 愛心
    "relationship-chat": ("#f472b6", "#db2777", """
        <rect x="28" y="30" width="64" height="40" rx="14" fill="none" stroke-width="6"/>
        <path d="M44 70 L38 86 L58 70" fill="none" stroke-width="6"/>
        <path d="M60 60 C54 51 43 52.5 43 45 C43 39.5 48.5 37 53 39.5 C56 41 58.5 43.5 60 46 C61.5 43.5 64 41 67 39.5 C71.5 37 77 39.5 77 45 C77 52.5 66 51 60 60 Z" class="fill"/>
    """),
    # 霧中真相 → 放大鏡裡的眼睛 + 霧
    "interactive-novel": ("#6366f1", "#3730a3", """
        <circle cx="54" cy="50" r="21" fill="none" stroke-width="6"/>
        <path d="M69 65 L86 82" fill="none" stroke-width="8"/>
        <path d="M43 50 q11 -11 22 0 q-11 11 -22 0 Z" fill="none" stroke-width="4"/>
        <circle cx="54" cy="50" r="3.5" class="fill"/>
        <path d="M24 88 h16 M30 97 h22" fill="none" stroke-width="5" opacity="0.75"/>
    """),
    # 最公平相聚地 → 中心大頭針 + 四方匯聚
    "fairmeet": ("#34d399", "#059669", """
        <path d="M60 34 c-10.5 0 -18 7.5 -18 17 0 12 18 27 18 27 s18 -15 18 -27 c0 -9.5 -7.5 -17 -18 -17 Z" fill="none" stroke-width="6"/>
        <circle cx="60" cy="50" r="6" fill="none" stroke-width="5"/>
        <circle cx="28" cy="28" r="4.5" class="fill"/>
        <circle cx="92" cy="28" r="4.5" class="fill"/>
        <circle cx="28" cy="92" r="4.5" class="fill"/>
        <circle cx="92" cy="92" r="4.5" class="fill"/>
        <path d="M33 33 L43 41 M87 33 L77 41 M33 87 L45 75 M87 87 L75 75" fill="none" stroke-width="5" opacity="0.85"/>
    """),
    # 美食地圖 → 大頭針裡的叉子
    "food-map": ("#fb923c", "#ea580c", """
        <path d="M60 26 c-12.7 0 -22 9.3 -22 21 0 15 22 45 22 45 s22 -30 22 -45 c0 -11.7 -9.3 -21 -22 -21 Z" fill="none" stroke-width="6"/>
        <path d="M53 38 v8 M60 38 v8 M67 38 v8 M60 46 v14" fill="none" stroke-width="4.5"/>
    """),
    # 家教 bot → 學士帽
    "tutoring-bot": ("#60a5fa", "#2563eb", """
        <path d="M60 30 L94 46 L60 62 L26 46 Z" fill="none" stroke-width="6"/>
        <path d="M42 54 v14 c0 7 36 7 36 0 v-14" fill="none" stroke-width="6"/>
        <path d="M94 46 v18" fill="none" stroke-width="5"/>
        <circle cx="94" cy="68" r="4" class="fill"/>
    """),
    # 歷史橋 → 拱橋
    "history-bridge": ("#f59e0b", "#b45309", """
        <path d="M20 78 H100" fill="none" stroke-width="6"/>
        <path d="M28 78 Q60 36 92 78" fill="none" stroke-width="6"/>
        <path d="M44 62 V78 M60 57 V78 M76 62 V78" fill="none" stroke-width="4.5"/>
        <circle cx="88" cy="32" r="7" fill="none" stroke-width="5"/>
    """),
    # 意志力記帳戰鬥 → 盾牌 + 閃電
    "b-battle": ("#a78bfa", "#7c3aed", """
        <path d="M60 26 L88 36 V60 C88 76 76 86 60 93 C44 86 32 76 32 60 V36 Z" fill="none" stroke-width="6"/>
        <path d="M66 42 L50 64 H60 L54 80 L70 57 H60 Z" class="fill" stroke-width="2"/>
    """),
    # 預算戰鬥 → 金幣 $
    "budget-battle": ("#4ade80", "#16a34a", """
        <circle cx="60" cy="60" r="27" fill="none" stroke-width="6"/>
        <path d="M60 43 V77" fill="none" stroke-width="5"/>
        <path d="M68 51 C65 46 52 46 52 53 C52 59 68 58 68 66 C68 73 55 74 51 69" fill="none" stroke-width="5"/>
    """),
    # 打破循環 → 斷開的循環箭頭 + 火花
    "break-the-loop": ("#22d3ee", "#0891b2", """
        <path d="M84.4 53.1 A26 26 0 1 1 68.9 37.6" fill="none" stroke-width="6"/>
        <path d="M76 40 L64.4 42.7 L68.8 30.5 Z" class="fill"/>
        <path d="M89 36 L96 29 M93 49 H102" fill="none" stroke-width="5"/>
    """),
    # 辦公室生存 → 公事包 + 心電圖
    "office-survival": ("#94a3b8", "#475569", """
        <rect x="28" y="46" width="64" height="40" rx="9" fill="none" stroke-width="6"/>
        <path d="M48 46 V40 a4 4 0 0 1 4 -4 h16 a4 4 0 0 1 4 4 v6" fill="none" stroke-width="5.5"/>
        <path d="M34 66 H46 L52 56 L60 76 L66 62 L70 66 H86" fill="none" stroke-width="5"/>
    """),
    # 斷捨離 → 打開的箱子往上丟
    "declutter": ("#6ee7b7", "#10b981", """
        <path d="M32 60 H88 V88 H32 Z" fill="none" stroke-width="6"/>
        <path d="M32 60 L24 48 M88 60 L96 48" fill="none" stroke-width="6"/>
        <path d="M60 52 V26 M60 26 L51 35 M60 26 L69 35" fill="none" stroke-width="6"/>
        <path d="M86 30 v10 M81 35 h10" fill="none" stroke-width="4"/>
    """),
    # 提醒系統 → 鈴鐺 + 通知點
    "weiwei-reminders": ("#fb7185", "#e11d48", """
        <path d="M60 30 c-12.5 0 -21 9 -21 21 v11 c0 7 -3.5 11 -8 15 H89 c-4.5 -4 -8 -8 -8 -15 V51 c0 -12 -8.5 -21 -21 -21 Z" fill="none" stroke-width="6"/>
        <path d="M60 30 V24" fill="none" stroke-width="6"/>
        <path d="M52 84 q8 9 16 0" fill="none" stroke-width="6"/>
        <circle cx="89" cy="31" r="9" class="fill"/>
    """),
    # 相簿整理 → 疊起來的照片 + 山景
    "album-organizer": ("#f59e0b", "#ef4444", """
        <rect x="40" y="24" width="50" height="38" rx="6" transform="rotate(8 65 43)" fill="none" stroke-width="5" opacity="0.6"/>
        <rect x="28" y="46" width="54" height="42" rx="6" fill="none" stroke-width="6"/>
        <path d="M33 82 L46 67 L55 76 L66 63 L77 82" fill="none" stroke-width="5"/>
        <circle cx="42" cy="56" r="4" class="fill"/>
    """),
    # 人際腦 → 愛心 + 關係網絡
    "partner-brain": ("#e879f9", "#c026d3", """
        <path d="M60 90 C40 76 28 64 28 49 C28 37 38 30 48 32.5 C53 33.8 57.5 37.5 60 42 C62.5 37.5 67 33.8 72 32.5 C82 30 92 37 92 49 C92 64 80 76 60 90 Z" fill="none" stroke-width="6"/>
        <circle cx="47" cy="50" r="4" class="fill"/>
        <circle cx="73" cy="50" r="4" class="fill"/>
        <circle cx="60" cy="68" r="4" class="fill"/>
        <path d="M50 53 L57 64 M70 53 L63 64 M52 50 H68" fill="none" stroke-width="3.5"/>
    """),
    # 家庭算命 → 水晶球 + 星星
    "family-destiny": ("#818cf8", "#4c1d95", """
        <circle cx="60" cy="52" r="24" fill="none" stroke-width="6"/>
        <path d="M45 82 H75 L81 93 H39 Z" fill="none" stroke-width="6"/>
        <path d="M58 36 C60 44 62 46 70 48 C62 50 60 52 58 60 C56 52 54 50 46 48 C54 46 56 44 58 36 Z" class="fill"/>
        <circle cx="72" cy="60" r="2.5" class="fill"/>
        <circle cx="70" cy="40" r="2" class="fill"/>
    """),
    # 旅遊日記 → 紙飛機 + 航跡
    "travel-journal": ("#38bdf8", "#0284c7", """
        <path d="M94 30 L26 54 L54 64 L60 90 Z" fill="none" stroke-width="6"/>
        <path d="M94 30 L54 64" fill="none" stroke-width="5"/>
        <path d="M26 86 q12 9 26 -1" fill="none" stroke-width="4.5" stroke-dasharray="1 9"/>
    """),
    # 特種部隊計畫 → 瞄準鏡
    "special-forces-planner": ("#84cc16", "#3f6212", """
        <circle cx="60" cy="60" r="24" fill="none" stroke-width="6"/>
        <circle cx="60" cy="60" r="10" fill="none" stroke-width="5"/>
        <circle cx="60" cy="60" r="3.5" class="fill"/>
        <path d="M60 24 V36 M60 84 V96 M24 60 H36 M84 60 H96" fill="none" stroke-width="6"/>
    """),
    # 時代大逃殺 → 沙漏（歷史洪流中求生）
    "era-survival": ("#b91c1c", "#450a0a", """
        <path d="M40 28 H80 M40 92 H80" fill="none" stroke-width="6"/>
        <path d="M45 30 C45 48 57 53 57 60 C57 67 45 72 45 90" fill="none" stroke-width="5.5"/>
        <path d="M75 30 C75 48 63 53 63 60 C63 67 75 72 75 90" fill="none" stroke-width="5.5"/>
        <path d="M53 38 h14" fill="none" stroke-width="4"/>
        <circle cx="60" cy="60" r="2.5" class="fill"/>
        <path d="M54 84 h12" fill="none" stroke-width="4"/>
        <path d="M90 34 C91 38 92 39 96 40 C92 41 91 42 90 46 C89 42 88 41 84 40 C88 39 89 38 90 34 Z" class="fill"/>
    """),
    # Daily Dose 每日一劑 → 日出
    "daily-dose": ("#fdba74", "#ea580c", """
        <path d="M28 76 H92" fill="none" stroke-width="6"/>
        <path d="M42 76 A18 18 0 0 1 78 76" fill="none" stroke-width="6"/>
        <path d="M60 40 V30 M36 50 L29 43 M84 50 L91 43" fill="none" stroke-width="5.5"/>
        <path d="M36 90 h12 M52 90 h12 M68 90 h12" fill="none" stroke-width="4.5" opacity="0.85"/>
    """),
    # LINE 家庭 bot → 機器人對話框
    "line-family-bot": ("#30d979", "#06a34a", """
        <rect x="30" y="36" width="60" height="40" rx="14" fill="none" stroke-width="6"/>
        <path d="M46 76 L40 92 L62 76" fill="none" stroke-width="6"/>
        <circle cx="48" cy="54" r="4.5" class="fill"/>
        <circle cx="72" cy="54" r="4.5" class="fill"/>
        <path d="M52 64 q8 7 16 0" fill="none" stroke-width="5"/>
        <path d="M60 36 V27" fill="none" stroke-width="5"/>
        <circle cx="60" cy="23.5" r="4" class="fill"/>
    """),
}

SVG_TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{top}"/>
      <stop offset="1" stop-color="{bottom}"/>
    </linearGradient>
    <radialGradient id="sheen" cx="0.5" cy="-0.1" r="1.1">
      <stop offset="0" stop-color="#ffffff" stop-opacity="0.28"/>
      <stop offset="0.55" stop-color="#ffffff" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="120" height="120" rx="27" fill="url(#bg)"/>
  <rect width="120" height="120" rx="27" fill="url(#sheen)"/>
  <g stroke="#0f172a" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="0.14" transform="translate(0, 1.8)">
{shadow}
  </g>
  <g stroke="#ffffff" fill="none" stroke-linecap="round" stroke-linejoin="round">
{glyph}
  </g>
</svg>
"""


def render_glyph(content: str, shadow: bool) -> str:
    """Indent glyph markup; resolve class="fill" to the right fill color."""
    fill = "#0f172a" if shadow else "#ffffff"
    out = []
    for line in content.strip().splitlines():
        line = line.strip().replace('class="fill"', f'fill="{fill}" stroke="none"')
        if shadow:
            # shadow copy: silhouette only, drop per-element fills that fight opacity
            line = line.replace('opacity="0.75"', "").replace('opacity="0.85"', "").replace('opacity="0.6"', "")
        out.append("    " + line)
    return "\n".join(out)


def main():
    import os

    out_dir = os.path.join(os.path.dirname(__file__), "icons")
    os.makedirs(out_dir, exist_ok=True)

    for name, (top, bottom, content) in ICONS.items():
        svg = SVG_TEMPLATE.format(
            top=top,
            bottom=bottom,
            shadow=render_glyph(content, shadow=True),
            glyph=render_glyph(content, shadow=False),
        )
        path = os.path.join(out_dir, f"{name}.svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"Created {path}")


if __name__ == "__main__":
    main()
