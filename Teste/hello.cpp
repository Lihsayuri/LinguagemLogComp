// importe o llvm Value.h
#include <llvm-c-10>
#include <llvm-10/llvm/IR/Value.h>
#include <iostream>

int main() {
    llvm::Value* val = nullptr;
    std::cout << "Hello, LLVM!\n";
    return 0;
}
