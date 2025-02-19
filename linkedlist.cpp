




#include "linkedlist.h"

LinkedList::LinkedList()
{
    head = nullptr;
    tail = nullptr;
    size = 0;
}

LinkedList::~LinkedList()
{
    if (size > 0)
    {
        Node* temp;

        while (head != nullptr)
        {
            // grabs the node after the head
            temp = head->next;

            // deletes the head
            delete head;

            // reassigns the head
            head = temp;
        }
    }
}

// given to students
void LinkedList::append(string title, string author)
{
    // if the list is currently empty
    if (size == 0)
    {
        // create a new node at the head
        // with the information brought in
        head = new Node(title, author);

        // assigns tail to the head
        tail = head;
    }

    // otherwise, if it's not empty
    else
    {
        // creates a new node
        // with the information brought in
        Node* temp = new Node(title, author);

        // point current tail to new node
        tail->next = temp;

        // make new node the new tail
        tail = temp;
    }

    size++;
}

int LinkedList::pop()
{
    // error check:
    // checks if the current size is zero
    if (size == 0)
    {
        cout << "List was empty -- pop failed!" << endl;
        return 1; // exits from the function with fail flag
    }

    // if removing a node will empty the list
    if (size == 1)
    {
        // store current head
        Node* temp = head;

        // sanity check clear head and tail
        head = nullptr;
        tail = nullptr;

        // delete node
        delete temp;
    }

    // otherwise, if it won't
    else
    {
        // start a temporary node at the head
        Node* temp = head;

        // loop to one before the tail
        while (temp->next->next != nullptr)
        {
            temp = temp->next;
        }

        // delete the current tail
        delete tail;

        // sanity check clear the next pointer
        // and assign the new tail
        tail = temp;
        tail->next = nullptr;
    }

    size--;

    return 0;
}

int LinkedList::display()
{
    // error check:
    // checks if the current size is zero
    if (size == 0)
    {
        cout << "List was empty -- display failed!" << endl;
        return 1; // exits from the function with fail flag
    }

    // starts temporary Node at the beginning (head)
    Node* temp = head;
    int count = 0;

    while (temp != nullptr)
    {
        // displays information
        cout << "Book " << count << ": ";
        cout << temp->title << " by " << temp->author << endl;

        // moves the temp node to the next node in the sequence
        temp = temp->next;

        count++;
    }

    return 0;
}

// you must create
int LinkedList::insert(string title, string author, int position)
{
    // error check: if the position is out of range
    if (position < 0 || position > size)
    {
        cout << "Not a valid insert -- out of range!" << endl;
        return 1;
    }

    // if inserting at the end
    if (position == size) {
        append(title, author);
        return 0;
    }
    // if inserting at the beginning
    else if (position == 0) {
        Node* newNode = new Node(title, author, head);
        head = newNode;
    }
    // inserting in the middle
    else {
        Node* temp = head;
        for (int i = 0; i < position - 1; ++i) {
            temp = temp->next;
        }
        Node* newNode = new Node(title, author);
        newNode->next = temp->next;
        temp->next = newNode;
    }

    size++;
    return 0;
}


int LinkedList::remove(int position)
{
    if (position < 0 || position >= size)
    {
        cout << "Not a valid remove -- out of range!" << endl;
        return 1;
    }


    // if removing the head
    if (position == 0) {
        Node* temp = head;
        head = head->next;
        delete temp;
        if (size == 1) {
            tail = nullptr;
        }
    }
    // if removing the tail
    else if (position == size - 1) {
        Node* temp = head;
        while (temp->next->next != nullptr) {
            temp = temp->next;
        }
        delete tail;
        tail = temp;
        tail->next = nullptr;
    }
    // removing from the middle
    else {
        Node* temp = head;
        for (int i = 0; i < position - 1; ++i) {
            temp = temp->next;
        }
        Node* toDelete = temp->next;
        temp->next = toDelete->next;
        delete toDelete;
    }

    size--;
    return 0;

    }   

int LinkedList::view(int position)
{
    if (position < 0 || position >= size)
    {
        cout << "Not a valid view -- out of range!" << endl;
        return 1;

    }

    Node* temp = head;
    for (int i = 0; i < position; ++i)
    {
        temp = temp->next;
    }

    cout << temp->title << " by " << temp->author << endl;
    return 0;


}