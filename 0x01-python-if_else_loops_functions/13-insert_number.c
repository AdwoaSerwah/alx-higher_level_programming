#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted list
 * @head: pointer to head of list
 * @number: Number
 * Return: Address or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_ask, *init_sk, *past_ask;

	if (head == NULL)
		return (NULL);
	new_ask = malloc(sizeof(listint_t));
	if (new_ask == NULL)
		return (NULL);
	new_ask->n = number;
	new_ask->next = NULL;
	init_sk = *head;
	past_ask = NULL;
	while (init_sk != NULL && init_sk->n < number)
	{
		past_ask = init_sk;
		init_sk = init_sk->next;
	}
	if (past_ask == NULL)
	{
		new_ask->next = *head;
		*head = new_ask;
	}
	else
	{
		past_ask->next = new_ask;
		new_ask->next = init_sk;
	}
	return (new_ask);
}
