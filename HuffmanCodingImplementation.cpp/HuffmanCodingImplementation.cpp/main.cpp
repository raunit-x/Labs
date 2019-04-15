#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <map>
#include <fstream>

using namespace std;



class minHeapNode
{
public:
    char data;
    int freq;
    minHeapNode * left;
    minHeapNode * right;
    minHeapNode(char data, int freq) : data(data), freq(freq), left(NULL), right(NULL){} 
};

class myComparator
{
public:
    int operator() (const minHeapNode * p1, const minHeapNode * p2)
    {
        return p1 -> freq > p2 -> freq;
    }
};


minHeapNode * buildHuffmanTree(map<char, int> & file)
{
    priority_queue<minHeapNode *, vector<minHeapNode*>, myComparator> minHeap;
    map<char, int> :: iterator it;
    for (auto it : file)
    {
        minHeap.push(new minHeapNode(it.first, it.second));
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

void getCodes(minHeapNode * root, string code, map<char, string> & codes)
{
    if(!root)
    {
        return;
    }
    if (root -> data != '$')
    {
        codes.insert({root -> data, code});
    }
    getCodes(root -> left, code + '0', codes);
    getCodes(root -> right, code + '1', codes);
}

string decode_file(minHeapNode * root, string code)
{
    string ans = "";
    minHeapNode * curr = root;
    for (int i = 0; i < code.size(); i++)
    {
        if (code[i] == '0')
            curr = curr -> left;
        else 
            curr = curr -> right;
        if (!curr -> left && !curr -> right)
        {
            ans += curr -> data;
            curr = root;
        }
    }
    return ans + '\0';
}


int main()
{
    string text = "aaabbbbbccccdddddeeeeeeeee"; // or input from any file!
    map<char, int> file;
    for (int i = 0; i < text.size(); i++)
    {
        if (file.count(text[i]) == 0)
        {
            file[text[i]] = 1;
        }
        else file[text[i]]++;
    }
    for(auto & it : file)
    {
        cout << it.first << ": " << it.second << endl;
    }
    minHeapNode * root = buildHuffmanTree(file);
    map<char, string> codes;
    getCodes(root, "", codes);
    
    for(auto it : codes)
    {
        cout << it.first << ": " << it.second << endl;
    }
    string encoded = "";
    for (int i = 0; i < text.size(); i++)
    {
        encoded += codes.at(text[i]);
    }
    float size = float(encoded.size());
    cout << "Average Length: " << 1.0 * size / text.size() << endl;
    cout << "Encoded file : " << encoded << endl;
    cout << "File Decoded : " << decode_file(root, encoded) << endl; // or writer << decoded_file << endl; 
  
}

