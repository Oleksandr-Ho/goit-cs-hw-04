import os
from timeit import default_timer as timer

def sequential_search():
    start = timer()
    target_string = "Data Science GoIT"
    found_files = []
    
    # Шляхи до файлів, що потрібно перевірити
    file_paths = [f'data/file_{i}.txt' for i in range(1, 6)]
    
    # Перебір файлів та пошук підрядка
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            if target_string in file.read():
                found_files.append(file_path)
                
    time_taken = timer() - start
    return found_files, time_taken

if __name__ == "__main__":
    results, time_taken = sequential_search()
    print("Sequential Results:", results)
    print("Time Taken:", time_taken)
