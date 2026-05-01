# scitex-datetime

<!-- scitex-badges:start -->
[![PyPI](https://img.shields.io/pypi/v/scitex-datetime.svg)](https://pypi.org/project/scitex-datetime/)
[![Python](https://img.shields.io/pypi/pyversions/scitex-datetime.svg)](https://pypi.org/project/scitex-datetime/)
[![Tests](https://github.com/ywatanabe1989/scitex-datetime/actions/workflows/test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-datetime/actions/workflows/test.yml)
[![Install Test](https://github.com/ywatanabe1989/scitex-datetime/actions/workflows/install-test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-datetime/actions/workflows/install-test.yml)
[![Coverage](https://codecov.io/gh/ywatanabe1989/scitex-datetime/graph/badge.svg)](https://codecov.io/gh/ywatanabe1989/scitex-datetime)
[![Docs](https://readthedocs.org/projects/scitex-datetime/badge/?version=latest)](https://scitex-datetime.readthedocs.io/en/latest/)
[![License: AGPL v3](https://img.shields.io/badge/license-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
<!-- scitex-badges:end -->

<p align="center">
  <a href="https://scitex.ai">
    <img src="docs/scitex-logo-blue-cropped.png" alt="SciTeX" width="400">
  </a>
</p>

<p align="center"><b>Small datetime helpers — linspace, normalize, parse, format.</b></p>

<p align="center">
  <a href="https://scitex-datetime.readthedocs.io/">Full Documentation</a> · <code>pip install scitex-datetime</code>
</p>

---

## Installation

```bash
pip install scitex-datetime
```

## Quick Start

```python
import scitex_datetime as sxd

dt = sxd.to_datetime("2026/04/27 10:30:00")
print(sxd.format_for_filename(dt))   # "2026-04-27_103000"
```

## 1 Interfaces

<details open>
<summary><strong>Python API</strong></summary>

<br>

```python
import scitex_datetime as sxd

# Linearly spaced timestamps
sxd.linspace(start, stop, num=100)

# Parse and standardize timestamps
sxd.normalize_timestamp("2026-04-27T10:30:00")
sxd.to_datetime("2026/04/27 10:30:00")
sxd.validate_timestamp_format("2026-04-27 10:30:00")

# Format
sxd.format_for_display(dt)       # "2026-04-27 10:30:00"
sxd.format_for_filename(dt)      # "2026-04-27_103000"

# Time deltas
sxd.get_time_delta_seconds(dt1, dt2)
```

</details>

## Status

Standalone fork of `scitex.datetime`. The umbrella package's `scitex.datetime`
import path is preserved via a `sys.modules`-alias bridge. `STANDARD_FORMAT`
is read from a scitex CONFIG when available, falling back to `"%Y-%m-%d %H:%M:%S"`.

## Part of SciTeX

`scitex-datetime` is part of [**SciTeX**](https://scitex.ai). Install via
the umbrella with `pip install scitex[datetime]` to use as
`scitex.datetime` (Python) or `scitex datetime ...` (CLI).

>Four Freedoms for Research
>
>0. The freedom to **run** your research anywhere — your machine, your terms.
>1. The freedom to **study** how every step works — from raw data to final manuscript.
>2. The freedom to **redistribute** your workflows, not just your papers.
>3. The freedom to **modify** any module and share improvements with the community.
>
>AGPL-3.0 — because we believe research infrastructure deserves the same freedoms as the software it runs on.

## License

AGPL-3.0-only (see [LICENSE](./LICENSE)).

---

<p align="center">
  <a href="https://scitex.ai" target="_blank"><img src="docs/scitex-icon-navy-inverted.png" alt="SciTeX" width="40"/></a>
</p>
