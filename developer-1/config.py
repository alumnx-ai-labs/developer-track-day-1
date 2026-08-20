"""Stale config from an old email/notifications feature. Not wired into main.py."""

SMTP_HOST = "smtp.old-mail-provider.example.com"
SMTP_PORT = 587
NOTIFICATIONS_ENABLED = False
FEATURE_FLAGS = {
    "legacy_export": True,
    "beta_dashboard": False,
}
