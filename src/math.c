#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "util.h"

char* add(char *l, char *r, int base)
{
  int len=0, i = 0, j = 0, c = 0, tmp = 0;
  char *result, *s;
  lstrip(l, '0');lstrip(r,'0');
  if (strlen(l) < strlen(r)) return add(r, l, base);

  if ((result = (char*)malloc(strlen(l)+2)) == NULL) return NULL;
  memset(result, 0, strlen(result));

  reverse(l);reverse(r);
  strcpy(result, l);
  len = strlen(r);

  s = r;
  i = 0, c = 0;
  //  printf("res len:%d\n", len);
  while(1){
    //    printf("===============%d=====================\n",i);
    if (i >= len) {
      if (c <= 0) break;
    }
    else tmp = ctoi(*(s+i));

    //    printf("r:%x\n", ctoi(*(result+i)));
    tmp += ctoi(*(result + i)) + c;
    //    printf("aftertmp:%x\n", tmp);
    c = tmp/base;
    tmp %=base;
    //    printf("tmp:%x\n", tmp);
    //    printf("c:%x\n", c);
    *(result + i) = itoc(tmp, base);
    i ++; tmp = 0;
  }
  reverse(l);reverse(r);reverse(result);
  return result;
}
