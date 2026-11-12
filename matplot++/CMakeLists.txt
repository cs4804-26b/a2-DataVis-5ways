cmake_minimum_required(VERSION 4.4)
project(Penguins)

include(FetchContent)

set(CMAKE_CXX_STANDARD 17)

FetchContent_Declare(
		matplot
		GIT_REPOSITORY https://github.com/alandefreitas/matplotplusplus.git
)
FetchContent_MakeAvailable(matplot)

add_executable(Penguins main.cpp)
target_link_libraries(Penguins matplot)