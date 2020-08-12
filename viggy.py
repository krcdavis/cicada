runes = ["ᚠ", "ᚢ", "ᚦ", "ᚩ", "ᚱ", "ᚳ", "ᚷ", "ᚹ", "ᚻ", "ᚾ", "ᛁ", "ᛄ", "ᛇ", "ᛈ", "ᛉ", "ᛋ", "ᛏ", "ᛒ", "ᛖ", "ᛗ", "ᛚ", "ᛝ", "ᛟ", "ᛞ", "ᚪ", "ᚫ", "ᚣ", "ᛡ", "ᛠ"]
letters = ["F", "V", "th", "O", "R", "C", "G", "W", "H", "N", "I", "J", "eo", "P", "X", "S", "T", "B", "E", "M", "L", "ng", "oe", "D", "A", "ae", "Y", "ia", "ea"]
pseudo = ["F", "V", "#", "O", "R", "C", "G", "W", "H", "N", "I", "J", "@", "P", "X", "S", "T", "B", "E", "M", "L", "&", "0", "D", "A", "(", "Y", "!", ")"]
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109]
exclude = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890/-.&$"#for creating freq-only files?

word = "DIVINITY"#pseudo
word2="CIRFVMFERENCE"
p=len(word)
q=len(word2)
chunk= "ᚢᛠᛝᛋᛇᚠᚳᚱᛇᚢᚷᛈᛠᛠ-ᚠᚹᛉ/"
plaint="WELCOMEWELCOME-PIL/"
vg = 0

#encode plaint
for n in range(len(plaint)):
    if plaint[n] in pseudo:
        b= ( pseudo.index(plaint[n]) + pseudo.index(word[vg]) )%29
        vg = (vg+1)%p
        print(runes[b],end='')
    else:
        print(plaint[n],end='')

#decode
vg=0
print('')
print(chunk)
for n in range(len(chunk)):
 print(word[n%p], end='')
print('')
for n in range(len(chunk)):
 if chunk[n] in runes:
  b = (  runes.index(chunk[n]) - pseudo.index(word[vg]) )%29
  vg = (vg+1)%p
  print(pseudo[b], end='')
 else:
  print(chunk[n], end='')
