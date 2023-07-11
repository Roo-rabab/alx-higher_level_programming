#include <stdio.h>
/**
 *main - Entry point
 *Return: Always 0 (Success)
 */
int main(void)
{

char ch = 'a', chUpper = 'A';

while (ch <= 'z')
{
putchar(ch);
ch++;
}

while (chUpper <= 'Z')
{
putchar(chUpper);
chUpper++;
}

putchar('\n');

return (0);
}
