#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it
 * @list: head node
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *by_one = list, *by_two = list;

	while (by_two && by_two->next)
	{
		by_one = by_one->next;
		by_two = by_two->next->next;
		if (by_one == by_two)
			return (1);
	}
	return (0);
}
