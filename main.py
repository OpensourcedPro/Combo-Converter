import os

zapros = input("request (word part of link) (ex: vk.)")



count = 0
try:
    inputFile = open(input("input file: "), "r+", encoding="utf-8")
    with open("tmp.txt", "w+", encoding="utf-8") as tmpFile:
            for line in inputFile:
                line = line.replace("http://","").replace("https://","")
                if line.count(zapros) != 0:
                    split = line.split(":")
                    if len(split) < 3:
                        print("format error - "+ line)
                        continue

                    tmpFile.write(split[1]+":"+split[2]+"\r\n")
    with open(zapros + ".txt", "w+", encoding="utf-8") as OutFile:
        lines = list(set(open("tmp.txt", "r+",encoding="utf-8").readlines()))
        for line in lines:
            if len(line) < 2 and line.count(":") != 2:
                continue
            count += 1
            OutFile.write(line)

except Exception as ex:
    print(ex)
print(f"Finished! Total {count} Output file - " +zapros+".txt")
os.remove("tmp.txt")
input()

input()
