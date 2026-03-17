#!/bin/bash
# Installeert de Sprankelend server als achtergrondservice.
# Na installatie draait de server automatisch bij het inloggen
# en na het ontwaken uit slaapstand.

PLIST_SRC="$(dirname "$0")/com.sprankelend.server.plist"
PLIST_DST="$HOME/Library/LaunchAgents/com.sprankelend.server.plist"

echo "🔥 Sprankelend server installeren..."

# Stop eventueel draaiende instantie
launchctl unload "$PLIST_DST" 2>/dev/null

# Kopieer plist naar LaunchAgents
cp "$PLIST_SRC" "$PLIST_DST"

# Laad de service
launchctl load "$PLIST_DST"

echo ""
echo "✓ Server geïnstalleerd en gestart!"
echo "  De server draait nu altijd op de achtergrond."
echo "  Open op je telefoon: https://$(python3 -c "import socket; s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.connect(('8.8.8.8',80)); print(s.getsockname()[0]); s.close()" 2>/dev/null || echo 'jouw-ip'):8443/sprankelend_compleet.html"
echo ""
echo "  Verwijderen: launchctl unload ~/Library/LaunchAgents/com.sprankelend.server.plist"
