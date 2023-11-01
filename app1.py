def create_diamond(star_count):
    if star_count % 2 == 0:
        star_count += 1  # 確保輸入是奇數

    # 上半部分
    for i in range(1, star_count + 1, 2):
        spaces = (star_count - i) // 2
        print(" " * spaces + "*" * i)

    # 下半部分
    for i in range(star_count - 2, 0, -2):
        spaces = (star_count - i) // 2
        print(" " * spaces + "*" * i)

star_count = int(input("請輸入星星數量（奇數）: "))
create_diamond(star_count)
