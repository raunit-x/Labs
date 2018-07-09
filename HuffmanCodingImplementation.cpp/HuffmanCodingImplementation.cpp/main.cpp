#include <iostream>
#include <queue>
#include <vector>
#include <string>

using namespace std;



class minHeapNode
{
public:
    char data;
    int freq;
    minHeapNode * left;
    minHeapNode * right;
    minHeapNode(char data, int freq)
    {
        this -> data = data;
        this -> freq = freq;
        left = right = NULL;
    }
    
};

class myComparator
{
public:
    int operator() (const minHeapNode * p1, const minHeapNode * p2)
    {
        return p1 -> freq > p2 -> freq;
    }
};


minHeapNode * buildHuffmanTree(char characters[], int frequency[], int size)
{
    priority_queue<minHeapNode *, vector<minHeapNode*>, myComparator> minHeap;
    for (int i = 0; i < size; i++)
    {
        minHeap.push(new minHeapNode(characters[i], frequency[i]));
    }
    
    while (minHeap.size() != 1)
    {
        minHeapNode * first = minHeap.top();
        minHeap.pop();
        minHeapNode * second = minHeap.top();
        minHeap.pop();
        minHeapNode * N1 = new minHeapNode('$', first -> freq + second -> freq);
        N1 -> left = first;
        N1 -> right = second;
        minHeap.push(N1);
    }
    
    return minHeap.top();
}

void printCodes(minHeapNode * root, string code)
{
    if(!root)
    {
        return;
    }
    
    if (root -> data != '$')
    {
        cout << root -> data << " : " << code << endl;
    }
    
    printCodes(root -> left, code + '0');
    printCodes(root -> right, code + '1');
}



int main()
{
    char characters[] = { 'a', 'b', 'c', 'd', 'e', 'f' };
    int frequency[] = { 5, 9, 12, 13, 16, 45 };
    
    int size = sizeof(characters) / sizeof(characters[0]);
    
   
    minHeapNode * root = buildHuffmanTree(characters, frequency, size);
    printCodes(root, "");
}
