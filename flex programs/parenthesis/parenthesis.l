%{
/* Checking if it is a well formed paranthesis or not */

#undef yywrap
#define yywrap() 1
int flag=0,ln=1;

%}

%%

"(" {flag++;	
}

")" { flag--;
}

[\n] {
	if(flag==0)
		printf("\n The paranthesis are balanced\n",ln);
	else
		printf("\n Not balanced\n",ln);
	flag=0;
	ln++;
}

%%

main()
{	
	
	yylex();
}