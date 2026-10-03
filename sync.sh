#!/usr/bin/env bash
# One-command sync script for Scholarship & Visa Dossier
# Works on Linux PC and Termux (Android)

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

echo "🔄 [1/3] Checking Git Status..."
git status --short

echo "📦 [2/3] Staging and Committing Changes..."
git add -A
if git diff-index --quiet HEAD -- 2>/dev/null; then
    echo "✨ Nothing new to commit. Working tree is clean."
else
    COMMIT_MSG="${1:-Update application records and progress $(date '+%Y-%m-%d %H:%M')}"
    git commit -m "$COMMIT_MSG"
    echo "✅ Committed: $COMMIT_MSG"
fi

echo "🚀 [3/3] Syncing with Remote GitHub Repository..."
if git remote get-url origin >/dev/null 2>&1; then
    git pull --rebase origin main || true
    git push origin main
    echo "🎉 Successfully synchronized with GitHub!"
else
    echo "⚠️ Remote 'origin' not configured yet."
fi
