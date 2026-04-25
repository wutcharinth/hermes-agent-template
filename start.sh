#!/bin/bash
set -e

# Mirror dashboard-ref-only's startup: create every directory hermes expects
# and seed a default config.yaml if the volume is empty. Without these,
# `hermes dashboard` endpoints that hit logs/, sessions/, cron/, etc. can fail
# with opaque errors even though no auth is actually involved.
mkdir -p /data/.hermes/cron /data/.hermes/sessions /data/.hermes/logs \
         /data/.hermes/memories /data/.hermes/skills /data/.hermes/pairing \
         /data/.hermes/hooks /data/.hermes/image_cache /data/.hermes/audio_cache \
         /data/.hermes/workspace

if [ ! -f /data/.hermes/config.yaml ]; then
  cat > /data/.hermes/config.yaml <<'EOF'
model:
  default: "google/gemini-2.5-flash"
  provider: "auto"

terminal:
  backend: "local"
  timeout: 120
  cwd: "/tmp"

agent:
  max_iterations: 100

data_dir: "/data/.hermes"
EOF
fi

# Seed skills (always overwrite so updates deploy cleanly)
cp /app/skills/*.md /data/.hermes/skills/ 2>/dev/null || true

[ ! -f /data/.hermes/.env ] && touch /data/.hermes/.env

exec python /app/server.py
