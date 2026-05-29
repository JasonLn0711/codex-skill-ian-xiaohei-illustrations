# Ian Xiaohei Illustrations

> 把中文文章裡的判斷、流程、狀態和隱喻，變成一張張白底、手繪、怪誕但清爽的內文配圖。
>
> 16:9 橫式 | 小黑 IP | 純白手繪 | 少量紅橙藍中文批註 | Codex Skill

## 來源與本版改動

這個 repo 是修改自 Ian 的原始專案：[helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations)。

原始專案提供了一套「小黑」手繪內文配圖的 Codex Skill：它定義了視覺 IP、構圖方法、圖片生成提示詞、QA 檢查規則，以及可用於中文文章、貼文、部落格和方法論內容的範例圖片。本 repo 保留原始專案的核心設計：純白背景、黑色手繪線稿、大量留白、少量紅橙藍中文批註，以及讓「小黑」參與核心概念動作的配圖邏輯。

我們在這個自行更新的 repo 裡，主要做了以下調整：

- 將所有 Markdown 與 YAML 文件從簡體中文轉為台灣慣用繁體中文，包含 README、prompt 範例、Skill 說明、agent metadata、風格 DNA、構圖規則、圖片生成提示詞與 QA checklist。
- 將部分用語調整為更自然的台灣語境，例如「貼文」、「部落格」、「內文配圖」、「橫式」、「影像」、「表情貼圖」、「重複使用」、「轉換」等。
- 在 Skill 的輸出規範中明確要求：所有中文輸出一律使用台灣慣用繁體中文，包含 shot list、圖片標註建議、交付說明、檔名說明與改圖指示。
- 在圖片生成提示詞中加入台灣繁體中文約束，要求圖片上的中文手寫標註使用台灣慣用繁體中文，並避免產生簡體中文。
- 將文件中的「正文配圖」調整為「內文配圖」，讓說明更貼近台灣常用的內容出版語境。
- 保留原作者、原始視覺 IP、範例圖片、授權資訊與相關專案連結，讓這個版本仍可清楚追溯到原始設計來源。

需要注意的是，範例 PNG 圖片本身是原始點陣圖素材；目前本 repo 主要完成文字文件與提示詞層級的台灣繁體化，沒有重新繪製或像素級修改既有範例圖片中的手寫字。

---

## 這個倉庫是什麼

Ian Xiaohei Illustrations 是一個 Codex Skill，用來指導 AI Agent 為中文文章、貼文、部落格、Notion 文件和方法論內容生成內文配圖。

它不是通用插畫 prompt，也不是 PPT 資訊圖模板。它的核心目標是：先理解文章裡的認知錨點，再把其中一個判斷、流程、結構、狀態或隱喻，變成一張有記憶點的 16:9 手繪解釋圖。

預設視覺 IP 是「小黑」：一個黑色實心、白點眼、細腿、空表情的小角色。小黑不是吉祥物，不是貼紙，也不是站在角落裡的裝飾物，而是正在認真參與系統運轉的荒誕工作者。

一句話：**讓 AI 不只是「配一張圖」，而是把文章裡的一個關鍵認知動作畫出來。**

---

## 適合誰用

特別適合：

- 寫中文文章，需要內文配圖和文章插圖的人
- 做知識型內容、方法論內容、AI 工作流程內容的人
- 想把抽象判斷畫成具體隱喻的人
- 想要一種比 PPT 資訊圖更輕、更怪、更有個人識別度的配圖風格的人
- 用 Codex 做內容生產，希望穩定重複使用一套視覺語言的人

不適合：

- 想要商業插畫、品牌 KV 或精緻扁平插畫的人
- 想要傳統 PPT 資訊圖、複雜架構圖或流程圖的人
- 想要兒童卡通、可愛 IP、表情貼圖風格的人
- 想把大量內文、長段解釋或完整課程頁塞進一張圖裡的人
- 需要嚴格可編輯向量原始檔的人

---

## 它會產出什麼

預設輸出：

- 16:9 橫式內文配圖
- 一篇文章的 4-8 張 shot list
- 每張圖的主題、核心意思、結構類型、小黑動作和中文標註建議
- 最終 PNG 圖片，儲存到 workspace 的 `assets/<article-slug>-illustrations/`

預設不輸出：

- PPTX / PDF / Keynote
- SVG / HTML / Canvas 可編輯圖
- 商業海報或封面 KV
- 大段文字型資訊圖

---

## 視覺風格

這個 skill 預設使用 Ian 的「小黑怪誕內文配圖」風格：

- 純白背景，不要紙紋、米色、陰影、漸變
- 黑色手繪線稿，細線，輕微抖動
- 大量留白，主體只佔畫面約 40%-60%
- 少量紅色、橙色、藍色中文手寫批註
- 一張圖只表達一個核心動作、結構、狀態或隱喻
- 小黑必須參與核心動作，不能只是裝飾
- 怪誕、有創意、清爽，但不幼稚、不裝可愛

---

## 範例效果

### 兩個斷點

![兩個斷點](examples/images/01-two-breakpoints.png)

### 按目的分揀

![按目的分揀](examples/images/02-sort-by-purpose.png)

### 一魚多吃

![一魚多吃](examples/images/03-one-fish-many-uses.png)

### 承接路徑

![承接路徑](examples/images/04-handoff-path.png)

### 資訊井

![資訊井](examples/images/05-information-well.png)

### 想法壓機

![想法壓機](examples/images/06-idea-press.png)

### 內容發酵

![內容發酵](examples/images/07-content-fermentation.png)

### 信任橋

![信任橋](examples/images/08-trust-bridge.png)

這些圖片是風格校準範例，不是構圖模板。使用時應該從當前文章重新發明隱喻，不要照抄舊案例的物件和構圖。

---

## 安裝

clone 倉庫：

```bash
git clone https://github.com/helloianneo/ian-xiaohei-illustrations.git
cd ian-xiaohei-illustrations
```

複製 skill 到 Codex skills 目錄：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R ./ian-xiaohei-illustrations "${CODEX_HOME:-$HOME/.codex}/skills/"
```

安裝後，在 Codex 裡使用：

```text
Use $ian-xiaohei-illustrations 為這篇中文文章設計並生成 5 張小黑怪誕內文配圖。
```

---

## 怎麼用

### 只做配圖規劃

```text
Use $ian-xiaohei-illustrations 先不要生成圖片。
請分析下面這篇文章哪裡值得配圖，輸出 5 張左右的 shot list。
每張圖寫清楚：放在哪段後、主題、核心意思、結構類型、小黑在做什麼、建議中文標註詞。

<貼上文章>
```

### 直接生成內文配圖

```text
Use $ian-xiaohei-illustrations 把下面這篇文章生成 4 張小黑怪誕內文配圖。
要求：16:9 橫式、純白背景、黑色手繪線稿、少量紅橙藍中文手寫批註。

<貼上文章>
```

### 為單個概念生成一張圖

```text
Use $ian-xiaohei-illustrations 為「信任不是喊出來的，而是一塊證據一塊證據鋪過去」生成一張內文配圖。
畫面要怪誕但清爽，小黑必須承擔核心動作。
```

### 去掉圖裡的標題或錯誤文字

```text
Use $ian-xiaohei-illustrations 幫我編輯這張圖，去掉左上角的「流程圖」標題，其他內容保持不變。
```

更多範例見 [examples/prompts.md](examples/prompts.md)。

---

## 工作流程

這個 skill 的流程是：

1. 讀取文章、Markdown、Notion 內容、截圖或使用者給的主題
2. 提煉核心觀點、認知轉折、流程結構和適合視覺化的段落
3. 先輸出 shot list：每張圖只選一個認知錨點
4. 為每張圖選擇結構類型：Workflow、系統局部、前後對比、角色狀態、概念隱喻、方法分層、地圖路線或小漫畫分鏡
5. 重新發明一個低科技、怪誕但成立的物理隱喻
6. 讓小黑承擔核心動作
7. 每張圖單獨呼叫影像模型生成
8. 按 QA checklist 檢查：白底、留白、小黑動作、中文標註、非 PPT 感、非舊案例復刻
9. 儲存最終 PNG，並報告用途和路徑

---

## 目錄結構

```text
.
├── README.md
├── LICENSE
├── NOTICE.md
├── assets/
│   └── ian-wechat-qr.jpg
├── examples/
│   ├── images/
│   │   ├── 01-two-breakpoints.png
│   │   ├── 02-sort-by-purpose.png
│   │   └── ...
│   └── prompts.md
└── ian-xiaohei-illustrations/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── assets/
    │   └── examples/
    └── references/
        ├── style-dna.md
        ├── xiaohei-ip.md
        ├── composition-patterns.md
        ├── prompt-template.md
        └── qa-checklist.md
```

真正需要安裝到 Codex 的是子目錄：

```text
ian-xiaohei-illustrations/
```

根目錄的 README、LICENSE、NOTICE 和 examples 是 GitHub 分享文件。

---

## 注意事項

- 所有中文輸出、圖片標註建議與交付說明一律使用台灣慣用繁體中文。
- 圖片裡的中文文字越短越穩定。
- 每張圖只講一個核心結構，不要把文章做成說明書。
- 小黑必須承擔核心動作；如果去掉小黑畫面仍然完全成立，說明小黑太裝飾了。
- 範例圖只用於校準線條密度、留白、顏色剋制和小黑參與方式，不要復刻構圖。
- AI 影像模型可能出現錯字、幻覺標籤、風格漂移或多餘標題，生成後需要檢查。
- 如果中文錯字嚴重，優先減少標註詞並重生成。

---

## 相關專案

- [Ian Handdrawn PPT](https://github.com/helloianneo/ian-handdrawn-ppt) — 中文手繪技術 PPT-style 頁面圖生成 Skill
- [Awesome Claude Code Skills](https://github.com/helloianneo/awesome-claude-code-skills) — Claude Code Skills / Agents / Plugins 精選合集
- [Obsidian + Claude AI Second Brain](https://github.com/helloianneo/obsidian-ai-second-brain) — Obsidian + Claude AI 個人知識庫搭建指南

---

## 關於作者

**Ian (伊恩)** — 產品設計師 / 一人公司實踐者 / AI Builder

用 AI 團隊打造一人公司。

- GitHub: [helloianneo](https://github.com/helloianneo)
- X/Twitter: [@ianneo_ai](https://x.com/ianneo_ai)
- 網站: [ianneo.xyz](https://ianneo.xyz)
- 微信: `ianneoxyz`
- 電子郵件: hello.neoc@gmail.com

---

## 下一步

如果你喜歡這套小黑配圖背後的工作方式，也可以繼續看我正在做的幾件事：

- **看見訊號：AI 開眼日報**
  每天篩選一輪 AI 世界裡真正和個人事業有關的產品、工具、工作流程和內容機會。

- **拿到地圖：AI × 一人公司知識庫**
  把 AI 工具、案例、模板和一人公司做法沉澱成一套可以反覆查、反覆用的行動地圖。

- **進入現場：Indie Builders**
  一群正在獨立做專案的人，用 AI 把自己的產品、內容、工具、知識庫和交付物做出來、曬出來、改出來。裡面有主題訓練、知識庫、專案推進和成員互評，但重點不是看資料，而是一起把東西往前推。

如果只是想先觀察，備註「開眼」進 AI 開眼群；如果想聊 Indie Builders，備註「OPC」。

<p>
  <img src="assets/ian-wechat-qr.jpg" alt="Ian 微信 QR code" width="120">
</p>

不方便掃描 QR code 也可以搜尋微信：`ianneoxyz`。

---

## License

MIT License. See [LICENSE](LICENSE).
