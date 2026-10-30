def test_version():
    from crypto_intel import __version__
    assert __version__ == "0.50.0"

def test_redact():
    from crypto_intel.security.redact import redact
    assert "[REDACTED]" in redact("my private key is abc")
