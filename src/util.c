#include <stdio.h>
#include <string.h>

char* reverse(char *p)
{
  int len = strlen(p), i = 0;
  char tmp;
  while(i < len/2)
    {
      tmp = *(p+i);
      *(p + i) = *(p + len - 1 - i);
      *(p + len - 1 - i) = tmp;
      i ++;
    }
  return p;
}

int ctoi(char c)
{
  switch(c&0xf0){
  case 0x30:
    return c&0x0f;
  case 0x40:
  case 0x60:
    return (c&0x0f) + 9;
  default:
    return c;
  }
}

char itoc(int i, int base)
{
  if (i >= 0 && i < base)
    {
      if(i <= 9)
	return (i | (0xf0 & 0x3f));
      else
	return ((i-9) | (0xf0 & 0x4f));
    }
  else return i;
}

char* lstrip(char *s, char c)
{
  int i = 0, l = 0, j = 0;
  l = strlen(s);
  while(i < l - 1) {
    if(*(s+i) != c) break;
    i ++;
  }
  if (i <= 0) {
    return s;
  }
  memset(s, 0, sizeof(char)*i);
  while(j < l - i)
    {
      *(s + j) = *(s + i + j);
      *(s + i + j) = 0;
      j++;
    }
  memset(s+l-i, 0, sizeof(char)*i);
  return s;
}

char* rpad(char* dest, char *src, char c, int len)
{
  int i = 0, slen = 0;
  slen = strlen(src);
  memset(dest, 0, len+1);
  strcpy(dest, src);
  if (len <= slen){
    return dest;
  }
  memset(dest+slen, c, len-slen);
  return dest;
}
