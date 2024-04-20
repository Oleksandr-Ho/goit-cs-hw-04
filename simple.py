import os
from timeit import default_timer as timer

def sequential_search(target_strings):
    start = timer()
    results = {key: [] for key in target_strings}
    
    # Шляхи до файлів, що потрібно перевірити
    file_paths = [f'data/file_{i}.txt' for i in range(1, 6)]
    
    # Перебір файлів та пошук підрядка
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                for key in target_strings:
                    if key in content:
                        results[key].append(file_path)
        except Exception as e:
            print(f"Failed to read {file_path}: {e}")
                
    time_taken = timer() - start
    return results, time_taken

if __name__ == "__main__":
    target_strings = ["Data Science GoIT", "GoIT_2", "GoIT_3"]
    results, time_taken = sequential_search(target_strings)
    print("Sequential Results:", results)
    print("Time Taken:", time_taken)
