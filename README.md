# bench-cyclictest
[![CI Actions Status](https://github.com/perftool-incubator/bench-cyclictest/workflows/crucible-ci/badge.svg)](https://github.com/perftool-incubator/bench-cyclictest/actions)

Scripts and configuration to run the [cyclictest](https://wiki.linuxfoundation.org/realtime/documentation/howto/tools/cyclictest/start) real-time latency benchmark within the [crucible](https://github.com/perftool-incubator/crucible) performance testing framework.

## Key Files

| File | Purpose |
|------|---------|
| `rickshaw.json` | Rickshaw integration: defines client/server scripts, parameter transformations |
| `multiplex.json` | Parameter validation rules, unit conversions, and presets for multiplex |
| `benchmark-metadata.json` | Machine-readable description and CDM-indexed source/type list (consumed by `crucible benchmarks list`) |
| `cyclictest-base` | Base setup shared by client and server |
| `cyclictest-client` | Client execution script |
| `cyclictest-server-start` / `cyclictest-server-stop` | Server lifecycle scripts |
| `cyclictest-runtime` | Runtime extraction |
| `cyclictest-post-process.py` | Post-processing: parses cyclictest output into crucible metrics |
| `client-workshop.json` / `server-workshop.json` | Engine image build: compiles rt-tests from source |
