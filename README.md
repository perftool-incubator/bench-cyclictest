# bench-cyclictest
[![CI Actions Status](https://github.com/perftool-incubator/bench-cyclictest/workflows/crucible-ci/badge.svg)](https://github.com/perftool-incubator/bench-cyclictest/actions)

Scripts and configuration to run the [cyclictest](https://wiki.linuxfoundation.org/realtime/documentation/howto/tools/cyclictest/start) real-time latency benchmark within the [crucible](https://github.com/perftool-incubator/crucible) performance testing framework.

## Key Files

| File | Purpose |
|------|---------|
| `rickshaw.json` | Rickshaw integration: defines client/server scripts, parameter transformations |
| `cyclictest-base` | Base setup shared by client and server |
| `cyclictest-client` | Client execution script |
| `cyclictest-server-start` / `cyclictest-server-stop` | Server lifecycle scripts |
| `cyclictest-runtime` | Runtime extraction |
| `cyclictest-post-process` | Post-processing: parses cyclictest output into crucible metrics |
| `workshop.json` | Engine image build: compiles rt-tests from source |
