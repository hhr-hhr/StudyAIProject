if __name__ == '__main__':
    msg = "Hello, World! "
    print(msg.rstrip())

    s1 = "hello"
    s2 = "world"
    i = 2

    # 不像java一样，python不支持字符串和数字的直接相加
    # print(s1 + i + s2)  这种写法会报错
    print(s1 + str(i) + s2)

    print(0.1+0.4)

    print("----------列表----------")
    # 列表
    bicycles = ['trek', 'cannondale', 'redline', 'specialized']
    print(bicycles[0].title())
    # 索引-1表示最后一个元素
    print(bicycles[-1])

    for bicycle in bicycles:
        print(bicycle + " is a good bike.")
    print("for end")

    myNumbers =list(range(1, 6))
    print(myNumbers)

    # 列表解析
    squares = [value ** 2 for value in range(1, 11)]
    print(squares)


    print("----------元祖----------")
    # 元祖
    dimensions = (200, 50)
    print(dimensions[0])
    # 列表转元祖
    myDimensions = tuple(myNumbers)
    print(myDimensions)
    # 元祖转列表
    listDimensions = list(myDimensions)
    print(listDimensions)

    print("----------字典----------")
    # 字典
    alien_0 = {'color': 'green', 'points': 5}
    print(alien_0['color'])

    # 遍历字典
    for key, value in alien_0.items():
        print(key + ": " + str(value))

    # 遍历字典的键
    for key in alien_0.keys():
        print(key)

    # 遍历字典的值
    for value in alien_0.values():
        print(value)

    # 按顺序遍历字典的键
    for key in sorted(alien_0.keys()):
        print(key)



