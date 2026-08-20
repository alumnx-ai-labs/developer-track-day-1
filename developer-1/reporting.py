"""Legacy sales/analytics reporting helpers. Unrelated to the leave request API."""
from datetime import date


def summarize_sales(records: list[dict]) -> dict:
    total = sum(r.get("amount", 0) for r in records)
    return {"total": total, "count": len(records)}


def format_report_header(report_name: str, generated_on: date) -> str:
    return f"=== {report_name} (generated {generated_on.isoformat()}) ==="
