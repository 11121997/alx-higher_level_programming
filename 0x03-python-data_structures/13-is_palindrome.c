#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - function that checks if a list is a palindrome
 * @head: head node of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (get_palindrome(head, *head));
}

/**
 * get_palindrome - function get two nodes in the list
 * @head: first node
 * @end: last node
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int get_palindrome(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (get_palindrome(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
