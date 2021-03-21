/*
  Puzzle of The Week
*/
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int gcd(int a, int b);
int calcPointsOnLine(int x0, int y0, int x1, int y1);

int main()
{
    int N;
    int l = 0, r = 0;
    int x0, y0;
    int pointsOnEdge = 0;
    int prev_x, prev_y;

    cin >> N; cin.ignore();
    for (int i = 0; i < N; i++) {
            int x;
            int y;
            cin >> x >> y; cin.ignore();
        if(i == 0){
            x0 = x;
            y0 = y;
        }
        else{
            r += prev_x * y;
            l += prev_y * x;
            pointsOnEdge += calcPointsOnLine(prev_x, prev_y, x, y);
        }
        prev_x = x;
        prev_y = y;
    }
    r += prev_x * y0;
    l += prev_y * x0;
    pointsOnEdge += calcPointsOnLine(prev_x, prev_y, x0, y0);

    cerr << "Points on Edge: " << pointsOnEdge << endl;
    cerr << "Area: " << (r - l) / 2 << '\n' << endl;
    double area = (r - l) / 2;
    area = ceil(area);

    int integralPointsInside = ceil(((area * 2) - (float)pointsOnEdge + 2)/2);

    cout << integralPointsInside << endl;
}

int gcd(int a, int b){
    if(b == 0)
        return a;
    return gcd(b, a%b);
}

int calcPointsOnLine(int x0, int y0, int x1, int y1){
    if(x1 == x0)
        return abs(y1 - y0);

    if (y1 == y0)
        return abs(x1 - x0);

    return gcd(abs(x1 - x0), abs(y1 - y0));
}
