%{
#include<stdio.h>
#include<stdlib.h>
int lon=0;
%}
%%
[0-9a-zA-Z]+ {
    if(yyleng>lon){
        lon = yyleng;
    }
}

%%
int yywrap(){return 1;}
int main()
{
printf("Enter a strings:\n");
yylex();
    printf("The length of the longest word is : %d",lon);

}