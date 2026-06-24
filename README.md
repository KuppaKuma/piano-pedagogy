# 🎹 Piano Pedagogy and Technique Synthesis

This repository houses a premium, structured synthesis of advanced piano pedagogy and keyboard mechanics, consolidating the teachings of the world's master piano teachers: **Tobias Matthay**, **Josef Lhevinne**, **Heinrich Neuhaus**, **Abby Whiteside**, **Boris Berman**, and **Seymour Fink**.

---

## 📂 Repository Contents

*   **[Lhevinne and Matthay - Pedagogical Summary.md](Lhevinne%20and%20Matthay%20-%20Pedagogical%20Summary.md)**: Integrates the Russian school's cantabile tone concept ("pneumatic tires" and "shock absorbers") with Matthay's mechanical weight-release and rotation concepts. Features a comparative terminology matrix and an integrated 10-minute technical warm-up regimen.
*   **[Piano Memorization - Theory and Practice.md](Piano%20Memorization%20-%20Theory%20and%20Practice.md)**: A cognitive and motoric memorization guide detailing the 8 channels of memory, Neuhaus's Master & Servant division, Matthay's neural "Memory Scratch" law, and the "Next-Note" fallacy (Darwin's sneeze). Includes an actionable 4-step practice workflow.
*   **[Piano Physiology and Finger Release.md](Piano%20Physiology%20-%20Theory%20and%20Practice.md)**: A deep anatomical dive into resolving **co-contraction** (the antagonistic flexor/extensor and pronator/supinator tug-of-war), keybedding, the biomechanics of the "finger snap" and "scratch touch" strokes, and step-by-step diagnostic tests and cures.
*   **[00 - Practice Plan/Chopin Etude 10-4.md](00%20-%20Practice%20Plan/Chopin%20Etude%2010-4.md)**: An actionable, 15-minute practicing routine applying these mechanical principles to master rapid sixteenth-note runs without tension.

---

## ⚙️ Obsidian Linking & Formatting Rules

To maintain database integrity and ensure seamless navigation for both humans and AI agents:
1.  **Repository-Relative Portability**: All links use repository-relative paths (e.g. `[[Josef Lhevinne/Josef Lhevinne - Basic Principles in Pianoforte Playing#CHAPTER III|Tone Secret]]`). This guarantees that when the repository is cloned and opened as a standalone Obsidian vault (or imported into an existing vault), all links and caret-level block anchors will resolve perfectly on any machine.
2.  **Strict Wiki-Links**: Always use double-bracket links `[[Path/To/File#^block-anchor|Label]]` or `[[Path/To/File#Heading|Label]]` without the `.md` extension.
3.  **Caret-level Block Anchors (`#^`)**: Never link to flat pages or general chapters when citing specific ideas or quotes. Ensure references link directly to a specific sentence's block anchor (e.g. `^eight-forms` or `^keybedding-definition`) in the primary treatise notes.
4.  **Link Verification**: Before committing or pushing changes, run the Python link validation script from the repository root:
    ```bash
    python3 "scripts/find_broken_links.py"
    ```

---

## 🛠️ Meta Skill: GPU-Optimized Marker PDF/EPUB Conversion

When converting scanned PDF or EPUB treatises into clean Markdown inside this vault, you must use the local `marker-pdf` tool configured to prevent Out of Memory (OOM) errors on the local GPU (`RTX 3070`) and high-core CPU environments.

### 🚀 Optimized Conversion Command

```bash
TESSERACT_GUIDE=0 DETECT_BATCH_SIZE=1 PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
~/jtenv/bin/marker_single \
  "/path/to/input.pdf" \
  --output_dir "/path/to/output_directory" \
  --output_format markdown \
  --layout_batch_size 1 \
  --detection_batch_size 1 \
  --ocr_error_batch_size 1 \
  --recognition_batch_size 8 \
  --table_rec_batch_size 1 \
  --disable_multiprocessing
```

### 📘 Command Configuration Guide

*   **`TESSERACT_GUIDE=0`**: Disables auxiliary Tesseract guides.
*   **`DETECT_BATCH_SIZE=1`**: Caps layout and detection VRAM load.
*   **`PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`**: Prevents GPU memory fragmentation and OOM errors.
*   **`--disable_multiprocessing`**: **Critical for high-core CPUs.** Spawning worker processes for each core loads PyTorch repeatedly, peaking memory usage at 28 GB+. Sequentially processing pages keeps CPU RAM under 3.7 GB.
*   **`--recognition_batch_size 8`**: Optimizes text recognition speed on GPU with minimal VRAM impact.

---

### ⚠️ Troubleshooting Common OOM Issues

#### 1. Giant Page Point Dimensions (Upscale Rendering OOM)
Scanned PDFs with giant dimensions (e.g. `4800 x 6500 pt` instead of standard `612 x 792 pt`) force `marker` to allocate massive page image buffers (exceeding 880 MB of RAM per page).
*   **Check PDF dimensions**:
    ```python
    python3 -c "import pypdf; print(pypdf.PdfReader('file.pdf').pages[0].mediabox)"
    ```
*   **Fix**: Scale down the mediabox using this Python snippet before running `marker_single`:
    ```python
    import pypdf
    reader = pypdf.PdfReader("input.pdf")
    writer = pypdf.PdfWriter()
    for page in reader.pages:
        box = page.mediabox
        aspect = float(box.height) / float(box.width)
        page.scale_to(612, int(612 * aspect))
        writer.add_page(page)
    with open("output_scaled.pdf", "wb") as f:
        writer.write(f)
    ```

#### 2. CUDA/GPU Out of Memory
If a `torch.OutOfMemoryError` is thrown:
*   Set `--recognition_batch_size` down to `4`, `2`, or `1`.
*   Verify that no other CUDA processes are consuming memory.

#### 3. Bypassing OCR (For Digital-Born Searchable PDFs)
For clean, digital PDFs, bypass the OCR models to reduce conversion time from hours to seconds by appending:
```bash
--disable_ocr
```

---

## 📄 License & Copyright

Copyright (c) 2026 KuppaKuma. All rights reserved.

This repository is licensed under the **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)** license. 

Under this license:
*   **No Commercial Use**: You may not use this material for commercial purposes.
*   **No Derivatives**: If you remix, transform, or build upon the material, you may not distribute the modified material.
*   **Attribution**: You must give appropriate credit and provide a link to the license.

For the full legal code, see the [LICENSE](LICENSE) file.

