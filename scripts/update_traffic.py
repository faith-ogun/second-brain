#!/usr/bin/env python3
"""Snapshot GitHub traffic (views + clones) into .stats/ so it can be badged.

Why this exists: GitHub only keeps the last 14 days of traffic, and the numbers
are private (push access only). This script is run daily by a GitHub Action, using
a token that can read traffic. It merges each day's snapshot into a rolling history
file so the record survives past 14 days, then writes small shields.io endpoint
JSONs the README badges point at.

Stdlib only, no dependencies. British English, no em dashes.
"""

import json
import os
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO = os.environ.get("GITHUB_REPOSITORY", "faith-ogun/second-brain")
TOKEN = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
STATS = Path(__file__).resolve().parent.parent / ".stats"
HISTORY = STATS / "history.json"

BLUE = "1f6feb"
GREEN = "2ea043"


def api(path: str) -> dict:
    """GET a GitHub API path and return parsed JSON."""
    if not TOKEN:
        sys.exit("No token. Set GH_TOKEN (a PAT with traffic access) in the environment.")
    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/{path}",
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "second-brain-traffic-badge",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def merge(series: dict, rows: list, key: str) -> None:
    """Merge per-day rows into the rolling history, keyed by date.

    The API is authoritative for the days it reports (the last 14), so we
    overwrite those and keep everything older that has already rolled off.
    """
    for row in rows:
        day = row["timestamp"][:10]
        series[day] = {"count": row["count"], "uniques": row["uniques"]}


def badge(name: str, label: str, message, colour: str) -> None:
    (STATS / name).write_text(
        json.dumps(
            {"schemaVersion": 1, "label": label, "message": str(message), "color": colour},
            indent=2,
        )
        + "\n"
    )


def main() -> None:
    STATS.mkdir(exist_ok=True)
    hist = {"views": {}, "clones": {}}
    if HISTORY.exists():
        loaded = json.loads(HISTORY.read_text())
        hist["views"] = loaded.get("views", {})
        hist["clones"] = loaded.get("clones", {})

    views = api("traffic/views")
    clones = api("traffic/clones")
    merge(hist["views"], views.get("views", []), "views")
    merge(hist["clones"], clones.get("clones", []), "clones")

    # All-time totals are the sum of daily counts we have ever stored. Tracking began
    # at repo creation, so this is genuinely all-time, and it only ever grows.
    # (GitHub only exposes UNIQUE visitors/cloners as a rolling 14-day figure, so an
    # all-time unique-people count is not derivable; total views/clones is.)
    views_total = sum(d["count"] for d in hist["views"].values())
    clones_total = sum(d["count"] for d in hist["clones"].values())
    tracking_since = min(hist["views"], default="")  # earliest date on record

    HISTORY.write_text(
        json.dumps(
            {
                "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "tracking_since": tracking_since,
                "views": dict(sorted(hist["views"].items())),
                "clones": dict(sorted(hist["clones"].items())),
            },
            indent=2,
        )
        + "\n"
    )

    badge("views-badge.json", "all-time views", views_total, BLUE)
    badge("clones-badge.json", "all-time clones", clones_total, GREEN)

    print(f"views_total={views_total} clones_total={clones_total} since={tracking_since}")


if __name__ == "__main__":
    main()
