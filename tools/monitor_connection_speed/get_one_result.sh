#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
. $script_dir/config.sh

mkdir -p $output_dir

echo Sending output to $output_file

# Write headers to output file, if it does not yet exist
if [[ ! -f $output_file ]] ; then
    echo Creating $output_file
    $script_dir/speedtest-cli-extras/bin/speedtest-csv --header > $output_file
fi

$script_dir/speedtest-cli-extras/bin/speedtest-csv --no-share >> $output_file

