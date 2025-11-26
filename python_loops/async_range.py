import asyncio
"""
asyncio是 Python 中用于编写并发代码的核心库，它主要利用 async/await语法来构建异步程序。
该库特别适合处理 I/O 密集型和高层级的结构化网络任务，能有效提升程序的执行效率和资源利用率
""" 


class AsyncRange:
    def __init__(self, start, end):
        self.data = range(start, end)

    async def __aiter__(self):  # 使用async def 定义的函数被称为协程（Coroutine）,一个可以被暂停执行，并稍后从暂停点恢复执行的特殊函数
        for index in self.data:
            await asyncio.sleep(0.5)  # await 只能在协程内部使用
            yield index


async def main():
    async for index in AsyncRange(0, 5):
        print(index)


asyncio.run(main())
