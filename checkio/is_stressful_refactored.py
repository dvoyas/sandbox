import re

def is_stressful(subj):
    """
        recognize stressful subject
    """
    red_words = ['HELP','ASAP','URGENT']
    for word in subj.split():
        s = ''.join(c for c in word if c.isalpha()).upper()
        s_new = s[0]
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                s_new += s[i]
        if s_new in red_words:
            return True
    return subj.isupper() or subj.endswith('!!!')

    # return (subj.isupper() or
    #         subj.endswith('!!!') or
    #         any(re.search('+[.!-]*'.join(c for c in word), subj.lower())
    #             for word in ['help', 'asap', 'urgent']))

print(is_stressful('HHHHHEEEEEEEE-LLLLL-pppp me'))


if __name__ == '__main__':
    # These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("H!E!e!e!L!P!") == True, "Third"
    print('Done! Go Check it!')
