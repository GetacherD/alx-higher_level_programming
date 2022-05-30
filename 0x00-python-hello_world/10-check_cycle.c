#include "lists.h"
/**
* check_cycle - check if cycle found in list
* @list: head pointer
* Return: 1 if cycle found else 0
*/
int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	first = list;
	second = list;
	while (first)
	{
		if (first == first->next)
			return (1);
		while (second != first)
		{
			if (second == first->next)
				return (1);
			second = second->next;
		}
		second = list;
		first = first->next;
	}
	return (0);
}


