#include<stdio.h>

float amount;
float atax;

int main(){
printf("enter an amount:");
scanf("%f",&amount);
atax = amount * 1.05;
printf("with tax added: %f",atax);
}
