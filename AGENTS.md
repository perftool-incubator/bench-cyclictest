# Bench-Cyclictest

## Purpose
Scripts and configuration to run the cyclictest real-time latency benchmark within the crucible framework. Measures scheduling latency by running periodic timer threads and recording wakeup delays.

## Language
- Bash for benchmark execution scripts
- Python for post-processing (`cyclictest-post-process.py`)

## Key Files
| File | Purpose |
|------|---------|
| `rickshaw.json` | Rickshaw integration: client/server scripts, parameter transformations |
| `multiplex.json` | Parameter validation rules, unit conversions, and presets for multiplex |
| `benchmark-metadata.json` | Machine-readable description and CDM-indexed source/type list (consumed by `crucible benchmarks list`) |
| `cyclictest-base` | Base setup shared by client and server scripts |
| `cyclictest-client` | Client-side benchmark execution |
| `cyclictest-server-start` / `cyclictest-server-stop` | Server lifecycle management |
| `cyclictest-runtime` | Extracts runtime from command-line options |
| `cyclictest-post-process.py` | Parses cyclictest output into crucible metrics |
| `client-workshop.json` / `server-workshop.json` | Engine image build: compiles rt-tests from source |
| `rt-tests-sched-headers.patch` | Patch applied to rt-tests source during build |

## Conventions
- Primary branch is `main`
- Standard Bash modelines and 4-space indentation
- Python code follows 4-space indentation with standard modelines
