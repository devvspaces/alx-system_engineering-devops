#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - Creates an infinite loop to make the program hang.
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
    while (1)
        sleep(1);
    return (0);
}

/**
 * main - Creates 5 zombie processes for the parent process.
 *
 * Return: Always return 0.
 */
int main(void)
{
    pid_t pid;
    char count = 0;

    while (count < 5)
    {
        pid = fork();
        if (pid > 0)
        {
            printf("Zombie process created, PID: %d\n", pid);
            sleep(1);
            count++;
        }
        else
            exit(0);
    }

    infinite_while();

    return (EXIT_SUCCESS);
}
