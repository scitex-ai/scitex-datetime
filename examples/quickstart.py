"""Quickstart for scitex_datetime.

Demonstrates timestamp normalisation, filename-safe formatting, and
a regular linspace between two datetimes.
"""

from datetime import datetime, timedelta

import scitex_datetime as sdt


def main() -> int:
    # Coerce heterogeneous inputs to a canonical datetime
    raw_inputs = [
        "2026-04-27 10:15:00",
        1714208400,  # unix seconds
        datetime(2026, 4, 27, 10, 15, 0),
    ]
    for x in raw_inputs:
        dt = sdt.to_datetime(x)
        print(f"  {x!r:<35} -> {dt.isoformat()}")

    now = datetime(2026, 4, 27, 14, 30, 5)
    print()
    print("display: ", sdt.format_for_display(now))
    print("filename:", sdt.format_for_filename(now))
    print("validates:", sdt.validate_timestamp_format("2026-04-27 14:30:05"))

    # Time-aware linspace: 5 evenly spaced timestamps over 1 hour
    end = now + timedelta(hours=1)
    grid = sdt.linspace(now, end, n_samples=5)
    print(f"\nlinspace ({len(grid)} points):")
    for t in grid:
        print(f"  {t}")

    # Sampling-rate variant: 4 Hz over 1 second -> 4 samples
    short = sdt.linspace(now, now + timedelta(seconds=1), sampling_rate=4.0)
    print(f"\n4 Hz, 1 s -> {len(short)} samples")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
