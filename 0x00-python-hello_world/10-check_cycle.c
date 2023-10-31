#include "lists.h"

/**
 * check_cycle - Checks for a cycle.
 * @list: A pointer head of list
 *
 * Return: 0 if no cycle, 1 if cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *sl_ask = list, *quick_sk = list;

	if (list == NULL)
		return (0);
	while (quick_sk != NULL && quick_sk->next != NULL)
	{
		sl_ask = sl_ask->next;
		quick_sk = quick_sk->next->next;

		if (sl_ask == quick_sk)
			return (1);
	}
	return (0);
}
