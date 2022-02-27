# Reconstruction
>Fun fact: This challenge requires competitors have knowledges about pixel of pictures... :D

[!hint](img/Reconstruction.png)

- We have an description and a [file](/MHSCTF2022-Write-Ups/General/Reconstruction/9712a0c4e51eae4c229538d050ae0d38.txt) as the picture.
- Okay! Open the file and we have many numbers split by `,` . A little attention the numbers have a range from 0 to 255 and in description have mention to `picture` so I guess this can be a information RGB (Red, Green, Blue) file.

[!hint](img/source.png)

- We need group 3 numbers in `(...)` before converting RGB txt to pictures :D
- I wrote script to group 3 number by `Python` :
  
    ```python
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
    ```

- After clearing data, I have [result.txt](result.txt). Finally, we need convert RGB data in `result.txt` file to picture.
- I wrote this Python script : 
  
    ```python
        from PIL import Image
        im = Image.new("RGB", (960,1280))
 
        infile = open('result.txt', 'r')
        data = infile.read().strip('\n').split(', ')
 
        rgblist = []
 
        for x in data:
            v = x.strip(')').strip('(').split()
            rgb = (int(v[0]),int(v[1]),int(v[2]))
            rgblist.append(rgb)
 
        im.putdata(rgblist)
        im.save("output.png") 
    ```

> In `im = Image.new("RGB", (960,1280))` we see resolution (960,1280) :D I must to try many resulutions until the words in picture clear to have [output.png](img/output.png).

- After converting to png file, we have : 
  
[!hint](img/output.png)

- Flip the picture to have flag :D
  
[!hint](img/flag.png)

- Flag : `flag{411_7h3_king5_h0rs3s_and_a11_th3_kings_m3n}`

