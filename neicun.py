###############内存管理##########################
"""
gc.disable()  # 暂停自动垃圾回收.
gc.collect()  # 执行一次完整的垃圾回收, 返回垃圾回收所找到无法到达的对象的数量.
gc.set_threshold()  # 设置Python垃圾回收的阈值.
gc.set_debug()  # 设置垃圾回收的调试标记. 调试信息会被写入std.err.

同时我们还使用了objgraphPython库, 本文中具体使用到的接口包括:
objgraph.count(typename)  # 对于给定类型typename,
返回Python垃圾回收器正在跟踪的对象个数.


Python有两种共存的内存管理机制: 引用计数和垃圾回收. 引用计数是一种非常高效的内存管理手段,
当一个Python对象被引用时其引用计数增加1, 当其不再被一个变量引用时则计数减1.
当引用计数等于0时对象被删除.
"""


import gc

import objgraph

gc.disable()


class A(object):
	pass

class B(object):
	pass

def test1():
	a = A()
	b = B()

test1()
print("Object count of A:",objgraph.count('A'))
print("Object count of B:",objgraph.count('B'))
