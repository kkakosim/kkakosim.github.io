@echo off
echo =======================================================
echo Starting al-folio Jekyll development server via WSL...
echo =======================================================
echo.
echo Once the server starts, open your browser to:
echo http://localhost:4000/
echo.
echo Press Ctrl+C to stop the server.
echo.
wsl bash -c "cd /mnt/e/github/kkakosim.github.io && export PATH=\"\$(ruby -e 'print Gem.user_dir')/bin:\$PATH\" && export BUNDLE_PATH=\"\$HOME/.bundle/kkakosim-github\" && bundle exec jekyll serve --host 0.0.0.0 --port 4000 --livereload --force_polling"
pause
