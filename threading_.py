import threading
from timeit import default_timer as timer

# Захист спільного ресурсу за допомогою блокування
lock = threading.Lock()

# Функція, яка виконує пошук в файлах
def thread_worker(file_paths, target_strings, results):
    local_found = {key: [] for key in target_strings}  # Локальний список знайдених файлів
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                for key in target_strings:
                    if key in content:
                        local_found[key].append(file_path)
        except Exception as e:
            print(f"Failed to read {file_path}: {e}")
            
    with lock:
        for key in local_found:
            results[key].extend(local_found[key])

# Функція для багатопотокового пошуку
def multi_threaded_search(target_strings):
    start = timer()
    threads = []
    results = {key: [] for key in target_strings}
    file_paths = [f'data/file_{i}.txt' for i in range(1, 6)]
    n_threads = 2
    files_per_thread = (len(file_paths) + n_threads - 1) // n_threads

    for i in range(n_threads):
        start_idx = i * files_per_thread
        end_idx = min((i + 1) * files_per_thread, len(file_paths))
        t_file_paths = file_paths[start_idx:end_idx]
        thread = threading.Thread(target=thread_worker, args=(t_file_paths, target_strings, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    end = timer()
    return results, end - start

if __name__ == '__main__':
    target_strings = ["Data Science GoIT", "GoIT_2", "GoIT_3"]
    results, time_taken = multi_threaded_search(target_strings)
    print("Threads Results:", results)
    print("Time Taken:", time_taken)