

#include<bits/stdc++.h> 

using namespace std; 

void restoreDown(int arr[], int len, int index, 
										int k) 
{ 
	
	int child[k+1]; 

	while (1) 
	{ 	
		
		for (int i=1; i<=k; i++) 
			child[i] = ((k*index + i) < len) ? 
					(k*index + i) : -1; 

		int max_child = -1, max_child_index ; 
	
		for (int i=1; i<=k; i++) 
		{ 
			if (child[i] != -1 && 
				arr[child[i]] > max_child) 
			{ 
				max_child_index = child[i]; 
				max_child = arr[child[i]]; 
			} 
		} 

		
		if (max_child == -1) 
			break; 

		
		
		if (arr[index] < arr[max_child_index]) 
			swap(arr[index], arr[max_child_index]); 

		index = max_child_index; 
	} 
} 



void restoreUp(int arr[], int index, int k) 
{ 
	
	
	int parent = (index-1)/k; 

	
	
	
	while (parent>=0) 
	{ 
		if (arr[index] > arr[parent]) 
		{ 
			swap(arr[index], arr[parent]); 
			index = parent; 
			parent = (index -1)/k; 
		} 

		
		else
			break; 
	} 
} 


void buildHeap(int arr[], int n, int k) 
{ 
	
	
	
	for (int i= (n-1)/k; i>=0; i--) 
		restoreDown(arr, n, i, k); 
} 




void insert(int arr[], int* n, int k, int elem) 
{ 
	
	arr[*n] = elem; 

	
	*n = *n+1; 

	
	restoreUp(arr, *n-1, k); 
} 




int extractMax(int arr[], int* n, int k) 
{ 
	
	int max = arr[0]; 

	
	arr[0] = arr[*n-1]; 

	
	*n = *n-1; 

	
	
	restoreDown(arr, *n, 0, k); 

	return max; 
} 


int main() 
{ 
	const int capacity = 100; 
	int arr[capacity] = {4, 5, 6, 7, 8, 9, 10}; 
	int n = 7; 
	int k = 3; 

	buildHeap(arr, n, k); 

	printf("Built Heap : \n"); 
	for (int i=0; i<n; i++) 
		printf("%d ", arr[i]); 

	int element = 3; 
	insert(arr, &n, k, element); 

	printf("\n\nHeap after insertion of %d: \n", 
			element); 
	for (int i=0; i<n; i++) 
		printf("%d ", arr[i]); 

	printf("\n\nExtracted max is %d", 
				extractMax(arr, &n, k)); 

	printf("\n\nHeap after extract max: \n"); 
	for (int i=0; i<n; i++) 
		printf("%d ", arr[i]); 

	return 0; 
} 
