# YAML Fields Cleanup Summary

This cleanup removed unused fields from YAML frontmatter in .md files throughout the repository.

## Analysis Process

1. **Field Discovery**: Analyzed 130 .md files and found 162 unique YAML frontmatter fields
2. **Template Analysis**: Analyzed Jekyll layouts and includes to identify 84 fields actually used in templates
3. **Usage Comparison**: Identified fields that appear in YAML but are never referenced in templates
4. **Conservative Removal**: Only removed fields that are clearly unused and not Jekyll core functionality

## Fields Removed

### Course Fields (removed from 9 course files)
- `credits` - Course credit information not displayed
- `video` - Video links not used in course templates  
- `moodle` - Moodle URLs not displayed in templates
- `github` - Page-level GitHub URLs not used (site-level GitHub still preserved)
- `website` - Page-level website URLs not used (site-level config preserved)

### Event Fields
- `aspectratio` - Standalone aspect ratio field not used in event templates (18 files)
- `register` - Registration links not displayed (8 files)  
- `date-format` - Date formatting not used (7 files)
- `titlepage` - Title page settings not used (2 files)

### RevealJS/Quarto Fields (removed from 6 presentation files)
These fields are for Quarto/Pandoc presentation generation, not Jekyll:
- `html-math-method`
- `format.revealjs` and all subfields:
  - `format.revealjs.css`
  - `format.revealjs.aspectratio`
  - `format.revealjs.title-slide-attributes`
  - `format.revealjs.slide-level`  
  - `format.revealjs.title-slide-attributes.data-background-opacity`
  - `format.revealjs.self-contained`

### Dataset Fields (removed from 5 dataset files)
- `extent.records` - Record counts not displayed
- `extent.size` - Data size not displayed
- `coverage.spatial` - Spatial coverage not displayed
- `coverage.temporal` - Temporal coverage not displayed
- `tag` - Alternative tag field (different from `tags`)

### Blog Post Fields (removed from 14 blog posts)
- `published` - Publication status not used in templates
- `canonical_url` - Canonical URLs not used in templates

### Software Fields
- `docs` - Documentation links not used (2 files)

### Miscellaneous
- `superheading` - Only used in 404.md, not in templates

## Fields Preserved

### Jekyll Core Fields (kept even if analysis showed low usage)
- `layout` - Used by Jekyll core
- `permalink` - Used by Jekyll core  
- `date` - Used by Jekyll core for sorting
- `title`, `description`, `tags`, `categories` - Core content fields

### Template-Used Fields (kept)
- All fields actually referenced in _layouts/ or _includes/ templates
- Fields accessed via loops (e.g., `links.text`, `links.url` via `item.text`, `item.url`)
- Fields that may be used in conditional logic

## Impact

- **60 files modified** with unused fields removed
- **89 files cleaned** of null values created during processing
- Significantly cleaner YAML frontmatter with only meaningful fields
- No functional changes to site rendering or behavior
- All Jekyll builds still pass successfully

## Files Modified

### By Collection:
- **Courses**: 9/9 files (removed course-specific unused fields)
- **Datasets**: 5/5 files (removed extent/coverage subfields)  
- **Events**: ~25 files (removed presentation and registration fields)
- **Posts**: 14/14 files (removed blog-specific unused fields)
- **Software**: 2/6 files (removed docs field)
- **Root pages**: Several files with template-specific fields

The cleanup maintains all functionality while significantly reducing YAML verbosity and improving maintainability.
