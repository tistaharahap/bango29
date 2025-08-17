# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Hugo static site for [bango29.com](https://bango29.com) - a personal blog by Batista Harahap. The site uses the PaperMod theme and is deployed via Coolify using Nixpacks.

## Common Commands

### Development
- `hugo server -D` - Run development server with drafts enabled
- `hugo --minify` - Build production site with minification
- `./build.sh` - Production build script using environment variables

### Content
- `hugo new posts/post-name.md` - Create new blog post
- Posts are stored in `content/posts/` with front matter including categories, tags, date, and optional cover images

### Deployment
- Site deploys automatically via Coolify using `nixpacks.toml`
- Hugo v0.148.2 is enforced via direct download in build phase
- Production URL: https://bango29.com

## Architecture

### Hugo Configuration
- **Theme**: PaperMod (git submodule at `themes/PaperMod/`)
- **Config**: `config.yaml` with customized parameters for personal blog
- **Permalinks**: Posts use `/:slug/` structure
- **Content**: Markdown posts in `content/posts/` directory

### Custom Template Overrides
The site overrides PaperMod theme templates in `layouts/partials/`:

- **Social Media Meta Tags**: Custom OpenGraph and Twitter card templates at `layouts/partials/templates/opengraph.html` and `layouts/partials/templates/twitter_cards.html` that prioritize post-specific cover images (`.Params.image`) over theme defaults
- **Google Analytics**: Custom `layouts/partials/google_analytics.html` for GA4 integration
- **Home Info**: Custom profile section with image and description

### Post Front Matter Structure
Posts support both `image` and `cover.image` parameters for social media sharing:
```yaml
+++
title = "Post Title"
date = 2025-01-01T00:00:00Z
image = "/content/images/cover.png"  # Prioritized for social sharing
categories = ["category"]
tags = ["tag"]
+++
```

### Deployment Configuration
- **Nixpacks**: Custom `nixpacks.toml` downloads Hugo v0.148.2 directly to avoid version conflicts
- **Build Process**: Downloads tar.gz, extracts, and runs Hugo with minification
- **Static Files**: Served from `/public` directory after build

### Theme Integration
- PaperMod theme as git submodule with customizations in main repository
- Custom templates override theme defaults without modifying theme files
- Social media meta tags properly handle post cover images for sharing

## Key Files

- `config.yaml` - Hugo site configuration
- `nixpacks.toml` - Deployment build configuration
- `content/posts/` - Blog post content
- `layouts/partials/templates/` - Custom template overrides for social media
- `themes/PaperMod/` - Hugo theme (git submodule)