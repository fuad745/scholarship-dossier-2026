# 🤖 Antigravity CLI (`agy`) System & Agent Instructions (PC & Termux Mobile)

> **PURPOSE:** This file is automatically read by the Antigravity CLI (`agy`) when launching in this repository on either PC (Linux) or Mobile Phone (Android via Termux).  
> It defines the applicant identity, operational protocols, current progress state, and synchronization workflows.

---

## 👤 1. Applicant Profile (Never Ask Fuad for These Basics)

When completing forms, drafting motivation letters, compiling application packages, or replying to professors, use the verified information in [APPLICANT_DOSSIER.md](file:///home/kichner/Desktop/stuff/docs/APPLICANT_DOSSIER.md):
* **Full Legal Name:** `TUBA, FUAD AHMED` (First: Fuad, Father: Ahmed, Grandfather: Tuba)
* **Date of Birth:** `16/02/1999` (Adama, Ethiopia) | **Nationality:** Ethiopian
* **Passport Number:** `E00340202` (Expires: `15/04/2036`) | **Authority:** ICS Ethiopia
* **Contact:** `fuadahmedt@gmail.com` | Phone / WhatsApp: `+251 925 278 350`
* **Undergraduate Degree:** BSc Computer Science, St. Mary's University, Addis Ababa (Graduated Aug 2022)
* **Major GPA:** `3.20 / 4.00` (~80% academic equivalent)
* **Language Exemption:** St. Mary's University official **English Medium of Instruction (MOI)** Certificate. **Zero IELTS / TOEFL is required** for Italy DSU, China CSC, France EEF, Russia Open Doors, Hungary Stipendium, or Canada UMGF.
* **Specialization:** Distributed Systems, High-Concurrency Backend Architecture, Cloud & Edge Infrastructure.

---

## 🧭 2. Real-Time State & "Where We Stopped"

Before executing any task, check [CURRENT_STATUS.md](file:///home/kichner/Desktop/stuff/docs/CURRENT_STATUS.md):
1. **France (Études en France):**
   * Candidate ID: **`ET26-00453`** | Password: `FuadFrance2027!#`
   * Profile is **100% COMPLETED** (Identity, 3-page BSc degree, Grade 12, CV, Languages).
   * 4 Target programs verified: `61801` (UGA MoSIG), `61800` (UGA Cloud M2), `60987` (Lille M1), `60589` (CentraleSupélec AI).
   * Program cart intake is currently locked by ministry ("out of period"). **Action:** Monitor intake opening twice weekly.
2. **China (CSC Type B):**
   * 6 professors contacted at HIT, BIT, USTC.
   * Follow-up dates: **October 12 & 13, 2026**.
3. **Russia (Open Doors):**
   * Portfolio **submitted with verified 93/100 points**. Stage 1 results due mid-November 2026.
4. **Italy (Politecnico di Milano & UNIPD):**
   * Polimi Round 1 closes **November 15, 2026**. UNIPD opens **November 2, 2026**.

---

## ⚡ 3. Autonomous Execution Rules for `agy`

1. **Be Fully Autonomous:**  
   The user explicitly directed: *"dont ask me everytime tell me when u finish u know everything about me"*. Do not ask trivial questions or request approval for standard data entries. Execute tasks end-to-end and report when done.
2. **Multi-Page Document Verification:**  
   Always check multi-page files before uploading or referencing:
   * Bachelor's degree and transcripts must be uploaded as the complete 3-page PDF:  
     `01_Master_Application_Dossier/Fuad Education Documents.pdf` or  
     `08_France_Campus_France_and_Eiffel_2027/Fuad_Ahmed_BSc_Degree_Complete_3Pages.pdf`.
   * High school certificates must be the combined Grade 10 & 12 PDF:  
     `08_France_Campus_France_and_Eiffel_2027/Fuad_Ahmed_High_School_Certificates.pdf`.
3. **Maintain Repository Synchronization:**  
   Whenever you modify application statuses, add documents, or update dossiers:
   * Update [applications.json](file:///home/kichner/Desktop/stuff/docs/applications.json)
   * Update [APPLICATIONS.md](file:///home/kichner/Desktop/stuff/docs/APPLICATIONS.md)
   * Update [CURRENT_STATUS.md](file:///home/kichner/Desktop/stuff/docs/CURRENT_STATUS.md)
   * Run `./sync.sh "<descriptive commit message>"` to commit and push cleanly to GitHub.

---

## 🔄 4. Synchronizing Between PC and Termux Mobile

* `sync.sh` automatically performs a `git pull --rebase origin main` before committing and pushing.
* If working on phone in Termux:
  ```bash
  ./sync.sh "Update from Termux mobile"
  ```
* If working on PC:
  ```bash
  ./sync.sh "Update from Linux PC"
  ```
* This guarantees that neither PC nor mobile will ever suffer from merge conflicts or out-of-sync states.

---

## 📱 5. Terminal CLI Quick Commands (Zero Dependencies)

Fuad or `agy` can run these in Termux or PC at any time:
```bash
python track.py list             # View all tracked programs and current statuses
python track.py show <id>        # View full dossier (e.g. `python track.py show france-campus-france`)
python track.py deadlines        # Chronological queue of upcoming deadlines
python track.py china            # China CSC professor outreach status & follow-up dates
python track.py france           # France EEF credentials, target program IDs, and reminder
python track.py profile          # Display Fuad's complete candidate profile
python track.py update <id> <st> # Update application status (e.g. `python track.py update italy-polimi APPLIED`)
```
