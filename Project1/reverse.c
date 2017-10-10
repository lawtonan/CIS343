#include "file_utils.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * The main function has all the functionality requried
 *
 * @param argc "The number of arguments"
 * @param argv "A list of the arguments"
 * @return int "Returns default."
 **/
int main(int argc, char** argv) {
	int exitCode = 0;

	//Checks if the number of arguments is the number required
	if (argc != 3) {
		printf("Usage: %s <INPUT_FILENAME> <OUTPUT_FILENAME>\n",
			argv[0]);	
	}
	else {
		//sets the input and output files from the arguments
		char* infile = argv[1];
		char* outfile = argv[2];

		// Reads the file from the infile and retruns the size
		char* buffer;
		int size = read_file(infile, &buffer);

		//The reverse functionality
		char temp;
		for (int i = 0; i < size/2; i++) {
			temp = *(buffer + i);
			*(buffer + i) = *(buffer + (size-1-i));
			*(buffer + (size-1-i)) = temp;
		}

		//Writes the file into an outfile
		 write_file(outfile, buffer, size);

		//frees the memory alocated
		free(buffer);
	}
	
	//default return
	return exitCode;
}
