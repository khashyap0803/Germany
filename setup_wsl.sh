#!/bin/bash
# ============================================
# WSL2 Development Setup Script for Khashyap
# Run this inside your Ubuntu-22.04 terminal
# ============================================

echo "🔧 Starting development environment setup..."
echo ""

# Step 1: Update package list
echo "📦 Step 1/4: Updating package list..."
sudo apt update -y

# Step 2: Install C development tools
echo ""
echo "📦 Step 2/4: Installing C development tools (gcc, g++, gdb, make, cmake, git)..."
sudo apt install -y gcc g++ gdb make cmake git build-essential

# Step 3: Install ARM cross-compilation tools (for STM32)
echo ""
echo "📦 Step 3/4: Installing ARM cross-compiler (for STM32 development)..."
sudo apt install -y gcc-arm-none-eabi gdb-multiarch

# Step 4: Install useful extras
echo ""
echo "📦 Step 4/4: Installing extras (valgrind, nano, tree, curl)..."
sudo apt install -y valgrind nano tree curl wget

# Verification
echo ""
echo "============================================"
echo "✅ VERIFICATION — Checking all tools:"
echo "============================================"
echo ""

echo "--- GCC (C Compiler) ---"
gcc --version | head -1

echo "--- G++ (C++ Compiler) ---"
g++ --version | head -1

echo "--- ARM GCC (STM32 Cross-Compiler) ---"
arm-none-eabi-gcc --version | head -1

echo "--- GDB (Debugger) ---"
gdb --version | head -1

echo "--- GDB-Multiarch (ARM Debugger) ---"
gdb-multiarch --version | head -1

echo "--- Make ---"
make --version | head -1

echo "--- CMake ---"
cmake --version

echo "--- Git ---"
git --version

echo "--- Valgrind (Memory Checker) ---"
valgrind --version

echo "--- Python3 ---"
python3 --version

echo ""
echo "============================================"
echo "🧪 COMPILE TEST — Building Hello World..."
echo "============================================"

# Create a test C program
cat > /tmp/test_setup.c << 'EOF'
#include <stdio.h>

int main(void) {
    printf("\n");
    printf("  ✅ Hello Khashyap!\n");
    printf("  ✅ GCC compiles and runs perfectly!\n");
    printf("  ✅ Your development environment is READY!\n");
    printf("\n");
    printf("  Next step: May 1st, 5:00 AM, K&R Chapter 1\n");
    printf("  Command:   gcc hello.c -o hello -Wall\n");
    printf("\n");
    return 0;
}
EOF

gcc /tmp/test_setup.c -o /tmp/test_setup -Wall
/tmp/test_setup
rm /tmp/test_setup /tmp/test_setup.c

echo "============================================"
echo "🎉 SETUP COMPLETE! All tools installed."
echo "============================================"
echo ""
echo "To start coding:"
echo "  1. cd /mnt/f/Documents/DEVELOP"
echo "  2. mkdir C-Practice && cd C-Practice"
echo "  3. nano hello.c   (or use VS Code)"
echo "  4. gcc hello.c -o hello -Wall"
echo "  5. ./hello"
echo ""
