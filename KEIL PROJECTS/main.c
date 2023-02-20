#include<stm32f10x.h>
int main(void)
{
	RCC->APB2ENR |= 0X10;
	GPIOA->CRH &= 0xFF0FFFFF;
	GPIOA->CRH |= 0x00300000;
}

