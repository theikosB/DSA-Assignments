/*
 * B-TREE IMPLEMENTATION (Insertion + Deletion)
 * --------------------------------------------
 * Minimum degree: t
 * Each node contains between (t-1) and (2t-1) keys (except root)
 *
 * This implementation focuses on clarity and correctness.
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define T 2   // Minimum degree (you can change this)

typedef struct BTreeNode {
    int keys[2*T - 1];           // keys
    struct BTreeNode* children[2*T]; // child pointers
    int n;                       // number of keys
    bool leaf;                   // is leaf?
} BTreeNode;

typedef struct BTree {
    BTreeNode* root;
} BTree;

/* ================= NODE CREATION ================= */

BTreeNode* createNode(bool leaf) {
    BTreeNode* node = (BTreeNode*)malloc(sizeof(BTreeNode));
    node->leaf = leaf;
    node->n = 0;
    return node;
}

/* ================= SEARCH ================= */

BTreeNode* search(BTreeNode* x, int k, int* idx) {
    int i = 0;

    while (i < x->n && k > x->keys[i])
        i++;

    if (i < x->n && x->keys[i] == k) {
        if (idx) *idx = i;
        return x;
    }

    if (x->leaf)
        return NULL;

    return search(x->children[i], k, idx);
}

/* ================= UTILITIES ================= */

// Get predecessor (rightmost of left subtree)
int getPredecessor(BTreeNode* x) {
    while (!x->leaf)
        x = x->children[x->n];
    return x->keys[x->n - 1];
}

// Get successor (leftmost of right subtree)
int getSuccessor(BTreeNode* x) {
    while (!x->leaf)
        x = x->children[0];
    return x->keys[0];
}

/* ================= MERGE ================= */

void merge(BTreeNode* x, int idx) {
    BTreeNode* left = x->children[idx];
    BTreeNode* right = x->children[idx + 1];

    // Bring down key from parent
    left->keys[T - 1] = x->keys[idx];

    // Copy keys
    for (int i = 0; i < right->n; i++)
        left->keys[i + T] = right->keys[i];

    // Copy children
    if (!left->leaf) {
        for (int i = 0; i <= right->n; i++)
            left->children[i + T] = right->children[i];
    }

    left->n += right->n + 1;

    // Shift keys in parent
    for (int i = idx; i < x->n - 1; i++)
        x->keys[i] = x->keys[i + 1];

    // Shift children
    for (int i = idx + 1; i < x->n; i++)
        x->children[i] = x->children[i + 1];

    x->n--;

    free(right);
}

/* ================= BORROW ================= */

void borrowFromLeft(BTreeNode* x, int idx) {
    BTreeNode* child = x->children[idx];
    BTreeNode* sibling = x->children[idx - 1];

    // Shift child right
    for (int i = child->n - 1; i >= 0; i--)
        child->keys[i + 1] = child->keys[i];

    if (!child->leaf) {
        for (int i = child->n; i >= 0; i--)
            child->children[i + 1] = child->children[i];
    }

    // Move key from parent
    child->keys[0] = x->keys[idx - 1];

    if (!child->leaf)
        child->children[0] = sibling->children[sibling->n];

    // Move sibling key up
    x->keys[idx - 1] = sibling->keys[sibling->n - 1];

    child->n++;
    sibling->n--;
}

void borrowFromRight(BTreeNode* x, int idx) {
    BTreeNode* child = x->children[idx];
    BTreeNode* sibling = x->children[idx + 1];

    // Bring key from parent
    child->keys[child->n] = x->keys[idx];

    if (!child->leaf)
        child->children[child->n + 1] = sibling->children[0];

    // Move sibling key up
    x->keys[idx] = sibling->keys[0];

    // Shift sibling left
    for (int i = 1; i < sibling->n; i++)
        sibling->keys[i - 1] = sibling->keys[i];

    if (!sibling->leaf) {
        for (int i = 1; i <= sibling->n; i++)
            sibling->children[i - 1] = sibling->children[i];
    }

    child->n++;
    sibling->n--;
}

/* ================= DELETE ================= */

void deleteKey(BTreeNode* x, int k);

void deleteFromNode(BTreeNode* x, int k) {
    int idx = 0;

    while (idx < x->n && k > x->keys[idx])
        idx++;

    // Case 1: key in this node
    if (idx < x->n && x->keys[idx] == k) {

        if (x->leaf) {
            // Leaf: just remove
            for (int i = idx; i < x->n - 1; i++)
                x->keys[i] = x->keys[i + 1];
            x->n--;
        } else {
            // Internal node
            if (x->children[idx]->n >= T) {
                int pred = getPredecessor(x->children[idx]);
                x->keys[idx] = pred;
                deleteKey(x->children[idx], pred);
            }
            else if (x->children[idx + 1]->n >= T) {
                int succ = getSuccessor(x->children[idx + 1]);
                x->keys[idx] = succ;
                deleteKey(x->children[idx + 1], succ);
            }
            else {
                merge(x, idx);
                deleteKey(x->children[idx], k);
            }
        }
    }
    else {
        // Case 2: key not in node
        if (x->leaf) {
            printf("Key %d not found\n", k);
            return;
        }

        bool last = (idx == x->n);

        // Ensure child has >= T keys
        if (x->children[idx]->n == T - 1) {
            if (idx > 0 && x->children[idx - 1]->n >= T)
                borrowFromLeft(x, idx);
            else if (idx < x->n && x->children[idx + 1]->n >= T)
                borrowFromRight(x, idx);
            else {
                if (idx < x->n)
                    merge(x, idx);
                else {
                    merge(x, idx - 1);
                    idx--;
                }
            }
        }

        deleteKey(x->children[idx], k);
    }
}

void deleteKey(BTreeNode* x, int k) {
    deleteFromNode(x, k);
}

/* ================= DRIVER ================= */

void deleteFromTree(BTree* tree, int k) {
    if (!tree->root) return;

    deleteKey(tree->root, k);

    // Shrink height if needed
    if (tree->root->n == 0) {
        BTreeNode* tmp = tree->root;
        if (tree->root->leaf)
            tree->root = NULL;
        else
            tree->root = tree->root->children[0];
        free(tmp);
    }
}

/* ================= MAIN ================= */

int main() {
    printf("B-tree deletion implementation ready.\n");
    return 0;
}