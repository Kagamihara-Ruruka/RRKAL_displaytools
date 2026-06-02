from __future__ import annotations

from pathlib import Path
from typing import Any


def write_preview_frame_png(frame_rgba: Any, preview_frame_path: Path) -> None:
    from PIL import Image

    tmp_path = preview_frame_path.with_name(preview_frame_path.name + ".tmp.png")
    Image.fromarray(frame_rgba, mode="RGBA").save(tmp_path)
    tmp_path.replace(preview_frame_path)
