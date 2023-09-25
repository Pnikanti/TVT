#pragma once
#include <random>

static std::random_device random_device;
static std::mt19937 generator(random_device());

int rng(int min, int max)
{
    std::uniform_int_distribution distribution(min, max);
    return distribution(generator);
}