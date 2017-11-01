/******************************************************************************** This is a lexing program used if our own language of Zoomjoystrong.
* It contains the regular expressions used to return tokens to the parsing
* program to check if they fall into the valid grammar. 
* 
* @author Andrew Lawton
*******************************************************************************/
%{

#include <stdio.h>
#include "zoomjoystrong.tab.h"
#include "zoomjoystrong.h"

%}

%option noyywrap

%%

(end)		{return END;}
\;		{return END_STATEMENT;}
[0-9]+		{
		yylval.ival = atoi(yytext);
		return INT;
		}
[0-9]*\.[0-9]+	{
		yylval.fval = atof(yytext);
		return FLOAT;
		}
(line)		{return LINE;}
(point)		{return POINT;}
(circle)	{return CIRCLE;}
(rectangle)	{return RECTANGLE;}
(set_color)	{return SET_COLOR;}
\t|\n|" "	;
.		{printf("You Messed Up");}

%%
