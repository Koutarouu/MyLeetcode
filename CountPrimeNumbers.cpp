/*
Count the number of prime numbers less than a non-negative number, n.
Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
*/
#include<iostream>
using namespace std;
class Solution {
	public:
	    int countPrimes(int N) {
	        const int NU=1000;//2000000;
	        
	        int i,j,a[NU+1];
	        
	        for(a[1]=0, i=2; i<=N; i++) a[i]=1;
	
	        for(i=2; i<=N/2; i++)
	            for(j=2; j<=N/i; j++)
	                a[i*j] = 0;
	
	        for(i=1, j=0; i<N; i++)
	            if(a[i]) j++;
	        
	        return j;
	    }
};

int main(){
	Solution s;
	int n;
	cout<<"Hasta que numero quiere contar primos: "<<endl;
	cin>>n;
	cout<<s.countPrimes(n);
}
