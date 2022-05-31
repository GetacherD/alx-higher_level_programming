#include "lists.h"
/**
* insert_node - insert node in sorted list
* @head: head pointer
* @number: new value for the node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *Node, *new;

	Node = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (head == NULL || *head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	while (Node)
	{
		if (Node->n < number && Node->next->n > number)
		{
			new->next = Node->next;
			Node->next = new;
			return (new);
		}
		if (Node->next == NULL)
		{
			Node->next = new;
			new->next = NULL;
			return (new);
		}
		Node = Node->next;
	}
	return (NULL);
}
