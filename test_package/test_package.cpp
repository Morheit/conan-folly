#include <cstdlib>
#include <iostream>

#include <folly/Format.h>

int main() {
    auto const string = folly::format("Formatting {} and {}", 1, 2);
    std::cout << string << std::endl;
    return 0;
}
