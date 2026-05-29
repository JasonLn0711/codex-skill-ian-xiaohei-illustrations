# Generation Protocol

Final illustrations must be generated through an image generation model,
one image at a time.

Do not use these tools to create final hand-drawn illustrations:

- PIL
- ImageDraw
- Matplotlib
- SVG generation
- Canvas / HTML drawing
- Graphviz or diagram tools
- Programmatic geometry

These tools may be used only for checking, resizing, compressing, moving, or
validating files. They must not create the visual content.

## Workflow

1. Read the target paragraph.
2. Extract the core idea.
3. Choose a mascot role from `references/mascot-cards.yaml`.
4. Choose a metaphor card from `references/metaphor-cards.md`.
5. Write a shot idea.
6. Generate 2-4 image candidates through `image_gen`, one candidate at a time.
7. Review against `docs/VISUAL_SYSTEM.md`.
8. Record provenance.
9. Replace the target asset.
10. Run repo checks.

## Provenance Records

Every generated illustration must have a provenance record.

Required fields:

- `image_path`
- `generated_date`
- `mascot`
- `scene_goal`
- `source_prompt_or_prompt_summary`
- `generation_method`
- `selected_by_human`
- `regenerated_from`
- `usage_location`
- `notes`

## Provenance Example

```text
image_path: examples/images/xiaoquan-generated/01-two-breakpoints.png
generated_date: 2026-05-29
mascot: 小拳
scene_goal: Show two hidden breakpoints in a content process.
source_prompt_or_prompt_summary: Xiaoquan repairs two broken path joints.
generation_method: image_gen
selected_by_human: yes
regenerated_from: failed low-fidelity programmatic redraw
usage_location: README.md
notes: Original generated image retained under ~/.codex/generated_images/.
```

## Existing Example Records

Current README example galleries keep their per-file source records in:

```text
examples/images/thinking-roles-v0/README.md
examples/images/role-examples-v1/README.md
examples/images/xiaoquan-generated/README.md
```

The `thinking-roles-v0` directory is the current role-sample gallery. The
`role-examples-v1` directory is the current article-example gallery. The older
`xiaoquan-generated` directory is retained as a previous generated calibration
set, not the main README gallery.

The upstream calibration examples under `examples/images/*.png` and
`ian-xiaohei-illustrations/assets/examples/*.png` are retained as inherited
style references. They should not be treated as new generated assets from this
adaptation.

The QR image under `assets/ian-wechat-qr.jpg` is a functional inherited asset.
Do not modify it unless the user explicitly requests a QR-code change.
