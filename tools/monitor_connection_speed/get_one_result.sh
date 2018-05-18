#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

output_dir=~/speedtest_results
mkdir -p $output_dir

output_file=$output_dir/`hostname`.tsv
echo Sending output to $output_file

# Write headers to output file, if it does not yet exist
if [[ ! -f $output_file ]] ; then
    echo Creating $output_file
    ./speedtest-cli-extras/bin/speedtest-csv --header > $output_file
fi

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
$script_dir/speedtest-cli-extras/bin/speedtest-csv --no-share >> $output_file

cat $output_file
