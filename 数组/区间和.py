import sys
# 一次性读取所有的输入数据
input = sys.stdin.read

def main():
    data = input().split()
    index = 0
    # n表示接下来要输入到数组元素的个数
    n = int(data[index])
    index += 1
    # 构建原始数组
    vec = []
    for i in range(n):
        vec.append(int(data[index+i]))
    index += n
    # 计算前缀和数组
    p = [0] * n
    persum = 0
    for i in range(n):
        persum +=  vec[i]
        p[i] = persum
    results = []
    # 批量处理区间查询
    while index < len(data):
        a = int(data[index])
        b = int(data[index+1])
        index+=2
        if a == 0:
            sum_value = p[b]
        else:
            sum_value = p[b] - p[a - 1]

        results.append(sum_value)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
    