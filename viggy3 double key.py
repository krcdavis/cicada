import string

runes = ["ᚠ", "ᚢ", "ᚦ", "ᚩ", "ᚱ", "ᚳ", "ᚷ", "ᚹ", "ᚻ", "ᚾ", "ᛁ", "ᛄ", "ᛇ", "ᛈ", "ᛉ", "ᛋ", "ᛏ", "ᛒ", "ᛖ", "ᛗ", "ᛚ", "ᛝ", "ᛟ", "ᛞ", "ᚪ", "ᚫ", "ᚣ", "ᛡ", "ᛠ"]
letters = ["F", "V", "th", "O", "R", "C", "G", "W", "H", "N", "I", "J", "eo", "P", "X", "S", "T", "B", "E", "M", "L", "ng", "oe", "D", "A", "ae", "Y", "ia", "ea"]
pseudo = ["F", "V", "#", "O", "R", "C", "G", "W", "H", "N", "I", "J", "@", "P", "X", "S", "T", "B", "E", "M", "L", "&", "0", "D", "A", "(", "Y", "!", ")"]
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109]

#MAKE SURE THEY GOOD
testkeys=["CIRCVMFERENCE",
"FIRFVMFERENFE",
"DIVINITY",
"C&",#king; probably useless but here it is
"#ENAMEOF#EMAN"]#the name of the man
#cat by length I guess

sectext=[0,3,8,15,23,27,33,40]

sectemp=["ᛋᚻᛖᚩᚷᛗᛡᚠ-ᛋᚣᛖᛝᚳ.ᚦᛄᚷᚫ-ᚠᛄᛟ-ᚩᚾᚦ-ᚾᛖᚹᛒᚪᛋᛟᛇᛁᛝᚢ-ᚾᚫᚷᛁᚦ-ᚻᛒᚾᛡ",
         "ᛚᛄ-ᛇᚻᛝᚳᚦᛏᚫᛄᛏᛉᚻ-ᛏᚢᛟ.ᛋᛈᚱᚷ-ᚣᚾᚪᚷᛇᛝᚾ-ᚹᚠᚣᚾᛒᛠᛡ-ᛈᚾᚣᚪᛋᛗ",
         "ᛉᛁᛉᛗ-ᚢᛉᛗᚳᚦᛈᚩᛒ-ᛡᚾᛏ-ᛠᛉ-ᛈᚱᚣ-ᚩᚳᛠᛗᛝᚷᛉᛚᚢ-ᛝᛁᛏᚩ-ᛄᚠᛝ-ᛋᛚᚾᛞ.",
         "ᚠᚢᛚᛗ-ᚪᛠᚣᛟᚪ.ᛚᚢᛝᚾ-ᚳᚢ-ᛒᚾᛏᚠᛝ.ᛁᚢᛁᚢ-ᛟᚫᛄᚠᚫ-ᚢᚷᛉᛇᛈᛉ-ᚣᛠᛚᚪᛉ-ᛟᛉᛡᚦᚻᛠ-ᚾ",
         "ᚢᚪ-ᚹᛝᚷᛉᛞᚷ-ᛁᛒᛁ-ᛇᛏᛒᛁᚣ.ᛠᚷᛋᚫᛈᚹᛗᛠ-ᛇᛄᛇ-ᚹᚻᛁ-ᚷᛠᛒᚢᚣᚻᚣ-ᛝᚹᚢᚱᛋ-ᚩᛡᚠᛡᛠ-ᛞᛟᚦᛗᚳᚾᛉ",
         "ᛗᛈᚣ-ᛚᛋᚩᚪᚫᚻᛚᛖᛇᛁᛗᛚ-ᛚᛋᚳᛈ.ᚾᚻᚷᚢᛡᚻᚢ-ᛒᚠ-ᛞᛄᚢ-ᛒᛖᛁ-ᚫᚠ-ᛈ-ᚫᛈᚦ-ᚱᛗᛚᚳ-",
         "ᛞᛇ-ᛉᚳᚠᛁᚪᚹᚻᚷ.ᛇᛟ-ᚠᛏᛖᛟᛠᚪᛡᛋᚷ-ᚣᛠᚾᚦᚫᚱ-ᚩᛡᛗ-ᚹᛉᛗ-ᚣᛞᛒᛏᚱ",
         "ᚠᚾᛗ-ᚣᚷᛞᚫᚻ-ᚪᛈᛉᚣᚻ-ᛇᛠᚩᛖ-ᛏᛝᛠ-ᛚᛁᛏᚦᚠ-ᛗᚪᚳᛖ.ᛞᚳ-ᛏᚱᛟᚷᛠᚾᚫᛒᚢᛖᛒᚢ-ᚦᚠᛟ"]#this is fine

    
for a in testkeys:
    for b in testkeys:
        if len(a) != len(b):
            p=len(a)
            q=len(b)
            vgp=0
            vgq=0
            for m in sectemp:
                for c in m:
                    #print(c)
                    if c not in runes:
                        print(c, end='')#end me
                    else:
                        #print(runes.index(c))
                        n=( runes.index(c) - pseudo.index(a[vgp]) )%29
                        n=( runes.index(c) - pseudo.index(b[vgq]) )%29
                        vgp=(vgp+1)%p
                        vgq=(vgq+1)%q
                        print(pseudo[n], end='')
            print('')

