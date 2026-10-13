# SVG diagrams

Write SVG directly to draw diagrams, schematics, concept maps, structure charts, illustrations, and charts. These rules assume figures for consulting and planning slides, and the same procedure and rules apply to other uses. Shared rules for color, fonts, and patterns to avoid follow visual.md. This file covers the details SVG needs.

Derive the diagram form anew for each request from the relationship structure of the message, and do not reuse the form of earlier outputs. Requests range from simple bar charts to concept diagrams defined for the first time, so a fixed form cannot be set in advance. The basis for decisions is:

- Form comes from the message. A form without a message is decoration.
- Assign numbers to encoding channels with high perceptual accuracy, and categories to lower channels.
- If removing an element still leaves the message intact, remove it.

## Drawing procedure

Before writing code, write the decisions of steps 1-3 in 3-5 lines. Without this record, forms converge on habit and stock AI shapes appear.

### Step 1: Fix the message

- Fix one statement the diagram must prove. A noun phrase such as "organizational structure" cannot serve as a message. A sentence holding a judgment, such as "Authority split across three layers delays decisions", is a message.
- If there are two or more messages, split the diagram. Do not put two messages in one diagram.
- Do not place the message sentence inside the diagram. The message is the baseline for choosing the form.

### Step 2: Identify the relationship structure

Pick one relationship the message claims from the table below. The deciding question is what the data is.

| Family | Structure | Cue words | Geometric form |
|--------|-----------|-----------|----------------|
| Quantitative | Component | ratio, share, composition | 100% stacked bar, divided circle |
| Quantitative | Item comparison | larger, rank, gap | Horizontal bar, dot plot |
| Quantitative | Time series | trend, change, growth | Vertical bar, line |
| Quantitative | Frequency distribution | range, frequency, distribution | Histogram, step |
| Quantitative | Correlation | correlation, co-movement, spread | Scatter, bubble |
| Relational | Sequence | procedure, stage, flow | Left-to-right aligned blocks with one direction mark (chevron) |
| Relational | Hierarchy | upper, lower, breakdown | Top-down tree, indented blocks |
| Relational | Containment | belonging, scope, boundary | Nested rectangles or circles |
| Relational | Connection | dependency, integration, reference | Nodes and edges |
| Relational | Correspondence | mapping, contrast, linkage | Two columns with correspondence lines |
| Relational | Cycle | repetition, feedback, return | Closed path |
| Relational | Overlap | common, intersection, overlap | Intersecting translucent shapes |
| State | Transformation | shift, improvement, target | Two panels on the same coordinate system |
| State | Gap | difference, shortfall, requirement | Baseline with difference bars |

- Fix the structure first, then fine-tune the form. Do not picture a form first and fit a structure to it backward.
- If there are more than three kinds of relationship, one diagram cannot express them. Split the diagram.

### Step 3: Assign encoding channels

- Use the channels with the highest perceptual accuracy for numbers first. The order of accuracy is position on a common scale, position on unaligned scales, length, slope and angle, area, volume, then lightness and saturation.
- Assign quantitative values to position and length. Do not express quantitative values with color or area alone.
- Circle area and color density produce large reading errors, so do not use them for values that need ranking.
- Assign categories to group position and texture. Do not express categories as length.
- To distinguish categories within a single color family, use up to four lightness steps, then move to hatching.

### Step 4: Canvas and grid

| Use | viewBox |
|-----|---------|
| Slide body 16:9 | `0 0 1600 900` |
| Slide body 4:3 | `0 0 1600 1200` |
| Horizontal band in a report | `0 0 1600 520` |
| Square concept diagram | `0 0 1200 1200` |
| Full A4 landscape | `0 0 1600 1131` |

- Do not fix the canvas height first. Estimate the content height and work backward. The diagram has no title inside, so fixing a standard ratio first leaves too much space at the top and pushes weight to the bottom.
- At a width of 1600, use side margins of 80, 12 columns of 98 each, and gutters of 24 (80 × 2 + 98 × 12 + 24 × 11 = 1600).
- Make top and bottom margins at least 5% of the shorter side.
- When a container acts as a frame, the content should fill at least 70% of the container's height. Below that, the container reads as empty space and the sense of hierarchy breaks.
- Choose spacing from 8, 16, 24, 40, and 64. Do not use arbitrary values.
- Align same-level elements to exactly the same coordinates. Even a 1px difference reads as misalignment.
- Use the grid as the basis for placement. Avoid uniform layouts that fill all 12 columns.

### Step 5: Text

SVG has no automatic line wrapping, so misjudging text width makes text overflow.

- Estimated width = font size × (sum of per-character coefficients)
- The per-character coefficients are 1.00 for Hangul syllables, 0.70 for Latin capitals, 0.55 for Latin lowercase, 0.62 for digits, 0.50 for punctuation, and 0.30 for spaces.
- The coefficients are the average advance widths (in em) of each character class in NanumGothic Bold, rounded up. For another font, recalculate them the same way.
- Minimum container width = estimated width × 1.08 + total horizontal padding
- Example: "디지털 전환 로드맵" (digital transformation roadmap) has 8 Hangul syllables and 2 spaces, so it is 8.6em. At font size 24 that is 206, 223 after × 1.08, and with 20 of padding on each side it needs at least 263.
- For columns holding text of varying length, set the width from the longest string. Overflow often happens when one item grows longer, such as a value label with a unit attached.
- Break lines by hand with `<tspan x="..." dy="1.35em">`. Break at word boundaries and do not split Korean particles from their words.
- Keep one line of a Korean label to 14 characters or fewer. (recommended)
- For centering, use `text-anchor="middle"` together with `dy="0.35em"`. `dominant-baseline` is ignored by some converters and ports poorly.
- When a label crosses a line or shape, clear the area around the text with `paint-order="stroke"` and a white stroke of 3-4. Renderers that do not support paint-order (such as CairoSVG) cover the text with the white stroke and the text disappears, so verify diagrams that use this technique by rendering them in a browser.
- The minimum font size is 20 at 1600×900. By role, use 56-72 for key figures, 28-32 for element titles, 22-24 for normal labels, and 20 for secondary labels.
- Set fonts with `font-family="NanumGothic, 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif"`.
- Use rotated text only for vertical axis labels, and only `rotate(-90)`. Do not use vertical writing.
- Do not place a diagram title, sources, explanatory notes, or tool information inside the diagram.

### Step 6: Verify

- If a rendering tool is available (browser, resvg, rsvg-convert, Inkscape, CairoSVG, and so on), convert to PNG and check by eye. If there are defects, fix the code and render again. If there are none, deliver.
- If no rendering tool is available, run an arithmetic audit. Compare the estimated width of every text with its container width, confirm the maximum coordinates of every element fall inside the viewBox, and confirm same-level elements share x or y coordinates.
- The review items are the same as the visual verification items in visual.md. Also confirm that shape lengths match the source numbers.
- Confirm the diagram is complete with filters removed.

## Using color

Use the color table in visual.md in SVG as follows.

| Value | Use | Text color on top |
|-------|-----|-------------------|
| #1A1A1A | Body text, main outlines | - |
| #2C466D | Highest emphasis surface | White |
| #4369A3 | High emphasis surface | White |
| #6B8EC2 | Default surface | #1A1A1A |
| #9AB2D6 | Secondary surface | #1A1A1A |
| #C9D6E9 | Tertiary surface, background areas | #1A1A1A |
| #EDF1F8 | Lowest surface, area shading | #1A1A1A |
| #595959 | Hairlines, axis lines, guide lines | - |
| #C0392B | One accent | White |

- White text on #6B8EC2 has a contrast of 3.35:1, which is too low. Use white text only on surfaces as dark as #4369A3 or darker.
- Use the accent color in one place per diagram.
- If a color outside the navy family and the accent is needed, ask the user.
- Map colors to categories one to one and do not add decorative color.
- Keep the background transparent by default. If needed, add a single `<rect fill="#FFFFFF">`.

## Using SVG elements

### Output format

- Write the root as `<svg xmlns="http://www.w3.org/2000/svg" viewBox="...">` and omit the width and height attributes. When placed in a slide, the figure must grow and shrink with its container.
- Do not use `<foreignObject>`, since many converters drop its content.
- Do not reference external images or import web fonts. Keep everything in one file.
- Give every `id` a prefix unique to the diagram. When one document holds several SVGs, identical ids overwrite each other's defs and break the diagrams.
- Record roles with a `data-role` attribute on `<g>` so elements can be traced while debugging.

### marker (uniform arrowheads)

- Use arrows only where they are needed to convey information flow, and leave them out of left-to-right sequences whose direction is obvious.
- Define arrowheads with marker instead of drawing polygons, so every arrow has the same shape and size.
- Fix arrowhead size with `markerUnits="userSpaceOnUse"` so it does not change with stroke width.
- Handle reversed arrows with `orient="auto-start-reverse"` without defining them separately.

### pattern (categories through hatching)

A way to add categories within a single color family. Use it after the lightness steps run out.

- 45-degree diagonals mean planned, unconfirmed, or future adoption.
- Vertical lines mean an external party or another organization's responsibility.
- Dots mean uncertain or under review.
- Fix hatch spacing with `patternUnits="userSpaceOnUse"` so it does not change with shape size.
- Write the meaning of hatching as a direct label on the element or its layer, with no separate legend. Hatching supports scanning, and the direct label fixes the meaning.
- Use no more than three kinds of hatching per diagram. More becomes unreadable.

### clipPath and mask

- Use clipPath for axis breaks, partially filled gauges, and progress.
- Use mask to show continuation beyond the frame and fading on a broken axis.
- Use gradients only inside a mask to show a break, and never as a fill color.

### symbol and use

- Define repeated shapes once with `<symbol>` and reference them with `<use>`.
- `transform="scale()"` scales stroke width too, so stroke widths become inconsistent. Set `vector-effect="non-scaling-stroke"` or avoid scale.

### filter (three allowed)

Use filters only to encode information or to solve a readability problem. Do not use any filter outside the three below unless you can state the information it carries.

| Filter | Information it expresses |
|--------|--------------------------|
| `feColorMatrix type="saturate" values="0"` | Out-of-scope element, not under discussion |
| `feGaussianBlur stdDeviation="2-4"` | Unsettled boundary, scope not defined |
| `feMorphology operator="dilate"` with `feComposite operator="out"` | An even outer boundary showing that separate elements form one unit |

- Filter support differs by renderer, and filters are sometimes ignored when converted to office documents. Design the diagram to be complete with filters removed, and do not rely on filters to carry information.
- Do not use depth effects based on `feDropShadow` or `feOffset`, or texture based on `feTurbulence`.
- Express overlapping areas with `fill-opacity="0.5"` overlap and no filter. The overlap darkens on its own.

### Lines and shapes

- Use stroke widths of `stroke-width="1.5"` for hairlines, `2` for default outlines, `3.5` for emphasized outlines, and `6` for group boundaries.
- The default `rx` is 0. Round corners only when rounding distinguishes a kind of element. Do not give every element the same radius.
- Do not use shadows, gradient fills, 3D, depth, or reflective highlights.
- Use curves only where curvature carries meaning, such as cycles. Draw everything else with straight lines.

## Drawing abstract concepts

For abstract concepts with no quantitative data, draw the structure as geometric relationships. Metaphor pictures borrow the look of objects unrelated to the concept and convey no information. Do not use mountain peaks, roads, stairs, puzzle pieces, light bulbs, rockets, gears, trees, bridges, or keys.

| Concept structure | Geometric expression |
|-------------------|----------------------|
| Containment, belonging, scope | Nested boundaries |
| Opposition, tension, conflict | Vectors in opposite directions, placement at both ends of a symmetry axis |
| Emergence, accumulation | Density change of small units followed by a boundary |
| Threshold | One cut line on an axis with different states on each side |
| Recursion, self-reference | Scaled-down repeated insertion |
| Phase change | A change in the arrangement rule of the same elements |
| Uncertainty, undefined | Blurred boundary, dashed line |
| Circular causation | Closed path with direction marks |
| Break, blockage | A narrowing section, a gap |

- Check whether the structure still reads with every label removed. If it does not, the form is decoration, so look for another expression.
- Put one structure in one diagram. Mixing two or more structures turns it into a collage.
- Manage complexity by the number of kinds of relationship. Thirty elements with one kind of relationship are readable. Six elements with five kinds are hard to read.

## Conventions for consulting and planning slides

- (Layered architecture) Give each layer the same height and put layer names in the left margin. Make the gap between layers twice the gap within a layer.
- (Current state and target state) Keep the coordinate system and scale of the two panels identical and show only the differences as form. With different scales, the two states cannot be compared.
- (Roadmap) Make phase column widths proportional to duration, and mark the decision points where phases change with vertical solid lines. Place deliverables inside their columns.
- (Functional breakdown) Give boxes at the same level the same width, and align lower levels within the width of the upper box.
- (Matrix) Write the judgment criterion on each axis label. Do not write "low" and "high" alone.
- (Numbering) Match the numbering order to the reading order starting from the top left.
- Show only quantitative values whose derivation or source is confirmed. Do not present example numbers as measured values.

## Patterns to avoid and the data-ink check

Apply every pattern to avoid in visual.md, and when one appears, remove it and redraw. Finish with the data-ink check. Remove elements one at a time and see whether the message shrinks. If it does not, the element spends ink without carrying information, so remove it.

## defs example

Replace `PFX` with a prefix unique to the diagram and include only the entries you need.

```xml
<defs>
  <!-- uniform arrowhead: fixed size regardless of stroke width -->
  <marker id="PFX-arrow" viewBox="0 0 12 12" refX="10" refY="6"
          markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse"
          orient="auto-start-reverse">
    <path d="M 0 1 L 11 6 L 0 11 z" fill="#1A1A1A"/>
  </marker>

  <!-- hatch 1: planned, unconfirmed -->
  <pattern id="PFX-hatch-plan" patternUnits="userSpaceOnUse"
           width="10" height="10" patternTransform="rotate(45)">
    <rect width="10" height="10" fill="#EDF1F8"/>
    <line x1="0" y1="0" x2="0" y2="10" stroke="#6B8EC2" stroke-width="2.5"/>
  </pattern>

  <!-- hatch 2: external party's responsibility -->
  <pattern id="PFX-hatch-external" patternUnits="userSpaceOnUse"
           width="9" height="9">
    <rect width="9" height="9" fill="#FFFFFF"/>
    <line x1="0" y1="0" x2="0" y2="9" stroke="#9AB2D6" stroke-width="2"/>
  </pattern>

  <!-- hatch 3: uncertain, under review -->
  <pattern id="PFX-dot-uncertain" patternUnits="userSpaceOnUse"
           width="10" height="10">
    <rect width="10" height="10" fill="#FFFFFF"/>
    <circle cx="5" cy="5" r="1.8" fill="#9AB2D6"/>
  </pattern>

  <!-- filter 1: desaturate out-of-scope elements -->
  <filter id="PFX-out-of-scope" x="-5%" y="-5%" width="110%" height="110%">
    <feColorMatrix type="saturate" values="0"/>
  </filter>

  <!-- filter 2: unsettled boundary -->
  <filter id="PFX-undefined-edge" x="-10%" y="-10%" width="120%" height="120%">
    <feGaussianBlur stdDeviation="3"/>
  </filter>

  <!-- filter 3: even outer boundary tying separate elements into one unit -->
  <filter id="PFX-unify-boundary" x="-15%" y="-15%" width="130%" height="130%">
    <feMorphology operator="dilate" radius="8" in="SourceAlpha" result="grown"/>
    <feComposite in="grown" in2="SourceAlpha" operator="out" result="ring"/>
    <feFlood flood-color="#4369A3" result="ringColor"/>
    <feComposite in="ringColor" in2="ring" operator="in"/>
  </filter>
</defs>
```

An example of clearing the area around a label:

```xml
<text x="800" y="450" font-family="NanumGothic, 'Malgun Gothic', sans-serif"
      font-size="24" font-weight="700" fill="#1A1A1A"
      text-anchor="middle" dy="0.35em"
      stroke="#FFFFFF" stroke-width="4" paint-order="stroke">
  Decision delay zone
</text>
```

## Checklist

- Is one message fixed, and does the diagram prove only that message?
- Is one relationship structure identified, and does the form come from it?
- Are quantitative values assigned to position or length?
- Does the estimated width of every text fit inside its container?
- Is text at least size 20 with a hierarchy by role?
- Is white text placed only on surfaces as dark as #4369A3 or darker?
- Is the accent color used in one place or fewer?
- Is spacing chosen only from 8, 16, 24, 40, and 64?
- Does every id have a unique prefix?
- Is the diagram complete with filters removed?
- Are there no elements from the patterns to avoid?
- After the data-ink check, does every remaining element carry information?

## References

- Cleveland, W. S. and McGill, R. (1984), Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods, Journal of the American Statistical Association 79(387). Source of the accuracy order for quantitative encodings.
- Mackinlay, J. (1986), Automating the Design of Graphical Presentations of Relational Information, ACM Transactions on Graphics 5(2). Source of the order in which position and texture come before length for categorical encodings.
