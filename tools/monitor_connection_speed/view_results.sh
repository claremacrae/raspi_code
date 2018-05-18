#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

output_dir=~/speedtest_results
mkdir -p $output_dir

output_file=$output_dir/`hostname`.tsv
cat $output_file
