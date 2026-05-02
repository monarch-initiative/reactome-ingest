"""Upstream source version fetcher for reactome-ingest.

Reactome publishes its current release version at the ContentService
endpoint /data/database/version (returns just the version number as
plain text, e.g. "96").
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import requests

from kozahub_metadata_schema import (
    now_iso,
    urls_from_download_yaml,
)


INGEST_DIR = Path(__file__).resolve().parents[1]
DOWNLOAD_YAML = INGEST_DIR / "download.yaml"


def _reactome_version() -> tuple[str, str]:
    try:
        r = requests.get(
            "https://reactome.org/ContentService/data/database/version",
            timeout=10,
        )
        r.raise_for_status()
        return r.text.strip(), "reactome_content_service"
    except Exception:
        return "unknown", "unavailable"


def get_source_versions() -> list[dict[str, Any]]:
    ver, method = _reactome_version()
    return [
        {
            "id": "infores:reactome",
            "name": "Reactome",
            "urls": urls_from_download_yaml(DOWNLOAD_YAML),
            "version": ver,
            "version_method": method,
            "retrieved_at": now_iso(),
        }
    ]
