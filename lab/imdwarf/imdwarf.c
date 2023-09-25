#include <stdlib.h>
#include "wait.h"
#include "rng.h"

int main()
{
    while (1) {
        int status = system("wall -n \"I am a dwarf and I'm digging a hole\"");
        int delay = rng(5, 15) * 1000;
        wait(delay);
    }
    return 0;
}