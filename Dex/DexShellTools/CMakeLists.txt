cmake_minimum_required(VERSION 3.12)
project(DexShellTools)

set(OPENCV_CXX11 ON)

INCLUDE_DIRECTORIES(/usr/local/opt/openssl/include)

link_libraries(z)
link_libraries(crypto)
add_executable(DexShellTools main.cpp )
