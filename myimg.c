#include <math.h>

#define NROWS 400
#define NCOLS 400

int image_nrows() { return NROWS; }
int image_ncols() { return NCOLS; }

void image_get(double *img)
{
  int i, j;
  for (i = 0; i < NROWS; i++)
    for (j = 0; j < NCOLS; j++)
      img[i*NCOLS+j] = sin(i*4*M_PI/NROWS)*cos(j*4*M_PI/NCOLS);
}

