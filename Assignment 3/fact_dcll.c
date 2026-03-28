#include <stdio.h>
#include <stdlib.h>

// Node structure
struct Node {
    int digit;
    struct Node* next;
    struct Node* prev;
};

// Create a new node
struct Node* createNode(int d) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->digit = d;
    newNode->next = newNode;
    newNode->prev = newNode;
    return newNode;
}

// Insert digit at end
struct Node* insertEnd(struct Node* head, int d) {
    struct Node* newNode = createNode(d);

    if (head == NULL)
        return newNode;

    struct Node* tail = head->prev;

    tail->next = newNode;
    newNode->prev = tail;

    newNode->next = head;
    head->prev = newNode;

    return head;
}

// Multiply the number by x
struct Node* multiply(struct Node* head, int x) {
    struct Node* temp = head;
    int carry = 0;

    // Traverse circular list
    do {
        int prod = temp->digit * x + carry;
        temp->digit = prod % 10;
        carry = prod / 10;

        temp = temp->next;
    } while (temp != head);

    // Handle remaining carry
    while (carry) {
        head = insertEnd(head, carry % 10);
        carry /= 10;
    }

    return head;
}

// Compute factorial
struct Node* factorial(int n) {
    struct Node* head = createNode(1); // start with 1

    for (int i = 2; i <= n; i++) {
        head = multiply(head, i);
    }

    return head;
}

// Print factorial
void printList(struct Node* head) {
    struct Node* temp = head->prev; // start from most significant digit
    struct Node* start = temp;

    do {
        printf("%d", temp->digit);
        temp = temp->prev;
    } while (temp != start);

    printf("\n");
}

// Main function
int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);

    struct Node* result = factorial(n);

    printf("%d! = ", n);
    printList(result);

    return 0;
}