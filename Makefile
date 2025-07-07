# Compiler and flags
CXX      := g++
CXXFLAGS := -std=c++17 -Wall -Wextra -Werror -O2

# Single source and target
SRC    := main.cpp
TARGET := app

# Default target
all: $(TARGET)

# Link the executable
$(TARGET): $(SRC)
    $(CXX) $(CXXFLAGS) -o $@ $^

# Clean up
clean:
    rm -f $(TARGET)

.PHONY: all clean

