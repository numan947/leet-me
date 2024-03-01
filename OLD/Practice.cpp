#include <bits/stdc++.h>
using namespace std;

#define EPS 1e-9
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define REP(i, a, b) for(int i=a; i<b; i++)


vi subset;
void subsetGeneration(int k, int n)
{
    if(k == n+1){
        REP(i,0,subset.size())
            cout<<subset[i]<<" ";
        cout<<endl;
        return;
    }
    subset.push_back(k);
    subsetGeneration(k+1, n);
    subset.pop_back();
    subsetGeneration(k+1, n);
}

void generateSubset(int n)
{
    subset.clear();

    subsetGeneration(1,n);

}

vi permutation;
bool p[10];

void generatePermutation(int n)
{
    if(permutation.size() == n){
        REP(i,0,permutation.size())
            cout<<permutation[i]<<" ";
        cout<<endl;
        return;
    }

    for(int i=1; i<=n; i++){
        if(p[i])continue;
        p[i] = true;
        permutation.push_back(i);
        generatePermutation(n);
        p[i] = false;
        permutation.pop_back();
    }
}


int arr[8] = {-1, 2, 4, -3, 5, 2, -5, 2};
void maximumSumSubArray(int n)
{
    int sum = 0, best = 0;

    for(int i=0; i<n; i++){
        sum = max(arr[i], arr[i]+sum);
        best = max(sum, best);
    }
    printf("%d\n", best);
}

int nqueen, nqueen_count;
bool col[100], diag1[2*100-1], diag2[2*100-1];
ll placeQueen(int y){ // y = which row we are placing the queen
    if(y == nqueen){
        return 1;
    }
    ll tmpC = 0;
    for(int x=0; x<nqueen; x++){
        //x = column number, we iterate over all of the columns of the current row to place a queen
        if(col[x] || diag1[x+y] || diag2[x-y+nqueen-1]) continue;
        col[x] = diag1[x+y] = diag2[x-y+nqueen-1] = true;
        tmpC += placeQueen(y+1);
        col[x] = diag1[x+y] = diag2[x-y+nqueen-1] = false;
    }
    return tmpC;
}

int getDiagSquareCount(int p, int n)
{
    if(p<=(2*n-1)/2)
        return p+1;
    else
        return 2*n - 1 - p;
}

int twoQueen(int n)
{
    ll count = 0;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            ll tp = (n*n) - (1+2*(n-1) + getDiagSquareCount(i+j,n)-1 + getDiagSquareCount(i-j+n-1, n)-1);
            cout<<i<<" "<<j<<" "<<tp<<endl;
            count += tp;
        }
    }

    return count;

}



int main()
{
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);

    printf("Hello World!\n");
    // generateSubset(4);

    // generatePermutation(5);

    // maximumSumSubArray(8);

    nqueen = 14;
    // cout<<placeQueen(0)<<endl;

    cout<<twoQueen(10)/2<<endl;
    return 0;
}