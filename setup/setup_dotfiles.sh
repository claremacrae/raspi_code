#!/bin/sh

set -u

# to force this script to run:
#   \rm -f ~/.bash_aliases && ./setup_dotfiles.sh && . ~/.bash_aliases

BASH_ALIASES=~/.bash_aliases
if [ ! -f $BASH_ALIASES ]; then
    cat > $BASH_ALIASES << 'EOF'

alias ll='ls -l'
alias lla='ls -la'
alias la='ls -A'
alias l='ls -CF'
alias rt='ls -lsrta'

alias gstat='cd /home/pi/develop ; for dir in * ; do     cd $dir; git status; echo $dir; echo " " ; cd ..;     done ; cd -'
alias gdiff='cd /home/pi/develop ; for dir in * ; do     cd $dir; git diff  ; echo $dir; echo " " ; cd ..;     done ; cd -'

CDPATH="."
for dir in \
    /home/pi/ \
    /home/pi/develop \
    /home/pi/develop/raspi_code/ \
    /home/pi/develop/raspi_code/hardware/ \
    /home/pi/develop/raspi_code/programming/ ; do
    if [ ! -d "$dir" ]; then
        continue
    fi
    CDPATH="$CDPATH:$dir"
done
EOF

fi
