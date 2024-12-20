#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void print_menu() {
    puts("1. Book a Flight.");
    puts("2. Cancel a flight");
    puts("3. Quit the program");
}

void whoisthis(char name[], char destination[], char referral[]) {

    int length = strlen(referral);

    for(int i=0; i<length; i++) {
        referral[i] = (referral[i] + ((strlen(name) + strlen(destination))%12)) % 256;
	printf("0x%hhx,",referral[i]);
	}
}


void booking() {
    char name[32];
    char address[32];
    char ssn[32];
    char destination[32];
    char referral[64];

    printf("Namamu sir/ms? ");
    fgets(name, sizeof(name), stdin);
    name[strcspn(name, "\n")] = '\0'; 

    printf("Alamat? ");
    fgets(address, sizeof(address), stdin);
    address[strcspn(address, "\n")] = '\0'; 
    
    printf("Social Security Number? ");
    fgets(ssn, sizeof(ssn), stdin);
    ssn[strcspn(ssn, "\n")] = '\0';

    printf("Mau kemana? ");
    fgets(destination, sizeof(destination), stdin);
    destination[strcspn(destination, "\n")] = '\0';

    printf("Punya kode referral? ");
    fgets(referral, sizeof(referral), stdin);
    referral[strcspn(referral, "\n")] = '\0';

    whoisthis(name,destination,referral);
}

int main() {
    puts("Welcome to Mumerica Airflight!");
    while(1) {
        print_menu();
        char menu[8];
        fgets(menu, sizeof(menu), stdin);
        menu[strcspn(menu, "\n")] = '\0';

        switch(atoi(menu)) {
            case(1):
                booking();
                exit(0);
            case(2):
                printf("Unfortunately this feature haven't been made yet..\n");
            case(3):
                exit(0);
            default:
                puts("Incorrect option!");
        };
    };
}
