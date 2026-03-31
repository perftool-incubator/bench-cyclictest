# Bench-Cyclictest

## Purpose
Scripts and configuration to run the cyclictest real-time latency benchmark within the crucible framework. Measures scheduling latency by running periodic timer threads and recording wakeup delays.

## Language
Bash — all scripts

## Key Files
| File | Purpose |
|------|---------|
| `rickshaw.json` | Rickshaw integration: client/server scripts, parameter transformations |
| `cyclictest-base` | Base setup shared by client and server scripts |
| `cyclictest-client` | Client-side benchmark execution |
| `cyclictest-server-start` / `cyclictest-server-stop` | Server lifecycle management |
| `cyclictest-runtime` | Extracts runtime from command-line options |
| `cyclictest-post-process` | Parses cyclictest output into crucible metrics |
| `workshop.json` | Engine image build: compiles rt-tests from source |
| `rt-tests-sched-headers.patch` | Patch applied to rt-tests source during build |

## Conventions
- Primary branch is `main`
- Standard Bash modelines and 4-space indentation
