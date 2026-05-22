#!/usr/bin/env bash

set -euo pipefail

# =========================
# CONFIG
# =========================
REPO="Cron-Routine-Orchestrator-Webapp/CROW-Client"

ZIP_NAME="crow-client-Linux.zip"
BINARY_NAME="crow-client"

INSTALL_DIR="$HOME/.local/share/crow-client"
SERVICE_DIR="$HOME/.config/systemd/user"
SERVICE_FILE="$SERVICE_DIR/crow-client.service"
# =========================

echo "Fetching latest release..."

LATEST_URL=$(curl -s "https://api.github.com/repos/$REPO/releases/latest" \
  | grep "browser_download_url" \
  | grep "$ZIP_NAME" \
  | cut -d '"' -f 4 \
  | head -n 1)

if [[ -z "$LATEST_URL" ]]; then
  echo "No matching Linux release found."
  exit 1
fi

TMP_ZIP="/tmp/crow-client.zip"

curl -L "$LATEST_URL" -o "$TMP_ZIP"

rm -rf "$INSTALL_DIR"
mkdir -p "$INSTALL_DIR"

unzip -o "$TMP_ZIP" -d "$INSTALL_DIR" >/dev/null

BIN_PATH=$(find "$INSTALL_DIR" -type f -name "$BINARY_NAME" | head -n 1)

if [[ -z "$BIN_PATH" ]]; then
  echo "Binary not found."
  exit 1
fi

chmod +x "$BIN_PATH"

mkdir -p "$SERVICE_DIR"

cat > "$SERVICE_FILE" <<EOF
[Unit]
Description=CROW Client
After=network.target

[Service]
ExecStart=$BIN_PATH
Restart=always
RestartSec=5

[Install]
WantedBy=default.target
EOF

systemctl --user daemon-reload
systemctl --user enable crow-client.service
systemctl --user start crow-client.service

echo "Installation complete. CROW Client is now running as a systemd service."
