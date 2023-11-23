#include "lists.h"
#include <stddef.h>

int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int array[3000] = {0};
	int len = 0, r_idx = 2999, tac = 0;

	if (head == NULL)
		return (1);

	ptr = *head;

	if (ptr == NULL || ptr->next == NULL)
		return (1);

	while (ptr != NULL)
	{
		array[r_idx] = ptr->n;
		len++;
		r_idx--;
		ptr = ptr->next;
	}
	ptr = *head;
	r_idx++;
	tac = len / 2;

	while (ptr != NULL && tac > 0)
	{
		if (ptr->n != array[r_idx])
			return (0);
		r_idx++;
		ptr = ptr->next;
		tac--;
	}

	return (1);
}
