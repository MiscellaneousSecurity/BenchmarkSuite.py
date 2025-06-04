import importlib, time

def bench_imports():
    modules = ["math", "json", "sqlite3",
               "functools", "concurrent.futures",
               "asyncio", "array", "re", "typing"]
    
    results = {}
    
    for name in modules:
        t0 = time.perf_counter()
        importlib.import_module(name)
        t1 = time.perf_counter()
        results[name] = t1 - t0
    return results