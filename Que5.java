// Java program for the above approach

class GFG {

	// structure of node of
	// doubly linked list
	static class Node {
		int data;
		Node next, prev;
	};

	// A utility function to insert
	// a new node at the beginning
	// of the doubly linked list
	static Node insert(Node head, int data)
	{

		// Allocate the node
		Node temp = new Node();

		// Fill in the data value
		temp.data = data;
		temp.next = temp.prev = null;
		if (head == null)
			(head) = temp;
		else {
			temp.next = head;
			(head).prev = temp;
			(head) = temp;
		}
		return temp;
	}

	// Function to print the quadruples
	// having sum equal to x
	static void PrintFourSum(Node head, int x)
	{

		// First pointer to the head node
		Node first = head;

		// Pointer to point to the second
		// node for the required sum
		Node second = head;

		// Pointer to point to the third
		// node for the required sum
		Node third = head;

		// Fourth points to the last node
		Node fourth = head;

		// Update the fourth pointer to
		// the end of the DLL
		while (fourth.next != null) {
			fourth = fourth.next;
		}

		// Node to point to the fourth node
		// of the required sum
		Node temp;
		while (first != null && fourth != null
			&& first != fourth && fourth.next != first) {

			// Point the second node to the
			// second element of quadruple
			second = first.next;

			while (second != null && fourth != null
				&& second != fourth
				&& fourth.next != second) {

				int reqsum = x - (first.data + second.data);

				// Points to the 3rd element
				// of quadruple
				third = second.next;

				// Points to the tail of the DLL
				temp = fourth;

				while (third != null && temp != null
					&& third != temp
					&& temp.next != third) {

					// Store the current sum
					int twosum = third.data + temp.data;

					// If the sum is equal,
					// then print quadruple
					if (twosum == reqsum) {

						System.out.println(
							"(" + first.data + ", "
							+ second.data + ", "
							+ third.data + ", " + temp.data
							+ ")");

						third = third.next;
						temp = temp.prev;
					}

					// If twosum is less than
					// the reqsum then move the
					// third pointer to the next
					else if (twosum < reqsum) {
						third = third.next;
					}

					// Otherwise move the fourth
					// pointer to the previous
					// of the fourth pointer
					else {
						temp = temp.prev;
					}
				}

				// Move to the next of
				// the second pointer
				second = second.next;
			}

			// Move to the next of
			// the first pointer
			first = first.next;
		}
	}

	// Driver Code
	public static void main(String args[])
	{

		Node head = null;
		head = insert(head, 2);
		head = insert(head, 1);
		head = insert(head, 0);
		head = insert(head, 0);
		head = insert(head, -1);
		head = insert(head, -2);
		int x = 0;

		PrintFourSum(head, x);
	}
}

// This code is contributed
// by kirtishsurangalikar
