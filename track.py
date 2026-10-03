#!/usr/bin/env python3
"""
Application & Scholarship Command-Line Tracker
Compatible with Linux Desktop, Server, and Android Termux (Zero Dependencies).
"""

import sys
import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "applications.json")

def load_data():
    if not os.path.exists(DATA_FILE):
        print(f"Error: Data file not found at {DATA_FILE}")
        sys.exit(1)
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    data["last_updated"] = datetime.now().isoformat()
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✅ Updated {DATA_FILE}")

def cmd_list(args):
    data = load_data()
    tracks = data.get("active_tracks", [])
    filter_country = args[0].lower() if args else None

    print("\n" + "=" * 105)
    print(f"{'ID':<18} | {'COUNTRY':<8} | {'INTAKE':<24} | {'DEADLINE':<12} | {'STATUS':<20} | {'PRIORITY'}")
    print("=" * 105)

    for t in tracks:
        if filter_country and filter_country not in t["country"].lower():
            continue
        print(f"{t['id']:<18} | {t['country']:<8} | {t['target_intake'][:24]:<24} | {t['deadline'][:12]:<12} | {t['status']:<20} | {t['priority']}")
    print("=" * 105)
    print(f"Total: {len(tracks)} tracked programs. Use `python track.py show <id>` for full details.\n")

def cmd_show(args):
    if not args:
        print("Usage: python track.py show <id>  (e.g., python track.py show italy-trento)")
        return
    tid = args[0].lower()
    data = load_data()
    for t in data.get("active_tracks", []):
        if t["id"].lower() == tid or tid in t["id"].lower():
            print("\n" + "-" * 70)
            print(f"📌 {t['university']} ({t['country']})")
            print("-" * 70)
            print(f"• Degree Program   : {t['program']}")
            print(f"• Funding Scheme   : {t['funding']}")
            print(f"• Financial Award  : {t['benefits']}")
            print(f"• English Policy   : {t['language_requirement']}")
            print(f"• Target Intake    : {t['target_intake']}")
            print(f"• Application Cutoff: {t['deadline']}")
            print(f"• Current Status   : {t['status']} (Priority: {t['priority']})")
            print(f"• Portal URL       : {t['portal_url']}")
            print(f"• Strategic Notes  : {t['notes']}")
            if "professors_contacted" in t:
                print(f"• Professors Contacted: {', '.join(t['professors_contacted'])}")
            print("-" * 70 + "\n")
            return
    print(f"No track found matching '{tid}'")

def cmd_deadlines(args):
    data = load_data()
    tracks = data.get("active_tracks", [])
    
    # Sort by deadline
    sorted_tracks = sorted(tracks, key=lambda x: x.get("deadline", "9999"))
    
    print("\n⏳ UPCOMING DEADLINES CHRONOLOGICAL QUEUE:")
    print("-" * 85)
    for t in sorted_tracks:
        print(f"• [{t['deadline']:<10}] {t['university']:<32} | {t['target_intake']:<25} | Status: {t['status']}")
    print("-" * 85 + "\n")

def cmd_china(args):
    data = load_data()
    profs = data.get("china_professors", [])
    print("\n🇨🇳 CHINA CSC PROFESSOR OUTREACH LOG:")
    print("=" * 95)
    print(f"{'TARGET':<8} | {'PROFESSOR':<22} | {'UNIVERSITY':<28} | {'SENT':<10} | {'FOLLOW-UP':<10} | {'STATUS'}")
    print("=" * 95)
    for p in profs:
        print(f"Target {p['target']:<1} | {p['professor']:<22} | {p['university'][:28]:<28} | {p['sent_date']:<10} | {p['follow_up_date']:<10} | {p['status']}")
    print("=" * 95 + "\n")

def cmd_update(args):
    if len(args) < 2:
        print("Usage: python track.py update <id> <new_status>  (e.g., python track.py update italy-trento APPLIED)")
        return
    tid = args[0].lower()
    new_status = args[1].upper()
    data = load_data()
    found = False
    for t in data.get("active_tracks", []):
        if t["id"].lower() == tid or tid in t["id"].lower():
            t["status"] = new_status
            found = True
            print(f"Updated {t['id']} status to: {new_status}")
            break
    if found:
        save_data(data)
    else:
        print(f"Track '{tid}' not found.")

def cmd_help():
    print("""
Application Tracker CLI (Desktop & Termux)
Usage:
  python track.py list             # List all tracked universities and programs
  python track.py list <country>   # Filter by country (e.g. `python track.py list italy`)
  python track.py show <id>        # View full dossier for an ID (e.g. `python track.py show italy-trento`)
  python track.py deadlines        # Chronological deadline countdown
  python track.py china            # Check China CSC professor outreach status & follow-up dates
  python track.py update <id> <st> # Update application status
""")

def main():
    if len(sys.argv) < 2:
        cmd_help()
        return
    cmd = sys.argv[1].lower()
    args = sys.argv[2:]

    if cmd == "list":
        cmd_list(args)
    elif cmd == "show":
        cmd_show(args)
    elif cmd in ("deadlines", "dl"):
        cmd_deadlines(args)
    elif cmd in ("china", "csc"):
        cmd_china(args)
    elif cmd == "update":
        cmd_update(args)
    else:
        cmd_help()

if __name__ == "__main__":
    main()
