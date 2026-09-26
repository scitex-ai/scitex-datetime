# scitex-datetime

<p align="center">
  <a href="https://scitex.ai">
    <img src="docs/scitex-logo-blue-cropped.png" alt="SciTeX" width="400">
  </a>
</p>

<p align="center"><b>Small datetime helpers — linspace, normalize, parse, format.</b></p>

<p align="center">
  <a href="https://scitex-datetime.readthedocs.io/">Full Documentation</a> · <code>uv pip install scitex-datetime[all]</code>
</p>

<!-- scitex-badges:start -->
<p align="center">
  <a href="https://pypi.org/project/scitex-datetime/"><img src="https://img.shields.io/pypi/v/scitex-datetime?label=pypi" alt="pypi"></a>
  <a href="https://pypi.org/project/scitex-datetime/"><img src="https://img.shields.io/pypi/pyversions/scitex-datetime?label=python" alt="python"></a>
  <a href="https://github.com/scitex-ai/scitex-datetime/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/scitex-ai/scitex-datetime/ci.yml?branch=develop&label=docs" alt="docs"></a>
  <a href="https://scitex-datetime.readthedocs.io/en/latest/"><img src="https://img.shields.io/readthedocs/scitex-datetime?label=docs" alt="docs-rtd"></a>
</p>
<p align="center">
  <a href="https://github.com/scitex-ai/scitex-datetime/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/scitex-ai/scitex-datetime/ci.yml?branch=develop&label=tests" alt="tests"></a>
  <a href="https://github.com/scitex-ai/scitex-datetime/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/scitex-ai/scitex-datetime/ci.yml?branch=develop&label=install-check" alt="install-check"></a>
  <a href="https://codecov.io/gh/scitex-ai/scitex-datetime"><img src="https://img.shields.io/codecov/c/github/scitex-ai/scitex-datetime/develop?label=cov" alt="cov"></a>
</p>
<!-- scitex-badges:end -->

---

## Quick Start

```python
import scitex_datetime as sxd

dt = sxd.to_datetime("2026/04/27 10:30:00")
print(sxd.format_for_filename(dt))   # "2026-04-27_103000"
```

## Demo

```mermaid
flowchart LR
    S1["'2026/04/27 10:30:00'"] --> P["sxd.to_datetime()"]
    S2["'2026-04-27T10:30:00'"] --> N["sxd.normalize_timestamp()"]
    P --> D["datetime"]
    N --> D
    D --> F["sxd.format_for_filename()<br/>→ '2026-04-27_103000'"]
    A["start, stop"] --> L["sxd.linspace(num=100)"]
    L --> R["[datetime, ...]"]
```

<p align="center"><sub><b>Figure 1.</b> Demo path. Parse and normalize converge on datetimes, then format for filenames; linspace covers ranges.</sub></p>

## Installation

```bash
uv pip install "scitex-datetime[all]"
```

<details>
<summary><b>Per-module extras</b></summary>

<br>

| Extra | Pulls in |
|---|---|
| `all` | scitex-io + `dev` (recommended) |
| `dev` | pytest, pytest-cov, ruff, Sphinx (maintainer tooling) |

```bash
uv pip install -e ".[dev]"               # editable install for contributors
```

</details>
## Architecture

```mermaid
flowchart LR
    Raw[heterogeneous strings] --> Parse[to_datetime / normalize_timestamp]
    Parse --> Std[standardized datetime]
    Std --> Display[format_for_display]
    Std --> File[format_for_filename]
    Range[start, stop] --> Lin[linspace]
    Lin --> Arr[[datetime, ...]]
```

<p align="center"><sub><b>Figure 2.</b> Helper flow. Raw strings parse to standard datetimes for display or filenames; linspace builds uniform arrays.</sub></p>

Pure-stdlib datetime helpers; the umbrella `scitex.datetime` import path
is preserved via a `sys.modules`-alias bridge.

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
