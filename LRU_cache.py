from collections import OrderedDict


# 定义LRUCache类
class LRUCache:
    # 初始化类，参数为capacity
    def __init__(self, capacity: int):
        # 初始化栈，用于存储键值对
        self.stack = OrderedDict()
        # 定义容量
        self.capacity = capacity

    # 获取键值对
    def get(self, key):
        # 如果键在栈中，则移动键值对到栈顶
        if key in self.stack:
            self.stack.move_to_end(key)
            return self.stack[key]
        # 如果键不在栈中，则返回None
        else:
            return None

    # 向栈中添加键值对
    def put(self, key, value) -> None:
        # 如果键在栈中，则移动键值对到栈顶
        if key in self.stack:
            self.stack[key] = value
            self.stack.move_to_end(key)
        # 如果键不在栈中，则添加键值对
        else:
            self.stack[key] = value
        # 如果栈的长度大于容量，则移除栈顶元素
        if len(self.stack) > self.capacity:
            self.stack.popitem(last=False)

    # 将容量调整为capacity
    def change_capacity(self, capacity):
        # 将容量赋值给实例变量
        self.capacity = capacity
        # 遍历栈，移除栈顶元素
        for i in range(len(self.stack) - capacity):
            self.stack.popitem(last=False)

    # 删除键值对
    def delete(self, key):
        # 如果键在栈中，则删除键值对
        if key in self.stack:
            del self.stack[key]

    # 获取栈中的键
    def keys(self):
        # 返回栈中的键
        return self.stack.keys()

    # 获取栈的长度
    def __len__(self):
        # 返回栈的长度
        return len(self.stack)

    # 判断是否包含某个键
    def __contains__(self, key):
        # 判断键是否在栈中
        return key in self.stack


if __name__ == '__main__':
    cache = LRUCache(2)

    cache.put(0, 1)
    cache.put(1, 1)
    cache.put(2, 1)
    print(0 in cache)
