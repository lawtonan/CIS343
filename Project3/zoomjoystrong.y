/****************************************************************************** 
* This is a parsing program used in our own language of Zoomjoystrong. 
* It contains the grammar rules of the language and uses C code to 
* call the provided graphics library to display the different functions
* of Zoomjoystrong.
*
* @author Andrew Lawton
*******************************************************************************/
%{

#include <stdio.h>
#include "zoomjoystrong.h"
/** Explicitly defining the yyerror and yylex commands */
int yyerror(char *s);
int yylex(void);

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
		  /* Calls finish for the drawing software */
		  finish();
		  /* Calls exit to leave the program */
		  exit(0);
		}
		;

line:		LINE INT INT INT INT END_STATEMENT
		{
		  /* Checks if starting point is out of bounds */
		  if($2 < 0 || $3 < 0 || $2 > WIDTH || $3 > HEIGHT){
		  	yyerror("Starting point out of bounds");
		  }else{
         	 	line($2,$3,$4,$5);
		  }
         	}
		;

point:		POINT INT INT END_STATEMENT
		{
		  /* Checks if point is out of bounds */
		  if($2 < 0 || $3 < 0 || $2 > WIDTH || $3 > HEIGHT){
		  	yyerror("Point out of bounds");
		  }else{
         	 	point($2,$3);
		  }
		}
		;

circle:		CIRCLE INT INT INT END_STATEMENT
		{
		  /* Checks if center is out of bounds */
		  if($2 < 0 || $3 < 0 || $2 > WIDTH || $3 > HEIGHT){
		  	yyerror("Center out of bounds");
		  }else{
		  	circle($2,$3,$4);
		  }
		}
		;

rectangle:	RECTANGLE INT INT INT INT END_STATEMENT
		{
		  /* Checks if corner is out of bounds */
		  if($2 < 0 || $3 < 0 || $2 > WIDTH || $3 > HEIGHT){
		  	yyerror("Corner out of bounds");
		  }else{
		  	rectangle($2,$3,$4,$5);
		  }
		}
		;

set_color:	SET_COLOR INT INT INT END_STATEMENT
		{
		  /* Checks if color codes are 0-255 */
		  if ($2<0 || $3<0 || $4<0 || $2>255 || $3>255 || $4>255){
			yyerror("Color Does Not Exist");
		  }else {
		  	set_color($2,$3,$4);
		  }
		}

%%

int main()
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
