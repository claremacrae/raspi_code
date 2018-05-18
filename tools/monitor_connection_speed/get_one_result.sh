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
    (echo -ne "pi_revision\\t"; $script_dir/speedtest-cli-extras/bin/speedtest-csv --header ) > $output_file
fi

# TODO Read https://www.raspberrypi.org/learning/networking-lessons/lessons/
# TODO Include a column for hostname - so I can use hostname to indicate location
# TODO Include a column for connection type - WiFi or Ethernet
#  For WiFi: iwgetid --raw      ... gives ESSID:
#            iwconfig           ... gives more info
#  For Ethernet: ifconfig eth0
#                ifconfig -s
#SEE ALSO
#       route(8), netstat(8), arp(8), rarp(8), iptables(8), ifup(8), interfaces(5).
#       http://physics.nist.gov/cuu/Units/binary.html - Prefixes for binary multiples

# For meaning of pi_revision values, see https://elinux.org/RPi_HardwareHistory
pi_revision=`cat /proc/cpuinfo | grep 'Revision' | awk '{print $3}' | sed 's/^1000//'`
(echo -ne "$pi_revision\\t"; $script_dir/speedtest-cli-extras/bin/speedtest-csv --no-share ) >> $output_file

