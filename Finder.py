# Andrew Neeser
# If your reading this file do not judge my code it is terrible I wrote pretty much most of this before I even knew how
# To code...

import Decoder
import Cleaner
import re
import os


class Finder:
    def __init__(self, term, inputFile, outputFile, regedit):
        self.term = term
        self.inputFile = inputFile
        self.outputFile = outputFile
        self.searchResults = []
        self.regeditterms = regedit
        self.regsearchresults = []

    def termFinder(self):  # supply with what you are search for and what file you are searching in
        for term in self.term:
            termlist = []
            foundsomething = False
            termlist.append('"')
            numberfiles = 0
            timesfound = 0
            for fileNumber in self.inputFile:  # fileNumber is which file in the list of inputFile you are reading from
                openfile = open(Decoder.decode(fileNumber), "r")
                num_lines = sum(1 for line in open(Decoder.decode(fileNumber)))
                numberfiles += 1

                linenumber = 1
                for line in openfile:  # Loops through all the lines in the file and open file
                    if term in line:
                        plaintext = Cleaner.cleanMe(line)
                        plaintext = re.sub(term, "", plaintext)

                        if plaintext is "":
                            linenumber += 1
                            continue

                        plaintext = os.path.splitext(os.path.basename(fileNumber))[0] + ": " + plaintext
                        if timesfound > 0:
                            plaintext = "\n" + plaintext
                        if "," in plaintext:
                            plaintext = plaintext.replace(",", ";")
                        if '"' in plaintext:
                            plaintext = plaintext.replace('"', ".")
                        print(plaintext)
                        termlist.append(plaintext)
                        foundsomething = True
                        linenumber += 1
                        timesfound += 1
                    elif linenumber == num_lines:
                        if foundsomething is False:
                            if numberfiles == len(self.inputFile):
                                termlist.append("Not Defined")
                                print("Not Defined")

                    else:
                        linenumber += 1

            termlist.append('"')
            termstring = ' '.join(termlist)
            self.searchResults.append(termstring)

        with open(self.outputFile, "a") as dest_file:
            for number in self.searchResults:
                dest_file.write(number + "\n")


    # Outputs the rededit search terms to the end of the file output file
    # TODO make one finder thing because this one can only output to end of file....
    def regtermFinder(self):
        for term in self.regeditterms:
            self.regsearchresults.append('"')
            foundterm = False
            for fileNumber in self.inputFile:
                    openfile = open(Decoder.decode(fileNumber), "r")
                    for line in range(sum(1 for line in open(Decoder.decode(fileNumber)))):
                        line = Cleaner.cleanMe(openfile.readline(line))
                        if foundterm is False and term in line:
                            print(term)

                            if foundterm is False:
                                self.regsearchresults.append(fileNumber + " " + term + " Disabled")

                            foundterm = True
            if foundterm is False:

                self.regsearchresults.append(term + ": Not Defined")
            self.regsearchresults.append('"')

        with open(self.outputFile, "a") as dest_file:
            for number in self.regsearchresults:
                dest_file.write(number + "\n")



