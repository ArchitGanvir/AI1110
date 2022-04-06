#include <stdio.h>

void print_plane_eq(int *n, int c)
{
  printf("%dx + %dy + %dz - %d = 0\n", n[0], n[1], n[2], c);
}

int main()
{
  int i;

  int n1[] = {2, 2, -3}, n2[] = {2, 5, 3}, n[3];
  int c1 = 7, c2 = 9, c;

  int lambda = 5;

  for (i = 0; i < 3; i++)
    n[i] = n1[i] + lambda * n2[i];
  c = c1 + lambda * c2;

  printf("The equation of the required plane is :-\n");
  print_plane_eq(n, c);

  return 0;
}
