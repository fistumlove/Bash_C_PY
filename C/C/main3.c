#include <stdio.h>

int main () {
   FILE *fp;
   char str[600];

   /* opening file for reading */
   fp = fopen("/home/fistum/Desktop/hosts.new" , "r"); //file.txt
   if(fp == NULL) {
      perror("Error opening file");
      return(-1);
   }
   if( fgets (str, 600, fp)!=NULL ) {
      /* writing content to stdout */
      puts(str);
   }
   fclose(fp);
   
   return(0);
}