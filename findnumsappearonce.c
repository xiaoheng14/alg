#include<stdio.h>
#include<stdlib.h>

void find(int arr[], int len)
{
	int i, j, k;
	for(i = 0; i < len; i++)
	{
		k = 0;
		for(j = 0; j < len; j++)
		{	
			if(arr[i] == arr[j])
			{
				k++; 
			}
		}
		if(k == 1)
		{
			printf("%d ", arr[i]);
		}
	}
	printf("\n");
}

int main()
{
	int arr[] = {1,2,3,4,1,2,3,5};
	int len = 0;
	len = sizeof(arr) / sizeof(arr[0]);
	find(arr, len);
	system("pause");
	return 0;
}


