import sys
import time
import importlib

# Normalizers to compare structural outputs correctly
def normalize_3sum(val):
    if not isinstance(val, list): return val
    try: return sorted([sorted(t) for t in val])
    except Exception: return val

def normalize_group_anagrams(val):
    if not isinstance(val, list): return val
    try: return sorted([sorted(g) for g in val])
    except Exception: return val

def normalize_intervals(val):
    if not isinstance(val, list): return val
    try: return sorted([list(i) for i in val])
    except Exception: return val

def normalize_indices(val):
    if not isinstance(val, list): return val
    try: return sorted(val)
    except Exception: return val

# Benchmark inputs for scaling performance measurement
BENCHMARKS = {
    1: ("longest_substring", ("abcabcbb" * 100,)),
    2: ("max_area", ([1, 8, 6, 2, 5, 4, 8, 3, 7] * 50,)),
    3: ("three_sum", ([-1, 0, 1, 2, -1, -4] * 20,)),
    4: ("group_anagrams", (["eat", "tea", "tan", "ate", "nat", "bat"] * 50,)),
    5: ("longest_consecutive", ([100, 4, 200, 1, 3, 2] * 50,)),
    6: ("product_except_self", ([1, 2, 3, 4] * 100,)),
    7: ("subarray_sum", ([1, 1, 1] * 100, 2)),
    8: ("merge_intervals", ([[1, 3], [2, 6], [8, 10], [15, 18]] * 50,)),
    9: ("find_anagrams", ("cbaebabacd" * 50, "abc")),
    10: ("decode_string", ("3[a]2[bc]" * 50,)),
}

# Verification test cases to ensure solutions are correct before timing
VERIFICATIONS = {
    1: {"args": ("abcabcbb",), "expected": 3, "norm": lambda x: x},
    2: {"args": ([1, 8, 6, 2, 5, 4, 8, 3, 7],), "expected": 49, "norm": lambda x: x},
    3: {"args": ([-1, 0, 1, 2, -1, -4],), "expected": [[-1, -1, 2], [-1, 0, 1]], "norm": normalize_3sum},
    4: {"args": (["eat", "tea", "tan", "ate", "nat", "bat"],), "expected": [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]], "norm": normalize_group_anagrams},
    5: {"args": ([100, 4, 200, 1, 3, 2],), "expected": 4, "norm": lambda x: x},
    6: {"args": ([1, 2, 3, 4],), "expected": [24, 12, 8, 6], "norm": lambda x: x},
    7: {"args": ([1, 1, 1], 2), "expected": 2, "norm": lambda x: x},
    8: {"args": ([[1, 3], [2, 6], [8, 10], [15, 18]],), "expected": [[1, 6], [8, 10], [15, 18]], "norm": normalize_intervals},
    9: {"args": ("cbaebabacd", "abc"), "expected": [0, 6], "norm": normalize_indices},
    10: {"args": ("3[a]2[bc]",), "expected": "aaabcbc", "norm": lambda x: x},
}

def main():
    print("==================================================")
    print("[-] Timing Solutions (Average of 100 Runs) ...")
    print("==================================================")
    
    all_passed = True
    all_runtimes = []
    
    for i in range(1, 11):
        module_name = f"problems.problem_{i}"
        func_name, bench_args = BENCHMARKS[i]
        ver_config = VERIFICATIONS[i]
        
        try:
            # Dynamically import the module and retrieve the function
            module = importlib.import_module(module_name)
            func = getattr(module, func_name)
            
            # 1. Verification Check
            actual = func(*ver_config["args"])
            normalizer = ver_config["norm"]
            
            if normalizer(actual) != normalizer(ver_config["expected"]):
                print(f"Problem {i:02d}: [X] FAILED (returned incorrect output)")
                all_passed = False
                continue
                
            # 2. Timing Runs (100 times) and collect individual runtimes
            problem_runs = []
            runs = 100
            for _ in range(runs):
                start_time = time.perf_counter()
                func(*bench_args)
                end_time = time.perf_counter()
                problem_runs.append((end_time - start_time) * 1000)  # Convert to ms
                
            all_runtimes.extend(problem_runs)
            avg_ms = sum(problem_runs) / len(problem_runs)
            print(f"Problem {i:02d}:  PASSED - Average Time: {avg_ms:.3f} ms")
            
        except Exception as e:
            print(f"Problem {i:02d}: [!] ERROR ({type(e).__name__}: {e})")
            all_passed = False

    print("==================================================")
    if not all_passed:
        print("[!] Some problems failed verification. Please solve them to get timing results.")
        sys.exit(1)
    else:
        # 3. Calculate overall metrics
        total_runs = len(all_runtimes)
        overall_avg = sum(all_runtimes) / total_runs
        
        sorted_runtimes = sorted(all_runtimes)
        mid = total_runs // 2
        if total_runs % 2 == 1:
            overall_median = sorted_runtimes[mid]
        else:
            overall_median = (sorted_runtimes[mid - 1] + sorted_runtimes[mid]) / 2.0
            
        print("OVERALL PERFORMANCE SUMMARY (All 1000 Runs):")
        print(f"  Average Run Time: {overall_avg:.4f} ms")
        print(f"  Median Run Time:  {overall_median:.4f} ms")
        print("==================================================")
        print("[Success] All solutions timed successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
