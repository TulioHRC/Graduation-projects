#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	printf("\n\n\tTradutor linguagem natural\n\n");

	// Recebendo dados
	printf("Digite o argumento que voce gostaria que fosse traduzido para a linguagem natural.\n");
	char string[100];
	char newString[100];
	fgets(string, 100, stdin);

	// Tradução
	int add = 0;
	for(int i = 0; i<100; i++){
		if(string[i]=='^'){
			strcat(newString, "e");
			puts(newString)
			add += 3
		} else if(string[i]=='v') {
			newString[i+add] = ' ';
			add += 1;
			newString[i+add] = 'o';
			add += 1;
			newString[i+add] = 'u';
			add += 1;
			newString[i+add] = ' ';
		} else {
			newString[i+add] = string[i];
		}
	}

	printf("\n%s\n\n", newString);

	return 0;
}
