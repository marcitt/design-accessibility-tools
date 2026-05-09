# Workflow Analysis Coding Scheme

## General Rules
- Square brackets are used around keywords - these may be useful for defining voice commands in the future
- Use dropdowns for all fixed-value columns
- Leave mistake rows blank (difficulty, tag, how) - kept for reference, excluded in analysis

---

## `action`
Physical description of what was observed. Format: `[verb] [object] using [method]`

> Not all actions follow this structure exactly. Multi-step actions use `+` to chain steps e.g. `[expand] [gui menu] + [click] [gui icon]`. Simple actions may have no object or method e.g. `[deselect]`. Actions describe what is physically observed - not the intent.

---

## `tag_primary` / `tag_secondary`

- `navigation` - zooming or panning
- `selection` - selecting, deselecting, multiselect, deep select
- `creating text` - creating a new text object
- `creating design object` - creating a new non-text design element
- `spatial positioning` - moving objects using cursor or keyboard
- `information revealing` - expanding menus, scrolling gui panels, tooltips
- `update text object content` - retyping or editing text
- `update text object property` - font, alignment, spacing - any text styling
- `update text object size` - font size specifically
- `update design object property` - colour, fill, stroke, corner radius
- `resize design object` - changing width/height
- `copy/paste` - duplicate or paste
- `activate tool` - selecting a tool from the toolbar
- `create autolayout` - creating a new autolayout frame
- `update autolayout` - changing autolayout properties

Use `tag_secondary` only when an action spans two categories. Leave blank otherwise.

---

## `how_primary` / `how_secondary`

- `cursor` - mouse click or drag
- `keyboard` - keyboard shortcut or text input
- `gesture` - single trackpad gesture, zoom only or pan only
- `complex gesture` - combined gesture, zoom AND pan together
- `multi_step` - multiple sequential steps required
- `multi_input` - simultaneous use of multiple input types

Use `how_secondary` when a second input is involved e.g. `how_primary = cursor`, `how_secondary = keyboard`. Leave blank otherwise.

---

## `location`

- `canvas` - main design canvas
- `gui` - any panel, menu, toolbar, or input field

Leave blank if not clearly one or the other.

---

## `difficulty_with_existing_speech_tools`

- `EASY` - doable with a single natural voice command today
- `MEDIUM` - possible but requires multiple steps or workarounds
- `HARD` - technically possible but practically very difficult
- `VERY HARD` - very difficult approaching not achievable with existing voice tools

When in doubt between two levels, pick the harder one. Leave blank for mistake/redundant rows.

---

## `intent`
What the user was trying to achieve. Keep brief e.g. `update text alignment`, `activate rectangle tool`. Leave blank if already fully captured by the action description.

---

## `insights_and_notes`
Free text. Use for anything unusual, multi-step complexity, or reasons for a difficulty rating.

---

# Action Reference

## Navigation
- `[zoom] and [pan]` - VERY HARD
- `[zoom]` - HARD
- `[zoom] to focus [design object]` - VERY HARD
- `[zoom] to show full context` - VERY HARD
- `[pan] to focus [design object]` - VERY HARD

## Selection
- `[select] [design object] on [canvas] using [cursor]` - HARD
- `[deep select] [design object] on [canvas] using [cursor]` - VERY HARD
- `[deep select] [text object] on [canvas] using [cursor]` - VERY HARD
- `[multiselect] [design objects] on [canvas] using [cursor]` - VERY HARD
- `[deselect]` - EASY

## Creating Objects
- `[create] [text object] at [new position] on [canvas]` - HARD
- `[create] [design object] at [new position] on [canvas]` - HARD
- `[drag] to [create] [design object] at [new position] on [canvas] using [cursor]` - VERY HARD
- `[create] [alignment guide] using [reference object]` - VERY HARD

## Spatial Positioning
- `[drag] [design object] to [new position] using [cursor]` - VERY HARD
- `[drag] [design object] to [new position] using [cursor] and [alignment grids]` - VERY HARD
- `[move] [selected] to [new position] using [keyboard] and [alignment grids]` - MEDIUM
- `[drag] [design object] to [new position] using [cursor] and [reference object]` - VERY HARD
- `[drag] [design object] to [resize] using [reference object]` - VERY HARD

## Updating Text
- `[update] [text object content]` - MEDIUM
- `[click] [gui icon]` - EASY
- `[update] [gui input] to [value]` - MEDIUM

## Updating Design Object Properties
- `[update] [gui input] to [value]` - MEDIUM
- `[expand] [gui menu] + [click] [gui icon]` - MEDIUM (due to multi-step increasing time)
- `[scroll] [gui panel] + [expand] [gui menu] + [click gui icon]` - MEDIUM (scrolling with voice is hard)
- `[expand] [gui menu] + [scroll] [gui panel] + [click gui icon]` - MEDIUM (scrolling with voice is hard)

## Information Revealing
- `[expand] [gui menu]` - EASY (single-click)
- `[scroll] [gui panel]` - MEDIUM (scrolling is harder with voice)

## Tools & Autolayout
- `[activate] [tool]` - EASY (single-click)
- `[create] [autolayout]` - MEDIUM (atomic command but requires objects to be selected which is the hard part)
- `[update] [gui input] to [value]` - MEDIUM

## Copy / Paste
- `[duplicate] [selected]` - MEDIUM (atomic commands but requires objects to be selected which is the hard part)
- `[undo]` - EASY

---

# Notes and References
This codebook was produced iteratively following several practice coding sessions. Claude Sonnet 4.6 was used to identify coding errors within spreadsheets, help create uniform codebook templates, increase the rigour of the coding approach and speed up repetitive processes such as reformatting the codebook.


This codebook was created to ensure workflow analysis can be reproducible and consistent. 
