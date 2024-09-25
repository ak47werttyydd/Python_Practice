sentence1 = ["great","acting","skills"]
sentence2 = ["fine","drama","talent"]
# sentence2 = ["good","drama","talent"]
similarPairs = [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]

zip_sen1sen2 = zip(sentence1, sentence2)
# [["great","find"],["acting","drama"],["skills","talent"]
lst_zip_sen1sen2 = list(zip_sen1sen2)

count = len(lst_zip_sen1sen2)
for pair in lst_zip_sen1sen2:
    pair=list(pair)
    # identical words
    if pair[0] == pair[1]:
        count -= 1
        print(count)
        continue
    # whether similar pairs
    else:
        pair2 = pair[::-1]
        if (pair in similarPairs) or (pair2 in similarPairs):
            count -= 1
            print(count)
            continue
        else:
            break
print(count)
if count == 0:
    print("True")
else:
    print("False")