import os
import sys
import slate
from PyPDF2 import PdfFileWriter, PdfFileReader

homeDirectory = os.path.dirname(os.path.abspath(__file__))

os.chdir(homeDirectory)

print ''
print 'Currently running bynder in ' + homeDirectory + '.'

filesInHomeDirectory = []
for (dirpath, dirnames, filenames) in os.walk(homeDirectory):
	filesInHomeDirectory.extend(filenames)
	break

pdfsInHomeDirectory = []
for fileName in filesInHomeDirectory:
	if '.pdf' in fileName:
		pdfsInHomeDirectory.append(fileName)

print '\tBynder found ' + str(len(pdfsInHomeDirectory)) + ' PDF files to search.'

if (len(pdfsInHomeDirectory) == 0):
        raw_input()
	sys.exit()

print '\tHow would you like the output sorted?'

sortOrder = ''
while (sortOrder != 'o') and (sortOrder != 'n'):
	sortOrder = raw_input('\tEnter n for newest first, o for oldest first: ')

if sortOrder == 'o':
	pdfsInHomeDirectory.sort()
else:
	pdfsInHomeDirectory.sort(reverse = True)

accountNumber = raw_input('\tPlease enter an account number: ')

outputFileName = homeDirectory + '/' + accountNumber + '.pdf'

if os.path.isfile(outputFileName):
	print('The file ' + outputFileName + ' already exists.')
	print('Please delete it and run bynder again.')
	raw_input()
	sys.exit()

output = PdfFileWriter()

for fileName in pdfsInHomeDirectory:
	with open(fileName, 'rb') as f:
		input = PdfFileReader(f)	
		slateDocument = slate.PDF(f)
		pages = []
		
		for i in range(len(slateDocument)):
			if accountNumber in slateDocument[i]:
				output.addPage(input.getPage(i))
		with open(outputFileName, 'wb') as out:
      			output.write(out)

print 'Output file written: ' + homeDirectory + '/' + accountNumber + '.pdf'
print 'Thanks for using bynder. Have a five star day.'

raw_input()
