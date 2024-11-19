# Python程序和C++程序之间的耦合程序较低，通过文件来交换数据
# Python程序主要的工作是运行必要的C++程序，处理指定输出文件中的关键信息来判断任务运行的进展和结果；
# C++侧实现的都是核心的业务任务，并将核心结果和指定检查点的结果输出到指定文件中。

import subprocess
import sys
from py.src.utils import time_format

# 指定需要完成的核心业务和对应二进制文件的项目路径
main_task_list = (
    ("demoTest1", "./cpp/bin/demoTest1"),
    ("demoTest2", "./cpp/bin/demoTest2")
)

# 指定保存标准输出的文件
task_track_file = "./task_tracker.log"

if __name__ == "__main__":
    # 任务初始化
    print(f"+++++++++++++++++++++++++++++++++++++++++++++++++++++++"
          f"\nTask Monitor Demo start in {time_format.get_formatted_time()}\n"
          f"Totally, there are {len(main_task_list)} tasks to do...\n"
          f"-------------------------------------------------------")

    for task in main_task_list:
        print(f"{task[0]} started in {time_format.get_formatted_time()}")

        # 保存标准输出的内容到文件
        with open(task_track_file, "a+") as file:
            # 备份原标准输出
            original_stdout = sys.stdout
            try:
                # 重定向标准输出到文件
                sys.stdout = file

                print(f"{task[0]} started in {time_format.get_formatted_time()}")

                result = subprocess.run([task[1]], capture_output=True, text=True)

                if result and not result.returncode:
                    print(f"{task[0]} exited in {time_format.get_formatted_time()}"
                          f" with output: {result.stdout}")
                else:
                    print(f"{task[0]} stopped in {time_format.get_formatted_time()}"
                          f" with error: {result.stderr}")

            finally:
                # 恢复原标准输出
                sys.stdout = original_stdout

        print(f"{task[0]} ended in {time_format.get_formatted_time()}")

    print(f"-------------------------------------------------------"
          f"\nDemo ended in {time_format.get_formatted_time()}, output has been saved to {task_track_file}.\n"
          f"+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
