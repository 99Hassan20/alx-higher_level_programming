#include "lists.h"

/**
 *get_list_size - get the size of the list
 *@head: the head of the list
 *Return: return the size of the list
 */

int get_list_size(listint_t *head)
{
listint_t *tmp = head;
int size = 0;

while (tmp)
{
size++;
tmp = tmp->next;
}
return (size);
}

/**
 *get_element_at - gets an elment at a specific index
 *@head: the head of the list
 *@index: the index of the element to retrieve
 *Return: the element if found else -1
 */

int get_element_at(listint_t *head, int index)
{
int i = 0;
listint_t *tmp = head;

while (tmp)
{
if (i == index)
return (tmp->n);
i++;
tmp = tmp->next;
}
return (-1);
}

/**
 *is_palindrome - checks if a list is palindrome
 *@head: the head of the list
 *Return: 1 if true else 0
 */

int is_palindrome(listint_t **head)
{
listint_t *tmp = *head;
int last_index = get_list_size(*head) - 1;

while (tmp)
{
if (tmp->n != get_element_at(*head, last_index))
return (0);
last_index--;
tmp = tmp->next;
}
return (1);
}
