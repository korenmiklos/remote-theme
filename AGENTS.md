# AGENTS.md

This file provides guidance to Claude Code and AI agents when working with code in this repository.

## Writing Style Guide

When writing blog posts or documentation for this site, follow these style characteristics observed in the author's existing posts:

### Voice and Tone
- Direct, conversational, accessible academic voice
- Use first person ("I") when sharing personal experiences
- Use second person ("you") to engage reader directly
- Balance technical precision with readability

### Sentence Structure
- **Short, declarative sentences for emphasis**: "Coding is like ultra running." "Strange, because if you think about it, everything in data analysis is a function." "Finding good looking keys is fun."
- **Rhetorical questions to engage reader**: "But how do these keys look in real life?" "What is the API of a data product?" "So why am I a big fan of plain text data despite all these problems?"
- **Block quotes for key takeaways**: Use `>` for pullout quotes that summarize main arguments, e.g., "> I believe portability and ease of exploration beats a tight schema-conforming database any time."

### Paragraph Organization
- Start with concrete examples or personal anecdotes
- Lead with the practical problem before theoretical explanation
- Use transitional headers as questions: "What's wrong with this?" "How does this work in practice?"

### Technical Content Style
- **Show, don't just tell**: Include code examples, data tables, concrete examples (e.g., the food CSV example in semantic versioning)
- **Real-world examples**: Use authentic scenarios from research ("Hungarian firms managed by foreign CEOs", "Belváros-Lipótváros Budapest Főváros V. kerület Polgármesteri Hivatal")
- **Analogies from everyday life**: Running ultras, Tupperware, eggs vs omelettes, time organization

### Humor and Cultural References
- Inject dry humor: "deep fried mars bar" as example, "Hungover Ltd." as company name
- Reference pop culture when relevant: Kinks song "David Watts" as blog title
- Include parenthetical asides: "(true story)", "(Mind you, I am not working in a bank. Or health care.)"

### Educational Approach
- **Build from simple to complex**: Start with obvious problems, then reveal deeper issues
- **Acknowledge reader intelligence**: "Do not just repeat what is in the table or the figure. You don't want to insult your coworker's intelligence."
- **Call to action**: End with practical next steps or encouragement: "Go out and have some.", "Nurture your code with the same love you nurture your calendar."

### Structural Elements
- Use numbered or bulleted lists for actionable advice
- Include relevant images with proper attribution
- Use code blocks with language specification
- Add explanatory notes in blockquotes (e.g., "> **Why June 21?**")

### Key Phrases and Patterns
- Imperative mood for recommendations: "Enter semantic versioning", "Automate all the data cleaning", "Join late", "Share your intermediate data products"
- Parallel structure in lists: "What deliverables have I completed? What did I learn? What actions do I need from you? What are my next steps?"
- Rhetorical setup: "Er, what?" to express confusion at complicated code

### Technical Writing Standards
- Define terms on first use
- Link to relevant resources and papers
- Cite sources appropriately (Joel Spolsky, Jenny Bryan, Uncle Bob Martin)
- Use bold for emphasis on key concepts
- Prefer active voice: "I think" over "It is thought"

### Sentence Examples for Reference
- Opening hooks: "In one of my research projects, I study how Hungarian firms managed by foreign CEOs perform relative to those managed by domestic CEOs."
- Practical transitions: "So what is the right level of abstraction? What is small enough? How many are few enough?"
- Authoritative statements: "For data analysis, we almost exclusively write code that does not require user interaction and would be well suited to the functional paradigm."
- Conversational asides: "(By the way, `X\Y` is a better way to write this in Julia.)"

## Project Overview

## Project Overview

This is a Jekyll-based academic website theme with multiple configurations:
- **Publications site** (koren.mk) - Academic publications and research
- **Courses site** (koren.dev) - Educational content and courses  
- **Blog site** (codedthinking.com) - Blog posts and articles

The site uses Jekyll with Tailwind CSS 3.0 for styling and supports multiple content types through Jekyll collections.

## Development Commands

### Initial Setup
```bash
bundle install          # Install Ruby dependencies
npm install             # Install Node.js dependencies
```

### Development
```bash
npm run dev             # Start development server with live reload
npm run build           # Production build (CSS + Jekyll)
npm run clean           # Clean generated files
```

This runs:
- `tailwindcss` watch process for CSS compilation 
- `bundle exec jekyll s --port 4001 --livereload` for Jekyll development server with live reload

### Manual Commands
```bash
bundle exec jekyll serve --port 4001 --livereload --trace  # Jekyll development server
tailwindcss -i ./assets/css/main.css -o ./assets/css/style.css --watch    # CSS compilation
npm run build:css       # Build and minify CSS only  
```

## Site Configuration

The site behavior is controlled by `_config.yml`:
- `website` parameter switches between "blog", "courses", or "publications" modes
- Each mode has different styling, logos, and content focus defined in `_data/config.yaml`

## Content Structure

### Jekyll Collections
- `_publications/` - Academic papers and research outputs
- `_courses/` - Educational course content
- `_posts/` - Blog articles  
- `_events/` - Academic events and presentations
- `_datasets/` - Research datasets
- `_software/` - Software tools and packages

### Content Types
All content uses Markdown with YAML frontmatter. Each collection has specific layouts:
- Publications use `layout: publication`
- Courses use `layout: course`
- Posts use `layout: post`
- Events use `layout: event`

### Styling System
- Uses Tailwind CSS 3.0 with custom configuration
- Custom color scheme: blue (#1D1D40), red (#E61E25), custom grays
- Custom font: Brockmann for sans-serif, DM Mono for monospaced
- Responsive design with mobile-first approach

## File Organization

### Key Directories
- `_layouts/` - Jekyll layout templates
- `_includes/` - Reusable HTML components
- `assets/css/` - Stylesheets (main.css is source, style.css is compiled)
- `assets/images/` - Images and assets organized by purpose
- `_data/` - Configuration data files
- `_site/` - Generated site (ignored by git)

### Important Files
- `_config.yml` - Main Jekyll configuration
- `_data/config.yaml` - Multi-site configuration data
- `tailwind.config.js` - Tailwind CSS configuration
- `package.json` - Node.js dependencies and scripts

## Development Notes

- The site uses `livereload: true` for automatic browser refresh during development
- Tailwind processes files from `_layouts/`, `_includes/`, and HTML files
- Custom fonts are loaded from `assets/fonts/`
- Multiple favicon configurations for different site modes
- Uses Jekyll pagination for blog posts (4 posts per page)

## Code Organization & Reusable Components

The codebase has been refactored for better maintainability with these reusable components:

### Button Components
- `_includes/button-cta.html` - Red CTA buttons with arrow icons
- `_includes/button-white.html` - White variant buttons for dark backgrounds

### Icons
- `_includes/icons/arrow-right.html` - Right arrow for buttons
- `_includes/icons/arrow-left.html` - Left navigation arrow  
- `_includes/icons/arrow-right-nav.html` - Right navigation arrow

### Layout Components  
- `_includes/swiper-section.html` - Reusable carousel/slider component
- `_includes/card-*.html` - Content card templates for different types

### Component Usage Examples
```liquid
{% include button-cta.html text="View More" url="/blog/" %}
{% include button-white.html text="Learn More" url="/courses/" %}
{% include swiper-section.html swiper_class="swiper-courses" collection=site.courses card_template="card-course.html" %}
```

## URL Generation for Multi-Site Configuration

The site uses dynamic URL generation for different site modes (publications, courses, blog). URLs are constructed using:

```liquid
{{ site.data.config[site.website].url }}{{ page.url }}
```

This pattern is used in:
- Dataset citation URLs in `_layouts/dataset.html`
- Cross-site linking where absolute URLs are needed

The configuration supports:
- Publications: https://koren.mk
- Courses: https://koren.dev  
- Blog: https://codedthinking.com