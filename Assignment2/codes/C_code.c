#include <stdio.h>

void print_plane_eq(int *n, int c)
{
  printf("%dx + %dy + %dz - %d = 0\n", n[0], n[1], n[2], c);
}

//Adds elements of two arrays n1 and n2 and stores resultant elements in array n
void array_add(int *n, int *n1, int *n2, int num)
{
  num--;
  for (; num >= 0; num--)
    n[num] = n1[num] + n2[num];
}

//Multiplies each element of array n by the scalar lambda
void scalar_mult (int *n, int num, int lambda)
{
  num--;
  for (; num >= 0; num--)
    n[num] *= lambda;
}

//Multiplies row matrix (array) n by column matrix e; returns value of element of resulting singleton matrix
int rc_mult(int *n, int e[][1], int num)
{
  int res = 0;

  num--;
  for (; num >=0; num--)
    res += n[num] * e[num][0];

  return res;
}

int main()
{
  int i;

  int n1[] = {2, 2, -3}, n2[] = {2, 5, 3}, n[3];
  int c1 = 7, c2 = 9, c;

  int e1[][1] = {
                  {1},
                  {0},
                  {0}
                };
  int e3[][1] = {
                  {0},
                  {0},
                  {1}
                };

  int lambda;

  lambda = (rc_mult(n1, e3, 3) - rc_mult(n1, e1, 3)) / (rc_mult(n2, e1, 3) - rc_mult(n2, e3, 3));

  scalar_mult(n2, 3, lambda);
  array_add(n, n1, n2, 3);
  c = c1 + lambda * c2;

  printf("The equation of the required plane is :-\n");
  print_plane_eq(n, c);

  return 0;
}
