import multiprocessing
from timeit import default_timer as timer

def process_worker(file_paths, target_strings, queue):
    local_found = {key: [] for key in target_strings}
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                for key in target_strings:
                    if key in content:
                        local_found[key].append(file_path)
        except Exception as e:
            print(f"Failed to read {file_path}: {e}")
    queue.put(local_found)

def multi_processed_search(target_strings):
    processes = []
    queue = multiprocessing.Queue()
    results = {key: [] for key in target_strings}
    file_paths = [f'data/file_{i}.txt' for i in range(1, 6)]
    n_processes = 2
    files_per_process = (len(file_paths) + n_processes - 1) // n_processes

    for i in range(n_processes):
        start_idx = i * files_per_process
        end_idx = min((i + 1) * files_per_process, len(file_paths))
        p_file_paths = file_paths[start_idx:end_idx]
        process = multiprocessing.Process(target=process_worker, args=(p_file_paths, target_strings, queue))
        processes.append(process)
        process.start()

    
    for _ in processes:
        part_result = queue.get()
        for key in part_result:
            results[key].extend(part_result[key])

    for process in processes:
        process.join()

    return results

if __name__ == '__main__':
    multiprocessing.freeze_support()
    start = timer()
    target_strings = ["Data Science GoIT", "GoIT_2", "GoIT_3"]
    results = multi_processed_search(target_strings)
    time_taken = timer() - start
    print("Process Results:", results)
    print("Time Taken:", time_taken)
