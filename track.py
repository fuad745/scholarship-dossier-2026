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
    print(f"{'ID':<20} | {'COUNTRY':<8} | {'INTAKE':<24} | {'DEADLINE':<12} | {'STATUS':<20} | {'PRIORITY'}")
    print("=" * 105)

    for t in tracks:
        if filter_country and filter_country not in t["country"].lower():
            continue
        print(f"{t['id']:<20} | {t['country']:<8} | {t['target_intake'][:24]:<24} | {str(t['deadline'])[:12]:<12} | {t['status']:<20} | {t['priority']}")
    print("=" * 105)
    print(f"Total: {len(tracks)} tracked programs. Use `python track.py show <id>` for full details.\n")

def cmd_show(args):
    if not args:
        print("Usage: python track.py show <id>  (e.g., python track.py show france-campus-france)")
        return
    tid = args[0].lower()
    data = load_data()
    for t in data.get("active_tracks", []):
        if t["id"].lower() == tid or tid in t["id"].lower():
            print("\n" + "-" * 75)
            print(f"📌 {t['university']} ({t['country']})")
            print("-" * 75)
            print(f"• Track ID         : {t['id']}")
            print(f"• Degree Program   : {t['program']}")
            print(f"• Funding Scheme   : {t['funding']}")
            print(f"• Financial Award  : {t['benefits']}")
            print(f"• English Policy   : {t['language_requirement']}")
            print(f"• Target Intake    : {t['target_intake']}")
            print(f"• Application Cutoff: {t['deadline']}")
            print(f"• Current Status   : {t['status']} (Priority: {t['priority']})")
            if "credentials" in t and t["credentials"]:
                c = t["credentials"]
                print(f"• Portal Account   : {c.get('created_by', 'User')} | ID: {c.get('username', 'N/A')} | Email: {c.get('email', 'N/A')}")
                print(f"• Portal Password  : {c.get('password', 'N/A')}")
            if "eef_candidate_id" in t and ("credentials" not in t or not t["credentials"]):
                print(f"• EEF Candidate ID : {t['eef_candidate_id']}")
            print(f"• Portal URL       : {t['portal_url']}")
            print(f"• Strategic Notes  : {t['notes']}")
            if "professors_contacted" in t:
                print(f"• Professors Contacted: {', '.join(t['professors_contacted'])}")
            if "required_documents" in t and t["required_documents"]:
                print("• Required Documents Readiness:")
                for d in t["required_documents"]:
                    icon = "✅ READY  " if d.get("ready") else "⏳ PENDING"
                    print(f"  [{icon}] {d.get('label')}")
            print("-" * 75 + "\n")
            return
    print(f"No track found matching '{tid}'")

def cmd_deadlines(args):
    data = load_data()
    tracks = data.get("active_tracks", [])
    sorted_tracks = sorted(tracks, key=lambda x: str(x.get("deadline", "9999")))
    
    print("\n⏳ UPCOMING DEADLINES CHRONOLOGICAL QUEUE:")
    print("-" * 88)
    for t in sorted_tracks:
        print(f"• [{str(t['deadline']):<10}] {t['university']:<32} | {t['target_intake']:<25} | Status: {t['status']}")
    print("-" * 88 + "\n")

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

def cmd_france(args):
    print("""
🇫🇷 FRANCE: ÉTUDES EN FRANCE (CAMPUS FRANCE) & EIFFEL SCHOLARSHIP
====================================================================================
• Candidate Identifier : ET26-00453 (Legal: TUBA, FUAD AHMED | DOB: 16/02/1999)
• Portal URL           : https://etudesenfrance.diplomatie.gouv.fr/
• Local Center         : Espace Campus France Éthiopie (Alliance Éthio-Française)
• Dossier Status       : DOSSIER PROFILE 100% COMPLETED

📁 VERIFIED ATTACHED DOCUMENTS:
• Passport             : E00340202 (ICS Ethiopia, valid through 15/04/2036)
• Higher Education     : Complete 3-Page PDF (Degree Certificate + 2-Page Transcripts)
• Secondary Education  : Combined Grade 12 National Exam (377/700) + Grade 10 EGSECE
• Academic CV          : Fuad_Ahmed_CV_France_Academic.pdf
• Language Evaluation  : English MOI Verified (No IELTS Needed) + French A1 Beginner

🎯 VERIFIED MASTER'S PROGRAMS (READY FOR PROGRAM CART):
1. [ID 61801] Université Grenoble Alpes - Master Informatique (MoSIG - M1)
   -> Fee waiver applied: ~€243/year | Eiffel eligible
2. [ID 61800] Université Grenoble Alpes - Cloud Computing & Data Infrastructures (M2)
   -> Fee waiver applied: ~€243/year | IdEx research stipend
3. [ID 60987] Université de Lille - Master Informatique (parcours Computer Sciences M1)
   -> Fee waiver applied: ~€243/year | Top northern France cluster
4. [ID 60589] CentraleSupélec / Université Paris-Saclay - MSc in Artificial Intelligence
   -> Eiffel Excellence Scholarship candidate: €1,181/mo + full fee waiver + airfare

🔔 ACTIVE INTAKE REMINDER:
• The portal returned: 'Submission out of period for process Autres (01/10/2025 - 01/03/2026)'.
• Campus France central administration is currently updating the 2026/2027 calendar dates.
• REMINDER: Check the portal every Monday & Friday to submit the 4 target programs as soon as unlocked!
====================================================================================
""")

def cmd_profile(args):
    data = load_data()
    app = data.get("applicant", {})
    print("""
👤 APPLICANT MASTER PROFILE (FUAD AHMED)
====================================================================================
• Full Legal Name : TUBA, FUAD AHMED
• Date of Birth   : 16/02/1999 (Adama, Ethiopia)
• Nationality     : Ethiopian
• Passport No.    : E00340202 (Valid to 15/04/2036)
• Email           : fuadahmedt@gmail.com
• Phone / WhatsApp: +251 925 278 350
• Location        : Addis Ababa, Ethiopia
• Degree          : BSc in Computer Science, St. Mary's University (Grad. Aug 2022)
• Cumulative GPA  : 3.20 / 4.00 (Major GPA: 3.20, ~80% equivalent)
• English Status  : Medium of Instruction (MOI) Verified -> 100% EXEMPT FROM IELTS
• Active Passports: ET26-00453 (France EEF), 396112 (Russia Open Doors)
====================================================================================
""")

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
  python track.py show <id>        # View full dossier for an ID (e.g. `python track.py show france-campus-france`)
  python track.py deadlines        # Chronological deadline countdown queue
  python track.py france           # France EEF credentials, target program IDs & cart reminder
  python track.py china            # Check China CSC professor outreach status & follow-up dates
  python track.py profile          # Display Fuad's complete candidate profile & credentials
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
    elif cmd in ("france", "eef", "campusfrance"):
        cmd_france(args)
    elif cmd in ("profile", "me", "whoami"):
        cmd_profile(args)
    elif cmd == "update":
        cmd_update(args)
    else:
        cmd_help()

if __name__ == "__main__":
    main()
