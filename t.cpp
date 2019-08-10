#include <bits/stdc++.h>
using namespace std;

int main(void)
{
    int treesArr[200010];
    long long treeStars[200010];
    int client[200000][2];

    int trees, i, j, x, y;
    cin >> trees;
    for (i = 0; i < trees; i++) {
        cin >> treesArr[i];
    }
    
    treeStars[0] = treesArr[0];
    for (i = 1; i < trees; i++) {
        treeStars[i] = treesArr[i] + treeStars[i - 1];
    }

    int clients;
    cin >> clients;
    for (i = 0; i < clients; i++) {
        for (j = 0; j < 2; j++) {
            cin >> client[i][j];
        }
    }
    
    for (i = 0; i < clients; i++) {
        x = (client[i][1] > client[i][0]) ? client[i][1] : client[i][0];
        y = (client[i][1] < client[i][0]) ? client[i][1] : client[i][0];
        if (y == 1) {
            cout << treeStars[x - 1] << "\n";
        }
        else {
            cout << treeStars[x - 1] - treeStars[y - 2] << "\n";
        }       
    }
    return 0;
}