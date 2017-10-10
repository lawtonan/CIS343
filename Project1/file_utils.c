#include "file_utils.h"
#include <string.h>
#include <sys/stat.h>
#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
/*
 * This method reads the file into a character array that can be acceced later
 *
 * @param filename "The file to be read in"
 * @param **buffer "A pointer to a location in memory where the array will be 	 *		    stored"
 * @return int "Returns the size of the file.
**/
int read_file( char* filename, char **buffer){
	//Finds Size of file (provided by professor)
	struct stat st;
	stat(filename, &st);
	int size = st.st_size;
	
	//Create and opens the file to be read from
	FILE *file;
	file = fopen(filename, "r");
	
	//if file doesn't exist, send an error
	if (file == NULL) {
		fprintf(stderr, "Error opening file. %s\n", strerror (errno));
		size = 0;
	}
	else {
		//Allocates memory for buffer
		*buffer  = malloc(size * sizeof(char));

		//Checks to see if malloc works
		if (*buffer == NULL){
			fprintf(stderr, "Error allocatiing memory %s\n", 
				strerror( errno));
		}	
		else{
			//reads information from file to the buffer
			fread(*buffer, size, 1, file);			
		}
		
		//Close file	
		fclose(file);		
	}

	//returns the size of the file to be used later
	return size;
}

/**
 * A method that writes the buffer into a new file.
 *
 * @param filename "The file to be written to"
 * @param *buffer "A pointer to the buffer*
 * @param size "The size of the file after reverse"
 * 
 * @return int "Default return"
 **/
int write_file( char* filename, char *buffer, int size){
	//creates the FILE to be written to
	FILE *outfile;
	outfile = fopen(filename, "w");

	//checks if file exists
	if (outfile == NULL) {
		fprintf(stderr, "Error opening file. %s\n", strerror( errno));
	}
	else {
		//writes the file from the buffer
		fwrite(buffer, size, 1, outfile);

		//closes file
		fclose(outfile);
	}
	
	//default return. If fwrite returns an int could return for error
	//checking, however, fwrite will send an error if there is one.
	return 0;
}
