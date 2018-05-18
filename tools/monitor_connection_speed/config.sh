#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

output_dir=~/speedtest_results
output_file=$output_dir/`hostname`.tsv
extras_dir=speedtest-cli-extras

