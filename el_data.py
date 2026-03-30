"""
El Generator v1 — Data tables
Ported from El Generator HTML by El Randolo
"""

import random

def pick(arr):
    return random.choice(arr) if arr else ""

def pick_n(arr, mn, mx):
    n = random.randint(mn, min(mx, len(arr)))
    return random.sample(arr, n) if arr else []

# ═══════════════════════════════════════════════════════════════
# ETHNICITIES
# ═══════════════════════════════════════════════════════════════
ETHNICITIES = {
    "european": {
        "skins": ["pale porcelain skin", "fair light skin", "light beige skin", "warm ivory skin"],
        "fmod": ""
    },
    "east_asian": {
        "skins": ["fair porcelain skin", "light ivory skin", "warm light skin", "pale smooth skin"],
        "fmod": "East Asian features, almond-shaped eyes"
    },
    "southeast_asian": {
        "skins": ["warm golden skin", "light tan skin", "golden complexion"],
        "fmod": "Southeast Asian features"
    },
    "south_asian": {
        "skins": ["warm olive skin", "golden tan skin", "medium brown skin"],
        "fmod": "South Asian features, dark eyes"
    },
    "middle_eastern": {
        "skins": ["warm olive skin", "golden olive skin", "light tan skin"],
        "fmod": "Middle Eastern features, defined dark eyes"
    },
    "african": {
        "skins": ["warm medium brown skin", "deep brown skin", "rich dark chocolate skin", "ebony complexion"],
        "fmod": "African features, defined bone structure"
    },
    "latin": {
        "skins": ["warm caramel skin", "golden tan skin", "warm olive skin"],
        "fmod": "Latin features"
    },
    "mixed": {
        "skins": ["warm beige skin", "light caramel skin", "honey complexion"],
        "fmod": "mixed heritage features"
    },
    "random": {
        "skins": [],
        "fmod": ""
    }
}

ETHNICITY_LIST = list(ETHNICITIES.keys())

# ═══════════════════════════════════════════════════════════════
# FACES
# ═══════════════════════════════════════════════════════════════
FACES = {
    "F": [
        "sharp defined jawline, high cheekbones, angular striking face",
        "soft round face, full cheeks, gentle features",
        "heart-shaped face, wide eyes, delicate features",
        "oval face, balanced elegant bone structure",
        "strong brow, sharp nose, full lips, intense face",
        "soft jaw, almond eyes, full lips"
    ],
    "M": [
        "strong square jaw, sharp cheekbones",
        "defined jaw, prominent brow, sharp features",
        "oval face, balanced clean-cut",
        "heavy jawline, intense expression",
        "defined jaw, high cheekbones, measured"
    ]
}

# ═══════════════════════════════════════════════════════════════
# ARCHETYPES
# ═══════════════════════════════════════════════════════════════
ARCHETYPES = {
    "cold": {
        "label": "Froide / Distante",
        "expr": "cold distant expression, sharp calculating gaze, controlled neutral face",
        "cards": [
            "rare cold smirk, contemptuous amused glance",
            "intense focused stare, jaw clenched, silent threat",
            "brief unguarded softer eyes, quickly masked"
        ]
    },
    "gentle": {
        "label": "Douce / Cachée",
        "expr": "soft contemplative expression, gentle downward gaze, quiet inner world",
        "cards": [
            "rare warm genuine smile, eyes crinkling",
            "pained suppressed emotion, lip bitten",
            "sudden sharp focus, hidden intensity"
        ]
    },
    "chaotic": {
        "label": "Chaotique",
        "expr": "sharp unpredictable energy, shifting eyes, mercurial expression",
        "cards": [
            "wide wild grin, electric eyes, dangerous",
            "sudden eerie stillness, unsettling calm",
            "laughing eyes with dark undertone"
        ]
    },
    "dominant": {
        "label": "Dominante",
        "expr": "commanding presence, direct piercing gaze, assured expression",
        "cards": [
            "slow dangerous smile, ownership in the eyes",
            "cold measuring appraisal, silent scan",
            "rare brief vulnerability, quickly masked"
        ]
    },
    "fragile": {
        "label": "Vulnérable / Résiliente",
        "expr": "composed careful exterior, guarded warmth",
        "cards": [
            "raw vulnerable moment, emotion breaking through",
            "sudden sharp edge, hidden strength surfacing",
            "sad eyes, brave front"
        ]
    },
    "mysterious": {
        "label": "Mystérieuse",
        "expr": "unreadable expression, half-lidded knowing eyes, enigmatic smile",
        "cards": [
            "slow knowing smile, secrets behind eyes",
            "direct blank stare, revealing nothing",
            "flash of real emotion, immediately hidden"
        ]
    },
    "playful": {
        "label": "Jouette / Sombre",
        "expr": "playful light surface with dark undercurrent, sharp eyes behind smile",
        "cards": [
            "bright teasing grin that doesn't reach cold eyes",
            "instant drop to flat cold, warmth gone",
            "conspiratorial expression, mischief and edge"
        ]
    },
    "noble": {
        "label": "Noble / Fière",
        "expr": "composed dignified expression, quiet authority, measured gaze",
        "cards": [
            "cool disdainful look, superior bearing",
            "genuine rare approval, weight of validation",
            "controlled contained fury, quiet restraint"
        ]
    },
    "timid": {
        "label": "Timide / Anxieuse",
        "expr": "shy timid expression, avoiding eye contact, slightly hunched, nervous quiet energy",
        "cards": [
            "brief accidental eye contact, instantly looking away, flushed",
            "small self-conscious fidgeting gesture, nervous hands",
            "rare genuine warm smile when comfortable, walls briefly down"
        ]
    },
    "enthusiastic": {
        "label": "Enthousiaste",
        "expr": "bright open energetic expression, warm engaged eyes, positive forward energy",
        "cards": [
            "wide excited grin, eyes genuinely lighting up, pure joy",
            "animated expressive gesture, enthusiasm breaking through",
            "fully focused intent expression, completely absorbed and in it"
        ]
    },
    "challenger": {
        "label": "Challengeuse",
        "expr": "competitive sharp expression, challenging direct gaze, slight aggressive edge, ready to compete",
        "cards": [
            "smug confident smirk, enjoying the competition, feeding on it",
            "intense competitive fire in the eyes, locked on target",
            "taunting half-smile, deliberately pushing for a reaction"
        ]
    },
    "rebel": {
        "label": "Rebelle",
        "expr": "defiant expression, chin slightly raised, doesn't care what you think, raw authentic energy",
        "cards": [
            "full eye-roll with amused contempt, completely done",
            "confrontational hard stare, daring you to say something, ready",
            "passionate outburst expression, real raw emotion, zero filter"
        ]
    },
    "random": {
        "label": "Random",
        "expr": "",
        "cards": []
    }
}

ARCHETYPE_LIST = list(ARCHETYPES.keys())

# ═══════════════════════════════════════════════════════════════
# VIBE MODIFIERS (1-10 scale)
# ═══════════════════════════════════════════════════════════════
VIBE_MODIFIERS = {
    1: "kawaii ultra-cute aesthetic, innocent wide doe eyes",
    2: "kawaii cute sweet expression, innocent face",
    3: "cute approachable warm expression",
    4: "sweet likeable natural cuteness",
    5: "",  # neutral
    6: "",
    7: "sharp confident magnetic energy",
    8: "intense striking edge, dangerous appeal",
    9: "dark brooding intensity, gothic edge",
    10: "maximum dark intensity, haunting extreme"
}

VIBE_NAMES = {1: "Kawaii", 2: "Kawaii", 3: "Cute", 4: "Cute", 5: "Neutre",
              6: "Neutre", 7: "Intense", 8: "Intense", 9: "Sombre", 10: "Sombre"}

# ═══════════════════════════════════════════════════════════════
# HAIR
# ═══════════════════════════════════════════════════════════════
HAIR_COLORS = [
    "black hair", "dark brown hair", "chestnut brown hair", "auburn hair",
    "red hair", "dark blonde hair", "blonde hair", "platinum blonde hair",
    "silver hair", "white hair", "dark blue hair", "deep purple hair",
    "rose pink hair", "teal hair"
]

HAIR_LENGTHS = {
    1: "buzz cut, very short cropped hair",
    2: "short pixie cut hair",
    3: "short bob haircut, jaw-length hair",
    4: "shoulder-length hair",
    5: "medium-long hair, chest-length",
    6: "long hair, waist-length",
    7: "extremely long flowing hair, hip-length, ultra long"
}

HAIR_THICKNESS = {
    1: "thin fine wispy hair",
    2: "",  # normal
    3: "thick voluminous dense hair"
}

HAIR_TEXTURES = [
    "straight", "wavy", "curly", "tightly curly coily",
    "messy tousled", "fluffy voluminous poofy", "sleek polished straight"
]

HAIR_STYLES = [
    "none", "ponytail", "bun updo", "braided hair",
    "half-up half-down hairstyle", "twin tails pigtails", "side ponytail"
]

BANGS = [
    "none", "straight blunt bangs", "curtain bangs, parted in middle",
    "side-swept bangs", "short micro bangs", "wispy thin bangs"
]

# ═══════════════════════════════════════════════════════════════
# EYE COLORS
# ═══════════════════════════════════════════════════════════════
EYE_COLORS = [
    "ice blue eyes", "deep blue eyes", "grey eyes", "green eyes",
    "forest green eyes", "hazel eyes", "amber eyes", "golden eyes",
    "warm brown eyes", "dark brown eyes", "violet eyes", "crimson eyes"
]

# ═══════════════════════════════════════════════════════════════
# SKIN QUIRKS
# ═══════════════════════════════════════════════════════════════
SKIN_QUIRKS = [
    "none",
    "freckles, light freckles across nose and cheeks",
    "heavy freckles covering face and shoulders",
    "glossy shiny skin, oily luminous skin",
    "small beauty mark, mole near lip",
    "pale skin",
    "light scar on cheek, old scar",
    "vitiligo patches, lighter skin patches",
    "flushed cheeks, blushing rosy cheeks",
    "sun-kissed light tan lines",
    "dark tan, deeply tanned skin"
]

# ═══════════════════════════════════════════════════════════════
# PHYSIQUE MAPS
# ═══════════════════════════════════════════════════════════════
HEIGHT_MAP = {
    1: "very petite tiny stature, miniature frame",
    2: "petite small frame, below average height",
    3: "",  # average
    4: "tall stature, long legs, above average height",
    5: "very tall towering height, extremely long limbs"
}

BUILD_MAP = {
    1: "very slender and thin build, extremely slim physique, lean frame",
    2: "slim slender build, thin physique",
    3: "",  # average
    4: "soft fuller figure, slightly chubby, round features",
    5: "chubby plus size body, round face, fuller frame, curvaceous"
}

BUST_MAP = {
    1: "flat chest, very small bust",
    2: "small bust, modest chest",
    3: "",  # average
    4: "large bust, full chest, busty",
    5: "very large bust, extremely busty"
}

HIPS_MAP = {
    1: "narrow hips, flat buttocks",
    2: "",  # average
    3: "",
    4: "wide hips, curvy figure, full buttocks",
    5: "very wide hips, hourglass figure, large buttocks, very curvaceous"
}

MUSCLE_MAP = {
    1: "lean slim no muscle",
    2: "light muscle tone, lean athletic",
    3: "athletic toned build, fit physique",
    4: "muscular well-defined muscles",
    5: "very muscular heavily built, bodybuilder physique"
}

# ═══════════════════════════════════════════════════════════════
# UNIVERSES & OUTFITS
# ═══════════════════════════════════════════════════════════════
UNIVERSES = [
    "moderne", "academie", "medieval", "darkfantasy", "sf",
    "murim", "samurai", "sport", "corpo", "jobs", "random"
]

OUTFITS = {
    "moderne": {
        "F": {
            "casual": ["oversized hoodie, high-waisted jeans, sneakers", "silk slip dress, leather jacket, ankle boots", "wide-leg trousers, fitted turtleneck, loafers"],
            "soiree": ["backless satin dress, stiletto heels", "fitted bodycon dress, thigh-high boots", "slip skirt, sheer top, strappy heels"],
            "sport": ["compression leggings, sports bra, training shoes", "track pants, fitted zip-up, sneakers"]
        },
        "M": {
            "casual": ["dark jeans, white tee, leather jacket", "chino trousers, oxford shirt, loafers"],
            "soiree": ["fitted dark suit, open-collar shirt", "all-black turtleneck, blazer"]
        }
    },
    "academie": {
        "F": {
            "uniforme": ["white school blouse, pleated skirt, knee socks, loafers", "school blazer, uniform skirt, tie"],
            "casual": ["hoodie, shorts, sneakers", "casual blouse, jeans"],
            "sport": ["sports uniform, athletic shorts", "cheerleader uniform, pleated skirt"]
        },
        "M": {
            "uniforme": ["school blazer, dress shirt, tie, trousers", "varsity jacket, school colors, jeans"],
            "casual": ["hoodie, jeans", "t-shirt, chinos, sneakers"]
        }
    },
    "medieval": {
        "F": {
            "combat": ["chainmail hauberk, leather pauldrons, fantasy warrior", "studded leather armor, hooded cloak, ranger", "dark assassin leather, daggers"],
            "noble": ["flowing medieval gown, embroidered bodice", "velvet court dress, fur trim, high collar"],
            "commoner": ["peasant linen blouse, full skirt", "traveling cloak, worn boots"]
        },
        "M": {
            "combat": ["full plate armor, sword and shield, knight", "dark leather armor, mercenary", "fur cloak, barbarian"],
            "noble": ["court doublet, rich fabric, sword"],
            "commoner": ["traveling cloak, practical clothes"]
        }
    },
    "darkfantasy": {
        "F": {
            "combat": ["dark gothic armor, rune-carved, fallen paladin", "black leather corset armor, dark enchantress", "tattered robes, necromancer, void energy"],
            "dark_formal": ["dark velvet gown, gothic lace, vampire", "deep purple ceremonial robes, arcane"]
        },
        "M": {
            "combat": ["black plate armor, death knight, rune eyes", "dark cloak, assassin of shadows"],
            "dark_formal": ["dark ceremonial robes, lich aesthetic"]
        }
    },
    "sf": {
        "F": {
            "combat": ["tactical bodysuit, cyberpunk, neon accents", "sleek combat exosuit, chrome panels"],
            "civilian": ["holographic crop top, dark leggings, platform boots", "neon street clothes, digital tattoos"]
        },
        "M": {
            "combat": ["combat exosuit, military SF", "tactical ops gear, cyberpunk"],
            "civilian": ["tech jumpsuit, near-future casual"]
        }
    },
    "murim": {
        "F": {
            "combat": ["flowing silk fighting robes, wide sleeves, sash, wuxia", "fitted martial arts attire, wrapped wrist bandages"],
            "noble": ["ornate hanfu, silk embroidered robes, hair ornaments", "flowing layered hanfu, jade accessories"]
        },
        "M": {
            "combat": ["flowing martial arts master robes, wuxia", "light warrior armor, chinese fantasy"],
            "noble": ["elegant scholar robes, jade pendant"]
        }
    },
    "samurai": {
        "F": {
            "warrior": ["elegant black kimono with haori, obi belt, katana", "kunoichi dark shinobi outfit, mask, kunai"],
            "casual": ["yukata, summer cotton, traditional japanese"]
        },
        "M": {
            "warrior": ["full lamellar samurai armor, kabuto, katana", "simple hakama and haori, ronin aesthetic"],
            "casual": ["casual hakama, simple haori"]
        }
    },
    "sport": {
        "F": {
            "training": ["compression leggings, sports bra, training shoes", "yoga pants, fitted tank top"],
            "competition": ["racing swimsuit", "gymnastics leotard"]
        },
        "M": {
            "training": ["gym shorts, compression shirt, training shoes"],
            "competition": ["sports uniform, team player"]
        }
    },
    "corpo": {
        "F": {
            "executive": ["tailored power suit, fitted pencil skirt, pumps", "smart blazer, tailored trousers, loafers"]
        },
        "M": {
            "executive": ["tailored dark suit, dress shirt, tie, oxford", "slim-fit suit, business casual"]
        }
    },
    "jobs": {
        "F": {
            "militaire": ["military combat BDU, tactical vest, combat boots", "female officer dress uniform, rank insignia"],
            "police": ["police officer uniform, badge, utility belt", "detective long coat, badge clipped"],
            "medical": ["hospital scrubs, stethoscope", "white lab coat, doctor, hospital"]
        },
        "M": {
            "militaire": ["full combat tactical gear, body armor, military", "military dress uniform, medals"],
            "police": ["police uniform, badge, utility belt", "detective coat, plain clothes"],
            "medical": ["hospital scrubs, doctor, stethoscope", "white lab coat, physician"]
        }
    }
}

# ═══════════════════════════════════════════════════════════════
# NAMES
# ═══════════════════════════════════════════════════════════════
NAMES = {
    "F": {
        "moderne": ["Zara","Noa","Mila","Sasha","Iris","Kira","Lena","Nyx","Vera","Demi","Cleo"],
        "academie": ["Dina","Lo","Tha","Yul","Luce","Peron","Yae","Mad","Va","Sora"],
        "medieval": ["Séraphine","Morgane","Elara","Rhiane","Vessa","Lyrien","Calinde","Thalira","Faye"],
        "darkfantasy": ["Nera","Vex","Asha","Sable","Vesper","Cendra","Riven","Malice"],
        "sf": ["Zeta","Nova","Lyra","Kestrel","Seren","Echo","Cipher","Helix"],
        "murim": ["Wei Hua","Lian Mei","Zhen Yu","Xiao Yue","Bai Ling","Qing Xia","Mei Zhen"],
        "samurai": ["Yuki","Hana","Rin","Satsuki","Kiri","Mizuki","Tsubaki","Akane"],
        "sport": ["Zara","Noa","Mila","Kira","Maya","Jade","Naomi"],
        "corpo": ["Claire","Elena","Nadia","Victoria","Sophia","Leila","Audrey"],
        "jobs": ["Kovacs","Serra","Torres","Reyes","Drake","Mira","Lena","Ash"]
    },
    "M": {
        "moderne": ["Kael","Theo","Soren","Liam","Axel","Ryo","Leon","Jules","Dex"],
        "academie": ["Alek","Marco","Theo","Yann","Rael","JB"],
        "medieval": ["Aldric","Caelan","Dorian","Faeron","Gorath","Ivar","Lysander"],
        "darkfantasy": ["Vael","Drek","Ash","Korm","Caeden","Riven","Bael"],
        "sf": ["Axiom","Rex","Kai","Zero","Orion","Arc","Nex"],
        "murim": ["Wei Long","Xiao Chen","Bai Feng","Ren Hao","Shen Mo"],
        "samurai": ["Kenji","Ryuu","Daiki","Takeshi","Musashi","Kuro"],
        "sport": ["Theo","Marcus","Kael","Leon","Dex","Hugo"],
        "corpo": ["Vincent","Alexis","Martin","Thomas","Simon","Marc"],
        "jobs": ["Kovacs","Ryen","Drake","Stern","Vane","Cross"]
    }
}

# ═══════════════════════════════════════════════════════════════
# SCENE PRESETS
# ═══════════════════════════════════════════════════════════════
SCENE_PRESETS = {
    "custom": {},
    "noir": {"light": "pure black background, spotlight only", "loc": "pure black studio background", "mood": "editorial, sharp contrast, dramatic", "angle": "eye level shot, direct frontal view", "frame": "medium shot, waist up, torso visible"},
    "blanc": {"light": "clean studio lighting, bright white background, soft fill light", "loc": "pure white seamless studio background", "mood": "editorial, clean minimal aesthetic", "angle": "eye level shot, direct frontal view", "frame": "medium shot, waist up, torso visible"},
    "glamour": {"light": "beauty dish lighting, soft butterfly lighting, glamour photography", "loc": "neutral grey gradient studio background", "mood": "fashion editorial, high-end magazine quality", "angle": "slight high angle, from above, flattering", "frame": "close-up portrait, face and shoulders"},
    "chroma": {"light": "studio photography lighting, frontal key light", "loc": "chroma key green screen background", "mood": "editorial, sharp focus", "angle": "eye level shot, direct frontal view", "frame": "full body shot, head to toe"},
    "nuit_urbaine": {"light": "neon colored lights, pink and blue reflections, night", "loc": "modern city street at night, neon signs, wet pavement", "mood": "cinematic film look, movie quality, anamorphic", "angle": "three-quarter angle, slight turn", "frame": "medium long shot, thighs up, American shot"},
    "golden_hour": {"light": "golden hour warm sunlight, soft long shadows", "loc": "rooftop terrace, city skyline behind", "mood": "romantic soft, warm tones, tender", "angle": "slight high angle, from above, flattering", "frame": "medium shot, waist up, torso visible"},
    "action": {"light": "dynamic lighting, motion blur atmosphere", "loc": "depends on character environment", "mood": "high energy action, adrenaline, intense", "angle": "low angle shot, looking up, powerful", "frame": "full body shot, head to toe"},
    "confrontation": {"light": "Rembrandt side lighting, dramatic shadow one side", "loc": "dark alley, urban gritty, shadows", "mood": "dark dramatic, moody, heavy atmosphere", "angle": "eye level shot, direct frontal view", "frame": "medium long shot, thighs up, American shot"},
    "intimite": {"light": "warm candlelight, flickering orange glow", "loc": "cozy bedroom, warm light, intimate setting", "mood": "sensual warm intimate, soft focus", "angle": "slight high angle, from above, flattering", "frame": "close-up portrait, face and shoulders"},
    "epique": {"light": "magical glowing light, fantasy luminescence", "loc": "destroyed ruins, post-apocalyptic setting", "mood": "epic heroic, powerful, imposing", "angle": "extreme low angle, very dramatic", "frame": "full body shot, head to toe"},
    "mode_mag": {"light": "studio photography lighting, frontal key light", "loc": "neutral grey gradient studio background", "mood": "fashion editorial, high-end magazine quality", "angle": "three-quarter angle, slight turn", "frame": "medium long shot, thighs up, American shot"},
    "melancolie": {"light": "overcast diffuse light, no shadows, flat even", "loc": "abandoned industrial warehouse, concrete, grunge", "mood": "melancholic, lonely, rain, introspective", "angle": "profile shot, side view", "frame": "medium shot, waist up, torso visible"}
}

# ═══════════════════════════════════════════════════════════════
# OUTFIT BUILDER OPTIONS
# ═══════════════════════════════════════════════════════════════
TOPS = [
    "none", "tank top", "crop top", "fitted t-shirt", "blouse", "silk shirt",
    "bustier", "corset", "hoodie", "cardigan", "blazer",
    "leather jacket", "oversized jacket", "trench coat", "fur coat"
]

TOPS_LENGTH = [
    "normal", "ultra-cropped showing underbust", "cropped showing midriff",
    "longline hip-length", "oversized thigh-length"
]

BOTTOMS = [
    "none", "micro mini skirt", "mini skirt", "midi skirt", "long slit skirt",
    "pleated skirt", "hot pants", "bike shorts", "bermuda shorts",
    "slim jeans", "wide-leg jeans", "high-waisted trousers",
    "wide-leg trousers", "leather pants", "leggings",
    "mini dress", "midi dress", "long gown"
]

SOCKS = [
    "none", "no-show ankle socks", "ankle socks", "mid-calf socks",
    "knee-high socks", "thigh-high stockings", "fishnet stockings",
    "sheer pantyhose", "black opaque tights", "patterned socks"
]

SHOES = [
    "none", "bare feet", "ballet flats", "white sneakers",
    "chunky platform sneakers", "ankle boots", "knee-high boots",
    "thigh-high boots", "stiletto heels", "block heels", "platform heels",
    "mules", "strappy sandals", "loafers", "lace-up combat boots", "creeper platforms"
]

ACCESSORIES = [
    "none", "delicate thin necklace", "black choker", "gold chain",
    "pearl necklace", "layered chains", "stud earrings", "hoop earrings",
    "drop earrings", "wristwatch", "thin bracelets", "cuff bracelet",
    "rings", "sunglasses", "hair clip", "small handbag", "leather belt"
]

MATERIALS = [
    "default", "cotton", "denim", "satin lustrous", "velvet", "leather",
    "sheer mesh semi-transparent", "delicate lace", "linen",
    "latex glossy", "knit wool", "faux fur", "silk"
]

SLEEVES = [
    "default", "sheer puffy sleeves, translucent puffed fabric",
    "puff sleeves, gathered at shoulder", "bishop sleeves, full and gathered at wrist",
    "bell sleeves, flared at wrist", "off-shoulder sleeves, bardot neckline",
    "ruffled sleeves, cascading ruffles", "detached sleeves, separate arm covers",
    "long sheer sleeves, transparent chiffon", "sleeveless, bare arms"
]

DETAIL_LEVELS = [
    "standard", "clean minimalist outfit, no embellishments",
    "ribbon bow accents, delicate trim details",
    "intricate embroidery, detailed ornamental stitching",
    "lace trim, sheer layered details, delicate fabric inserts",
    "elaborate ornate outfit, layered fabric, multiple decorative elements, highly detailed"
]

COLORS_MAIN = [
    "default", "black", "white", "grey", "deep red", "bright red",
    "navy blue", "beige nude", "burgundy", "emerald green",
    "dusty rose", "pastel lavender", "gold", "camel brown", "neon pink"
]

# ═══════════════════════════════════════════════════════════════
# POSE OPTIONS
# ═══════════════════════════════════════════════════════════════
POSITIONS = [
    "standing upright, composed", "sitting, relaxed seated",
    "squatting, crouching low", "lying down, stretched out",
    "kneeling on one knee", "leaning forward, hunched slightly",
    "leaning back, arched back", "leaning against wall casually",
    "sitting on edge, legs dangling"
]

GAZES = [
    "none", "direct confident gaze", "sideways glance, looking away",
    "half-lidded heavy gaze", "downward gaze, looking down",
    "looking up, upward gaze", "wide open eyes, surprised",
    "intense piercing stare", "winking, one eye closed",
    "eyes narrowed, suspicious", "eyes closed, serene", "teary eyes, glistening"
]

MOUTHS = [
    "none", "neutral closed lips", "slight soft smile", "full warm smile, showing teeth",
    "smirk, one corner raised", "lips slightly parted, breathless",
    "biting lower lip", "pout, pouty lips", "open mouth, shocked expression",
    "laughing openly, carefree", "tongue slightly out, playful",
    "gritted teeth, intensity"
]

LEFT_HAND = [
    "natural", "left hand in pocket", "left hand on hip",
    "left hand touching own hair", "left hand against cheek, touching face",
    "left hand raised, fingers spread", "left arm crossed",
    "left hand gripping wrist or arm", "left hand behind back",
    "left hand reaching toward camera", "left hand holding clothing, pulling fabric"
]

RIGHT_HAND = [
    "natural", "right hand in pocket", "right hand on hip",
    "right hand touching chin, thinking", "right hand in hair, fingers through hair",
    "right hand reaching forward, extended", "right hand grabbing someone else",
    "right hand holding phone", "right hand against wall, leaning",
    "right hand pointing, finger directed"
]

LEGS = [
    "natural", "legs together, feet close",
    "legs slightly apart, grounded wide stance",
    "legs crossed, one over other", "one leg raised, bent knee",
    "in motion, walking mid-stride", "one foot forward, weight shifted",
    "on tiptoe, raised on balls of feet"
]

ACTIONS = [
    "none", "walking confidently forward, mid-stride",
    "running, full sprint, dynamic", "dancing, fluid body movement",
    "fighting combat dynamic pose, action", "jumping, mid-air, energetic",
    "pulling someone close, grabbing", "pushing someone away, forceful",
    "whispering to someone close", "laughing, head tilted back, carefree",
    "looking at phone screen, scrolling", "adjusting clothing, fixing outfit"
]

INTERACTIONS = [
    "solo", "with another woman, side by side", "with a man beside her",
    "face to face with another person, confrontation or intimacy",
    "group, multiple people around", "couple, intimate close together"
]

# ═══════════════════════════════════════════════════════════════
# SCENE OPTIONS
# ═══════════════════════════════════════════════════════════════
LIGHTINGS = [
    "default", "soft natural daylight, window light",
    "studio photography lighting, frontal key light",
    "Rembrandt side lighting, dramatic shadow one side",
    "backlight, rim lighting, silhouette edge",
    "neon colored lights, pink and blue reflections, night",
    "warm candlelight, flickering orange glow",
    "cold clinical fluorescent light, harsh",
    "golden hour warm sunlight, soft long shadows",
    "dark chiaroscuro, extreme contrast, deep shadows",
    "magical glowing light, fantasy luminescence",
    "pure black background, spotlight only",
    "overcast diffuse light, no shadows, flat even"
]

LOCATIONS = [
    "default", "pure black studio background", "pure white seamless studio background",
    "neutral grey gradient studio background", "chroma key green screen background",
    "modern city street at night, neon signs, wet pavement",
    "cozy bedroom, warm light, intimate setting",
    "luxury apartment interior, modern design",
    "dark alley, urban gritty, shadows",
    "rooftop terrace, city skyline behind",
    "sleek corporate office, glass walls, city view",
    "forest, nature, trees, dappled light",
    "beach at sunset, ocean, sand",
    "destroyed ruins, post-apocalyptic setting",
    "fantasy tavern, warm torches, medieval interior",
    "dark dungeon, stone walls, torch light",
    "cherry blossom garden, japanese aesthetic",
    "cyberpunk district, neon holograms, future city",
    "abandoned industrial warehouse, concrete, grunge"
]

MOODS = [
    "default", "cinematic film look, movie quality, anamorphic",
    "fashion editorial, high-end magazine quality",
    "dark dramatic, moody, heavy atmosphere",
    "mysterious, ambiguous, tension",
    "sensual warm intimate, soft focus",
    "epic heroic, powerful, imposing",
    "melancholic, lonely, rain, introspective",
    "high energy action, adrenaline, intense",
    "dreamy surreal, soft colors, ethereal",
    "raw documentary, real, grounded",
    "romantic soft, warm tones, tender"
]

CAMERA_ANGLES = [
    "default", "eye level shot, direct frontal view",
    "three-quarter angle, slight turn", "profile shot, side view",
    "slight high angle, from above, flattering",
    "low angle shot, looking up, powerful",
    "extreme low angle, very dramatic",
    "back view, from behind, facing away",
    "bird's eye view, aerial top-down",
    "dutch angle, tilted dramatic",
    "over the shoulder perspective"
]

FRAMINGS = [
    "default", "extreme close-up, face only, eyes to lips",
    "close-up portrait, face and shoulders",
    "medium shot, waist up, torso visible",
    "medium long shot, thighs up, American shot",
    "full body shot, head to toe",
    "wide establishing shot, character in environment, small figure"
]

MODIFIERS = [
    "none", "masterpiece, best quality, highly detailed",
    "film grain, cinematic color grading",
    "soft natural lighting, golden hour",
    "dramatic studio lighting",
    "neon lights, colorful glow",
    "candlelight, warm flickering light",
    "rainy day, wet reflections on ground",
    "cherry blossom petals falling",
    "highly saturated vivid colors",
    "monochrome, black and white"
]
