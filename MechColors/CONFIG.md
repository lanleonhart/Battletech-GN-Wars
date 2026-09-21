# MechColors — configuring

The heraldry colour picker now shows **only** the colours listed in `colors.json`.
Vanilla swatches are hidden.

## Adding a colour

Open `colors.json` and add an entry to the `colors` array:

```json
{ "id": "housedavion", "color": "#8B1A1A", "smoothness": 0.30, "metallic": 0.05 }
```

| Field | Meaning |
|---|---|
| `id` | Unique name. `mechcolor_` is prepended automatically if you leave it off. |
| `color` | `#RRGGBB` or `#RRGGBBAA`. |
| `smoothness` | 0–1 gloss. ~0.25 matte military, 0.7+ wet lacquer. |
| `metallic` | 0–1. 0 painted, 1 bare polished metal. |

**File order is picker order.** A colour placed at the top of the array is the first
one you see, with no scrolling. Nothing is sorted.

Only `id` and `color` are required — `smoothness` defaults to 0.32 and `metallic` to
0.08 if omitted.

Duplicate IDs are ignored with a warning, so a colour can never silently overwrite
another. Restart the game after editing.

To get the original 102 back, delete `colors.json` and launch — it regenerates.

## Settings in mod.json

```json
"hideVanilla": true
```
Hides the 55 vanilla swatches so only `colors.json` shows. Set `false` to keep them,
listed after your custom colours. If `colors.json` ends up empty, vanilla is kept
regardless — an empty picker would crash the widget.

```json
"addPalette": true
```
Master switch. `false` disables custom colours entirely and leaves the picker vanilla.

```json
"applyToCompany": false
```
Bypasses the picker and **forces** your company's three colours to the exact
`primary`/`secondary`/`accent` hex values below. Useful for a colour you have not
added to `colors.json`, or to verify the paint pipeline works. When `true`, the picker
selection is ignored.

## Verifying

After launching, `BattleTech_Data\output_log.txt` should contain:

```
[MechColors] active. 102 colours from colors.json. addPalette=True hideVanilla=True ...
[MechColors] picker list built: 102 custom + 0 vanilla = 102 colours (vanilla hidden).
```

If it says `built-in defaults` instead of `colors.json`, the file failed to parse and
the mod fell back — check the log for the reason.

## Uninstalling cleanly

Your save stores colour IDs like `mechcolor_powder`. Remove the mod and those resolve
to nothing, so `HeraldryDef.Refresh()` falls back to `ErrorSwatch` — **magenta mechs**.

Before removing: set `"hideVanilla": false`, launch, pick three vanilla colours in the
heraldry screen, save, then delete the mod folder.

## Notes

- Three paint layers is a hard engine limit. `_PaintColor1/2/3` are literal strings in
  `MechCustomization.SetPaintColors()` and the pattern mask only has RGB channels.
- Which layer appears where is set by the chassis pattern mask. Change the pattern in
  the Mech Bay.
- Single-player. Heraldry is network-serialised as these ID strings, so a peer without
  the mod would see magenta.
