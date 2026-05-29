# Visual System

This repository is a thinking-character system for hand-drawn concept
illustrations. Its purpose is to help articles, READMEs, research notes, and
workflow documents become easier to understand through small, strange, readable
visual metaphors.

It is not a character universe. Mascots exist only when they represent a
thinking function.

## Core Principle

Each mascot must answer one thinking question:

- 小黑: 哪裡怪怪的？
- 小拳: 什麼可以砍掉？
- 小藍: 結構是什麼？
- 小綠: 它怎麼長大？
- 小紫: 哪裡會壞掉？
- 小黃: 還能怎麼想？

Do not add a mascot only because it is cute, expressive, or visually distinct.
The illustration should preserve the idea behind the text, not merely decorate
the page.

## Shared Style

- Pure white background.
- Rough black hand-drawn lines.
- Strange but readable object scenes.
- Small handwritten Traditional Chinese annotations.
- Limited accent colors.
- Playful but not childish.
- Conceptual but not corporate.
- Handmade, not programmatic.

Mascots should remain mostly black-line or black-body drawings. Their identity
comes from a small accent cue, not a full-body color swap.

Examples:

- 小藍 uses blue notes, node marks, tiny glasses, or connection lines.
- 小綠 uses a sprout, green growth mark, soil, or fermentation cue.
- 小紫 uses a purple review stamp, magnifier, warning mark, or checklist.
- 小黃 uses sparks, dots, loose lines, or a surprising metaphor card.

## Visual Differentiation Contract

The six roles must be distinguishable at three levels:

1. Thinking function: what question the mascot asks.
2. Silhouette: how the mascot reads even before labels are visible.
3. Scene behavior: what kind of object the mascot naturally manipulates.

Do not solve differentiation by changing the whole body color. The shared
system language stays white background, black hand drawing, and small accent
colors. The role identity comes from silhouette, prop, posture, motion, and
scene anchor.

| Mascot | Silhouette | Signature Prop | Motion Language | Accent Placement |
| --- | --- | --- | --- | --- |
| 小黑 | round soft black blob, tiny legs, wide still eyes | broken part, weird gap, loose thread | stare, point, pause, lean toward anomaly | mostly black body; almost no color |
| 小拳 | compact black body with one oversized glove-like fist | press, stamp, stop pedal, red/orange target dot | compress, stamp, push through, prune | red/orange on fist path, stamp, or pressure point |
| 小藍 | narrow black body with tiny blue glasses or antenna nodes | node pen, ruler, boundary wire, grid card | align, connect, label boundary, map causality | blue on glasses, nodes, wires, or grid |
| 小綠 | small black body carrying a sprout or repair patch | watering can, soil tray, fermentation jar, bandage | water, mend, tend, compost, wait | green on sprout, growth marks, soil edge, or repair patch |
| 小紫 | black body with purple magnifier / stamp posture | magnifier, checklist, audit stamp, warning tape | inspect, circle flaw, block shortcut, compare record | purple on magnifier, stamp, check mark, or audit ring |
| 小黃 | black body with spark crown or loose jump lines | spark card, odd connector, metaphor switch, open box | jump, connect distant objects, light spark, reframe | yellow on sparks, loose orbit lines, or idea card |

Minimum visual rule: if the accent color is removed, the silhouette and prop
should still hint at the role. If the prop is removed, the posture and scene
behavior should still hint at the role.

## The Six Mascots

| Mascot | Thinking Function | Use For | Accent Cue |
| --- | --- | --- | --- |
| 小黑 | anomaly observation | problem discovery, absurdity, stuck states | black body, odd posture, confused attention |
| 小拳 | compression and execution | simplification, pruning, decision | red/orange pressure point, stamp, small fist |
| 小藍 | structure and logic | architecture, workflow, causal chain, first principle | blue nodes, grid, wires |
| 小綠 | growth and repair | learning, habits, research progress, long accumulation | green sprout, soil, fermentation |
| 小紫 | critique and risk | QA, security, reviewer checks, counterexamples | purple stamp, magnifier, warning mark |
| 小黃 | imagination and jump | analogy, metaphor, sudden idea, playful translation | yellow sparks, light dots, loose motion |

Six is the limit. Adding more roles risks turning the repository into lore
instead of a working concept-illustration system.

## Good Illustration Signals

A good illustration:

- Has one clear conceptual focus.
- Uses rough hand-drawn lines and enough white space.
- Makes the mascot an active participant in the idea.
- Uses handwritten Traditional Chinese notes sparingly.
- Contains a strange but understandable object metaphor.
- Helps the reader understand the idea faster.

## Failure Signals

### Programmatic Drawing

- Perfect circles, boxes, and straight lines.
- System font labels.
- Icon-like or flowchart-like composition.
- Mascot pasted beside the structure.
- No irregular hand-drawn feeling.

### Decorative Mascot

- The mascot appears but does not affect the scene.
- Removing the mascot leaves the idea unchanged.
- The image is cute but explains nothing.

### Too Much Text

- The image becomes a poster.
- Handwritten notes explain everything.
- The visual metaphor becomes unnecessary.

### Wrong Tone

- Too corporate.
- Too glossy.
- Too realistic.
- Too close to an existing cartoon, Disney, Pixar, anime, game, or brand IP.

## Release Gate

Before publishing an update:

- [ ] README images render correctly.
- [ ] New generated images have provenance records.
- [ ] QR code images were not modified unless explicitly requested.
- [ ] Generated images follow this visual system.
- [ ] Each mascot has a distinct silhouette, prop, and scene behavior.
- [ ] Role samples cover all six mascots before the README claims a complete role set.
- [ ] No final illustration was generated with PIL, SVG, Canvas, Matplotlib, or diagram tools.
- [ ] Traditional Chinese annotations use Taiwan wording.
- [ ] No Simplified Chinese appears in handwritten annotations.
- [ ] No Disney, Pixar, or existing-IP imitation appears in mascot design.
- [ ] MIT notice and attribution remain correct.
- [ ] Example images still match the documented mascot roles.
