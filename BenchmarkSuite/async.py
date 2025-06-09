import time, asyncio

async def trivial_task(n):
    for _ in range(n):
        await asyncio.sleep(0)

def bench_asyncio(n_tasks=1000, loops=100):
    async def runner():
        await asyncio.gather(*(trivial_task(loops) for _ in range(n_tasks)))
    t0 = time.perf_counter()
    asyncio.run(runner())
    t1 = time.perf_counter()
    return t1 - t0