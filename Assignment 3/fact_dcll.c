#include <stdio.h>
#include <stdlib.h>

// Doubly circular linked list node storing one digit
struct Node {
    int digit;
    struct Node* next;
    struct Node* prev;
};

// Create a new node initialized with digit d
struct Node* createNode(int d) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->digit = d;
    newNode->next = newNode; // 1-Circular dll
    newNode->prev = newNode;
    return newNode;
}

// Insert a digit at the end (highest place value)
struct Node* insertEnd(struct Node* head, int d) {
    struct Node* newNode = createNode(d);

    if (head == NULL)
        return newNode;

    struct Node* tail = head->prev;

    // Link new node between tail and head
    tail->next = newNode;
    newNode->prev = tail;
    newNode->next = head;
    head->prev = newNode;

    return head;
}

// Multiply the dcll (number) by x
struct Node* multiply(struct Node* head, int x) {
    struct Node* temp = head;
    int carry = 0;

    // Traverse all digits (lowest to highest place value)
    do {
        int prod = temp->digit * x + carry;
        temp->digit = prod % 10;   // store current digit
        carry = prod / 10;         // carry forward

        temp = temp->next;
    } while (temp != head);

    // Append remaining carry as new digits
    while (carry) {
        head = insertEnd(head, carry % 10);
        carry /= 10;
    }

    return head;
}

// Print number in correct order (highest to lowest place value)
void printList(struct Node* head) {
    struct Node* temp = head->prev; // start from highest place value (tail)
    struct Node* start = temp;

    do {
        printf("%d", temp->digit);
        temp = temp->prev;
    } while (temp != start);

    printf("\n");
}

// Compute n! using repeated multiplication
struct Node* factorial(int n) {
    struct Node* head = createNode(1); // initialize with 1

    for (int i = 2; i <= n; i++) {
        head = multiply(head, i);
    }

    return head;
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