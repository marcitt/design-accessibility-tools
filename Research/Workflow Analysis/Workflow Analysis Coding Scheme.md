# Workflow Analysis Coding Scheme

## Key Decisions

**Generalisation**
The code `[reference]` is used as a generalised term for any canvas object (rectangle, circle, frame, text, etc.). Text objects are distinguished using `[text object]` where the distinction is meaningful (e.g. text editing actions). The `[reference(s)]` notation covers both singular and plural cases where the distinction does not meaningfully affect the action.

In some cases this distinction is important, as it is helpful in understanding whether a system needs to be able to work with the context of multiple references.

**Positioning** 
A second coding pass was performed to differentiate positioning methods (freehand, alignment, reference-based) to support voice command grammar design decisions. Examples:
- Place `[reference]` next to `[reference]` (reference positioning)
- Create `[reference]` using `[alignment grids]` (alignment positioning)
- Drag `[reference]` to `[new position]` using `[freehand positioning]` (freehand positioning)
- Create `[reference] [in place]` (in place positioning)

**Tagging**
- `tag_primary` - captures the highest level of interaction abstraction
- `tag_secondary` - provides a slightly lower level of abstraction
- `action` - lowest level of abstraction 

Some hierarchical examples:
1. `tag_primary`: `selection` (highest level) 
2. `tag_secondary`: `multiselect`
3. `action`: `[drag] to [multiselect] [references] on [canvas] using [cursor]` (lowest level)

The highest level is for understanding which categories appear most frequently. The lowest level is useful for understanding how voice commands i.e. the command grammar may be built and what specific tools and contexts may be required. 


## General Rules
- Square brackets are used around keywords - these may be useful for defining voice commands in the future (i.e. the grammar)
- Use dropdowns for all fixed-value columns
- Leave mistake rows blank (difficulty, tag, how) - kept for reference, excluded in analysis

---

## `action`
Lowest level description of what was observed. The format is flexible but loosely follows: `[verb] [object] using [method]`

> Not all actions follow this structure exactly. Multi-step actions use `+` to chain steps e.g. `[expand] [gui menu] + [click] [gui icon]`. Simple actions may have no object or method e.g. `[deselect]`. Actions aim to encode what is physically observed - not the intent. This helps with understanding what exactly is going on within the process and what input modes the user primarily focuses on e.g. using cursor, using keyboard shortcuts, dragging to select vs using the layers panel to select - this helps to understand designer thought processes and which series of actions feel most natural to users. 

---

## `tag_primary` / `tag_secondary`

### Navigation
Zooming or panning to move around the canvas.

| tag_primary | tag_secondary | Description |
|---|---|---|
| `navigation` | `navigate` | General zoom or pan with no specific target |
| `navigation` | `navigate to reference` | Zooming/panning to focus a specific object |
| `navigation` | `navigate to region of interest` | Zooming/panning to a general area |
| `navigation` | `navigate to fit context` | Zooming to fit everything in view |

### Wayfinding
Hovering over objects to reveal information — distinct from navigation as the designer is not moving the viewport.

| tag_primary | tag_secondary | Description |
|---|---|---|
| `wayfinding` | `wayfinding using canvas` | Hovering over objects on the canvas |
| `wayfinding` | `wayfinding using layers` | Hovering over objects in the layers panel |


### Selection

| tag_primary | tag_secondary | Description |
|---|---|---|
| `selection` | `select` | Single object selection |
| `selection` | `deep select` | Selecting a nested object within a group/frame |
| `selection` | `multiselect` | Selecting multiple objects simultaneously |
| `selection` | `deselect` | Deselecting current selection |


### Spatial Positioning
Moving objects to a new position on the canvas.

| tag_primary | tag_secondary | Description |
|---|---|---|
| `positioning` | `alignment positioning` | Using alignment grids or snapping |
| `positioning` | `reference positioning` | Using another object as a positional reference |
| `positioning` | `freehand positioning` | Free cursor-based positioning without guides |

### Resizing
Changing the width or height of an object.

| tag_primary | tag_secondary | Description |
|---|---|---|
| `resizing` | `gui resizing` | Typing values into the properties panel |
| `resizing` | `alignment resizing` | Dragging with alignment guides |
| `resizing` | `reference resizing` | Resizing relative to another object |
| `resizing` | `freehand resizing` | Free cursor-based resizing without guides |

### Creating Design Objects
Creating a new non-text design element.

| tag_primary | tag_secondary | Description |
|---|---|---|
| `creating design object` | `creating design object using freehand` | Dragging to create without guides |
| `creating design object` | `creating design object using alignment` | Dragging to create with alignment grids |
| `creating design object` | `creating design object using reference` | Creating relative to another object |
| `creating design object` | `creating design object in place` | Creating at a fixed/default position - this is common when using plugins etc. |

### Creating Text
Creating a new text object.

| tag_primary | tag_secondary | Description |
|---|---|---|
| `creating text` | `creating text using freehand` | Placing text freely |
| `creating text` | `creating text using reference` | Placing text relative to an object |
| `creating text` | `creating text using alignment` | Placing text with alignment guides |

### Grouping / Structure
Creating or modifying structural groupings.

| tag_primary | tag_secondary | Description |
|---|---|---|
| `grouping` | `autolayout` | Creating or modifying an autolayout frame |
| `grouping` | `framing` | Creating a frame from selected objects |
| `grouping` | `grouping` | Creating a standard group |
| `grouping` | `ungrouping` | Ungrouping a group or frame |


### Updating Objects

| tag_primary | tag_secondary | Description |
|---|---|---|
| `update text object content` | — | Retyping or editing text content |
| `update text object property` | — | Font, alignment, spacing — any text styling |
| `update text object size` | — | Font size specifically |
| `update design object property` | — | Stroke, corner radius, opacity, and other properties |
| `update colour` | `update design object property` | Fill or colour updates |

### GUI Interaction
Interactions with panels, menus, toolbars, or input fields that don't fall into other categories.

| tag_primary | tag_secondary | Description |
|---|---|---|
| `gui interaction` | `gui interaction` | General GUI click or panel interaction |
| `gui interaction` | `activate tool` | Selecting a drawing tool from the toolbar |
| `gui interaction` | `autolayout` | Modifying autolayout constraints via GUI |

Should `gui interaction` | `autolayout` be replaced with `grouping` | `autolayout`- or maybe seperate `gui interaction` autolayout especially for modifications

---

## `how_primary` / `how_secondary`

- `cursor` — mouse click or drag
- `keyboard` — keyboard shortcut or text input
- `gesture` — single trackpad gesture (zoom only or pan only)
- `complex gesture` — combined or targeted gesture (zoom AND pan, or zoom to focus)
- `multi_step` — multiple sequential steps required
- `multi_input` — simultaneous use of multiple input types e.g. cursor + keyboard

Use `how_secondary` when a second input is involved e.g. `how_primary = cursor`, `how_secondary = keyboard`. Leave blank otherwise.

---

## `location`

- `canvas` — main design canvas
- `gui` — any panel, menu, toolbar, or input field
- `layers panel` — the layers panel specifically

Leave blank if not clearly one or the other.

---

## `difficulty_with_existing_speech_tools`

These will be filled in retrospectively after completing benchmarking.

- `EASY` — doable with a single natural voice command today
- `MEDIUM` — possible but requires multiple steps or workarounds
- `HARD` — technically possible but practically very difficult
- `VERY HARD` — very difficult, approaching not achievable with existing voice tools

When in doubt between two levels, pick the harder one. Leave blank for mistake/redundant rows.


---

## `intent` (Optional)
What the user was trying to achieve. Keep brief e.g. `update text alignment`, `activate rectangle tool`. Leave blank if already fully captured by the action description.

---

## `insights_and_notes` (Optional)
Free text. Use for anything unusual, multi-step complexity, or reasons for a difficulty rating.

---

# Complete Action Reference

Every action in the coding scheme with its expected column values, grouped by category.

> **Multiple options** are shown where the correct tag depends on context — use the `initial_code` column to decide.

---

## Navigation

| Action | tag_primary | tag_secondary | how_primary | location | Notes |
|---|---|---|---|---|---|
| `[zoom]` | navigation | navigate | gesture | canvas | Simple zoom only |
| `[pan]` | navigation | navigate | gesture | canvas | Simple pan only |
| `[zoom] and [pan]` | navigation | navigate | complex gesture | canvas | Combined gesture |
| `[zoom] to focus [reference]` | navigation | navigate to reference | complex gesture | canvas | |
| `[pan] to focus [reference]` | navigation | navigate to reference | complex gesture | canvas | |
| `[navigate] to focus [reference]` | navigation | navigate to reference | complex gesture | canvas | |
| `[zoom] to focus [area of interest]` | navigation | navigate to region of interest | complex gesture | canvas | |
| `[pan] to focus [area of interest]` | navigation | navigate to region of interest | complex gesture | canvas | |
| `[navigate] to focus [area of interest]` | navigation | navigate to region of interest | complex gesture | canvas | |
| `[zoom] to fit context in viewport` | navigation | navigate to fit context | complex gesture | canvas | |

*Decision: Should I condense e.g. `[zoom]` vs `[pan]` commands for navigating to specific references or areas of interest to a single action code instead of multiple variations?*

For now I have left these original codes to maintain granularity in the case that this data is useful in the future.

---

## Wayfinding

| Action | tag_primary | tag_secondary | how_primary | location | Notes |
|---|---|---|---|---|---|
| `[hover] over [reference(s)] in [layers panel]` | wayfinding | wayfinding using layers | cursor | layers panel | |
| `[hover] over [reference(s)] on [canvas]` | wayfinding | wayfinding using canvas | cursor | canvas | |

---

## Selection

| Action | tag_primary | tag_secondary | how_primary | location | Notes |
|---|---|---|---|---|---|
| `[select] [reference] on [canvas] using [cursor]` | selection | select | cursor | canvas | |
| `[select] [reference] on [layers panel] using [cursor]` | selection | select | cursor | layers panel | |
| `[deep select] [reference] on [canvas] using [cursor]` | selection | deep select | cursor | canvas | |
| `[multiselect] [references] on [canvas] using [cursor]` | selection | multiselect | cursor | canvas | |
| `[drag] to [multiselect] [references] on [canvas] using [cursor]` | selection | multiselect | cursor | canvas | |
| `[deselect]` | selection | deselect | cursor | canvas | |
| `[deselect] [reference]` | selection | deselect | cursor | canvas | Edge case: deselecting one object from a multiselect |

---

## Spatial Positioning

| Action | tag_primary | tag_secondary | how_primary | location | Notes |
|---|---|---|---|---|---|
| `[drag] [reference] to [new position] using [cursor]` | positioning | freehand positioning | cursor | canvas | |
| `[drag] [reference] to [new position] using [cursor] and [freehand positioning]` | positioning | freehand positioning | cursor | canvas | |
| `[drag] [reference] to [new position] using [cursor] and [alignment grids]` | positioning | alignment positioning | cursor | canvas | |
| `[drag] [reference] to [new position] using [cursor] and [alignment grids] and [reference(s)]` | positioning | alignment positioning | cursor | canvas | Alignment is primary method |
| `[drag] [reference] to [new position] using [cursor] and [reference(s)]` | positioning | reference positioning | cursor | canvas | |
| `[move] [reference] to [new position] using [keyboard] and [alignment grids]` | positioning | alignment positioning | keyboard | canvas | Arrow key nudging ||

---

## Resizing

| Action | tag_primary | tag_secondary | how_primary | location | Notes |
|---|---|---|---|---|---|
| `[drag] [reference] to [resize]` | resizing | freehand resizing | cursor | canvas | |
| `[drag] [reference] to [resize] using [freehand positioning]` | resizing | freehand resizing | cursor | canvas | |
| `[drag] [reference] to [resize] using [alignment grids]` | resizing | alignment resizing | cursor | canvas | |
| `[drag] [reference] to [resize] using [reference]` | resizing | reference resizing | cursor | canvas | |
| `[gui interaction]` *(resize via panel)* | resizing | gui resizing | cursor | gui | Use when initial code mentions width/height/size values being typed in |

---

## Creating Design Objects

| Action | tag_primary | tag_secondary | how_primary | location | Notes |
|---|---|---|---|---|---|
| `[create] [reference] at [new position] on [canvas] [in place]` | creating design object | creating design object in place | cursor | canvas | Created at default position, no drag |
| `[drag] to [create] [reference] at [new position] on [canvas] using [cursor] and [freehand positioning]` | creating design object | creating design object using freehand | cursor | canvas | |
| `[drag] to [create] [reference] at [new position] on [canvas] using [cursor] and [alignment grids]` | creating design object | creating design object using alignment | cursor | canvas | |
| `[drag] to [create] [reference] at [new position] on [canvas] using [cursor] and [reference]` | creating design object | creating design object using reference | cursor | canvas  | |
| `[duplicate] [reference] to [new position] using [freehand positioning]` | creating design object | creating design object using freehand | cursor | canvas | Use `creating design object` when initial code emphasises placement; use `copy/paste/cut` when initial code emphasises duplication only |
| `[duplicate] [reference] to [new position] using [alignment grids]` | creating design object | creating design object using alignment | cursor | canvas | Use `creating design object` when initial code emphasises placement; use `copy/paste/cut` when initial code emphasises duplication only |
| `[duplicate] [reference] to [new position] using [reference(s)]` | creating design object | creating design object using reference | cursor | canvas | Use `creating design object` when initial code emphasises placement; use `copy/paste/cut` when initial code emphasises duplication only |

---

## Creating Text

| Action | tag_primary | tag_secondary | how_primary | location | Notes |
|---|---|---|---|---|---|
| `[create] [text object] at [new position] on [canvas] using [freehand positioning]` | creating text | creating text using freehand | cursor | canvas | |
| `[create] [text object] at [new position] on [canvas] using [reference]` | creating text | creating text using reference | cursor | canvas | |

---

## Creating Spline Objects

Edge cases involving the pen/vector tool.

| Action | tag_primary | tag_secondary | how_primary | location | Notes |
|---|---|---|---|---|---|
| `[click] to [create] [reference] at [new position] on [canvas] using [cursor] and [freehand positioning]` | creating spline object | creating spline object using freehand | cursor | canvas | Pen tool point placement |
| `[click] to [create] [reference] at [new position] on [canvas] using [cursor] and [alignment grids]` | creating spline object | creating spline object using freehand | cursor | canvas | Pen tool point placement with snapping |
| `[double click] [reference] on [canvas] using [cursor]` | creating spline object | creating spline object using freehand | cursor | canvas | Entering vector edit mode |

---

## Grouping / Structure

| Action | tag_primary | tag_secondary | how_primary | location | Notes |
|---|---|---|---|---|---|
| `[create] [autolayout]` | grouping | autolayout | keyboard | canvas | Shift+A shortcut |
| `[create] [frame] from [reference]` | grouping | framing | keyboard | canvas | |
| `[create] [group] from [reference(s)]` | grouping | grouping | keyboard | canvas | |
| `[ungroup] [reference] using [cursor]` | grouping | ungrouping | cursor | canvas | |
| `[mask]` | grouping | grouping | keyboard | canvas | |
| `[paste] into [frame]` | copy/paste/cut | copy/paste/cut | keyboard | canvas | |

---

## Updating Objects

| Action | tag_primary | tag_secondary | how_primary | location | Notes |
|---|---|---|---|---|---|
| `[update] [text object] using [keyboard]` | update text object content | update text object content | keyboard | canvas | |
| `[update] [text object] with [keyboard]` | update text object content | update text object content | keyboard | canvas | |
| `[update] [reference name]` | update design object property | update design object property | multi_input | layers panel | Double-click then type |
| `[update][colour] using [colour wheel]` | update colour | update design object property | cursor | gui | |
| `[eyedropper]` | gui interaction | gui interaction | cursor | canvas | |

Deprecated: `[update] [gui input] to [value]`


---

## GUI Interaction

> **Decision rule:** 
Check `initial_code`. 
If it mentions a tool name - `activate tool`. 
If it mentions autolayout properties (hug, fixed, spacing) - `autolayout`. 
If it mentions width/height values for design object - tag as `resizing | gui resizing`
Otherwise - `gui interaction` (general catch all).
>
> **how_primary:** Use `cursor` for single clicks. Use `multi_step` when initial code implies multiple sequential steps (e.g. scroll then click, navigate then select).

| Action | tag_primary | tag_secondary | how_primary | location | Notes |
|---|---|---|---|---|---|
| `[gui interaction]` | gui interaction | gui interaction | cursor | gui | Default |
| `[gui interaction]` *(tool activation)* | gui interaction | activate tool | cursor | gui | initial code mentions a tool name |
| `[gui interaction]` *(autolayout property)* | gui interaction | autolayout | cursor | gui | initial code mentions autolayout |
| `[collapse] [group] on [layers panel]` | gui interaction | wayfinding using layers | cursor | layers panel | |
| `[create] [alignment guide] using [reference]` | gui interaction | gui interaction | cursor | canvas | Creating a guide line |
| `[exit figma]` | switch to another app | switch to another app | cursor | gui | |

Any action codes with `[activate tool]` should actually be removed from the excel.

---

## Copy / Paste / Clipboard

| Action | tag_primary | tag_secondary | how_primary | location | Notes |
|---|---|---|---|---|---|
| `[duplicate] [reference]` | copy/paste/cut | copy/paste/cut | keyboard | canvas | Cmd+D |
| `[copy]` | copy/paste/cut | copy/paste/cut | keyboard | canvas | |
| `[paste]` | copy/paste/cut | copy/paste/cut | keyboard | canvas | |
| `[cut]` | copy/paste/cut | copy/paste/cut | keyboard | canvas | |
| `[delete]` | delete | delete | keyboard | canvas | |
| `[undo]` | undo | undo | keyboard | canvas | |

---

## Mistakes / Redundant

| Action | tag_primary | tag_secondary | how_primary | location | Notes |
|---|---|---|---|---|---|
| `[mistake/redundant]` | — | — | — | — | Leave all columns blank |


---

# Notes and References
This codebook was produced iteratively following several practice coding sessions. Claude Sonnet 4.6 was used to identify coding errors within spreadsheets, help create uniform codebook templates, increase the rigour of the coding approach and speed up repetitive processes such as reformatting the codebook.


This codebook was created to ensure workflow analysis can be reproducible and consistent. 
