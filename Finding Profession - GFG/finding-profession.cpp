// { Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
// User function Template for C++

class Solution{
public:
    char profession(int level, int pos){
        if(level == 1 || pos==1) return 'E';
        char parent = profession(level-1, (pos+1)/2);
        if(pos&1) return parent;
        return parent == 'E' ? 'd':'E';
    }
};

// { Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int level, pos;
        cin>>level>>pos;
        
        Solution ob;
        if(ob.profession(level, pos) == 'd')
            cout<<"Doctor\n";
        else
            cout<<"Engineer\n";
    }
    return 0;
}  // } Driver Code Ends