#include "lists.h"

/**
 * insert_node - Inserts node
 * @head: Head of the linked list
 * @number: number to be added to the list
 * Return: Pointer to a node or null if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (curr == NULL || number < curr->n)
	{
		new_node->next = curr;
		*head = new_node;
		return (new_node);
	}

	while (curr != NULL)
	{
		if (number < curr->next->n)
		{
			break;
		}
		curr = curr->next;
	}
	new_node->next = curr->next;
	curr->next = new_node;

	return (new_node);
}
