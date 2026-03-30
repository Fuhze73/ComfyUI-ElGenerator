"""
El Generator v1 — ComfyUI Custom Node Pack
Ported from El Generator HTML by El Randolo

Wildcard / character prompt generator for Anima and similar models.
Outputs STRING that connects directly to CLIPTextEncode (positive prompt).
"""

from .el_nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]

WEB_DIRECTORY = None
