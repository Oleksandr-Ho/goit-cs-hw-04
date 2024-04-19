from faker import Faker
import os

def create_files(directory='data', num_files=5, num_entries=10, special_indexes={1, 5}, special_text="Data Science GoIT"):
    faker = Faker()
    os.makedirs(directory, exist_ok=True)
    paths = []

    for i in range(1, num_files + 1):
        filename = f'file_{i}.txt'
        file_path = os.path.join(directory, filename)
        paths.append(file_path)
        with open(file_path, 'w', encoding='utf-8') as file:
            for _ in range(num_entries - 1):
                file.write(f"{faker.last_name()}, {faker.first_name()}, {faker.address().replace('\n', ', ')}\n")
            if i in special_indexes:
                file.write(special_text + "\n")
            else:
                file.write(f"{faker.last_name()}, {faker.first_name()}, {faker.address().replace('\n', ', ')}\n")
    return paths

file_paths = create_files()