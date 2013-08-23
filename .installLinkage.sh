#!/usr/bin/env bash
#
# Links all Xcode code snippets to the appropriate Xcode folder.
#

# Determine appropriate Xcode folder for code snippets
installDirectory=~/Library/Developer/Xcode/UserData/CodeSnippets

# Determine current directory
currentDirectory="$(pwd)"

COLOR='\033[01;31m'
RESET='\033[00;00m'

ln -s $currentDirectory $installDirectory

echo "Xcode Code Snippets are now linked to ${COLOR}$installDirectory${RESET}"