cmake_minimum_required(VERSION 3.16.3)
project(TaskMonitor)
set(CMAKE_CXX_STANDARD 17)

#设置源文件目录和输出目录
set(SRC_DIR "${CMAKE_SOURCE_DIR}/cpp/src")
set(BIN_DIR "${CMAKE_SOURCE_DIR}/cpp/bin")

#强制链接静态版本的依赖库（对于独立运行十分重要，不然难以使用python脚本来直接调用）
#macOS的工具链默认不支持完全的静态链接，不提供标准库的静态版本，即使指定了-static，编译器也无法找到所有必要的静态库
#set(CMAKE_EXE_LINKER_FLAGS "-static")

#创建可执行文件输出目录
file(MAKE_DIRECTORY ${BIN_DIR})

#遍历src目录下所有的cpp文件
file(GLOB CPP_FILES "${SRC_DIR}/*.cpp")

#针对每个遍历到的cpp文件生成单独的可执行文件
foreach (CPP_FILE ${CPP_FILES})
    #获取不带路径和后缀名的文件名
    get_filename_component(FILE_NAME ${CPP_FILE} NAME_WE)
    #指定生成的target文件的名称
    set(TARGET_NAME ${FILE_NAME})
    #添加可执行文件（CMake关键步骤）
    add_executable(${TARGET_NAME} ${CPP_FILE})
    #设置对应可执行文件的输出目录
    #如果未设置RUNTIME_OUTPUT_DIRECTORY，
    #可执行文件默认输出到CMAKE_BINARY_DIR下的对应子目录
    set_target_properties(${TARGET_NAME} PROPERTIES
            RUNTIME_OUTPUT_DIRECTORY ${BIN_DIR})
endforeach ()
