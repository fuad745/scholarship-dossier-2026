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

## 🔍 2. Opportunity Screening & Ingestion Protocol (MANDATORY)

Whenever Fuad gives you a link or name for a **new scholarship, fellowship, internship, apprenticeship, or work visa**:

### Step 1: Scan & Inspect Link
* Use `/browser` or `read_url_content` to inspect the program page, guidelines, eligibility criteria, and fee schedule.

### Step 2: Perform Comprehensive Suitability Audit against Fuad's Profile
You **must** evaluate and report these 5 criteria before starting any application:
1. **Language Requirement:**  
   * Does the university accept an **English Medium of Instruction (MOI)** letter from St. Mary's University?
   * Or does it strictly require an IELTS / TOEFL / Duolingo certificate?
2. **Financials & Fees:**  
   * Is there an application fee (e.g. €50, $100)?
   * Is it a 100% full-ride scholarship (Tuition + Housing + Monthly Stipend), a partial tuition waiver, or self-funded?
3. **Academic & Degree Match:**  
   * Does it accept a 4-year BSc in Computer Science with a **3.20 GPA**?
4. **Nationality / Citizenship Eligibility:**  
   * Is it open to **Ethiopian / Non-EU nationals**? Are there specific national quotas?
5. **Mandatory Documentation Requirements:**  
   * What exact documents are required? (e.g., Police Clearance / Non-Criminal Record, Foreigner Physical Medical Exam, Supervisor Acceptance Letter, Financial Affidavits).

### Step 3: Present Suitability Verdict & Wait for Confirmation
Report a concise audit summary to Fuad with a clear verdict:
* **`🟢 RECOMMENDED (NO IELTS / FULL RIDE)`** — Meets all criteria, 100% MOI accepted, full funding.
* **`🟡 CONDITIONAL (NEEDS IELTS OR SUPERVISOR)`** — Great opportunity, but requires taking IELTS or securing professor consent first.
* **`🔴 NOT RECOMMENDED / INELIGIBLE`** — Strict IELTS requirement without waiver, exorbitant fees, or GPA threshold above 3.50.

### Step 4: Ingestion into Repository & Website Tracker
Once Fuad confirms (*"Yes, apply"* or *"Yes, add to tracker"*):
1. Add the opportunity to [applications.json](file:///home/kichner/Desktop/stuff/docs/applications.json) and [index.html](file:///home/kichner/Desktop/stuff/docs/index.html).
2. Configure its **scholarship-specific document checklist** (e.g. including Police Clearance and Hospital Medical Report for China, or ISEE Parificato for Italy).
3. If an account is created by `agy`, record the login credentials under `credentials` with `created_by: "AI Agent"`.
4. Set initial status (`NOT_STARTED` or `STARTED`).
5. Run `./sync.sh "Add new opportunity: <Name>"` to commit and push.

---

## 🔑 3. Portal Account Creation & Credential Logging Rule

Whenever `agy` creates an account on any university, government, or scholarship portal:
1. Always use Fuad's primary email: `fuadahmedt@gmail.com`.
2. Generate or use a strong, compliant password (e.g. `FuadFrance2027!#` or standard secure scheme).
3. Record the credentials in `applications.json` and `index.html`:
   ```json
   "credentials": {
     "created_by": "AI Agent",
     "email": "fuadahmedt@gmail.com",
     "username": "<Candidate ID or Username>",
     "password": "<Password>",
     "portal_url": "<Login URL>"
   }
   ```
4. This ensures Fuad can view, copy, or use the credentials at any time on the website card.
5. If Fuad created the account himself, provide the interactive `🔑 Add Login Credentials` option on the card.

---

## ⚡ 4. Autonomous Execution Rules for `agy`

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
   * Update `applications.json`, `APPLICATIONS.md`, `CURRENT_STATUS.md`, and `index.html`.
   * Run `./sync.sh "<descriptive commit message>"` to commit and push cleanly to GitHub.

---

## 🔄 5. Synchronizing Between PC and Termux Mobile

* `sync.sh` automatically performs a commit, then `git pull --rebase origin main`, and pushes.
* If working on phone in Termux:
  ```bash
  ./sync.sh "Update from Termux mobile"
  ```
* If working on PC:
  ```bash
  ./sync.sh "Update from Linux PC"
  ```

---

## 📱 6. Terminal CLI Quick Commands (Zero Dependencies)

```bash
python track.py list             # View all tracked programs and current statuses
python track.py show <id>        # View full dossier (e.g. `python track.py show france-campus-france`)
python track.py deadlines        # Chronological queue of upcoming deadlines
python track.py china            # China CSC professor outreach status & follow-up dates
python track.py france           # France EEF credentials, target program IDs & cart reminder
python track.py profile          # Display Fuad's complete candidate profile & credentials
python track.py update <id> <st> # Update application status
```
