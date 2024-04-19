import threading
from timeit import default_timer as timer

# Захист спільного ресурсу за допомогою блокування
lock = threading.Lock()

# Функція, яка виконує пошук в файлах
def thread_worker(file_paths, results):
    local_found = []  # Локальний список знайдених файлів
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            if "Data Science GoIT" in file.read():
                local_found.append(file_path)
    with lock:
        results.extend(local_found)

# Функція для багатопотокового пошуку
def multi_threaded_search():
    start = timer()
    threads = []
    results = []
    file_paths = [f'data/file_{i}.txt' for i in range(1, 6)]
    n_threads = 2
    files_per_thread = (len(file_paths) + n_threads - 1) // n_threads

    for i in range(n_threads):
        start_idx = i * files_per_thread
        end_idx = min((i + 1) * files_per_thread, len(file_paths))
        t_file_paths = file_paths[start_idx:end_idx]
        thread = threading.Thread(target=thread_worker, args=(t_file_paths, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    end = timer()
    return results, end - start

results, time_taken = multi_threaded_search()
print("Threads Results:", results)
print("Time Taken:", time_taken)