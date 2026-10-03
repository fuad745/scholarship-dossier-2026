# 📱 Autonomous Setup Prompt for `agy cli` in Android Termux (Rooted)
## Background Non-Headless Virtual Browser Automation System

> **Instructions for Fuad:**  
> Copy the text block below inside the triple backticks and paste it directly into `agy cli` inside Termux on your rooted phone. `agy cli` will execute the entire setup autonomously end-to-end.

---

```text
You are running inside Termux on a rooted Android device. Your mission is to configure a complete, bulletproof, background non-headless browser automation environment for yourself (agy cli) so that you can autonomously navigate websites, fill scholarship application forms, and bypass anti-bot protections without disturbing the user or showing up on the phone screen.

Execute the following setup steps autonomously:

### Step 1: Package Repositories & Tooling Installation
Run the following package manager commands non-interactively:
1. Update packages: `pkg update -y`
2. Enable X11 and TUR repos: `pkg install -y x11-repo tur-repo`
3. Install required software: `pkg install -y xorg-server-xvfb chromium tmux tsu termux-tools x11vnc procps net-tools`

### Step 2: Create the Persistent Virtual Browser Environment Script
Write an executable script to `~/start-virtual-browser.sh` with the following implementation:
```bash
#!/data/data/com.termux/files/usr/bin/bash
set -e

# 1. Acquire wake lock to keep CPU active when phone screen is off
termux-wake-lock 2>/dev/null || true

# 2. Clean up any previous dead displays
killall Xvfb chromium x11vnc 2>/dev/null || true
rm -f /tmp/.X99-lock /tmp/.X11-unix/X99 2>/dev/null || true

# 3. Create invisible 1080p Virtual Framebuffer Desktop on :99
echo "🖥️ Starting invisible Virtual Desktop on DISPLAY=:99..."
Xvfb :99 -screen 0 1920x1080x24 -ac +extension GLX +render -noreset >/dev/null 2>&1 &
export DISPLAY=:99
sleep 2

# 4. Launch Desktop Chromium inside the virtual screen
echo "🌐 Launching full Chromium desktop engine in background..."
chromium \
  --display=:99 \
  --no-sandbox \
  --disable-dev-shm-usage \
  --disable-gpu \
  --disable-software-rasterizer \
  --window-size=1920,1080 \
  --remote-debugging-port=9222 \
  --user-data-dir="$HOME/.config/chromium-agy" \
  about:blank >/dev/null 2>&1 &

sleep 3

# 5. Optional local VNC server (localhost only, for optional peek/CAPTCHA solving)
x11vnc -display :99 -forever -nopw -listen localhost -bg >/dev/null 2>&1 || true

echo "✅ Background Virtual Browser active on DISPLAY=:99 (CDP Port: 9222)!"
```
Make it executable: `chmod +x ~/start-virtual-browser.sh`

### Step 3: Apply Root Immunity (Anti-LMK & Anti-Phantom Killer)
Using `su` / `tsu`, configure Android kernel parameters so that Termux and Chromium are completely immune to Android's low memory killer (LMK) and background app termination:
1. Set `oom_score_adj` of Termux processes to `-1000` (highest kernel priority, never killed):
   `su -c "for p in $(pgrep -f com.termux); do echo -1000 > /proc/\$p/oom_score_adj 2>/dev/null || true; done"`
2. Disable Android 12+ Phantom Process Killer:
   `su -c "device_config put activity_manager max_phantom_processes 2147483647 2>/dev/null || true"`
   `su -c "setprop persist.sys.fflag.override.settings_enable_monitor_phantom_procs false 2>/dev/null || true"`

### Step 4: Environment Profile Setup
Append the following exports to `~/.bashrc` if not already present:
```bash
export DISPLAY=:99
alias vbrowser='~/start-virtual-browser.sh'
alias vstatus='ps aux | grep -E "Xvfb|chromium"'
```

### Step 5: Verification Test
1. Execute `~/start-virtual-browser.sh`.
2. Verify that `Xvfb` is running on port `:99` and `chromium` is listening on port `9222`:
   `netstat -tlpn 2>/dev/null | grep -E "9222|6099|5900" || ps aux | grep -E "Xvfb|chromium"`
3. Confirm that everything is operational and report the final status to Fuad.
```

---

### 💡 Daily Usage Instructions for Fuad Once Setup is Complete:

1. **Start a background session in Termux:**
   ```bash
   tmux new -s agy
   ```
2. **Start the silent virtual browser:**
   ```bash
   vbrowser
   ```
3. **Give `agy cli` your tasks:**
   ```bash
   agy "/browser Navigate to https://etudesenfrance.diplomatie.gouv.fr/ and check application review"
   ```
4. **Swipe away Termux:**
   Use your phone normally. Chromium and `agy cli` will continue clicking, filling forms, and compiling dossiers in the virtual background.
