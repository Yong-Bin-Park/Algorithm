# 입력
# 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
# 둘째 줄부터 M개의 줄에는 바구니의 순서를 역순으로 만드는 방법이 주어진다. 방법은 i j로 나타내고,
# 왼쪽으로부터 i번째 바구니부터 j번째 바구니의 순서를 역순으로 만든다는 뜻이다. (1 ≤ i ≤ j ≤ N)
# 도현이는 입력으로 주어진 순서대로 바구니의 순서를 바꾼다.

# 출력
# 모든 순서를 바꾼 다음에, 가장 왼쪽에 있는 바구니부터 바구니에 적혀있는 순서를 공백으로 구분해 출력한다.

x, y = map(int, input().split())
xlist = [i+1 for i in range(x)]

for a in range(y):
    i, j = map(int, input().split())
    tmp_list = [0 for k in range(j-i+1)]
    c_list = []
    for b in range(i,j+1):
        tmp_list[b-i]=xlist[b-1]
    for c in range(len(tmp_list)):
        c_list.append(tmp_list[-(c+1)])
    xlist[i-1:j] = c_list

for d in xlist:
    print(d, end=' ')