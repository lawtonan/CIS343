%{

#include <stdio.h>
#include "zoomjoystrong.tab.h"
#include "zoomjoystrong.h"

%}

%option noyywrap

%%

(end)		{return END;}
\;		{return END_STATEMENT;}
[0-9]+		{return INT;}
[0-9]*\.[0-9]+	{return FLOAT;}
(line)		{return LINE;}
(point)		{return POINT;}
(circle)	{return CIRCLE;}
(rectangle)	{return RECTANGLE;}
(set_color)	{return SET_COLOR;}
\t|\n|" "	;
.		{printf("You Messed Up");}

%%
