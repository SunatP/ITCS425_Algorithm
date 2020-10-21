#include <stdlib.h>
#include <stdio.h>

void material_loading(material* mat, int max_weight, int Number_material, int w)
{
    heapsort(mat, Number_material);

    int n = Number_material;
    
    for (int i = 1; i <= n; i++)
    {
        w[i] = 0;
    }

    for (int i = 1; i <= n && mat[i].weight <= max_weight ; i++)
    {
        w[mat[i].id] = 1;
        max_weight -= mat[i].weight;
    }
}
