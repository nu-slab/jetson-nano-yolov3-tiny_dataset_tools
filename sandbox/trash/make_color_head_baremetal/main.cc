#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <cstdlib>

#include "vis_module.h"
//#include "color_setting.h"

#define DEFAULT_CLASS 80
#define CHANNEL 3

int main(){
  std::ofstream ofs("color_setting.h");
  std::stringstream default_cls_str,channel_str;
  default_cls_str << DEFAULT_CLASS; channel_str << CHANNEL;
  ofs << "int color_setting[" << default_cls_str.str() <<"]["<<channel_str.str()<<"]={"<<std::endl;
  for(int i=0;i<DEFAULT_CLASS;i++){
    ofs << "{";
    for(int j=0;j<CHANNEL;j++){
      std::stringstream tmp_str;
      tmp_str << make_color(i*CHANNEL+j);
      ofs << tmp_str.str();
      if(j==CHANNEL-1){
	if(i==DEFAULT_CLASS-1)
	  ofs << "}" << std::endl;
	else
	  ofs << "}," << std::endl;
      }
      else
	ofs << ","; 
    }
  }
  ofs << "};";
  return 0;
}
