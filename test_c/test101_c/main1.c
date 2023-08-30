#include "main.h"




// Node Initializing!
struct node *HEAD;
struct node *ONE = NULL;
struct node *TWO = NULL;
struct node *THREE = NULL;

// Allocating memory!
ONE = malloc(sizeof(struct node));
TWO = malloc(sizeof(struct node));
THREE = malloc(sizeof(struct node));

// Assigning the values of data!
ONE->data = 23;
TWO->data = 34;
THREE->data = 90;

// Connecting nodes with each other!
ONE->next = TWO;
TWO->next = THREE;
THREE->next = NULL;

// Saving the address of first node
HEAD = ONE;