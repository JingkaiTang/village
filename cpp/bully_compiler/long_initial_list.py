#! /usr/bin/env python

LENGTH = 100000000

if __name__ == '__main__':
    code = r'''#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    auto list = {%s};

    for_each(list.begin(), list.end(), [](int i) {
        cout << i << " ";
    });
    cout << endl;

    return 0;
}
''' % (', '.join(map(str, range(LENGTH))))

    open('long_initial_list.cpp', 'w').write(code)

