#include <stdio.h>
#include <stdlib.h>

int lomuto_comp_count = 0, hoare_comp_count = 0;
int lomuto_swap_count = 0, hoare_swap_count = 0;

void swap_elements(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int lomuto_partition(int a[], int low, int high)
{
    int pivot, pivotPos, tmp;
    int i, j;
    pivot = a[low];
    j = low;
    for (i = low + 1; i <= high; i++)
    {
        lomuto_comp_count++;
        if (a[i] < pivot)
        {
            j++;
            lomuto_swap_count++;
            swap_elements(&a[i], &a[j]);
        }
    }
    pivotPos = j;
    lomuto_swap_count++;
    swap_elements(&a[low], &a[pivotPos]);

    return pivotPos;
}

int hoare_partition(int a[], int low, int high)
{
    int pivot, pivotPos, tmp;
    int i, j;

    pivot = a[low];
    i = low - 1;
    j = high + 1;
    while (1)
    {
        do 
        {
            hoare_comp_count++;
            i++;
        } while (a[i] < pivot);
        
        do 
        {
            hoare_comp_count++;
            j--;
        } while (a[j] > pivot);

        if (i < j)
        {
            hoare_swap_count++;
            swap_elements(&a[i], &a[j]);
        }
        else
            return j;
    }
    pivotPos = j;
    hoare_swap_count++;
    swap_elements(&a[low], &a[pivotPos]);

    return pivotPos;
}

void quick_sort_lomuto(int v[], int low, int high)
{
    int pivotPos;
    if (high > low)
    {
        pivotPos = lomuto_partition(v, low, high);
        quick_sort_lomuto(v, low, pivotPos - 1);
        quick_sort_lomuto(v, pivotPos + 1, high);
    }
}

void quick_sort_hoare(int v[], int low, int high)
{
    int pivotPos;
    if (high > low)
    {
        pivotPos = hoare_partition(v, low, high);
        quick_sort_hoare(v, low, pivotPos);
        quick_sort_hoare(v, pivotPos + 1, high);
    }
}

int main()
{
    int t = 0;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        lomuto_comp_count = 0;
        lomuto_swap_count = 0;
        hoare_comp_count = 0;
        hoare_swap_count = 0;

        int count = 0;
        scanf("%d", &count);
        int *nums_lomuto = (int *)malloc(count * sizeof(int));
        int *nums_hoare = (int *)malloc(count * sizeof(int));
        for (int c = 0; c < count; c++)
        {
            scanf("%d", &nums_lomuto[c]);
            nums_hoare[c] = nums_lomuto[c];
        }
        quick_sort_lomuto(nums_lomuto, 0, count - 1);
        quick_sort_hoare(nums_hoare, 0, count - 1);
        printf("%d %d %d %d\n", hoare_swap_count, lomuto_swap_count, hoare_comp_count, lomuto_comp_count);

        free(nums_lomuto);
        free(nums_hoare);
    }
    return 0;
}