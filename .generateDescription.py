from xml.dom import minidom
import os
import glob

print "Updating README.md based on .codesnippet files"

file = open('README.md', 'w')
file.write('# Xcode Code Snippets\n\n')
file.write('### Convenience installation (recommended)\n')
file.write('Link code snippets to the appropriate Xcode code snippet folder and install the pre-commit hook which updates the documentation on every commit by running the following command:\n\n')
file.write('    sh .install.sh\n\n')
file.write('### Manual installation\n')
file.write('Clone the repository into the following path:\n\n')
file.write('    cd ~/Library/Developer/Xcode/UserData/CodeSnippets\n')
file.write('    git clone git@github.com:martinstolz/CodeSnippets.git .\n\n')
file.write('Or link from your cloned folder to the appropriate Xcode code snippet folder by running the following command:\n\n')
file.write('    sh .installLinkage.sh\n\n')
file.write('#### Installing the pre-commit hook\n')
file.write('This README is generated automatically using `.generateDescription.py`.\n')
file.write('To run this script automatically before each commit, install the pre-commit hook like this:\n\n')
file.write('    python .installPrecommitHook.py\n\n')
file.write('### Snippet Descriptions\n\n')

listing = os.listdir(".")
for fileName in listing:
    
    if not fileName.endswith(".codesnippet"):
    	continue

    xmldoc = minidom.parse(fileName)
    keyslist = xmldoc.getElementsByTagName('key')
    allChilds = xmldoc.getElementsByTagName('dict')[0].childNodes

    for x in allChilds:
    	if not x.firstChild:
    		allChilds.remove(x)

    title=""
    summary=""
    shortcut=""
    contents=""

    for key in keyslist:
    	value = key.firstChild.nodeValue
    	if (value == "IDECodeSnippetCompletionPrefix"):
    		shortcut = allChilds[allChilds.index(key)+1].firstChild.nodeValue
    	elif value == "IDECodeSnippetContents":
    		contents = allChilds[allChilds.index(key)+1].firstChild.nodeValue
    	elif value == "IDECodeSnippetSummary":
    		summary  = allChilds[allChilds.index(key)+1].firstChild.nodeValue
    	elif value == "IDECodeSnippetTitle":
    		title    = allChilds[allChilds.index(key)+1].firstChild.nodeValue

    file.write('**' + fileName + '**  (' + title + ')  \n')
    file.write('Shortcut: `' + shortcut + '`  \n')
    file.write(summary + '\n\n')
    file.write('    ' + contents.replace('\n', '\n    ') + '\n\n')

file.close()
