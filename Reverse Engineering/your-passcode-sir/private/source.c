#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

    char user_input[32];
    int result = 1;
    printf("It's easy give me the password: ");
    fgets(user_input, sizeof(user_input), stdin);

    if (user_input[0] != 'd') { printf("Incorrect!\n"); exit(1); }
    if (user_input[1] != 'a') { printf("Incorrect!\n"); exit(1); }
    if (user_input[2] != '@') { printf("Incorrect!\n"); exit(1); }
    if (user_input[3] != 'K') { printf("Incorrect!\n"); exit(1); }
    if (user_input[4] != 'e') { printf("Incorrect!\n"); exit(1); }
    if (user_input[5] != 'y') { printf("Incorrect!\n"); exit(1); }
    if (user_input[6] != 'i') { printf("Incorrect!\n"); exit(1); }
    if (user_input[7] != 's') { printf("Incorrect!\n"); exit(1); }
    if (user_input[8] != 'C') { printf("Incorrect!\n"); exit(1); }
    if (user_input[9] != 'o') { printf("Incorrect!\n"); exit(1); }
    if (user_input[10] != 'r') { printf("Incorrect!\n"); exit(1); }
    if (user_input[11] != 'r') { printf("Incorrect!\n"); exit(1); }
    if (user_input[12] != 'e') { printf("Incorrect!\n"); exit(1); }
    if (user_input[13] != 'c') { printf("Incorrect!\n"); exit(1); }
    if (user_input[14] != 't') { printf("Incorrect!\n"); exit(1); }
    if (user_input[15] != '!') { printf("Incorrect!\n"); exit(1); }
    if (user_input[16] != 'y') { printf("Incorrect!\n"); exit(1); }
    if (user_input[17] != 'e') { printf("Incorrect!\n"); exit(1); }
    printf("Password is correct!!\n");
    return 0;
}