"""Expanded redaction for zero-trust."""
import re

SECRET_PATTERNS = [
    re.compile(r"(?i)(private[_ ]?key|seed|mnemonic|bip39|wif|pem|aws[_ ]?key|github[_ ]?pat)"),
    re.compile(r"[1-9A-HJ-NP-Za-km-z]{32,44}"),  # Solana-style
    # Add more as needed
]

def redact(text: str) -> str:
    for pat in SECRET_PATTERNS:
        text = pat.sub("[REDACTED]", text)
    return text
