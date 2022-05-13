import csv
import sys


def main():

    if len(sys.argv) != 3:
        sys.exit("Usage: dna.py CSV txt")

    # TODO: Read database file into a variable --> reader to make a simple list instead of dict
    csvList = []
    with open(sys.argv[1], "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            csvList.append(row)

    #cast all numerical csv inputs in list into ints
    for i in range(1,len(csvList)):
        for j in range(1,len(csvList[0])):
            csvList[i][j] = int(csvList[i][j])

    # TODO: Read DNA sequence file into a variable
    txt = open(sys.argv[2],'r')
    dna_seq = txt.read()

    #create a dictionary to print in results of str repeating for each name
    result = []

    #loop over every str and every name and find max times the str repeats and store it in a list.
    for i in range(1,len(csvList[0])):
        ocur = longest_match(dna_seq,csvList[0][i])
        result.append(ocur)

    #if list of max occurences matches a row of one of our names, print that name.
    for j in range(1,len(csvList)):
        if result == csvList[j][1:]:
            print(csvList[j][0])
            sys.exit(1)

    print("No Match")

# longest_match(casabcabcabcdde,abc) = 3
def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
