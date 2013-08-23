#!/usr/bin/env bash
#
# Copies all Xcode code snippets to the appropriate folder.
#

# Link Xcode code snippets to appropriate Xcode code snippet folder
sh .installLinkage.sh

# Install pre-commit hook to auomatically generate a documentation of all code snippets
sh .installPrecommitHook.sh
