import multiprocessing
from timeit import default_timer as timer

def process_worker(file_paths, queue):
    local_found = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            if "Data Science GoIT" in file.read():
                local_found.append(file_path)
    queue.put(local_found)

def multi_processed_search():
    processes = []
    queue = multiprocessing.Queue()
    file_paths = [f'data/file_{i}.txt' for i in range(1, 6)]
    n_processes = 2
    files_per_process = (len(file_paths) + n_processes - 1) // n_processes

    for i in range(n_processes):
        start_idx = i * files_per_process
        end_idx = min((i + 1) * files_per_process, len(file_paths))
        p_file_paths = file_paths[start_idx:end_idx]
        process = multiprocessing.Process(target=process_worker, args=(p_file_paths, queue))
        processes.append(process)
        process.start()

    all_results = []
    for _ in processes:
        all_results.extend(queue.get())

    for process in processes:
        process.join()

    return all_results

if __name__ == '__main__':
    multiprocessing.freeze_support()
    start = timer()
    results = multi_processed_search()
    time_taken = timer() - start
    print("Process Results:", results)
    print("Time Taken:", time_taken)
