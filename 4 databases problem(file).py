rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))

with open("input_data.txt", "w") as f:

    f.write(f"{rows} {cols}\n")

    for i in range(rows):
        row = []
        for j in range(cols):
            val = int(input())
            row.append(str(val))
        f.write(" ".join(row) + "\n")

    row_query = int(input("Enter query for server 1 (row): "))
    col_query = int(input("Enter query for server 1 (column): "))
    cs = int(input("Enter CHANGE index of row: "))
    ct = int(input("Enter CHANGE index of column: "))

    f.write(f"{row_query}\n")
    f.write(f"{col_query}\n")
    f.write(f"{cs}\n")
    f.write(f"{ct}\n")

with open("input_data.txt") as f:
    data = f.read().strip().split()

# Extract matrix size
rows = int(data[0])
cols = int(data[1])

# Extract matrix
idx = 2
serv1 = []
for i in range(rows):
    row = list(map(int, data[idx:idx+cols]))
    serv1.append(row)
    idx += cols

row_query = int(data[idx]); idx += 1
col_query = int(data[idx]); idx += 1
cs = int(data[idx]); idx += 1
ct = int(data[idx]); idx += 1

serv2 = serv1
serv3 = serv1
serv4 = serv1


s1 = list(bin(row_query)[2:])
t1 = list(bin(col_query)[2:])

s2 = []
t2 = []

for i in range(len(s1)):
    s2.append('1' if (i == cs and s1[i] == '0') else
              '0' if (i == cs and s1[i] == '1') else
              s1[i])

for i in range(len(t1)):
    t2.append('1' if (i == ct and t1[i] == '0') else
              '0' if (i == ct and t1[i] == '1') else
              t1[i])


sum1 = sum2 = sum3 = sum4 = 0

for i in range(len(s1)):
    for j in range(len(t1)):
        if i < rows and j < cols:
            if (s1[i] == t1[j]) and s1[i] == '1':
                sum1 ^= serv1[i][j]
            if (s2[i] == t1[j]) and s2[i] == '1':
                sum2 ^= serv2[i][j]
            if (s1[i] == t2[j]) and s1[i] == '1':
                sum3 ^= serv3[i][j]
            if (s2[i] == t2[j]) and s2[i] == '1':
                sum4 ^= serv4[i][j]

result = sum1 ^ sum2 ^ sum3 ^ sum4
print("Result:", result)
