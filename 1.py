from string import maketrans

orig_str="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

trans_str=""

for char in orig_str:
    if char not in [' ','.','(',')','\'']:
        trans_ord = ord(char)+2
        if trans_ord > 122:
            trans_ord = trans_ord - 122 + 96
        trans_str += chr(trans_ord)
    else: 
        trans_str += char

print trans_str


######## now using maketrans #########

intab="abcdefghijklmnopqrstuvwxyz"
outtab="cdefghijklmnopqrstuvwxyzab"

trantab = maketrans(intab, outtab)

print orig_str.translate( trantab )


url="map"

print url.translate(trantab)
