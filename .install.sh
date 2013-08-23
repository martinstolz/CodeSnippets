#!/usr/bin/env bash
#
# Copies all Xcode code snippets to the appropriate folder.
#

# Determine Xcode folder for code snippets
installDirectory=~/Library/Developer/Xcode/UserData/CodeSnippets

echo "Xcode Code Snippets will be installed to $installDirectory"

# Create the install directory if it does not exist.
if [ ! -d "$installDirectory" ]
then
	mkdir -p "$installDirectory"
fi

# Copy all of the Xcode code snippets into the install directory.
cp -r *.codesnippet "$installDirectory"
