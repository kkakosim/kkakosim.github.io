# Local Development on This Workstation

This is the site-specific setup record for building and previewing
`kkakosim.github.io` on its current Windows workstation. The general al-folio
instructions remain in [INSTALL.md](INSTALL.md).

## Confirmed Environment

Recorded and validated on 2026-09-11.

### Windows host

- Node.js 24.11.0
- npm 11.6.1
- Playwright 1.58.2 from this repository's npm dependencies
- Playwright Chromium browser installed with `npx playwright install chromium`

There is no native Windows Ruby or Docker installation for this site. Ruby and
Jekyll run inside WSL; the browser and Playwright run on Windows.

### WSL

- WSL distribution: Ubuntu 24.04.3 LTS, x86-64
- Ruby 3.2.3
- Bundler 4.0.6, installed in the Ruby user gem directory
- Ruby bundle path: `/home/kkakosim/.bundle/kkakosim-github`
- Node.js 18.19.1, used by the Jekyll Terser integration
- ImageMagick 6.9.12-98
- APT packages: `ruby-full`, `ruby-dev`, `build-essential`, `zlib1g-dev`,
  `imagemagick`, and `nodejs`

`jupyter-nbconvert` is not installed. This is currently harmless because the
site has no Jupyter notebook posts. Run `./bin/setup-python-deps` in WSL before
adding notebook content.

Ruby gems and the Playwright browser are installed outside the repository.
They must be installed again after replacing the WSL distribution, Windows
user profile, or Ruby version.

## One-Time Setup

Install the Windows-side test dependencies from PowerShell:

```powershell
cd E:\github\kkakosim.github.io
npm ci
npx playwright install chromium
```

Install the Linux build dependencies from Ubuntu WSL:

```bash
sudo apt update
sudo apt install ruby-full ruby-dev build-essential zlib1g-dev imagemagick nodejs
gem install bundler -v 4.0.6 --user-install
```

Prepare the shell and install the locked Ruby dependencies:

```bash
cd /mnt/e/github/kkakosim.github.io
export PATH="$(ruby -e 'print Gem.user_dir')/bin:$PATH"
export BUNDLE_PATH="$HOME/.bundle/kkakosim-github"
bundle install
```

`bundle install` needs access to both RubyGems and GitHub because
`jekyll-terser` is locked to a Git commit. The migration setup encountered a
temporary WSL-to-GitHub connectivity failure; retry after confirming GitHub is
reachable if that dependency cannot be fetched.

## Browser Preview

For normal editing, start Jekyll from Ubuntu WSL:

```bash
cd /mnt/e/github/kkakosim.github.io
export PATH="$(ruby -e 'print Gem.user_dir')/bin:$PATH"
export BUNDLE_PATH="$HOME/.bundle/kkakosim-github"
bundle exec jekyll serve --host 0.0.0.0 --port 4000 --livereload --force_polling
```

Open `http://localhost:4000/` in a Windows browser. The site has an empty
`baseurl`, so no additional path component is required. Stop the server with
`Ctrl+C`.

## Production-Style Check

The migration was tested by building first and serving the generated `_site`
directory separately:

```bash
cd /mnt/e/github/kkakosim.github.io
export PATH="$(ruby -e 'print Gem.user_dir')/bin:$PATH"
export BUNDLE_PATH="$HOME/.bundle/kkakosim-github"
JEKYLL_ENV=production bundle exec jekyll build
ruby -run -e httpd _site -p 4173
```

Open `http://127.0.0.1:4173/` in a Windows browser. This mode tests the exact
static output that will be deployed rather than Jekyll's development server.

The 2026-09-11 migration check used Windows Playwright Chromium at 1366x900 and
390x844. It confirmed HTTP 200 responses for `/`, `/cv/`, `/publications/`,
`/projects/`, `/people/`, `/teaching/`, and `/bookstech/`; desktop and mobile
navigation; publication abstract open/close; author expansion; no horizontal
overflow; and no browser console or page errors. The temporary server was
stopped after the check.

## Validation Commands

Run these before merging an al-folio dependency upgrade:

```bash
bundle exec al-folio upgrade audit --no-fail
bundle exec al-folio upgrade overrides audit
JEKYLL_ENV=production bundle exec jekyll build
```

Run the repository checks from PowerShell:

```powershell
npm run lint:style-contract
npx prettier . --check --end-of-line auto
```

The `BUNDLE_PATH` and Ruby user-bin exports must be present in each new WSL
shell unless they are added to `~/.bashrc`.
