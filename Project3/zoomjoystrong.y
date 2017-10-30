%{

#include <stdio.h>
#include "zoomjoystrong.h"
int yyerror(char *s);

%}

%start statement_list

%union {
	int ival;
	float fval;
}

%token END
%token END_STATEMENT
%token POINT
%token LINE
%token CIRCLE
%token RECTANGLE
%token SET_COLOR
%token <ival> INT
%token <fval> FLOAT


%%                   /* beginning of rules section */

statement_list:
		statement
		| 
		statement statement_list
		;

statement:	line
		|
		point
		|
		circle
		|
		rectangle
		|
		set_color
		|
		end
		;

end:		END END_STATEMENT
		{
		finish();
		exit(0);
		}
		;

line:		LINE INT INT INT INT END_STATEMENT
		{
		  if($2 < 0 || $3 < 0 || $2 > WIDTH || $3 > HEIGHT){
		  	yyerror("HEIGHT or WIDTH is out of bounds");
		  }else{
         	 	line($2,$3,$4,$5);
		  }
         	}
		;

point:		POINT INT INT END_STATEMENT
		{
		  point($2,$3);
		}
		;

circle:		CIRCLE INT INT INT END_STATEMENT
		{
		  circle($2,$3,$4);
		}
		;

rectangle:	RECTANGLE INT INT INT INT END_STATEMENT
		{
		  rectangle($2,$3,$4,$5);
		}
		;

set_color:	SET_COLOR INT INT INT END_STATEMENT
		{
		  set_color($2,$3,$4);
		}

%%

main()
{
 setup();
 return(yyparse());
}

int yyerror(char *s)
{
  fprintf(stderr, "%s\n",s);
}

int yywrap()
{
  return(1);
}
