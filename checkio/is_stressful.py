def is_stressful(subj):
    """
        recognize stressful subject
    """
    help = False
    subj_list = subj.split()
    for word in subj_list:
        s = ''.join(c for c in word if c.isalpha())
        print('s = ' + s)
        str_ = sorted(set(s.upper()))
        # print(len(['EHLP'.split()]))
        help = ['E','H','L','P'] == str_ or ['E','H','L','P'] == str_
        print('boolean ', help)




    return subj.upper() == subj or str(subj[len(subj)-3::]) == '!!!'
    # return str(subj[len(subj)-3::])

#print(is_stressful('LBOEFEFE dsfs!!!'))
print(is_stressful('HHHHHEEEEEEEE-LLLLL-pppp me'))


# if __name__ == '__main__':
#     # These "asserts" are only for self-checking and not necessarily for auto-testing
#     assert is_stressful("Hi") == False, "First"
#     assert is_stressful("I neeed HELP") == True, "Second"
#     print('Done! Go Check it!')
