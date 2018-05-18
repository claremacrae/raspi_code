#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

# Based on https://makezine.com/projects/send-ticket-isp-when-your-internet-drops/

sudo pip install speedtest-cli

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $script_dir
extras_dir=speedtest-cli-extras
if [ ! -d "$extras_dir" ]; then
    echo Creating $extras_dir
    git clone https://github.com/HenrikBengtsson/speedtest-cli-extras.git
fi