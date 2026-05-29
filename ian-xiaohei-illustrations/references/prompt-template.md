# 圖片生成提示詞模板

每張圖單獨生成。根據內文內容替換變數，不要把多張圖拼在一起。

```text
Generate one standalone 16:9 horizontal Chinese article illustration.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art. Slightly wobbly pen lines. Lots of empty white space. Sparse red/orange/blue handwritten Traditional Chinese annotations as used in Taiwan. Clean absurd product-sketch feeling. No gradients, no shadows, no paper texture, no complex background, no commercial vector style, no PPT infographic look, no cute mascot poster, no children's illustration, no realistic UI.

Mascot character required:
{吉祥物設定。未指定時使用小黑：a small solid-black absurd creature with white dot eyes, tiny thin legs, blank serious expression, slightly uneven hand-drawn body shape. 若指定小拳，使用小拳：an original minimalist calm problem-solving mascot with a simple small body, blank serious expression, and one slightly larger glove-like fist used as a conceptual tool, not a fighting pose.}

The mascot must perform the core conceptual action, not decorate the scene. Keep the mascot serious, deadpan, slightly bizarre, and not cute.

Theme:
{內文配圖主題}

Structure type:
{結構類型：Workflow / 系統局部 / 前後對比 / 角色狀態 / 概念隱喻 / 方法分層 / 地圖路線 / 小漫畫分鏡}

Core idea:
{這張圖要表達的核心意思}

Composition:
{具體畫面：指定吉祥物在哪裡、正在做什麼、主要物件是什麼、資訊如何流動}

Suggested elements:
{元素1} / {元素2} / {元素3} / {元素4}

Chinese handwritten labels:
{標註詞1} / {標註詞2} / {標註詞3} / {標註詞4} / {可選標註詞5}

Color use:
Black for main line art and the mascot. Orange for main flow/path/arrows. Red only for key warnings/problems/results. Blue only for secondary notes or feedback/system state.

Constraints:
One image explains only one core structure. Keep the main subject around 40%-60% of the canvas. Preserve at least 35% blank white space. Use at most 5-8 short handwritten Traditional Chinese labels as used in Taiwan. Do not use Simplified Chinese. Do not write a title in the top-left corner. Do not write the structure type on the image. Do not make it a formal diagram, course slide, or dense explainer. Do not copy prior examples or reuse known case compositions unless explicitly requested; invent a fresh visual metaphor for this specific article. If using 小拳, do not use any existing manga/anime/game/brand character design, costume, face, name, logo, signature pose, or recognizable worldbuilding. It should be clear but not instructional, interesting but not childish, strange but clean.

Production rule:
This final illustration must be generated directly by image_gen as a raster image. Do not simulate the style with PIL, SVG, Canvas, HTML, diagram software, plotted geometry, or programmatic drawing. Hand-drawn texture, irregular line weight, natural handwritten labels, and the mascot's imperfect shape are required.
```

## 影像編輯提示

去掉左上角標題：

```text
Edit the provided image. Remove only the handwritten title "{要刪除的文字}" and its underline from the top-left corner. Fill that area with the same clean white background, matching the surrounding blank paper. Preserve everything else exactly: characters, labels, paths, line style, composition, aspect ratio, and image quality. Do not add any new text or objects.
```

增強怪誕感：

```text
Regenerate this illustration with the same core meaning and simple layout, but make the selected mascot more central to the conceptual action. The mascot should be doing the strange work that explains the idea, not standing beside the diagram. Keep it clean, sparse, hand-drawn, and not cute.
```
