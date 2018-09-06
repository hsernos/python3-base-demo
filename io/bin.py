import base64
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
#                   1.二进制读写                            #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# 读取
with open('data/test.jpg', 'rb') as f:
    image_data = f.read(10)  # 读取10B
    base64_data = base64.b64encode(image_data)    # 使用 base64 编码
    print(base64_data)
# ==>b'/9j/4AAQSkZJRg=='

# 写入
with open('data/test.jpg', 'rb') as f:
    image_data = f.read()

with open('data/test2.png', 'wb') as f:
    f.write(image_data)