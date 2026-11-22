---
name: grand-viz-style
description: "Visual direction for rich, formal visuals at large project briefings, policy announcements, vision ceremonies and similar events of Korean public institutions and large corporations. Builds conclusion-first slides with a head message, labeled panels and a conclusion band. Covers background lightness and treatment chosen by purpose and venue, role colors, contrast checks on the real background, gradients, light, 3D, photos and icons used by importance, shapes sized to their text, figures without standalone giant numbers, and tests for dated and AI-made patterns. Use it whenever the user makes or edits slides, infographics, diagrams, roadmaps, charts, posters, HTML or SVG visuals and says '/grand-viz-style', 'make it impactful', 'make it look impressive', 'government presentation look', 'vision ceremony deck' or similar, or asks for large presentation visuals for Korean institutions. Not for minimal or whitespace-heavy consulting tones. Does not build slide files. User-set colors, fonts and structure prevail."
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# grand-viz-style

> This English version was translated from the Korean original. It may behave differently from what the original intends. Rules written for Korean slides (Korean fonts, the noun-ending text style) keep their Korean examples.

This skill sets the direction for visuals shown at large project briefings, policy announcements, vision ceremonies and similar events of Korean public institutions and large corporations. The style uses photos, icons, 3D objects, gradients, wide color fields and similar materials to show the scale of a project and how well it is prepared. The skill keeps that richness and gives the criteria that stop slides from looking dated or AI-made.

This document fixes no coordinates, color codes or templates. When one template repeats, different content lands in the same container and content and form drift apart. The model designs each slide anew for each request with the criteria below.

## Terms

The terms below keep the same meaning throughout this document.

| Term | Meaning |
|---|---|
| Slide | One presentation slide, or one face of a visual such as an infographic or poster |
| Use setting | The combination of the venue where the slide is shown and the way it is distributed |
| Background | The base surface of the whole slide |
| Background lightness | The choice of a light or dark background (light: white, light gray and similar, dark: deep navy, dark gray and similar) |
| Background treatment | Decoration placed on the background, such as light, color fields, shapes or photos |
| Content surface | The surface that holds text, diagrams, charts and similar content (panel fills and similar) |
| Color field | A surface filled with color, such as a shape or band |
| Role colors | Primary, secondary and accent colors |
| Hero element | The element that carries the slide's message and must be seen first |
| Effect method | The way gradients, shadows or light are each produced |

## Scope

- Applies to slides first, and to infographics, diagrams, frameworks, roadmaps, charts, posters and similar visuals.
- Works in any medium or tool. HTML, SVG, slide files, images, charts drawn in code and similar outputs follow the same criteria.
- When the user sets colors, fonts, structure, aspect ratio, template files and similar items, those settings take priority over this document.
- In work that applies this skill, set color, form, information density, title placement and effects by this document. Work rules such as code quality, security and user confirmation steps fall outside this document, so follow the other guidelines in use.
- Follow the tool in use for how to produce files.

## Principles

Every criterion in the sections below comes from these principles. Use them to decide cases the document does not cover.

- (Strict logic) State the conclusion first and split the evidence without gaps or overlaps. The richer the effects, the messier a slide looks when this skeleton breaks.
- (Effects follow importance) Keep the number of effect types small and give elements with the same role the same effect. Match effect strength to the order of importance. When every element shines, no element stands out.
- (Every element carries this project) Photos, icons, shapes, copy and every other element point to something specific to the project. An element that would still work on another project's slide only takes up space.
- (Verified facts only) Do not invent information or sources you do not know. When facts, figures, organization names, dates, sources and similar items are uncertain, ask the user or leave them off the slide.
- (The viewer's eye decides) The visual criteria in this document exist so the audience reads the slide with ease and finds it pleasant. Fix anything that looks off to the audience or to practitioners, even when no item here covers it. When breaking a visual criterion gives a result that reads better and looks better than following it, choose the better result.

When a decision is hard, check it this way.

- (Squint test) Shrink or blur the slide. Check that the element you see first is the most important one.
- (Swap test) Look for elements that would still fit if you changed only the project name and pasted them into another deck. Replace any you find with content from this project.
- (Consistency test) Check that elements with the same role share the same color, form and effect.
- (Flatness test) Check whether the slide looks like a document table or list. If it does, enlarge the color fields, raise their contrast and give the hero element more weight.
- (Removal test) Remove decorations one at a time. If the message and impression stay the same without one, delete it.
- (Era test) Look at one shape on its own. If it resembles a button or window title bar from a 2000s operating system, strip the surface effects and return it to a flat fill.

## Planning order

Set the direction in this order before building. For work that produces files, record the design direction in a short document. For work that ends in one response, write it in 3-5 lines before the build. Writing the direction first keeps elements from piling up on the fly.

1. (Read the setting) Find out the presenting organization, audience, purpose, aspect ratio, use setting and similar facts. Venues split into bright meeting rooms, dimmed event halls and the like. Distribution splits into screen-only, screen plus printed handouts and the like. Set the use setting by the criteria in the use setting section below. Among the other items, ask only about those the request leaves out and you cannot infer, all at once. Use 16:9 when no aspect ratio is given.
2. (Fix the message) Set one judgment statement that the slide delivers. This statement becomes the head message.
3. (Identify the relation) Identify the relation among the supporting content and pick the main structure. The criteria are in the section on relations.
4. (Decide the background) Set the background lightness and the level of background treatment. The criteria are in the background section.
5. (Assign effects) Decide the color roles, the hero element, the effect methods and whether to use photos and icons.
6. (Build) Build to the direction you set.
7. (Verify) Look at the rendered result and check the items in the verification section.

For a multi-slide deck, set the storyline and the fixed elements listed in the multiple slides section before designing each slide's body.

### Use setting

- When the user states the use setting, follow it.
- When the request makes the use setting clear without stating it, follow that setting. Requests that mention printed handouts, a place in a report, reading before a meeting and similar fall in this group.
- When the user does not state the use setting and the request does not make it clear, set it to screen showing at a large venue with no handouts. Proceed with this default without asking about the use setting. Use this default to set the information density and text size.
- Under this default, set the background lightness with the lighting and distribution treated as unknown. The criteria are in the background section.
- Judge the use setting from information about how the slide will be used, such as the venue, handouts and where it will be published. Adjust slides with much content by the criteria in the information density section.

## Slide skeleton

A body slide has the zones below. Place and size each zone to fit the content.

| Zone | Role | Criteria |
|---|---|---|
| Position marker | Shows where the current section sits in the deck | Section number and name in small type, same place and form across the deck |
| Head message | Delivers the slide's conclusion | One judgment statement, the largest text on the slide |
| Body | Presents evidence for the conclusion | 2-4 labeled panels, with shapes showing the relations between panels |
| Conclusion band | Shows the next step the body leads to | One of implications, expected effects, direction of action and similar, omitted when it repeats the head message |

- For a single slide with no known section number or name, put the document name or the slide's nature (review results, action plan and similar) in the position marker. Do not invent a section number.
- When the user's content holds no next step for the conclusion band, omit the band. Do not invent a sentence to fill it.

### Head message

- Put a judgment in the head message. "Energy trends" is a topic label. "Energy demand, supply expansion urgent as industrial parks electrify" is a judgment.
- Color only one or two keywords. Coloring the whole sentence in the accent color cancels the emphasis.
- Keep it to two lines or fewer.
- When the user specifies a template with large section titles, place the judgment as one line under the section title.

### Body panels

- Give every panel a label. The label is a noun phrase that sums up the panel and sits on a color field to set it apart from the body.
- The panel count follows how the content is classified. Use one classification criterion.
- Size each panel to the importance and amount of its content. The most important panel gets the largest area.
- Place shapes that show relations between panels, such as arrows, opposition markers and plus signs. Panels placed side by side with no relation shown read as a plain list.
- A panel can hold diagrams, small charts, photos, short noun phrases and similar items. Full sentences appear only in the head message and conclusion band.

### Information density

- Make the relation between the conclusion and its evidence clear from one slide alone.
- Slides that double as printed handouts get read without the presenter, so they carry the situation, cause and direction on the slide itself.
- When the user sets the content, build within it. You may add labels such as the names of comparison criteria. Do not add facts, figures or judgments.
- As density rises, raise the consistency of alignment and spacing with it. The more elements a slide has, the more a misaligned spot stands out.
- Do not add empty elements to fill space. When space remains, enlarge the diagrams or charts in the main panels or strengthen the evidence.
- Screen-only slides come with the presenter's explanation, so they carry fewer elements and larger text than slides that double as handouts.

### Non-body slides

- Covers and dividers carry the strongest effects in the deck. They can use a large image, a 3D shape or similar elements that show the subject.
- A divider holds the section number, section name and a one- or two-line tagline by default. The tagline names what the section covers. You may add a hero element and a list of subsections, and you may drop the position marker.
- Lay out the table of contents so the order and relations between sections show.

## Expression by relation

Identify the relation among the content first, then pick the form that shows that relation most directly. Picking the form first and fitting the content to it distorts the relation.

| Relation | Cues | Expression |
|---|---|---|
| Transition | Current versus future, generational change, reorganization and similar | Two panels left and right with a thick arrow between them, the future side wider and with a darker label |
| Opposition | Competition, two-way comparison, trade-offs and similar | Symmetric panels left and right with an opposition marker in the middle, a different color for each side |
| Stages | Sequence, generations, procedures, maturity and similar | Chevron band or steps, accent color on the current or final stage only |
| Parallel | Equal tasks, fields, components and similar with no order | Side-by-side panels or circles, a number or icon on each item, no arrows implying order |
| Framework | Top-down relation of vision, goals, strategies, tasks and similar | A tiered table stacked top to bottom with row labels on the left |
| Convergence | Several factors lead to one conclusion | Side-by-side items, a downward marker, a conclusion band |
| Center and periphery | One subject and its components or fields of application | A central circle with surrounding elements, each with its own name and content |
| Matrix | Two criteria crossed | A grid with row labels on the left and column heads on top |
| Schedule | Yearly rollout, phased implementation and similar | Interval bars on a time scale, with phase names and deliverables |
| Governance | Roles and reporting lines between organizations | Organization chart with the lead body on top and roles written in the boxes |
| Location | Position, distance, regions and similar | Map with markers, radius circles, distances and travel times |
| Quantity comparison | Size, trend, composition, distribution and similar | Chart (see the data display section) |

- Set one main structure per slide. Use one or two secondary structures inside panels at most. When the user asks for two kinds of content on one slide, make the one closer to the message the main structure and put the other in a secondary panel.
- When the order and end point are the message, use stages. When durations and timing are the message, use a schedule.
- Check the deck order so the same main structure does not appear twice in a row. When the content relations are the same, the same structure is fine.
- Use center and periphery only when the surrounding elements are specific to the project. A central circle ringed with generic nouns carries no information.

## Background

Background lightness and background treatment change both the impression and the readability of a slide. Set both in step 4 of the planning order with the criteria below.

### Background lightness

This style works with light and dark backgrounds. Pick whichever works better for the purpose and use setting.

| Factor | Light background fits | Dark background fits |
|---|---|---|
| Amount of text | Slides with much body text, tables, charts and similar content | Slides with little text, built around photos, 3D objects, large shapes and similar |
| Venue | Bright meeting rooms, individual screen reading and similar | Dimmed event halls, large screens and similar |
| Distribution | Printed handouts, possible grayscale printing and similar | Screen-only showing |
| Organization template | The template has a light base | The template has a dark base |

- Dark text on a light ground is easier to read than the reverse. That is why light backgrounds suit text-heavy slides.
- In a dimmed venue, a fully bright screen dazzles the audience.
- Dark backgrounds use a lot of ink when printed and lose quality in grayscale.
- When the lighting and distribution are unknown, leave the venue row and the distribution row out and decide from the remaining rows and the slide's purpose and subject.
- Slides that ask the audience to read and weigh evidence get a light background. Analyses, plans, review results and similar fall in this group. Slides that leave an impression with one scene get a dark background. Vision announcements, covers, dividers and similar fall in this group.
- Reflect the subject when what it covers is itself a dark or light scene. Night landscapes, space, stages and similar suit a dark background. When the purpose and subject do not settle the choice, pick a light background.
- Write the reason for the choice in the design direction in one line, citing the slide's content.
- Body slides on a dark background still place their content on light content surfaces. Floating light surfaces on a dark background gives both richness and readability.
- Covers and dividers may use a different background lightness from body slides. In that case, set the shade of each role color for both backgrounds.

### Background treatment

Set whether to use background treatment, and how strongly, by the message and purpose of the slide. A plain single-color background with no treatment is a valid choice in this style. Follow the first row of the table below that applies, reading from the top.

| Slide type | Background that fits |
|---|---|
| Slides where a photo sets the mood | No treatment besides the photo |
| Slides dense with charts, tables, diagrams and similar | Plain single-color background or a split with a light color field |
| Slides meant to leave an impression, such as covers, dividers and vision declarations | Background treatment tied to the subject |
| Body slides with one hero element and little text | Restrained background treatment that supports the hero element |
| Other body slides | Plain single-color background or a split with a light color field |

- Background treatments include a gentle gradient of the primary color, a wide color field on one side, a subject photo under a color overlay, a large shape partly off the edge, a line drawing tied to the subject such as a map or plan, a soft glow, thin arcs and similar.
- Treatment tied to the subject tends to stay in memory with the project content. Treatment unrelated to the subject competes with the content for attention.
- Pick one kind of background treatment for the whole deck, following the allocation rules in the effects section, and vary only its strength by slide type. Slides without treatment keep the same background color.
- Keep background treatment weaker than the content but strong enough to see. Remove treatment that is barely visible, following the removal test. Do not let treatment lower the contrast of the text placed over it.

## Color

The color criteria in this section and the WCAG contrast criteria are not a right answer for every situation. During verification, adjust any color that looks jarring or unnatural to the audience and practitioners toward what is easy to read, pleasant and natural for them.

### Role assignment

Use chromatic colors only in the roles of primary, secondary and accent. Make every other color from lightness steps of these colors and from neutrals. With fixed roles, the audience can tell what an element is from its color alone.

| Role | Used for | Selection criteria |
|---|---|---|
| Primary | Position marker, panel labels, main shapes, base chart series and similar | The organization's signature color or a deep color that fits the subject |
| Secondary | The second category paired with the primary, the opposing side in an opposition layout and similar | An adjacent hue that differs from the primary and sits comfortably next to it |
| Accent | Keywords in the head message, the final stage, changed figures, the highlighted chart series and similar | A warm color with clear contrast against the primary |
| Neutral | Body text, lines, panel fills, comparison chart series and similar | White, gray steps, dark gray and similar |

Pick clear, vivid chromatic colors.

- Give each role color a dark step, a vivid middle step and a light step. Keep saturation fixed and change only lightness when making steps.
- Make light steps by mixing in white for a clear tint. Do not use grayish, muddy middle tones in chromatic roles.
- Pick a secondary color lighter than the primary and keep it clear, so the two colors also differ in lightness.
- Pick an accent color with high saturation and middle lightness. An accent darkened down loses its emphasis.

The same role color uses different steps depending on background lightness.

| Use | Light background | Dark background |
|---|---|---|
| Background | White, light gray, the lightest primary step and similar | The darkest primary step, dark gray and similar |
| Bands, labels, main shapes | Dark step or vivid step | Vivid step or light step |
| Panel fills, area shading | Light step that stands apart from the background at a glance | White or light-step content surfaces |
| Icons, bullets, arrows, lines | Dark step with ample contrast against the background | Light step with ample contrast against the background |

Set the color of each role in this order.

1. Colors the user specifies
2. The presenting organization's signature colors (read them from a logo or past materials if the user provided them)
3. With no instruction or clue, a deep navy primary, a teal or sky-blue secondary and an orange-leaning vermilion accent (see the contrast section for its lightness)

- When the primary is set to a warm color such as red, vermilion or orange and the accent falls to the default, the vermilion accent does not stand apart from the primary. This happens when a user-specified color or the organization's signature color is warm. In that case, ask the user how to assign the primary and accent colors.

### Order of color fields

- Raise a color field's contrast with the background as its importance rises. On a light background, color the hero element darkest, the conclusion band and panel labels next, and the panel fills light, and keep the surfaces that hold content close to white. On a dark background, color the hero element the most vivid and brightest.
- Make panels and content surfaces stand apart from the background at a glance. A very pale panel on a white background loses its edge, so show the section with a fill one step deeper, an outline, a header band, a distinct shadow or similar means.
- Use color bands to hold text such as section names, panel labels, conclusion statements and similar. Do not use bands that hold no text.
- On one slide, use the accent color only on the head message keywords and one or two spots in the body. Accents that point to the same target count as one spot even when they appear in several places.
- With four or more categories, separate them with lightness steps of the primary. Ask the user before adding more hues. Categories that step back, such as the current approach, items being reduced, comparison targets and similar, may get a neutral color.
- Map colors to categories one to one and keep the same mapping across the deck.

### Contrast

- Text-to-ground contrast meets the WCAG 2.x AA criteria as a floor. Normal text needs 4.5:1 or more. Large text (18pt and up, or 14pt bold and up) needs 3:1 or more.
- Icons, arrows, bullets, lines, chart marks and other elements that carry meaning without text need 3:1 or more contrast against adjacent colors. On light backgrounds, light secondary steps tend to fall short of this. On dark backgrounds, dark primary steps do. In those cases, switch to a higher-contrast step of the same hue, or add an outline.
- Contrast that barely passes looks faint in a real presentation. Room lighting lowers the contrast of projected screens, and print washes colors out. Aim for about 7:1 for body text and give graphic elements ample contrast above the floor as well.
- Compute contrast ratios by running code against the colors that touch.
- Pick vivid colors first and meet the criteria through text color assignment. Darkening color fields to pass the criteria muddies the secondary and accent colors and makes the whole slide sink.
- For each color field, assign white text or dark text (the darkest primary step), whichever gives higher contrast. Light fields such as sky blue, teal, orange, yellow and similar get dark text.
- When neither white nor dark text reaches 4.5:1 on a color field that carries normal text, use a lightness step of that color for the field. Fix the hue and saturation and find, in code, the passing lightness closest to the original.
- For the default accent, choose the hue closest to orange among the vermilions that stay vivid at the lightness that passes 4.5:1 with white text. Fix the hue and saturation and find the lightest value that passes, in code.
- Apply the same criteria when the accent or secondary color is used as a text color. A color that lacks contrast with its ground becomes the field behind the text, and the text stays white or dark.
- For text on gradients, light, photos and similar grounds, compute against the lowest-contrast point in the area under the text. For semi-transparent text, compute with the color that results from blending with the ground.
- When slides with different background lightness mix, such as a cover and body slides, a role color may pass on one background only. Set background-specific steps for each role color and compute contrast on both backgrounds.
- When rendering is available, measure the contrast of every text box from the rendered pixels. One method reads the background color of each text box area from a render with the text hidden and compares it with the text color. Comparing color codes alone misses text on light effects and gradients.

## Effects

Gradients, shadows, light, 3D and similar effects are core materials of this style. Richness comes from space and light across the screen, from the size and contrast of color fields, and from images. Decorating the surface of each shape gives the look of 2000s operating systems and web buttons.

### Richness criteria

First drafts tend to drift toward flat layouts made of tables and lists. Meet the criteria below, then refine with the allocation criteria.

- Give every body slide at least one hero element. The largest, highest-contrast shape on the screen, a central group of overlapping shapes, a 3D object, a photo and similar elements qualify. A slide made only of pale rectangles reads as a document table and misses the purpose of this style.
- Give equal items an icon or number badge so each item has a face. It applies to items at the panel or task level. Bullets inside a panel get none.
- Mix two or three kinds of shapes with different characters, such as square panels, circles, chevrons, arrows and similar, to give the screen rhythm.
- Let chromatic surfaces take a clear share of the screen. On light backgrounds, use large deep solid fields. On dark backgrounds, use large vivid color fields and light content surfaces. A slide reduced to thin lines and light gray on white reads as the minimal style.
- Overlap large shapes or let them run partly off the edge to create a sense of scale.
- When a draft looks flat, enlarge color fields, raise their contrast and give the hero element more weight before adding elements.

### Allocation

- Lower effect strength in this order: covers, dividers, hero elements of body slides, other elements.
- Pick one or two hero elements per body slide. Elements that carry the message directly, such as a central circle, a transition arrow, a conclusion band, the final stage and similar, become heroes.
- Give the hero element the largest area, the strongest contrast with the background and the clearest depth. Leave the other elements as calm solid fields.
- Pick one gradient method, one shadow method and one light method for the whole deck and repeat them. A background treatment and the light that belongs to it count as one method. As methods multiply, the deck looks assembled from pieces made by different people.

### Gradients

- Shape surfaces are solid by default. Use gradients on wide or long surfaces such as backgrounds, hero bands, arrows that show direction and similar.
- Use gradients between different hues only between adjacent colors such as the primary and secondary, and keep them long and gentle.
- Use gradients that fade to transparent at one end to show direction of travel or a spread of light.
- Do not use top-to-bottom lightness gradients on small shapes such as labels, header bands, circular badges and similar. That gradient creates a button-like material.
- Keep one direction across the deck.

### Depth

- Design depth in three levels or fewer: background, content surface and elements floating above it.
- Build depth from overlapping shapes and wide, soft shadows. Do not add a thick base under shapes.
- Spread shadows wide and soft, and keep their color close to the dark step of the primary. Do not use dark, hard-edged black shadows.
- Shadows barely show on dark backgrounds. Build depth there from a lightness gap by lifting content surfaces lighter than the background.
- Keep shadow direction and distance the same within a slide. The light source must read as one.
- Give elements at the same depth level the same shadow.

### Light

- Place light on the background and behind the hero element. A wide spread of light color, light rays and similar effects qualify.
- Light shows on dark backgrounds. On light backgrounds, bright light almost disappears, so light color fields or shadows take over its role.
- Pick light colors from the light steps of the secondary or primary.
- Do not use bright highlight bands on shape surfaces, reflections, glass-bead bulges, white rims around shapes, translucent glass panels and similar effects.
- Keep light under text weak enough that it does not lower text-to-ground contrast.

### 3D

- Use 3D for objects that become the hero of the slide. 3D images the user provided or made with an approved tool, plinths, blocks and steps drawn in code, and similar objects qualify. In 3D drawn with code, shade each face with a single flat color.
- Keep shapes that carry information, such as labels, bands, arrows, panels and similar, flat. Put text that belongs to a 3D object on a flat label or card next to the object.
- The height and size of 3D drawn without data can read as quantities. Show only the direction of growth or decline and add no scales or figures.
- Use one projection per slide. When mixing front-facing shapes with oblique 3D shapes, group the 3D shapes together.

### Requests to adjust intensity

- When the user asks for more flash, raise the presence of the background treatment, the depth of the hero element and the share of photos. Keep the skeleton, color roles and number of effect methods.
- When the user asks for a calmer look, reduce background treatment and depth levels, and limit photos to evidence photos.

## Imagery

### Sourcing

- Use photos and illustrations the user provided first. Without provided files, use a generation or search tool the user approved.
- Use photos, illustrations, icons and similar assets found through search only after confirming their terms of use (license). When the terms require attribution, credit the source on the slide.
- With neither user files nor an approved tool, build the same spot from 3D shapes drawn in code, diagrams, color fields and similar elements. Add empty photo placeholders only when the user asks.
- Use photos of real people and organization logos only from files the user provided. Do not change a logo's proportions or colors.

### Photos

- Photos on body slides serve as evidence that shows the real thing, such as facilities, products, sites, maps, events and similar subjects.
- Mood photos go on covers, dividers and backgrounds. Photos there only need to show the field the presentation covers.
- Match the tone and brightness of photos on one slide. Tinting them with the primary color or lowering their saturation together are among the methods.
- Keep crop shapes and corner treatment the same within a slide.
- When placing text on a photo, lay a color overlay under the text to secure contrast.
- Give each photo a short caption that says what it shows.

### Icons

- Take icons from a single set with the same stroke weight and fill style. Mixed styles look messy.
- Use icons as markers next to labels that help readers find items fast. Icons do not replace text.
- Keep icon size and color consistent by role. Pick colors from the role colors.
- Pair icons and their grounds with ample contrast, such as white icons on deep role-color circles or deep icons on white. Middle-tone icons on pale circles look faint from a distance.
- Do not use emoji.
- When no icon set is available in the environment, use number badges or simple shapes instead.

## Form

- Rounded rectangular panels, pill labels, circles, hexagons, chevrons, thick arrows, brackets, dashed sections and similar shapes recur in this style.
- Use the same form for the same role. When forms differ, the audience reads different roles.
- Keep corner radii and stroke weights to two levels each across the deck.
- Use arrows only where a real relation exists, such as order, cause, transition and similar. Use a thick arrow for the slide's one main direction and thin arrows for secondary relations.
- Align elements to a grid and keep spacing equal between elements at the same level. Alignment is the biggest difference between a rich slide and a messy one.
- Leave margins on all four edges of the screen. On a 16:9 slide, use about 0.5 inch as the reference.

### Shapes that hold text

- Center text vertically inside shapes by default.
- Center single-line labels horizontally by default. Left-align multi-line text with bullets by default. Align the second line after a bullet with the start of the first line's text.
- Size a shape that holds text to its block of text. Fit the height to the number of lines and keep top and bottom padding near the height of one text line. Fit the width to the text, and when widening shapes to grid columns, give every shape in the row the same width. Measure text width with the rendering tool (see the media implementation section).
- Equal shapes in the same row share the size of the shape with the longest text.
- When a shape is larger than needed and its empty space looks wider than its block of text, shrink the shape or add content.

## Text

- Use Korean gothic (sans-serif) typefaces with several weights. Pretendard, NanumSquare Neo, Noto Sans KR and similar faces are examples. Many weights let you separate levels of importance without enlarging text.
- Use one or two typefaces across the deck.
- When rendering in code, check that the fonts are installed before rendering. Without a Korean font, text breaks into boxes or falls back to another typeface. Install missing fonts or ask the user for the font files. Check in the rendered result that the specified typeface was applied.
- Keep text in flat, single colors. Gradients, outlines, shadows, 3D effects and similar treatments on text are the biggest cause of a dated look. Restrained effects are allowed in one spot only, the title of a cover or divider.
- Split text sizes into about four levels: head message, panel labels, body noun phrases and notes. Make adjacent levels different enough to tell apart at a glance.
- On a 16:9 slide 13.33 inches wide, use 12pt or more for body text.
- In pixel-based media, treat the screen width as 13.33 inches and convert points. At 1600px wide, 1pt is about 1.67px. Use the same conversion to judge large text for the contrast criteria.
- Set head messages and labels in bold and body text in medium weight. Show emphasis inside body text with weight and color. Do not use underline or italics.
- Write slide text in terse noun-ending style, the Korean gaejosik convention (e.g., '공급 거점 확충 추진', 'Supply hub expansion underway', and '처리 기간 단축', 'Shorter processing time'). When the user wants another style, apply that style across the deck.
- Write body text as noun phrases. Keep the text in one box to three lines or fewer.
- Break lines at units of meaning. Do not break inside a word or between a modifier and the word it modifies.
- Name the project's subject, region, technology and similar items in taglines and copy. Do not use aspirational copy that would fit any project.
- Slide text conveys the information the audience needs. Do not put meta information or meta narration from the maker's point of view on slides, such as the production process, tools used, internal reasoning, or the fact that drafting rules such as the same scale or a zero baseline were followed.

## Data display

### Figures

- Do not make one number the hero of the screen. Do not line up tiles that pair a big number with a short caption either. This style places figures next to claims as evidence. A standalone number display pushes the number forward without its evidence and breaks the line of argument a formal presentation needs.
- This criterion applies to data figures. Section numbers, step numbers, serial numbers and similar labels are exempt. Attach multipliers and change markers to a chart or a pair of figures.
- Place figures inside charts, tables or noun phrases. State the unit, period and point of comparison (prior year, target, other organizations, total and similar).
- Emphasize figures with color and weight. Enlarge them by one or two size levels above the surrounding text at most.
- Show change as a pair of the previous figure and the target figure. Use an arrow or change marker to show direction.
- Use only code-computed results for derived figures such as multiples, rates of change, compound annual growth rates and similar.
- Write a source for every figure in small type close to the chart or table.

### Charts

- Use charts as evidence inside panels. Set the message a chart delivers first, then pick its form.
- Use pie charts or stacked bars for composition, horizontal bars for item comparison, vertical bars or lines for change over time, and scatter plots for correlation and distribution.
- Write data labels directly next to the marks. Do not make readers tell series apart from a legend alone.
- Color one highlighted series in the accent color. Color the other series in lightness steps of the primary or in neutrals.
- Start the value axis of bar charts at 0. Bar length must be proportional to value or size comparisons get distorted.
- Write units on axis labels (e.g., Revenue (KRW 100 million)).
- Sort categories without time order by value and put "Other" last.
- Arrange pie slices clockwise from 12 o'clock, largest first. Beyond 5-6 slices, sizes become hard to tell apart, so group the small slices into "Other".
- Keep only the axis lines and gridlines needed for reading.
- You may add arrows and multiplier markers that signal growth or decline on top of a chart. Do not let added markers cover the data marks.
- Keep chart data marks flat, with no 3D, gloss, patterns or similar effects. 3D bars and 3D pies distort size comparisons. Give the panel around a chart the same effects as other panels.

### Tables

- Set header rows as dark color fields with white text, and mark total rows and highlighted rows with light color fields or bold text.
- Right-align numbers and put units in the header row or above the table.
- When a table is the slide's main structure, use the accent color on one or two highlighted cells only.

## Media implementation

- Measure text width with the rendering tool when sizing shapes. A browser's text measurement, an image library's text width calculation and similar functions work. Without a measurement tool, estimate one Korean character as wide as the font size and Latin letters and digits as a bit over half of it, and leave room.
- Give SVG a viewBox on the root element and omit fixed width and height. The graphic then fits its slot when placed in another document.
- Write SVG text as text elements. Text inside foreignObject disappears in some conversion tools.
- When one document holds several SVGs, identical ids overwrite each other's definitions. Prefix every id with a name unique to each diagram.
- Set the vertical position of SVG text with dy values. Some conversion tools ignore the dominant-baseline attribute.
- Render HTML that uses web fonts after the fonts finish loading. A capture taken before loading keeps the fallback typeface.
- When a medium does not support an effect, switch to the closest supported method and use it across the deck.

## Patterns to avoid

Redesign any part of a draft that matches the patterns below or patterns of the same kind.

### Dated effects

- The same strength of shadow, gloss and 3D applied to every element of a slide
- Color schemes mixing four or more saturated primary colors, rainbow gradients
- Gradients, outlines, shadows or 3D on text, warped text
- Metal textures, glass-bead textures, reflections covering half a surface
- Top-to-bottom lightness gradients on every label and header band, highlight bands on the top of shapes, thick bases under shapes, circular badges with white rims
- Shadows and gradients pointing in different directions on one slide
- Mixed clip art and icon styles, photos with mismatched tones
- 3D bar charts, 3D pie charts, pie charts with exploded slices
- Starburst shapes, wavy banners, speech bubbles unrelated to the content
- Text placed directly on a background with a strong pattern

### Patterns that recur in AI output

- Slides filled only with same-size cards of icon, title and description with no relations shown (side-by-side parallel items inside a panel or band do not count)
- Rows of metric tiles that pair a big number with a short caption
- Vertical color strips on one edge of a card, horizontal color bands with no text, short accent underlines under titles
- Ribbon markers placed before titles or items, ribbon decorations wrapped behind titles and similar
- Boxes that dress plain text up as a code block or code editor window (with ribbon decorations, a left vertical strip, window control dots, line numbers and similar)
- Purple-to-blue gradients, translucent glass panels, neon glow
- Emoji
- Generic images such as handshakes, light bulbs, globes and similar placed as evidence in the body
- A large central circle ringed with small circles of generic nouns
- Repeated symmetric layouts with every element centered

### Logic flaws

- Head messages that name a topic with no judgment
- Panels set side by side with no relation shown
- Conclusion bands that repeat the head message
- Text-heavy slides that keep all their information when every shape is deleted
- Panel sets that mix classification criteria

## Multiple slides

- Elements fixed across the deck are the position marker's place and form, background lightness, color roles, typefaces, effect methods and margins. Background lightness for covers and dividers follows the background section.
- Elements that change per slide are the body's main structure, the number and size of panels, and the hero element.
- Fixed elements create unity, and differences in body structure reduce monotony.
- When the user asks for the same layout repeated, keep the body structure the same as well.

## Verification

After building, render the result as an image and look at it. Fix any defect and render again. Reading code alone cannot reveal text overflow or overlaps. Without a way to check images, check coordinates and text widths by calculation and state in the result that the output is unverified. After checking the items below, look again through the eyes of the audience and practitioners and fix anything that looks off, even when no item covers it.

### Readability checks

- Does any text overflow or get cut off at its box?
- Do line breaks avoid splitting words and avoid awkward spots?
- Does each shape that holds text fit its block of text, with the text centered vertically?
- Do elements avoid overlapping?
- Does all text, including text on gradients, light and photos, meet WCAG AA contrast against its real background?
- Do icons, arrows, bullets, lines, chart marks and similar elements have 3:1 or more contrast against adjacent colors?
- When the slide is shrunk, do panel edges, icons, lines and secondary text stay clear?
- Are elements at the same level aligned and evenly spaced?
- Was the specified typeface applied?

### Effect checks

- Was the use setting set by the criteria in the use setting section?
- Does the background lightness fit the amount of text, the venue and the distribution?
- Does the background treatment serve the message and pass the removal test?
- In the squint test, is the hero element seen first?
- Does the hero element stand out in area, contrast and depth, and does the slide avoid looking like a table or list?
- In the era test, are there no shapes that look like buttons or window title bars?
- Do shadows and gradients read in one direction?
- Do effect methods stay within the set number?
- Is the accent color used only at the set spots?
- Are the secondary and accent colors clear and vivid, with no muddy middle tones in chromatic roles?
- Is the slide free of the patterns to avoid?

### Content checks

- Is the slide free of generic elements caught by the swap test?
- Is every piece of slide text information the audience needs, with no meta information or meta narration?
- Is slide text consistent in the noun-ending style or in the style the user set?
- Is there no standalone number display, and does every figure have a unit, period, point of comparison and source?
- Do the slide's facts, figures and sources match the user's materials or verified materials?
- Was no information without a source, uncertain or unknown made up without the user's confirmation?
- For multi-slide decks, are the fixed elements consistent and do body structures differ?

## Decisions left to the user

- Whether to use the organization's signature colors, logo and template files
- Providing photos and illustrations, or approving a generation tool
- Adding chromatic color roles
- Assigning the primary and accent colors when the primary is a warm color
- Verifying information without a confirmed source
- Verifying the terms of use of images and icons whose terms are unconfirmed
- The final level of effect intensity

