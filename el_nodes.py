"""
El Generator v1 — ComfyUI Custom Nodes
Ported from El Generator HTML by El Randolo

5 nodes:
  - ElGenerator_Character : generates the base character prompt
  - ElGenerator_Outfit    : builds outfit prompt (manual or from universe)
  - ElGenerator_Pose      : builds pose/expression prompt
  - ElGenerator_Scene     : builds scene/lighting/camera prompt
  - ElGenerator_Combine   : assembles sections → STRING for CLIPTextEncode
"""

import random
from .el_data import (
    ETHNICITIES, ETHNICITY_LIST, FACES, ARCHETYPES, ARCHETYPE_LIST,
    VIBE_MODIFIERS, HAIR_COLORS, HAIR_LENGTHS, HAIR_THICKNESS,
    HAIR_TEXTURES, HAIR_STYLES, BANGS, EYE_COLORS, SKIN_QUIRKS,
    HEIGHT_MAP, BUILD_MAP, BUST_MAP, HIPS_MAP, MUSCLE_MAP,
    UNIVERSES, OUTFITS, NAMES,
    SCENE_PRESETS, TOPS, TOPS_LENGTH, BOTTOMS, SOCKS, SHOES,
    ACCESSORIES, MATERIALS, SLEEVES, DETAIL_LEVELS, COLORS_MAIN,
    POSITIONS, GAZES, MOUTHS, LEFT_HAND, RIGHT_HAND, LEGS, ACTIONS,
    INTERACTIONS, LIGHTINGS, LOCATIONS, MOODS, CAMERA_ANGLES,
    FRAMINGS, MODIFIERS,
    pick, pick_n
)


# ═══════════════════════════════════════════════════════════════
# NODE 1: CHARACTER GENERATOR
# ═══════════════════════════════════════════════════════════════
class ElGeneratorCharacter:
    """Generates a complete character base prompt (physique, hair, eyes, archetype)."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "genre": (["female", "male"],),
                "age": ("INT", {"default": 22, "min": 18, "max": 65}),
                "universe": (UNIVERSES,),
                "ethnicity": (ETHNICITY_LIST,),
                "archetype": (ARCHETYPE_LIST,),
                "vibe": ("INT", {"default": 5, "min": 1, "max": 10, "step": 1,
                         "tooltip": "1=Kawaii → 10=Sombre"}),
                "height": ("INT", {"default": 3, "min": 1, "max": 5, "step": 1,
                           "tooltip": "1=Mini → 5=Très grande"}),
                "build": ("INT", {"default": 3, "min": 1, "max": 5, "step": 1,
                          "tooltip": "1=Très mince → 5=Chubby"}),
                "bust": ("INT", {"default": 3, "min": 1, "max": 5, "step": 1,
                         "tooltip": "Female only: 1=Plate → 5=Très forte"}),
                "hips": ("INT", {"default": 3, "min": 1, "max": 5, "step": 1,
                         "tooltip": "Female only: 1=Étroites → 5=Très larges"}),
                "muscle": ("INT", {"default": 3, "min": 1, "max": 5, "step": 1,
                           "tooltip": "Male only: 1=Mince → 5=Très musclé"}),
                "hair_color": (["random"] + HAIR_COLORS,),
                "hair_length": ("INT", {"default": 4, "min": 1, "max": 7, "step": 1,
                                "tooltip": "1=Rasé → 7=Ultra long"}),
                "hair_thickness": ("INT", {"default": 2, "min": 1, "max": 3, "step": 1,
                                   "tooltip": "1=Fin → 3=Épais"}),
                "hair_texture": (["random"] + HAIR_TEXTURES,),
                "hair_style": (HAIR_STYLES,),
                "bangs": (BANGS,),
                "eye_color": (["random"] + EYE_COLORS,),
                "skin_quirk": (SKIN_QUIRKS,),
                "include_expression": ("BOOLEAN", {"default": True,
                                       "tooltip": "Include archetype neutral expression"}),
                "include_outfit": ("BOOLEAN", {"default": True,
                                   "tooltip": "Include a random outfit from the universe"}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("base_prompt", "expression", "outfit", "character_name")
    FUNCTION = "generate"
    CATEGORY = "ElGenerator"

    def generate(self, seed, genre, age, universe, ethnicity, archetype,
                 vibe, height, build, bust, hips, muscle,
                 hair_color, hair_length, hair_thickness, hair_texture,
                 hair_style, bangs, eye_color, skin_quirk,
                 include_expression, include_outfit):

        rng = random.Random(seed)

        # Resolve randoms
        g = "F" if genre == "female" else "M"

        if universe == "random":
            universe = rng.choice([u for u in UNIVERSES if u != "random"])

        if ethnicity == "random":
            ethnicity = rng.choice([e for e in ETHNICITY_LIST if e != "random"])
        eth = ETHNICITIES[ethnicity]

        if archetype == "random":
            archetype = rng.choice([a for a in ARCHETYPE_LIST if a != "random"])
        arch = ARCHETYPES[archetype]

        # Hair
        hc = rng.choice(HAIR_COLORS) if hair_color == "random" else hair_color
        hl = HAIR_LENGTHS.get(hair_length, "shoulder-length hair")
        ht = HAIR_THICKNESS.get(hair_thickness, "")
        htex = rng.choice(HAIR_TEXTURES) if hair_texture == "random" else hair_texture
        hair_parts = [hl]
        if ht:
            hair_parts.append(ht)
        hair_parts.append(htex + " hair")
        if hair_style != "none":
            hair_parts.append(hair_style)
        hair_str = ", ".join(filter(None, hair_parts))

        bang_str = ""
        if bangs != "none":
            bang_str = ", " + bangs

        # Eyes
        ec = rng.choice(EYE_COLORS) if eye_color == "random" else eye_color

        # Skin
        skin = rng.choice(eth["skins"]) if eth["skins"] else rng.choice(
            ETHNICITIES["european"]["skins"])
        face = rng.choice(FACES[g])
        face_desc = f"{face}, {eth['fmod']}" if eth["fmod"] else face

        # Physique
        phy_parts = []
        h_mod = HEIGHT_MAP.get(height, "")
        b_mod = BUILD_MAP.get(build, "")
        if h_mod:
            phy_parts.append(h_mod)
        if b_mod:
            phy_parts.append(b_mod)
        if g == "F":
            bust_mod = BUST_MAP.get(bust, "")
            hips_mod = HIPS_MAP.get(hips, "")
            if bust_mod:
                phy_parts.append(bust_mod)
            if hips_mod:
                phy_parts.append(hips_mod)
        else:
            mus_mod = MUSCLE_MAP.get(muscle, "")
            if mus_mod:
                phy_parts.append(mus_mod)
        build_str = ", ".join(filter(None, phy_parts))

        # Vibe
        vibe_mod = VIBE_MODIFIERS.get(vibe, "")

        # Skin quirk
        skin_q = ""
        if skin_quirk != "none":
            skin_q = ", " + skin_quirk

        # Age description
        if age <= 19:
            age_desc = "young teen"
        elif age <= 24:
            age_desc = "young adult"
        elif age <= 34:
            age_desc = "adult"
        elif age <= 49:
            age_desc = "mature adult"
        else:
            age_desc = "older adult"

        g_token = "1girl" if g == "F" else "1boy"

        # Build the base prompt
        base_parts = [
            g_token,
            f"{age} years old, {age_desc}",
            f"{hair_str}{bang_str}",
            hc, ec, skin, build_str, face_desc
        ]
        if vibe_mod:
            base_parts.append(vibe_mod)
        base = ", ".join(filter(None, base_parts)) + skin_q

        # Expression
        expr = arch["expr"] if include_expression else ""

        # Outfit from universe
        outfit = ""
        if include_outfit:
            u_outfits = OUTFITS.get(universe, OUTFITS["moderne"])
            g_outfits = u_outfits.get(g, u_outfits.get("F", {}))
            all_items = []
            for cat_items in g_outfits.values():
                all_items.extend(cat_items)
            if all_items:
                outfit = rng.choice(all_items)

        # Name
        name_pool = NAMES.get(g, NAMES["F"]).get(universe, NAMES.get(g, NAMES["F"])["moderne"])
        name = rng.choice(name_pool)

        return (base, expr, outfit, name)


# ═══════════════════════════════════════════════════════════════
# NODE 2: OUTFIT BUILDER
# ═══════════════════════════════════════════════════════════════
class ElGeneratorOutfit:
    """Builds a detailed outfit prompt from individual clothing pieces."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "mode": (["manual", "random"],),
                "top": (TOPS,),
                "top_length": (TOPS_LENGTH,),
                "top_color": (COLORS_MAIN,),
                "bottom": (BOTTOMS,),
                "bottom_color": (COLORS_MAIN,),
                "socks": (SOCKS,),
                "shoes": (SHOES,),
                "shoes_color": (COLORS_MAIN,),
                "material": (MATERIALS,),
                "sleeves": (SLEEVES,),
                "detail_level": (DETAIL_LEVELS,),
            },
            "optional": {
                "accessory_1": (ACCESSORIES,),
                "accessory_2": (ACCESSORIES,),
                "accessory_3": (ACCESSORIES,),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("outfit_prompt",)
    FUNCTION = "build"
    CATEGORY = "ElGenerator"

    def build(self, seed, mode, top, top_length, top_color, bottom, bottom_color,
              socks, shoes, shoes_color, material, sleeves, detail_level,
              accessory_1="none", accessory_2="none", accessory_3="none"):

        rng = random.Random(seed)

        if mode == "random":
            top = rng.choice([t for t in TOPS if t != "none"])
            top_length = rng.choice(TOPS_LENGTH)
            top_color = rng.choice(COLORS_MAIN)
            bottom = rng.choice([b for b in BOTTOMS if b != "none"])
            bottom_color = rng.choice(COLORS_MAIN)
            socks = rng.choice(SOCKS)
            shoes = rng.choice([s for s in SHOES if s != "none"])
            shoes_color = rng.choice(COLORS_MAIN)
            material = rng.choice(MATERIALS)
            sleeves = rng.choice(SLEEVES)
            detail_level = rng.choice(DETAIL_LEVELS)
            acc_pool = [a for a in ACCESSORIES if a != "none"]
            accs = rng.sample(acc_pool, min(rng.randint(0, 3), len(acc_pool)))
        else:
            accs = [a for a in [accessory_1, accessory_2, accessory_3]
                    if a != "none"]

        parts = []

        # Top
        if top != "none":
            t_len = (top_length + " ") if top_length != "normal" else ""
            t_col = (top_color + " ") if top_color != "default" else ""
            parts.append(f"{t_col}{t_len}{top}".strip())

        # Bottom
        if bottom != "none":
            b_col = (bottom_color + " ") if bottom_color != "default" else ""
            parts.append(f"{b_col}{bottom}".strip())

        # Sleeves
        if sleeves != "default":
            parts.append(sleeves)

        # Material
        if material != "default":
            parts.append(f"{material} fabric")

        # Detail
        if detail_level != "standard":
            parts.append(detail_level)

        # Socks
        if socks != "none":
            parts.append(socks)

        # Accessories
        if accs:
            parts.append(", ".join(accs))

        # Shoes
        if shoes != "none":
            s_col = (shoes_color + " ") if shoes_color != "default" else ""
            parts.append(f"{s_col}{shoes}".strip())

        return (", ".join(filter(None, parts)),)


# ═══════════════════════════════════════════════════════════════
# NODE 3: POSE BUILDER
# ═══════════════════════════════════════════════════════════════
class ElGeneratorPose:
    """Builds a pose/expression prompt from body position, gaze, hands, etc."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "mode": (["manual", "random"],),
                "position": (POSITIONS,),
                "gaze": (GAZES,),
                "mouth": (MOUTHS,),
                "left_hand": (LEFT_HAND,),
                "right_hand": (RIGHT_HAND,),
                "legs": (LEGS,),
                "action": (ACTIONS,),
                "interaction": (INTERACTIONS,),
            },
            "optional": {
                "expression_override": ("STRING", {"default": "",
                                        "tooltip": "Plug the expression output from Character node to override gaze+mouth",
                                        "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("pose_prompt",)
    FUNCTION = "build"
    CATEGORY = "ElGenerator"

    def build(self, seed, mode, position, gaze, mouth, left_hand, right_hand,
              legs, action, interaction, expression_override=""):

        rng = random.Random(seed)

        if mode == "random":
            position = rng.choice(POSITIONS)
            gaze = rng.choice([g for g in GAZES if g != "none"])
            mouth = rng.choice(MOUTHS)
            left_hand = rng.choice(LEFT_HAND)
            right_hand = rng.choice(RIGHT_HAND)
            legs = rng.choice(LEGS)
            action = rng.choice(ACTIONS) if rng.random() > 0.4 else "none"
            interaction = "solo"

        parts = []

        if position:
            parts.append(position)

        # If expression_override provided, use it instead of gaze+mouth
        if expression_override and expression_override.strip():
            parts.append(expression_override.strip())
        else:
            if gaze != "none":
                parts.append(gaze)
            if mouth != "none":
                parts.append(mouth)

        if left_hand != "natural":
            parts.append(left_hand)
        if right_hand != "natural":
            parts.append(right_hand)
        if legs != "natural":
            parts.append(legs)
        if action != "none":
            parts.append(action)
        if interaction != "solo":
            parts.append(interaction)

        return (", ".join(filter(None, parts)),)


# ═══════════════════════════════════════════════════════════════
# NODE 4: SCENE BUILDER
# ═══════════════════════════════════════════════════════════════
class ElGeneratorScene:
    """Builds a scene prompt from lighting, location, mood, camera angle, framing."""

    @classmethod
    def INPUT_TYPES(cls):
        presets = list(SCENE_PRESETS.keys())
        return {
            "required": {
                "preset": (presets, {"default": "custom"}),
                "lighting": (LIGHTINGS,),
                "location": (LOCATIONS,),
                "mood": (MOODS,),
                "camera_angle": (CAMERA_ANGLES,),
                "framing": (FRAMINGS,),
                "modifier": (MODIFIERS,),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("scene_prompt",)
    FUNCTION = "build"
    CATEGORY = "ElGenerator"

    def build(self, preset, lighting, location, mood, camera_angle, framing, modifier):

        # If preset is not custom, override individual settings
        if preset != "custom" and preset in SCENE_PRESETS:
            p = SCENE_PRESETS[preset]
            parts = []
            if p.get("loc"):
                parts.append(p["loc"])
            if p.get("light"):
                parts.append(p["light"])
            if p.get("mood"):
                parts.append(p["mood"])
            if p.get("angle"):
                parts.append(p["angle"])
            if p.get("frame"):
                parts.append(p["frame"])
            return (", ".join(parts),)

        # Manual mode
        parts = []
        if location != "default":
            parts.append(location)
        if lighting != "default":
            parts.append(lighting)
        if mood != "default":
            parts.append(mood)
        if camera_angle != "default":
            parts.append(camera_angle)
        if framing != "default":
            parts.append(framing)
        if modifier != "none":
            parts.append(modifier)

        return (", ".join(filter(None, parts)),)


# ═══════════════════════════════════════════════════════════════
# NODE 5: COMBINE
# ═══════════════════════════════════════════════════════════════
class ElGeneratorCombine:
    """Combines character + outfit + pose + scene into a single prompt string.
    Output connects directly to CLIPTextEncode (positive prompt)."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "base": ("STRING", {"default": "", "forceInput": True,
                         "tooltip": "Character base prompt"}),
                "outfit": ("STRING", {"default": "", "forceInput": True,
                           "tooltip": "Outfit prompt"}),
                "pose": ("STRING", {"default": "", "forceInput": True,
                         "tooltip": "Pose/expression prompt"}),
                "scene": ("STRING", {"default": "", "forceInput": True,
                          "tooltip": "Scene/camera prompt"}),
                "extra": ("STRING", {"default": "", "multiline": True,
                          "tooltip": "Any additional text to append"}),
                "separator": (["comma", "newline", "period"], {"default": "comma"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "combine"
    CATEGORY = "ElGenerator"
    OUTPUT_NODE = False

    def combine(self, base="", outfit="", pose="", scene="", extra="", separator="comma"):
        sep_map = {"comma": ", ", "newline": "\n", "period": ". "}
        sep = sep_map.get(separator, ", ")

        parts = [s.strip() for s in [base, outfit, pose, scene, extra] if s and s.strip()]
        return (sep.join(parts),)


# ═══════════════════════════════════════════════════════════════
# NODE REGISTRATION
# ═══════════════════════════════════════════════════════════════
NODE_CLASS_MAPPINGS = {
    "ElGenerator_Character": ElGeneratorCharacter,
    "ElGenerator_Outfit": ElGeneratorOutfit,
    "ElGenerator_Pose": ElGeneratorPose,
    "ElGenerator_Scene": ElGeneratorScene,
    "ElGenerator_Combine": ElGeneratorCombine,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ElGenerator_Character": "El Generator — Character 🎲",
    "ElGenerator_Outfit": "El Generator — Outfit 👗",
    "ElGenerator_Pose": "El Generator — Pose 💪",
    "ElGenerator_Scene": "El Generator — Scene 🎬",
    "ElGenerator_Combine": "El Generator — Combine ✏️",
}
