from typing import List

def sort_by_ext(files: List[str]) -> List[str]:
    def take_index(elem):

        if elem[0] =='':
            return '1' + elem[1]
        elif elem[1] == '':
            return '1' + elem[0]
        else:
            return elem[1] + elem[0]

    extentions = []
    files_new = []

    for extention in files:
        # print(('.'.join(extention.split('.')[:-1]), "".join(extention.split('.')[-1])))
        extentions.append(('.'.join(extention.split('.')[:-1]), "".join(extention.split('.')[-1])))
    print(extentions)
    files = sorted(extentions, key=take_index)
    for a,b in files:
        files_new.append(a + '.' + b)
    return files_new


# OTHER SOLUTIONS
# BEST
#     skey = lambda s: (bool(s[:(i:=s.rfind('.'))]), s[i+1:], s[:i])
#     return sorted(files,key=skey)

#     1
#     return sorted(files,key=lambda x:(bool(i:=x.rfind('.')),x[i+1:],x[:i]))

#     2
#     def splitter(x):
#         parts = x.rsplit('.', 1)
#         return '' if (not parts[0] or not parts[1]) else parts[1], parts[0]  # returns two keys for sorting, first is extension, then by filename
#
#     return sorted(files, key=splitter)

if __name__ == '__main__':
    # print("Example:")
    # print(sort_by_ext(['1.cad', '2.bat', '3.aa', '1.aa', '2.aa']))
    # print(sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']))
    print(sort_by_ext([".config","my.doc","1.exe","345.bin","green.bat","format.c","no.name.","best.test.exe"]))


    # These "asserts" are used for self-checking and not for an auto-testing
    # assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    # assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    # assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    # assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    # assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    # assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    # assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    # assert sort_by_ext([".config","my.doc","1.exe","345.bin","green.bat","format.c","no.name.","best.test.exe"]) == [".config","no.name.","green.bat","345.bin","format.c","my.doc","1.exe","best.test.exe"]
    print("Coding complete? Click 'Check' to earn cool rewards!")

['.config', 'green.bat', '345.bin', 'format.c', 'my.doc', '1.exe', 'best.test.exe', 'no.name.']
[".config","no.name.","green.bat","345.bin","format.c","my.doc","1.exe","best.test.exe"]