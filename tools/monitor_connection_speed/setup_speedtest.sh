#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
. $script_dir/config.sh

# Based on https://makezine.com/projects/send-ticket-isp-when-your-internet-drops/

sudo apt-get install python-pip -y
sudo pip install speedtest-cli

cd $script_dir
if [ ! -d "$extras_dir" ]; then
    echo Creating $extras_dir
    git clone https://github.com/HenrikBengtsson/speedtest-cli-extras.git
fi
