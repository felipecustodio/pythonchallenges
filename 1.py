# Get alphabet
from string import ascii_lowercase

alphabet = ascii_lowercase
message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url = "map"
translated = ""

for i in range(0, len(url)):
    for j in range(0, len(alphabet)):
        if (url[i] == alphabet[j]):
            if (j+2 >= len(alphabet)):
                translated += alphabet[len(alphabet) - j-2]
            else:
                translated += alphabet[j+2]

print translated