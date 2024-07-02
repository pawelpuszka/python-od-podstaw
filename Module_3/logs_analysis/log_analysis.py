LOG_FILE_DIR = 'data/server_logs.txt'

def get_logs_from_file(log_file_dir: str) -> list():
    logs = list()
    with open(log_file_dir, 'r') as log_file:
        for line in log_file:
            line = line.strip('\n').split(sep=' ')
            logs.append(tuple(line))

    return logs


def get_errors_number(logs: list) -> int():
    errors_num = 0
    for log in logs:
        if int(log[3]) >= 400:
            errors_num += 1
    return errors_num

def get_correct_reqs_number(logs: list) -> int():
    correct_reqs_num = 0
    for log in logs:
        if int(log[3]) < 400:
            correct_reqs_num += 1

    return correct_reqs_num


def get_requests_number(logs: list) -> int():
    reqs_num = len(logs)
    return reqs_num


def write_results_to_file(logs: list) -> int():
    old_file_exists_error = True
    reqs_num = get_requests_number(logs)
    errors_num = get_errors_number(logs)
    correct_reqs_num = get_correct_reqs_number(logs)

    while old_file_exists_error:
        try:
            with open('data/log_results.txt', 'x') as file:
                file.write(f'Number of logs: {reqs_num} \n')
                file.write(f'Number of successful requests: {correct_reqs_num} \n')
                file.write(f'Number of failed requests: {errors_num} \n')
            old_file_exists_error = False
        except FileExistsError:
            import os
            os.remove('data/log_results.txt')


logs = get_logs_from_file(LOG_FILE_DIR)
write_results_to_file(logs)

