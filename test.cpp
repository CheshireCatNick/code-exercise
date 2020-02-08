#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <time.h>
#include <string>

using namespace std;

int c;

void printAll(string data, string output) {
    for (int i = 0; i < data.length(); i++) {
        output.push_back(data[i]);
        if (output.length() == 5) {
            cout << output << '\n';
            c++;
            output.pop_back();
            continue;
        }
        string newData = data;
        newData.erase(i, 1);
        printAll(newData, output);
        output.pop_back();
    }
    return;
}
int main(void) {
    string data = "0123456789";
    c = 0;
    printAll(data, "");
    cout << c << '\n';
}