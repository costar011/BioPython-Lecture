with open("dream.txt", "r") as my_file:
  i = 0
  while 1:
    line = my_file.readline()
    if not line:
      break
    print(str(i) + "===" + line.replace("\n",""))
    i = i + 1

    # 인코딩

f = open("count_log.txt", "a", encoding="utf8")
for i in range(1,11):
  data = "%d 번째 줄입니다 \n" % i
  f.write(data)
f.close()