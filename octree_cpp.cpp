#include <bits/stdc++.h>
using namespace std;

class Point{
public:
    float x;
    float y;
    float z;
    Point(){}
    Point(const Point& p) { this->x = p.x; this->y = p.y; this->z = p.z; }
    Point(float _x,float _y,float _z) { this->x = _x; this->y = _y; this->z = _z; }
};

Point operator + (const Point& a, const Point& b){ return Point(a.x+b.x,a.y+b.y,a.z+b.z); }
Point operator - (const Point& a, const Point& b){ return Point(a.x-b.x,a.y-b.y,a.z-b.z); }
Point operator * (const Point& a, const Point& b){ return Point(a.x*b.x,a.y*b.y,a.z*b.z); }
Point operator / (const Point& a, const Point& b){ return Point(a.x/b.x,a.y/b.y,a.z/b.z); }

ostream& operator<<(ostream& output, Point& a) {
    return output << "x=" << a.x << ", y=" << a.y << ", z=" << a.z << "\n";
}

class Octree{
public:
    Point base_point;
    Point top_point;
    Octree * ptr_father;
    Octree * ptr_child[8];
    Point data;

    Octree(){}
    ~Octree(){}
};

int main() {
    Point p1(1.0, 2.0, 3.0);
    Point p2(4.0, 5.0, 6.0);

    Point sum = p1 + p2;
    std::cout << "Sum: " << sum;

    return 0;
}