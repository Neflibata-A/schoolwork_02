void StackInit(ST* ps)
{
	assert(ps);
	ps->a = NULL;
	ps->top = 0;
	ps->capacity = 0;

}

void StackDestroy(ST** pps)
{
	ST* ps = pps;
	assert(ps);
	free(ps->a);
	ps->a = NULL;
	ps->capacity = 0;
	ps->top = 0;
}

void StackPrint(ST* ps)
{
	assert(ps);
	int i = 0;

	while (i < ps->top)
	{
		printf("%d ", ps->a[i]);
		i++;
	}
	printf("\n");

}






void StackPush(ST* ps, STDataType x)
{
	if (ps->top == ps->capacity)
	{
   	    int newCapacity = ps->capacity == 0 ? 4 : ps->capacity* 2;
    	STDataType* tmp = realloc(ps->a, sizeof((STDataType*)newCapacity));

     	if (tmp == NULL)
	    {
		    printf("realloc fail\n");
		    exit(-1);
	    }
	    ps->a = tmp;
	    ps->capacity = newCapacity;
    }
	ps->a[ps->top] = x;
	ps->top++;
	 
}
void StackPop(ST* ps)
{
	assert(ps);
	assert(!StackEmpty(ps));
	ps->top--;

}

STDataType StackTop(ST* ps)
{
	assert(ps);
	assert(!StackEmpty(ps));
	return ps->a[ps->top - 1];

}

int StackSize(ST* ps)
{
	assert(ps);

	return ps->top;
}
bool StackEmpty(ST* ps)
{

	return ps->top == 0;
}
