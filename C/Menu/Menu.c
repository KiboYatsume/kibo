#include<stdio.h>
#include<stdlib.h>

void DispalyMenu();
int main()
{
    int Choice;

    do
    {
        DispalyMenu();
        printf("Enter An Option:");
        scanf("%d",&Choice);
        switch(Choice)
        {
            case 1:
                printf("Option 1 has been Selected!");
                break;
            case 2:
                printf("Option 2 has been Selected!");
                break;
            case 3:
                printf("Option 3 has been Selected!");
                break;
            case 4:
                printf("Option 4 has been Selected! \n Exiting Program");
                exit(0);
            default:
                printf("Invalid Option , Select A Valid Option!");
        }
    } while (Choice != 4);

      return 0;
    
}
void DispalyMenu()
{
    printf("\n***Menu***\n");
    printf("1. Option 1 \n");
    printf("2. Option 2 \n");
    printf("3. Option 3 \n");
    printf("4. Exit \n");
}