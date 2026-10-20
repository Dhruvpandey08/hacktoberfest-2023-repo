//Binary Serach program in C++
#include<bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};//sorted array
    int target = 7;//element to be searched
    int left = 0, right = arr.size() - 1;
    while(left <= right)
    {
        int mid = left + (right - left) / 2;//declaring the mid index
        if(arr[mid] == target)//if the element is found
        {
            cout << "Element found at index: " << mid << endl;
            return 0;
        }
        else if(arr[mid] < target)//if the element is greater than the mid element
        {
            left = mid + 1;
        }
        else//if the element is smaller than the mid element
        {
            right = mid - 1;
        }
    }
    cout << "Element not found" << endl;//if the element is not found in the array
    return 0;
}
