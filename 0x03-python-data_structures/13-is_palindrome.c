#include "lists.h"
#include <stdlib.h>

/**
 * rev_ltsk - Reverses a linked list
 * @head: Pointer
 * Return: Pointer
 */
listint_t *rev_ltsk(listint_t *head)
{
	listint_t *init_sk = NULL, *pres_sk = head, *next = NULL;

	while (pres_sk != NULL)
	{
		next = pres_sk->next;
		pres_sk->next = init_sk;
		init_sk = pres_sk;
		pres_sk = next;
	}
	return (init_sk);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer
 * Return: 1 if palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *snail = *head, *hare = *head, *half_init = *head;
	listint_t *half_fin = NULL, *init_snail = *head;
	int is_drome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (hare != NULL && hare->next != NULL)
	{
		hare = hare->next->next;
		init_snail = snail;
		snail = snail->next;
	}
	if (hare != NULL)
	{
		snail = snail->next;
	}
	half_fin = rev_ltsk(snail);
	half_init = *head;
	while (half_fin != NULL)
	{
		if (half_init->n != half_fin->n)
		{
			is_drome = 0;
			break;
		}
		half_init = half_init->next;
		half_fin = half_fin->next;
	}
	rev_ltsk(snail);
	init_snail->next = snail;
	return (is_drome);
}
