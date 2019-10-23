//Algoritmo de Euclides

#include<iostream>
using namespace std;

int mcd(int u, int v){
	int t;
	while(u>0){
		if(u<v) { t=u; u=v; v=t; };
		u-=v;
	}
	return v;
}

int main(){
	int x,y;
	while(cin>>x && cin>>y)
		if(x>0 && y>0) cout<<x<<' '<<y<<' '<<mcd(x,y)<<'\n';
	return 0;
}

//ejemplo de 461952 y 116298 el mcd de ambos es 18
