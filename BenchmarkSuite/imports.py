import importlib, time

def bench_imports() -> tuple[dict[str, float], float]:
    modules = ["math", "json", "sqlite3",
               "functools", "concurrent.futures",
               "asyncio", "array", "re", "typing"]
    
    results = {}
    total_length = 0.0
    
    for name in modules:
        t0 = time.perf_counter()
        importlib.import_module(name)
        t1 = time.perf_counter()
        tt = t1 - t0
        total_length += tt
        results[name] = tt
    return results, total_length