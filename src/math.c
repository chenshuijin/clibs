#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "util.h"

char* add(char *l, char *r, int base)
{
  int len=0, i = 0, j = 0, c = 0, tmp = 0;
  char *result, *s, tmpc;
  lstrip(l, '0');lstrip(r, '0');
  if (strlen(l) < strlen(r)) return add(r, l, base);

  if ((result = (char*)malloc(strlen(l)+2)) == NULL) return NULL;
  memset(result, 0, strlen(l) + 2);

  reverse(l);reverse(r);
  strcpy(result, l);
  len = strlen(r);

  s = r;
  i = 0, c = 0, tmp = 0;

  while(1){
    if (i >= len) {
      if (c <= 0) break;
    }
    else tmp = ctoi(*(s+i));

    tmp += ctoi(*(result + i)) + c;

    c = tmp/base;
    tmp %=base;

    tmpc = itoc(tmp, base);
    *(result + i) = tmpc;
    i ++; tmp = 0;
  }

  reverse(l);reverse(r);reverse(result);
  lstrip(result, '0');

  return result;
}

char* muli(char *dest, char *l, int r, int base)
{
  int len = 0, i = 0, tmp = 0, c = 0;
  char *result;

  if (r == 0) return "0";

  lstrip(l, '0');
  len = strlen(l);
  if (len == 0) return "0";

  reverse(l);
  memset(dest, 0, len+2);

  i = 0; tmp = 0; c = 0;
  while(1) {
    if (i >= len) {
      if (c <= 0) break;
    }
    else tmp = r * ctoi(*(l+i));

    tmp += c;
    c = tmp/base;
    tmp %= base;
    *(dest + i) = itoc(tmp, base);
    i ++;
    tmp = 0;
  }
  reverse(l);
  reverse(dest);
  lstrip(dest, '0');
  return dest;
}

char* mul(char *l, char *r, int base)
{
  int len=0, i = 0, llen = 0, c = 0, tmp = 0;
  char *result, *s, *ms, tmpc;
  lstrip(l, '0');lstrip(r, '0');
  if (strlen(l) < strlen(r)) return mul(r, l, base);

  reverse(r);

  len = strlen(r);
  llen = strlen(l);

  if ((s=(char*)malloc(len+llen+2))==NULL)return NULL;
  memset(s, 0, len+llen+2);
  if ((ms=(char*)malloc(len+llen+2))==NULL)return NULL;
  memset(ms, 0, len+llen+2);

  i = 0, c = 0, tmp = 0;
  result = "0";
  while(i<len){
    s = rpad(s, l, '0', llen + i);
    muli(ms, s, ctoi(*(r+i)), base);
    result = add(result, ms, base);
    i++;
  }
  reverse(r);
  lstrip(result, '0');
  return result;
}
