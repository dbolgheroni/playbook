cmake_minimum_required(VERSION 3.12)

project(playbook VERSION 1.0)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

set(CMAKE_C_COMPILER "clang")
set(CMAKE_CXX_COMPILER "clang++")

# main
find_package(Boost REQUIRED)

set(SOURCE_DIR src)
set(OBJECT_DIR obj)
set(INCLUDE_DIR include)

file(GLOB_RECURSE SOURCES ${SOURCE_DIR}/*.cpp)

add_executable(main ${SOURCES})

target_include_directories(main PRIVATE ${Boost_INCLUDE_DIRS})
target_include_directories(main PRIVATE ${INCLUDE_DIR})

target_compile_options(main PRIVATE -Og -g -gdwarf-2 -c -Wall -Wno-unused)

# test
find_package(GTest REQUIRED)

set(TEST_DIR test)

file(GLOB_RECURSE SOURCES_TESTS ${TEST_DIR}/*.cpp ${SOURCE_DIR}/pb.cpp)

add_executable(test ${SOURCES_TESTS})

target_include_directories(test PRIVATE ${Boost_INCLUDE_DIRS})
target_include_directories(test PRIVATE ${INCLUDE_DIR})

target_compile_options(test PRIVATE -Og -g -gdwarf-2 -c -Wall -Wno-unused)

target_link_libraries(test PRIVATE GTest::gtest GTest::gtest_main)
