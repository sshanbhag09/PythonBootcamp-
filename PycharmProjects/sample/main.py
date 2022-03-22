
def countValidWords(sentence):
        """
        :type sentence: str
        :rtype: int

        """
        tokens = 0
        list_s = sentence.split()
        print(list_s)
        for elem in list_s:
            leng = len(elem)
            if elem.islower() == True and elem.isdigit() == False:
                if '-' in elem:
                    if elem.index("-") == 1 or elem.index("-") == leng:
                        continue
                    elif '!' in elem:
                        if elem.index("!") != leng:
                            continue
                        elif elem.index("!")==len:
                            tokens+=1

                    else:
                        tokens+=1


                elif '-' not in  elem:
                    if '!' in elem:
                        if elem.index("!") != leng:
                            continue
                        elif elem.index("!")==len:
                            tokens+=1

                    else:
                        tokens+=1

            else:
                continue
        return tokens
print(countValidWords("he! bought 2 pencils, 3 erasers, and 1  pencil-sharpener."))
