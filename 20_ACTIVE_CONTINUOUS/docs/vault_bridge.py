#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Canonical ItsAPlan SecretVault Bridge (53.ACT.288 / UC-USER-01).
Connects project secret & PII resolution directly to AgentCredentialVault
(L1 SQLite ~/.gemini/vault/agent_vault.db + L2 ItsAPlan PostgreSQL public.app_secret).
"""
from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Optional

PM_ROOT = Path(r"d:\WORK\01_PROJECTS\53_PROJECT_MANAGEMENT")
if str(PM_ROOT) not in sys.path:
    sys.path.insert(0, str(PM_ROOT))

from agentic_os.vault import SecretVaultManager
from scripts.agent_credential_vault import (
    AgentCredentialVault,
    get_global_vault,
    get_vault_secret,
    inject_vault_env,
    resolve_vault_uri,
)


def get_project_secret(key: str, default: Optional[str] = None, required: bool = False) -> Optional[str]:
    """Resolves a secret or vault://itsaplan/<KEY> pointer from ItsAPlan SecretVault."""
    val = get_vault_secret(key, default=default, required=required)
    if isinstance(val, str) and val.startswith("vault://itsaplan/"):
        return resolve_vault_uri(val) or default
    return val


__all__ = [
    "AgentCredentialVault",
    "SecretVaultManager",
    "get_global_vault",
    "get_project_secret",
    "get_vault_secret",
    "inject_vault_env",
    "resolve_vault_uri",
]
