#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *Node, *new;
	if (head == NULL || *head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (*head);
	new->n = number;
	new->next = NULL;
	if (number < (*head)->n)
	{
		new->next= *head;
		*head = new;
		return (*head);
	}
	Node = *head;
	while(Node)
	{
		if(number >= Node->n && number <= Node->next->n)
		{
			new->next = Node->next;
			Node->next = new;
			return (*head);
		}
		Node = Node->next;
		if (Node->next == NULL)
		{
			Node->next = new;
			return (*head);
		}

	}
	return (*head);
}
