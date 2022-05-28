#include <math.h>
#include <cstdlib>      // srand,rand

int make_color(int id){
  std::srand(id);
  unsigned int color = rand() % 255;
  if(color>=255){
    color = 255;
  }
  return (int)color;
}
