# Shared visual rules

These rules apply to charts, diagrams, slide figures, posters, and HTML visual elements. Use color only for data and emphasis on an achromatic base, so the reader sees where to look at a glance. Type-specific rules are in chart.md, svg.md, and flowchart.md.

## Planning order

- Write the design direction before implementing any visualization. For work that produces files, write a design direction document (.md). For work finished in a single response, write it as 3-5 lines before the code.
- The order is: fix the message, set the design direction, fix the layout, implement, verify.
- (Fix the message) Fix one message the visualization must deliver, as a judgment sentence. This sentence sets the baseline for the design direction. Keep it out of the figure itself.
- (Set the design direction) Decide space and structure (how space is divided by information hierarchy), color and tone (a color system that fits the message), proportion and rhythm (size contrast and repetition between elements), composition and balance (eye flow and distribution of visual weight), and visual hierarchy (how importance is shown visually).
- (Fix the layout) Place elements in space according to the design direction, then implement it in code.
- (Verify) After implementation, run the visual verification in this file.
- Unless the user asks for immediate generation, show a plan for charts and diagrams first (form, reason for the choice, displayed elements) and build after confirmation.

## Title and message placement

- Place the message sentence outside the figure (slide headline, document caption, response text).
- Do not place a title, explanatory notes, sources, or tool information inside the figure.
- If the user asks for a title inside the figure or the figure is distributed on its own, add a title. Write it as a judgment sentence, such as "The materials division generated more than half of company-wide revenue growth". Do not use topic labels such as "Chart" or "Results by division".

## Color

| Use | Value | Where |
|-----|-------|-------|
| Background | #FFFFFF | White or transparent |
| Body text | #1A1A1A | Titles, body, data labels |
| Secondary text and lines | #595959 | Axis labels, units, notes, axis lines, guide lines |
| Data default | #6B8EC2 | Pastel navy blue, single-series data |
| Category lightness steps | #2C466D, #4369A3, #6B8EC2, #9AB2D6 | Multiple series and categories, darkest first |
| Surface shades | #C9D6E9, #EDF1F8 | Area shading, backgrounds inside shapes |
| Accent | #C0392B | The one element the reader should see first |

- Keep the whole composition achromatic by default. Use chromatic color only for data and emphasis.
- Do not add decorative color. Do not use colors outside the table above (including Tailwind's default indigo and purple). If another color family is required, ask the user.
- Map colors to categories one to one.
- Distinguish categories with the four lightness steps, darkest first. When there are more than four categories, add hatching (hatching rules are in svg.md).
- Use the accent color in one place per visualization. Used in several places, it stops working as emphasis. Paint the emphasized item in the accent color in place of its category color.
- Paint data shapes on a white background in colors with at least 3:1 contrast against white. #2C466D (9.5:1), #4369A3 (5.5:1), #6B8EC2 (3.4:1), and #C0392B (5.4:1) qualify.
- Give data shapes filled with a color below 3:1 against white, such as #9AB2D6, a #4369A3 outline (1.5px) so their edges show.
- For text inside shapes, choose whichever of #1A1A1A and #FFFFFF has the higher contrast with the fill. The result is white text on #2C466D, #4369A3, and #C0392B, and #1A1A1A text on #6B8EC2, #9AB2D6, #C9D6E9, and #EDF1F8.
- Calculate contrast ratios in code with the WCAG 2.x relative luminance formula.

## Fonts

- The default font is NanumGothic Bold. It covers both Hangul and Latin characters and is available from Google Fonts and operating system packages (for example fonts-nanum).
- Before work, check that the font is installed in the operating system and install it first if not.
- Use at least 12pt Bold for chart text, with 16pt as the default size. SVG text sizes follow svg.md.
- Make text as large as the layout allows.
- Do not use default fonts common in AI outputs, such as Inter, Roboto, Arial, and Open Sans.
- Do not use a font stack made only of system fallback fonts.
- Do not give every element the same text size. Build hierarchy with size and weight.

## Form

- Do not use icons, emoji, clip art, or illustrations.
- Express structure with simple geometric shapes, such as rectangles, circles, and straight lines, and with chevrons.
- Express steps and flow with chevrons. A chevron shows direction by its own shape, so do not add separate arrows.
- Express relationships with straight or orthogonal connectors.
- Share and scale can be shown as area. In that case add numeric labels, and show values that need ranking with position or length.
- Use arrows only where they are needed to convey information flow.
- Build a flat composition with no shadows, gradients, 3D, depth effects, or translucent glass effects.
- Do not round corners, or keep the radius minimal.

## Text placement

- Place only the information the reader needs to check inside the figure. Leave out the writing process, tools used, and tech stack, which readers do not ask about.
- Split text of two or more lines into bullets.
- Center text vertically inside shapes, chevrons, and table cells.
- Show information hierarchy with text size, weight, and position, and leave decorative color out of it.
- Use a single classification criterion for any listed items.
- Wording follows text.md and wording.md. Do not use aspirational copy or generic descriptions that fit any product or business, such as "Build the future", "Your all-in-one platform", "Design the future", or "End-to-End innovation".

## Layout

- Keep margins on all four sides of the canvas and make them equal. On slides, keep at least 0.5 inch from the edges.
- Align elements to a grid and keep spacing between same-level elements consistent.
- Leave enough space between elements.
- Do not add elements to fill empty space.
- Place only the minimum elements needed to deliver the message. If removing an element still leaves the message intact, remove it.
- Divide screen space without overlap, so the divided areas together cover the whole screen.
- Match the visual hierarchy of elements to the order of information importance.
- When making several visualizations, give each its own information structure and layout. Offset the monotony of a minimal style with varied structure. Keep color and form rules the same across all of them.
- If the user asks to repeat one template, the unique structure rule does not apply.

## Patterns to avoid

These are forms AI tools produce again and again through statistical convergence. Do not use them even partially, and redesign when a draft contains one.

- (Band decoration) vertical color bands on the left or right edge of cards or boxes, horizontal color bands along the top or bottom edge of a canvas or box, full-width decorative color bars, short decorative underlines under titles, curved ribbons behind titles
- (Code block imitation) boxes holding ordinary text dressed up like code examples in web documents. This covers text continued next to a vertical band or bracket-shaped curve on the left, filled rectangles used like code blocks, editor windows imitated with a title bar, copy button, and window dots, text with line numbers or command prompt symbols, and the combination of a dark rounded rectangle, monospaced text, and three colored dots at the top left.
- (Repeated grids) mechanical grid repetition of cards with the same size, padding, and corner radius, default 2x2 or 3x3 bento card layouts, icon plus title plus description repeated in three columns, monotonous symmetric layouts with every element centered
- (Effects) purple-to-blue gradients, gradient text, purposeless gradients, translucent glass effects, shadows on every box, depth effects such as isometric cubes and 3D pie charts, reflective highlights, entrance animations repeated without purpose
- (Decorative backgrounds) dot grids, halftones, contour patterns, watermarks
- (Content substitutes) emoji or generic icons standing in for content, a large central circle ringed with small circles of generic nouns such as "AI", "Data", "Cloud", object metaphor pictures (svg.md), text slides where removing the shapes leaves all the information intact
- (Chart defaults) matplotlib default colors used as is, all four spines kept, full grid kept, legend-only identification of data, 3D charts that distort values, pattern or texture fills
- (Connectors) curved arrows without reason, dotted connectors without direction

## Visual verification

- Run visual verification after making any visualization.
- The order is render (run the code and convert to an image such as PNG, PDF, or a screenshot), check the render (look at the image directly and find defects), fix (if there are defects, fix the code and render again), and finish (deliver when no defects remain).
- In file-based environments, convert to PDF or PNG and check. In environments that render on screen, check the rendered result directly.
- If there is no way to check an image, run the arithmetic audit in svg.md.

Review items:

- Text clipped or overflowing
- Words or sentences cut by line wrapping
- Overlapping elements
- Data label legibility (text size and color contrast)
- Missing margins (less than 0.5 inch at slide edges)
- Low color contrast (light text on light backgrounds, missing outlines on shapes below 3:1, and so on)
- Misaligned horizontal or vertical alignment between same-level elements
- Mismatch between the source data and the numbers in the figure
- Broken design consistency
- Unneeded components
- Spacing between elements (too far, too close, or inconsistent)
- Any pattern to avoid

## Checklist

- Are there no elements from the patterns to avoid?
- Does each visualization deliver one message only?
- Are data labels shown directly according to the criteria?
- Is text at least 12pt Bold?
- Did you remove unneeded visual elements?
- Did you check the rendered result?
- Does each of several visualizations have its own structure?
- Is the accent color used in one place only?
