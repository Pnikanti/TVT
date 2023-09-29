#include "../include/httplib.h"
#include "../include/json.hpp"
#include <iostream>

using json = nlohmann::json;

int main()
{
    httplib::Client cli("http://jsonplaceholder.typicode.com");
    auto res = cli.Get("/photos/1");
    auto data = json::parse(res->body);
    std::cout << data["title"] << std::endl;
}