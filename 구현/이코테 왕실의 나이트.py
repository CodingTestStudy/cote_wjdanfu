data = input();

row= int (data[1])
column=int(ord(data[0]))-int(ord('a'))+1

steps=[[-2,1],[-2,-1],[2,1],[2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]

count =0
for step in steps:
  n_row=row+step[0]
  n_co=column+step[1]
  if 0<n_row<=8 and 0<n_co<=8:
    count+=1;

print(count)
