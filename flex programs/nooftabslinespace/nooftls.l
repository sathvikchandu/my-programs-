%{
	#include<stdio.h>
	int lc = 0, sc = 0, tc = 0, ch = 0;
%}

%%
\n lc++;
([ ])+ sc++;
\t tc++;
. ch++;
%%
int yywrap(void){}

int main()
{
	yylex();

	printf("\n No. of lines = %d", lc);
	printf("\n No. of spaces = %d", sc);
	printf("\n No. of tab spaces = %d", tc);
	printf("\n No. of characters = %d", ch);
}
