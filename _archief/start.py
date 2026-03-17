#!/usr/bin/env python3
"""
Start een HTTPS server zodat je Sprankelend kunt openen op je telefoon.

Gebruik:
  python3 start.py

Open dan op je telefoon:
  https://<jouw-ip>:8443/sprankelend_compleet.html

Je telefoon geeft een beveiligingswaarschuwing — dat is normaal.
Klik op "Toon details" / "Advanced" → "Ga toch door" / "Proceed".
"""

import http.server
import ssl
import os
import subprocess
import socket

PORT = 8443
DIR = os.path.dirname(os.path.abspath(__file__))
CERT_FILE = os.path.join(DIR, '.cert.pem')
KEY_FILE = os.path.join(DIR, '.key.pem')

def get_local_ip():
    """Vind het lokale IP-adres op het netwerk."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "localhost"

def generate_cert():
    """Maak een self-signed certificaat aan."""
    if os.path.exists(CERT_FILE) and os.path.exists(KEY_FILE):
        return
    print("🔐 Certificaat aanmaken (eenmalig)...")
    subprocess.run([
        'openssl', 'req', '-x509', '-newkey', 'rsa:2048',
        '-keyout', KEY_FILE, '-out', CERT_FILE,
        '-days', '365', '-nodes',
        '-subj', '/CN=localhost'
    ], check=True, capture_output=True)
    print("✓ Certificaat aangemaakt")

if __name__ == '__main__':
    os.chdir(DIR)
    generate_cert()

    handler = http.server.SimpleHTTPRequestHandler
    server = http.server.HTTPServer(('0.0.0.0', PORT), handler)

    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(CERT_FILE, KEY_FILE)
    server.socket = ctx.wrap_socket(server.socket, server_side=True)

    ip = get_local_ip()
    print(f"""
╔══════════════════════════════════════════════════╗
║  🔥 Sprankelend draait!                         ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  Op deze computer:                               ║
║  https://localhost:{PORT}/sprankelend_compleet.html  ║
║                                                  ║
║  Op je telefoon:                                 ║
║  https://{ip}:{PORT}/sprankelend_compleet.html
║                                                  ║
║  ⚠️  Je browser geeft een waarschuwing.          ║
║  Dat is normaal — klik op "Ga toch door".        ║
║                                                  ║
║  Stop met: Ctrl+C                                ║
╚══════════════════════════════════════════════════╝
""")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n✓ Server gestopt")
        server.server_close()
