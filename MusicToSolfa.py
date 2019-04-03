#open text file called sampleMusic.txt

#from beginning of text until end
#	for each line
#
#		read character
#			if exists in dictionary
#			Then replace with doremi
#			else skip
#		next character
#	next line / end if final line

##Handle
#New lines
#random characters in text: ' + more


#Strategy:
#	Maybe do it line by line


from sys import argv

script, from_file, to_file = argv

print(f"This code takes: {from_file} as input.")

#Now Read the first line of the file


in_file = open(from_file)

#------------------Read Line by Line
#indata = in_file.read()
print("""----------------------------------------
-----------------START------------------\n""")

print(f'---------------Begin readline Example (read {from_file} line by line)\n')
print(in_file.readline(), end='')
print("boo")
print(in_file.readline(), end='')
print('---------------End readline Example\n')

#Turn sentence into list of characters

#------------------Dictionary Example
print('---------------Dictionary Example\n')
dict = {'A':'d', 'B':'r', 'C':'m'} #{} curly brackets make a 'Dictionary'
print("Here is the thing related to 'B' in dictionary: ", dict['B'])
print('---------------End Dictionary Example\n')

#------------------Write line by line
##do this next^
out_file = open(to_file, 'w') #Write mode
out_file.truncate() #NEW this Deletes what's in the file!
out_file.write("Once upon a time")
out_file.write("\n")
out_file.write("there was a house")
out_file.write("\n")
out_file.write("made of clay")

out_file.close()
in_file.close()
