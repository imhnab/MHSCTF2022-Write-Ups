import re

with open('9712a0c4e51eae4c229538d050ae0d38.txt') as fin:
    text=fin.read()

pattern="\d+,\d+,\d+"
lst=re.findall(pattern,text)
res=""
for item in lst:
    tmp=item.split(",")
    tmpstr=" ".join(tmp)
    tmpstr="("+tmpstr+")"
    res+=tmpstr+", "
res=res[:-2]

with open('result.txt','w') as fout:
    fout.write(res)