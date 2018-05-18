#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
. $script_dir/config.sh

echo "Results file: $output_file"
cat $output_file
