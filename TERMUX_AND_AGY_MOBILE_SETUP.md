# 📱 Complete Termux (Rooted Android) + Antigravity CLI (`agy`) Mobile Setup Guide

This guide walks you through setting up **Termux** on your Android phone so you can run the **Antigravity CLI (`agy`)**, track your applications, and edit or advance your dossiers on the go with full AI pairing.

---

## ⚡ Why This System is 10x Better Than Excel on Mobile

| Feature | Excel on Mobile (`.xlsx`) | Git + Markdown + JSON + `agy` in Termux |
| :--- | :--- | :--- |
| **Mobile UX** | Tiny pinch-to-zoom cells, slow app loading | Fast terminal UI, instant text rendering, native CLI commands |
| **AI Integration** | Cannot interact naturally with LLMs | `agy cli` reads entire repository context and writes updates automatically |
| **Syncing** | Cloud conflicts, locked files, OneDrive/Google Drive sync errors | Standard `git push` & `git pull` with exact commit history |
| **Offline Access** | Slow or requires cloud login | 100% offline access to all dossiers, SOPs, CVs, and scripts |
| **Automation** | Complex VBA macros that break on Android | Zero-dependency Python CLI (`python track.py list`) |

---

## 🛠️ Step 1: Install & Set Up Termux on Android

1. **Install Termux:**  
   Always install Termux from **F-Droid** (or GitHub releases), **NOT** the deprecated Google Play Store version.  
   Download link: [F-Droid Termux](https://f-droid.org/packages/com.termux/)

2. **Open Termux and update base packages:**
   ```bash
   pkg update && pkg upgrade -y
   ```

3. **Grant storage access:**
   ```bash
   termux-setup-storage
   ```
   *(Tap "Allow" when the Android prompt appears).*

4. **Install essential developer tools (Git, Python, Node.js, OpenSSH, Curl, JQ):**
   ```bash
   pkg install git python nodejs openssh curl jq gh -y
   ```

---

## 🚀 Step 2: Install Antigravity CLI (`agy`) on Termux

Because your phone is rooted and running standard Linux binaries inside Termux:

1. **Install `antigravity-cli` via npm:**
   ```bash
   npm install -g @google/antigravity-cli
   ```
   *(Or if using the standalone release binary, put `agy` in `$PREFIX/bin`).*

2. **Verify installation:**
   ```bash
   agy --version
   ```

3. **Authenticate `agy` on mobile:**
   ```bash
   agy
   ```
   *(Follow the one-time browser login prompt to link your Google account).*

---

## 🔄 Step 3: Clone Your Applications Repository in Termux

1. **Configure Git on your phone:**
   ```bash
   git config --global user.name "fuad"
   git config --global user.email "fuadahmed745@gmail.com"
   ```

2. **Authenticate GitHub in Termux:**
   ```bash
   gh auth login
   ```
   * Select `GitHub.com` -> `HTTPS` -> Log in with a web browser.
   * Or generate a GitHub Personal Access Token (PAT) with `repo` scope and paste it.

3. **Clone your scholarship workspace:**
   ```bash
   cd ~
   git clone https://github.com/fuad745/scholarship-dossier-2026.git
   cd scholarship-dossier-2026
   ```

---

## 🎯 Step 4: How to Use `agy` on Your Phone with Full Context

Whenever you launch `agy` inside the cloned directory:
```bash
cd ~/scholarship-dossier-2026
agy
```

**`agy` will immediately read:**
- `APPLICATIONS.md` (Master tracker with all 14 universities, deadlines, intakes, and statuses).
- `applications.json` (Structured single source of truth database).
- `SESSION_STATE_AND_NEXT_STEPS_OCT_2026.md` (Full context of what was done, contacted professors, and scores).
- All your CVs, SOPs, recommendation letters, and guides.

### Example Prompts You Can Give to `agy` on Mobile:
* *"I just got an email back from Prof. Song Yang at BIT agreeing to supervise me. Update our tracker and draft a formal thank-you email with the Provisional Acceptance Letter (PAL)."*
* *"What is my next immediate deadline this month?"*
* *"Show me the Italian DSU universities that accept my St. Mary's MOI letter and their ranking."*
* *"Commit our latest updates and push to GitHub."*

---

## ⌨️ Step 5: Quick Terminal Commands on Your Phone

You can also use the custom zero-dependency CLI tracker directly without even launching AI:

```bash
# List all tracked programs
python track.py list

# Chronological countdown of deadlines
python track.py deadlines

# Check the China CSC professor outreach status
python track.py china

# View full details of a specific university
python track.py show italy-trento

# Update status when you submit
python track.py update italy-trento SUBMITTED

# Sync with PC (commit & push)
git add .
git commit -m "Update from mobile"
git push
```
