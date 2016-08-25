import csv

filepath = raw_input("Enter the path of the file (Eg: file.csv): ")
with open(filepath, 'r') as file_dp:
    stringArr = list(csv.reader(file_dp))[0]

while len(stringArr) > 1:
    word = stringArr[0]

    # mating starts with 1 because palindromes are not to be included in result
    matex = 1
    for mate in stringArr[1:]:

        # check if word reversed is the same as mate
        if word[::-1] == mate:

            # remove mate from array
            stringArr.pop(matex)

            print word + ' ' + mate
            break
        else:
            matex += 1
    stringArr.pop(0)
