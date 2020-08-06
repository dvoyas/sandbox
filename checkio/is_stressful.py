def is_stressful(subj):
    """
        recognize stressful subject
    """
    red = False
    subj_list = subj.split()
    for word in subj_list:
        s = ''.join(c for c in word if c.isalpha())
        s_new = s[0]
        for i  in range(1,len(s)):
            if s[i] != s[i-1]:
                s_new += s[i]
        red = 'HELP' == s_new.upper() or 'ASAP' == s_new.upper() or 'URGENT' == s_new.upper()
        if red:
            break

    return subj.upper() == subj or str(subj[len(subj)-3::]) == '!!!' or red
    # return str(subj[len(subj)-3::])

#print(is_stressful('LBOEFEFE dsfs!!!'))
print(is_stressful('HHHHHEEEEEEEE-LLLLL-pppp me'))


if __name__ == '__main__':
    # These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')
