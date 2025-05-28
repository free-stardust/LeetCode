#include <ios>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct TreeNode {
    int val = 0;
    TreeNode *left = nullptr;
    TreeNode *right = nullptr;
};

class TreeNode2 {
public:
    int val;
    TreeNode2 *left;
    TreeNode2 *right;
    TreeNode2() :
        val(0), left(nullptr), right(nullptr) {
    }
};

void levelOrder(TreeNode *root) {
    queue<TreeNode *> q;

    q.push(root);

    while (!q.empty()) {
        TreeNode *tmpNode = q.front();
        if (tmpNode != nullptr) {
            cout << tmpNode->val << endl;
            if (tmpNode->left != nullptr)
                q.push(tmpNode->left);
            if (tmpNode->right != nullptr)
                q.push(tmpNode->right);
        }
        q.pop();
    }
}

TreeNode *buildTree(vector<int> treeList, int index) {
    if (index > treeList.size())
        return nullptr;

    int num = treeList[index - 1];

    if (num != -1) {
        TreeNode *root = new TreeNode();
        root->val = num;
        root->left = buildTree(treeList, index * 2);
        root->right = buildTree(treeList, index * 2 + 1);
        return root;
    } else {
        return nullptr;
    }
}

TreeNode *buildTree2() {
    TreeNode *root = new TreeNode();
    root->val = 4;

    TreeNode *node1 = new TreeNode();
    node1->val = 9;

    TreeNode *node2 = new TreeNode();
    node2->val = 20;

    root->left = node1;
    root->right = node2;

    return root;
}

int main() {
    vector<int> treeList = {3, 9, 20, -1, -1, 15, 7};
    TreeNode *root = buildTree(treeList, 1);
    levelOrder(root);
    cout << "test" << endl;
    return 0;
}