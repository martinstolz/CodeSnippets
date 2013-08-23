#!/usr/bin/env bash
#
# Copies all Xcode code snippets to the appropriate folder.
#

# Determine Xcode folder for code snippets
installDirectory=~/Library/Developer/Xcode/UserData/CodeSnippets

COLOR='\033[01;31m'
RESET='\033[00;00m'

echo "Xcode Code Snippets will be installed to ${COLOR}$installDirectory${RESET}"

# Create the install directory if it does not exist.
if [ ! -d "$installDirectory" ]
then
	mkdir -p "$installDirectory"
fi

# Copy all of the Xcode code snippets into the install directory.
cp -r *.codesnippet "$installDirectory"
