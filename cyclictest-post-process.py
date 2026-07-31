#!/usr/bin/env python3
# -*- mode: python; indent-tabs-mode: nil; python-indent-level: 4 -*-
# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4 filetype=python

import argparse
import json
import os
import sys
from pathlib import Path

TOOLBOX_HOME = os.environ.get("TOOLBOX_HOME")
if TOOLBOX_HOME:
    sys.path.append(str(Path(TOOLBOX_HOME) / "python"))

from toolbox.cdm_metrics import CDMMetrics


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--duration", default=None)
    parser.add_argument("--policy", default=None)
    parser.add_argument("--interval", type=int, default=None)
    parser.add_argument("--smt", default=None)
    parser.parse_known_args()

    primary_metric = "wakeup-latency-usec"

    if not (os.path.exists("begin.txt") and os.path.exists("end.txt")):
        print("cyclictest-post-process(): could not find begin.txt and/or end.txt")
        print("Is the current directory for the cyclictest server (no result file)?")
        return

    times = {}
    for name in ("begin", "end"):
        with open(f"{name}.txt") as f:
            times[name] = int(float(f.read().strip()) * 1000)

    result_file = "histogram.txt"
    if not os.path.exists(result_file):
        return

    metrics = CDMMetrics()
    metric_data_name = None

    with open(result_file) as f:
        for line in f:
            match = line.strip()
            if match.startswith("# Max Latencies:"):
                latencies = match.split(":", 1)[1].split()
                system_max_latency = int(latencies[-1])
                desc = {"source": "cyclictest", "type": primary_metric, "class": "latency", "default-aggregation": "max"}
                sample = {"begin": times["begin"], "end": times["end"], "value": system_max_latency}
                metrics.log_sample("0", desc, {}, sample)

    metric_data_name = metrics.finish_samples()

    if metric_data_name:
        sample_data = {
            "rickshaw-bench-metric": {"schema": {"version": "2021.04.12"}},
            "benchmark": "cyclictest",
            "primary-period": "measurement",
            "primary-metric": primary_metric,
            "periods": [
                {
                    "name": "measurement",
                    "metric-files": [metric_data_name],
                }
            ],
        }

        with open("postprocess/post-process-data.json", "w") as f:
            json.dump(sample_data, f)


if __name__ == "__main__":
    main()
