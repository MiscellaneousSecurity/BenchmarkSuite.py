import json, time

def json_impl() -> str:
    if json.__name__ == "json" and hasattr(json, "_C_IMPLEMENTATION"):
        return "C Accelerator"
    return "Pure Python"

def is_json_c_accelerated() -> bool:
    return json_impl() == "C Accelerator"

def bench_serialization(n=100_000) -> tuple[float, float]:
    assert(isinstance(n, int) and n > 0)
    data = {str(i): i for i in range(n)}
    # JSON
    t0 = time.perf_counter()
    s = json.dumps(data)
    t1 = time.perf_counter()
    _ = json.loads(s)
    t2 = time.perf_counter()
    return t1 - t0, t2 - t1