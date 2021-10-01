%{ 
int n = 0 ;  
%} 
  
%% 
  
"while"|"if"|"else" {n++;}  
  

"int"|"float" {n++;printf("\t keywords : %s", yytext);}   
  

[a-zA-Z_][a-zA-Z0-9_]* {n++;} 
  

"<="|"=="|"="|"++"|"-"|"*"|"+" {n++;}
  

[(){}|, ;]    {n++;} 
  

[0-9]*"."[0-9]+ {n++;}  
  

[0-9]+ {n++;}                        
  
.    ;
%% 

   
int yywrap(void){}

int main() 
  
{ 
      
    yylex();
      
    printf("\n total no. of token = %d\n", n);   
       
}