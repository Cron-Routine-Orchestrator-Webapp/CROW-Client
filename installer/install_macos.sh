#!/usr/bin/env bash

set -euo pipefail

# =========================
# CONFIG
# =========================
REPO="Cron-Routine-Orchestrator-Webapp/CROW-Client"

ZIP_NAME="crow-client-macOS.zip"
BINARY_NAME="crow-client"

INSTALL_DIR="$HOME/Library/Application Support/crow-client"
PLIST_DIR="$HOME/Library/LaunchAgents"
PLIST_FILE="$PLIST_DIR/com.crow.client.plist"
# =========================

echo "Fetching latest release..."

LATEST_URL=$(curl -s "https://api.github.com/repos/$REPO/releases/latest" \
  | grep "browser_download_url" \
  | grep "$ZIP_NAME" \
  | cut -d '"' -f 4 \
  | head -n 1)

if [[ -z "$LATEST_URL" ]]; then
  echo "No matching macOS release found."
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

mkdir -p "$PLIST_DIR"

cat > "$PLIST_FILE" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.crow.client</string>

  <key>ProgramArguments</key>
  <array>
    <string>$BIN_PATH</string>
  </array>

  <key>RunAtLoad</key>
  <true/>

  <key>KeepAlive</key>
  <true/>
</dict>
</plist>
EOF

launchctl load "$PLIST_FILE"

echo "Installation complete. CROW Client is now running as a Launch Agent."
