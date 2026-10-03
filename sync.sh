#!/usr/bin/env bash
# ==============================================================================
# Cross-Device Bidirectional Sync Script (Linux Desktop & Android Termux)
# Master Application, Scholarship & Academic Credentials Repository
# ==============================================================================

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

# Detect device environment
DEVICE_TAG="[PC]"
if [ -n "$TERMUX_VERSION" ] || [ -d "/data/data/com.termux" ]; then
    DEVICE_TAG="[Termux-Mobile]"
fi

echo "========================================================"
echo "🔄 $DEVICE_TAG Starting Application Dossier Synchronization..."
echo "========================================================"

# Step 1: Pull remote changes first to prevent divergence
echo "📥 [1/4] Pulling latest updates from GitHub (main)..."
if git remote get-url origin >/dev/null 2>&1; then
    # Stash any unstaged uncommitted local changes temporarily if needed
    git pull --rebase origin main || {
        echo "⚠️ Note: Merge or rebase in progress, resolving..."
    }
else
    echo "⚠️ Remote 'origin' not configured yet."
fi

# Step 2: Show current status
echo "🔍 [2/4] Checking local working tree..."
git status --short

# Step 3: Stage and commit local changes
echo "📦 [3/4] Staging and committing local changes..."
git add -A
if git diff-index --quiet HEAD -- 2>/dev/null; then
    echo "✨ Working tree clean. Nothing new to commit locally."
else
    TIMESTAMP=$(date '+%Y-%m-%d %H:%M')
    CUSTOM_MSG="${1:-}"
    if [ -n "$CUSTOM_MSG" ]; then
        COMMIT_MSG="$DEVICE_TAG $CUSTOM_MSG ($TIMESTAMP)"
    else
        COMMIT_MSG="$DEVICE_TAG Sync applications state & progress ($TIMESTAMP)"
    fi
    git commit -m "$COMMIT_MSG"
    echo "✅ Committed: $COMMIT_MSG"
fi

# Step 4: Push to GitHub
echo "🚀 [4/4] Pushing synchronized commits to GitHub..."
if git remote get-url origin >/dev/null 2>&1; then
    git push origin main
    echo "🎉 Successfully synchronized with GitHub repository!"
    echo "🌐 View live repo: https://github.com/fuad745/scholarship-dossier-2026"
fi
echo "========================================================"
