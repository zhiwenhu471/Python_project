import time
import asyncio

def sync_task(name):
    print(f"[{name}] 开始请求...")
    time.sleep(1)  # 模拟阻塞 I/O
    print(f"[{name}] 请求完成。")
    return f"Data from {name}"

start_time = time.time()
sync_task("任务A")  # 必须等待 1 秒
sync_task("任务B")  # 必须再等待 1 秒
print(f"同步总耗时：{time.time() - start_time:.2f} 秒")

print()

async def sync_task(name):
    print(f"[{name}] 开始请求...")
    await asyncio.sleep(1)  # 模拟阻塞 I/O
    print(f"[{name}] 请求完成。")
    return f"Data from {name}"

async def main():
    start_time = time.time()
    results = await asyncio.gather(
    sync_task("任务A"),  # 必须等待 1 秒
    sync_task("任务B")  # 必须再等待 1 秒        
    )
    print(f"同步总耗时：{time.time() - start_time:.2f} 秒")
    print(f"结果：{results}")

if __name__ == "__main__":
    asyncio.run(main())