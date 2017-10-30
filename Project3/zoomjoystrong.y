%{

#include <stdio.h>
#include "zoomjoystrong.h"

%}

%start statement_list

%token END
%token END_STATEMENT
%token POINT
%token LINE
%token CIRCLE
%token RECTANGLE
%token SET_COLOR
%token INT
%token FLOAT


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
		}

line:		LINE INT INT INT INT END_STATEMENT
		{
         	  line($2,$3,$4,$5);
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

int yyerror(s)
char *s;
{
  fprintf(stderr, "%s\n",s);
}

int yywrap()
{
  return(1);
}
