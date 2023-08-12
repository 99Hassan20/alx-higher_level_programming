#include "lists.h"

/**
 * list_to_array - converts a linked list to an array
 * @head: the head of the list
 * @size: the size of the array
 * Return: return an array
 */

int *list_to_array(listint_t *head, int size)
{
int i = 0;
int *array = malloc(sizeof(int) * size);

listint_t *tmp = head;
if (!array)
return (NULL);
while (tmp)
{
array[i] = tmp->n;
i++;
tmp = tmp->next;
}
return (array);
}


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
int list_size = get_list_size(*head);
int *array = list_to_array(*head, list_size);
int last = list_size - 1;
int begin = 0;

while (begin < last)
{
if (array[begin] != array[last])
return (0);
last--;
begin++;
}
free(array);
return (1);
}
