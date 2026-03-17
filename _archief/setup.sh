#!/bin/bash
# ═══════════════════════════════════════════════════
# Sprankelend Setup
# Installeert alles naar ~/.sprankelend/ en start
# de server als achtergrondservice.
# ═══════════════════════════════════════════════════

BRON="$(cd "$(dirname "$0")" && pwd)"
DOEL="$HOME/.sprankelend"
PLIST_NAAM="com.sprankelend.server"
PLIST_DST="$HOME/Library/LaunchAgents/${PLIST_NAAM}.plist"

echo ""
echo "🔥 Sprankelend Setup"
echo "════════════════════"

# 1. Stop eventueel draaiende service
launchctl unload "$PLIST_DST" 2>/dev/null

# 2. Maak doelmap aan
mkdir -p "$DOEL"

# 3. Kopieer bestanden
cp "$BRON/sprankelend_compleet.html" "$DOEL/"
cp "$BRON/start.py" "$DOEL/"

# Kopieer certificaten als ze bestaan
[ -f "$BRON/.cert.pem" ] && cp "$BRON/.cert.pem" "$DOEL/"
[ -f "$BRON/.key.pem" ] && cp "$BRON/.key.pem" "$DOEL/"

echo "✓ Bestanden gekopieerd naar $DOEL"

# 4. Maak LaunchAgent plist
cat > "$PLIST_DST" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>${PLIST_NAAM}</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>${DOEL}/start.py</string>
    </array>
    <key>WorkingDirectory</key>
    <string>${DOEL}</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>${DOEL}/.server.log</string>
    <key>StandardErrorPath</key>
    <string>${DOEL}/.server.log</string>
</dict>
</plist>
EOF

echo "✓ LaunchAgent aangemaakt"

# 5. Start de service
launchctl load "$PLIST_DST"

# Wacht even tot server start
sleep 2

# 6. Check of het werkt
if launchctl list | grep -q "$PLIST_NAAM"; then
    IP=$(python3 -c "import socket; s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.connect(('8.8.8.8',80)); print(s.getsockname()[0]); s.close()" 2>/dev/null || echo "jouw-ip")
    echo ""
    echo "╔══════════════════════════════════════════════╗"
    echo "║  ✓ Server draait!                            ║"
    echo "║                                              ║"
    echo "║  Op je telefoon:                             ║"
    echo "║  https://${IP}:8443/sprankelend_compleet.html"
    echo "║                                              ║"
    echo "║  De server start nu automatisch mee met      ║"
    echo "║  je laptop (ook na slaapstand).              ║"
    echo "║                                              ║"
    echo "║  Verwijderen:                                ║"
    echo "║  launchctl unload ~/Library/LaunchAgents/    ║"
    echo "║    com.sprankelend.server.plist              ║"
    echo "╚══════════════════════════════════════════════╝"
else
    echo ""
    echo "⚠ Server lijkt niet te draaien."
    echo "  Check: cat ~/.sprankelend/.server.log"
fi
echo ""
