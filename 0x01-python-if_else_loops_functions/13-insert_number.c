#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 *is_list_sorted - checks if a linked list is sorted or not
 *@head: the head of the list
 *Return: 1 if the list is sorted else 0 is returned
 */

int is_list_sorted(listint_t *head)
{
listint_t *tmp = head;

while (tmp && tmp->next)
{
	if (tmp->n > tmp->next->n)
		return (0);
	tmp = tmp->next;
}
return (1);
}

/**
 *insert_node - inserts a node into a sorted linkded list
 *@head: the head of the linked list
 *@number: the number to insert
 *Return: the address of the new node
 */


listint_t   *insert_node(listint_t **head, int number)
{
listint_t *new = malloc(sizeof(listint_t));
listint_t *tmp = *head;

if (!new)
	return (NULL);
new->n = number;
new->next = NULL;
if (!is_list_sorted(*head))
{
	free(new);
	return (NULL);
}
if (!*head)
	*head = new;
else if (number <= (*head)->n)
{
	new->next = *head;
	*head = new;
}
else
{
while (tmp && tmp->next)
{
	if (number >= tmp->n && number <= tmp->next->n)
		break;
	tmp = tmp->next;
}
new->next = tmp->next;
tmp->next = new;
}
return (new);
}
