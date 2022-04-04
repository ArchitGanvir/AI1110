#include <stdio.h>

int recdep(int P, int n, int r)
{
  int MV;
  MV = P * n + P * (n * (n + 1) / (2 * 12.0)) * (r / 100.0);
  return MV;
}

int main()
{
  int P, n, r, MV;
  P = 600;
  n = 2.5 * 12;
  r = 10;
  
  MV = recdep(P, n, r);
  printf("The maturity value of the recurring deposit is %d\n", MV);

  return 0;
}
