import time


def progress_bar_update(current_step, total_steps):
    progress = current_step / total_steps
    bar = '#' * int(progress * 50) + '-' * (50 - int(progress * 50))
    print(f"\rProgress: [{bar}] {current_step}/{total_steps}", end='')


if __name__ == "__main__":
    print("test on process bar update:")
    progress_bar_update(20, 100)
    time.sleep(0.2)
    progress_bar_update(50, 100)
    time.sleep(0.2)
    progress_bar_update(80, 100)
    time.sleep(0.2)
    progress_bar_update(100, 100)
    print("\ntest end.")

