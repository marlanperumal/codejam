#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/detail/standard_policies.hpp>
using ll = int64_t;
using ld = long double;
using ull = uint64_t;
using namespace std;
using namespace __gnu_pbds;

constexpr int P = 100;



map<int, int> solocnt;
vector<int> counts;
int curmax;


template <int y>
void mdf(int x) {
    int& sc = solocnt[x];
    --counts[sc];
    ++counts[sc += y];
    if (counts[curmax + 1]) {
        ++curmax;
    }

    if (!counts[curmax]) {
        --curmax;
    }
}

struct Val: private multiset<int> {
    template <int y>
    void self() {
        if (!empty()) {
            int v = *begin();
            if (v == *rbegin()) {
                mdf<y>(v);
            }
        }
    }

    void add(int x) {
        self<-1>(); 
        insert(x);
        self<1>();
    }

    bool rm(int x) {
        self<-1>();
        erase(find(x));
        self<1>();
        return empty();
    }
};

map<int, Val> vals;

void add(int x, int y) {
    vals[x].add(y);
}

void rm(int x, int y) {
    if (vals[x].rm(y)) {
        vals.erase(x);
    }
}

bool check() {
    return curmax + 1 >= vals.size();
}

const int INF = 1e8;

void init(int n) {
    solocnt.clear();
    vals.clear();
    counts = vector<int>(n + 3);
    counts[0] = INF;
    curmax = 0;
}



void solve() {
    int n;
    cin >> n;
    init(n);
    vector<int> l(n + 1, INF), r(n + 1, INF);
    for (int i = 0; i < n; ++i) {
        int a, b, d;
        cin >> d >> a >> b;
        l[i] = d + a;
        r[i] = d - b;
    }

    int p = 0;
    int anss = 0, ansc = 0;

    for (int i = 0; i < n; ++i) {
        while (p <= n && check()) {
            add(l[p], r[p]);
            ++p;
        }

        int cans = p - i - 1;
        if (cans > anss) {
            anss = cans;
            ansc = 0;
        }

        if (cans == anss) {
            ++ansc;
        }

        rm(l[i], r[i]);
    }

    cout << anss << " " << ansc << "\n";
}

int main() {
#ifdef BZ
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr); cout.setf(ios::fixed); cout.precision(20);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }
}