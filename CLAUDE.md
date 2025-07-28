# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

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