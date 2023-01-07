/*
 * Tracing 'malloc' c program 01
 */

#include <stdlib.h>

int main(int argc, char *argv[])
{
	char *s = malloc (10);
	free (s);
	return 0;
}
