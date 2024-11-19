//
// Created by xio sun on 2024/11/18.
//
#include <chrono>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
#include <thread>

int main() {
    // 获取当前文件名
    const std::string file_name = __FILE__;
    const std::string file_name_without_ext = std::filesystem::path(file_name).stem().string();

    // 指定输出的文件路径
    const std::string output_file = file_name_without_ext + "_output.log";

    // 打开文件进行写入
    std::ofstream out(output_file, std::ios::app);// 使用追加模式
    if (!out.is_open()) {
        std::cerr << "failed to open the file: " << output_file << std::endl;
        return 1;
    }

    // 写入开始运行的信息
    out << "======> " << file_name << std::endl;

    // 延时 3 秒
    std::this_thread::sleep_for(std::chrono::seconds(3));

    // 写入结束运行的信息
    out << "<====== " << file_name << std::endl;

    // 关闭文件
    out.close();

    std::cout << "task ended and logged to " << output_file << std::endl;

    return 0;
}
