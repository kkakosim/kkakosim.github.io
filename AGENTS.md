# Repository Guide

This repository is a customized fork of `alshedivat/al-folio` for Konstantinos
Kakosimos's academic site. Preserve the site owner's content when changing theme
code or importing a new al-folio release.

## Sources of Truth

- `_config.yml`: site identity, URLs, navigation, integrations, and Scholar
  author matching. The Scholar name must remain `Kakosimos` / `Konstantinos`.
- `_pages/about.md`, `_pages/people.md`, `_pages/projects.md`,
  `_pages/teaching.md`, and `_pages/publications.md`: primary site pages.
- `_projects/{ED,EU,IN,RE,RI}_*_project.md`: real funded-project records.
- `_news/20*.md`: real announcements.
- `_bibliography/papers.bib`: real publication data. Do not replace it with the
  al-folio Einstein example bibliography.
- `assets/json/resume.json` and `assets/pdf/`: CV data and downloadable files.
- `_pages/books/*.md`, `_pages/bookstech.md`, `_bibliography/books.bib`, and
  site-specific files under `assets/img/`: owner-authored content and media.

Treat `_config.yml`, `_pages/projects.md`, `_sass/_base.scss`, and theme layouts
as mixed files: they contain both upstream structure and local behavior. Merge
these deliberately instead of restoring either version wholesale.

## Local Customizations to Preserve

- The production URL is `https://kkakosim.github.io` with an empty `baseurl`.
- The home page uses the real profile, enables real announcements, and does not
  show sample latest posts.
- The projects page groups `EU`, `Industry`, `Education`, and `Qatar`, supports
  horizontal cards, and filters highlighted projects by `importance`.
- `_sass/_base.scss` gives project cards visual emphasis through
  `.importance-1`, `.importance-2`, and `.importance-3`.
- `_layouts/default.liquid` must load `{% include scripts.liquid %}`. The legacy
  per-library includes read obsolete top-level dependency settings and generate
  invalid URLs such as `jquery@/`, breaking jQuery-dependent theme features.
- Publication toggles in `assets/js/common.js` and `_layouts/bib.liquid` must
  remain native DOM interactions without inline jQuery, so abstracts and
  expanded author lists still work if the external jQuery CDN is unavailable.
- The bookshelf and demo profile pages are not part of the public site.
- The deployment workflow must retain all scripts required by the default
  layout and must build successfully before deployment.

The recovery commits after the previous upgrade are useful audit references:
`62d1b7d2`, `a03c860a`, `faec1744`, `3b25fb50`, `51cc0cdf`, `cbd60c83`, and
`a6f70bc2`.

## Upgrading al-folio

Do not start with `git rebase upstream/main`. At the time this guide was added,
`main` and `upstream/main` had no merge base. First verify with:

```sh
git fetch origin upstream --tags
git merge-base HEAD upstream/main
```

If that prints no commit, use a fresh integration branch:

```sh
git status --short
git branch backup/pre-al-folio-<version>
git switch -c upgrade/al-folio-<version> upstream/main
```

Restore owner-controlled content from the backup branch with `git restore
--source backup/pre-al-folio-<version> -- <paths>`. Restore the source-of-truth
files and directories above wholesale, except the mixed files. Port mixed-file
changes manually onto the new upstream versions. Keep upstream dependency,
layout, include, plugin, and workflow changes unless a local requirement is
documented here.

Before replacing `main`, compare the integration branch with the backup and
verify that it contains no al-folio demo identity or content:

```sh
rg -n "Albert Einstein|A simple inline announcement|title: project [0-9]" \
  _config.yml _data _pages _news _projects _bibliography
npx prettier . --check
bundle exec jekyll build
rg -n "jquery@/|mdbootstrap@/" _site
```

If local Ruby/Bundler is unavailable, run `docker compose up --build` and inspect
the site at `http://localhost:8080`. Also verify `/`, `/projects/`,
`/publications/`, `/people/`, `/teaching/`, and `/cv/`; confirm author
highlighting, project filters, navigation, images, PDF links, and announcements.
Only update `main` after these checks pass.

## Editing Notes

- Keep text files in UTF-8 and preserve meaningful accents and scientific
  symbols. On Windows, use `Get-Content -Encoding utf8`; default PowerShell
  display decoding can make valid UTF-8 look corrupted.
- Do not commit `_site`, caches, `vendor`, or `node_modules`.
- Do not restore demo projects, announcements, CV entries, or Einstein
  bibliography records during an upstream upgrade.
