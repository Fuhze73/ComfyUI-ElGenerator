# ComfyUI-ElGenerator

**El Generator v1** — Custom node pack for ComfyUI  
Ported from the HTML wildcard generator by **El Randolo**

Générateur de prompts wildcard pour **Anima** et modèles similaires (SDXL, WAN).  
Le résultat s'applique directement dans le prompt positif via un connecteur STRING → CLIPTextEncode.

---

## 📦 Installation

### Option 1 — ComfyUI Manager
Cherchez `ElGenerator` dans le ComfyUI Manager et installez.

### Option 2 — Manuel
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/VOTRE_REPO/ComfyUI-ElGenerator.git
# ou copiez simplement le dossier ComfyUI-ElGenerator dans custom_nodes/
```

Redémarrez ComfyUI. Les nodes apparaissent dans la catégorie **ElGenerator**.

---

## 🧩 Nodes disponibles

### 🎲 El Generator — Character
Génère le prompt personnage complet :
- **Genre** (F/M), **Âge** (18-65)
- **Univers** : Moderne, Académie, Médiéval, Dark Fantasy, SF, Murim, Samouraï, Sport, Corpo, Métiers
- **Ethnicité** : Européenne, Est-Asiatique, Sud-Est Asiatique, Sud-Asiatique, Moyen-Orient, Africaine, Latine, Métisse
- **Physique** : Taille, Corpulence, Poitrine (F), Hanches (F), Musculature (M)
- **Cheveux** : Couleur, Longueur, Épaisseur, Texture, Coiffure, Frange
- **Yeux**, **Archétype** (12 personnalités), **Vibe** (Kawaii → Sombre)
- **Particularités de peau**

**Sorties :**
| Sortie | Type | Description |
|--------|------|-------------|
| `base_prompt` | STRING | Prompt physique complet |
| `expression` | STRING | Expression de l'archétype |
| `outfit` | STRING | Tenue aléatoire de l'univers |
| `character_name` | STRING | Nom généré |

### 👗 El Generator — Outfit
Assembleur de tenue pièce par pièce :
- Haut (14 options + longueur + couleur)
- Bas/Robe (17 options + couleur)
- Chaussettes, Chaussures (+ couleur)
- Matière, Manches, Niveau de détails
- Jusqu'à 3 accessoires

Mode **random** pour randomiser toutes les pièces d'un coup.

### 💪 El Generator — Pose
Constructeur de pose :
- Position globale (9 options)
- Regard, Bouche/Expression
- Main gauche, Main droite (10 options chacune)
- Jambes, Action/Mouvement
- Interaction (solo, duo, groupe…)
- **Expression override** : branchez la sortie `expression` du Character node

### 🎬 El Generator — Scene
Constructeur de scène :
- **12 presets** : Fond noir, Fond blanc, Glamour, Chroma key, Nuit urbaine, Golden hour, Action, Confrontation, Intimité, Épique, Mode mag, Mélancolie
- Ou mode **custom** : Lumière, Décor, Ambiance, Angle caméra, Cadrage
- Modificateurs qualité (masterpiece, film grain, etc.)

### ✏️ El Generator — Combine
Assembleur final — combine les 4 sections en un seul prompt :
- `base` ← Character
- `outfit` ← Outfit (ou sortie outfit du Character)
- `pose` ← Pose
- `scene` ← Scene
- `extra` ← Texte libre additionnel
- Séparateur configurable (virgule, retour ligne, point)

**La sortie `prompt` se connecte directement à CLIPTextEncode.**

---

## 🔌 Workflow typique

```
[ElGenerator_Character] ──base_prompt──→ [ElGenerator_Combine] ──prompt──→ [CLIPTextEncode] → positive
                        ──expression──→ [ElGenerator_Pose]     ──pose──↗
                        ──outfit─────────────────────────────────outfit──↗

[ElGenerator_Scene] ──scene──↗
```

Ou en version simple :
```
[ElGenerator_Character] ──base_prompt──→ [ElGenerator_Combine] ──prompt──→ [CLIPTextEncode]
```

---

## 🎯 Compatibilité

- ComfyUI ≥ 0.18.0
- Python ≥ 3.10
- Aucune dépendance externe (uniquement `random` de la stdlib)
- Fonctionne avec tout modèle text-to-image : SDXL, Anima, WAN, Flux, etc.

---

## 🎰 Le seed

Chaque node a un **seed** qui contrôle la randomisation. Avec le même seed et les mêmes paramètres, vous obtiendrez toujours le même résultat. Mettez `mode: random` sur Outfit/Pose et changez le seed pour explorer des variations.

---

*Fait par El Randolo pour les kheyous — ahi*
