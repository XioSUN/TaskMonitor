import time


def get_formatted_time():
    local_time = time.localtime()
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    return formatted_time


if __name__ == "__main__":
    print(f"output test:{get_formatted_time()}")
