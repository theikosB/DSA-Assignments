#include <stdio.h>
#include <limits.h>

void main() {
    long long fact = 1;

    for (int i = 1; i <= 25; i++) {
        if (fact > LLONG_MAX / i) {
            printf("Overflow occurs at %d!\n", i);
            break;
        }
        fact *= i;
    }
}