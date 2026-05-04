#include<stdio.h>

int radius = 0;
float fraction = 4.0/3.0;
float y;
int main(){
printf("Enter the Radius of Sphere:");
scanf("%d",&radius);
y= fraction * 3.14 * radius * radius * radius;
printf("%f",y);
}
