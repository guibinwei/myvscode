#include <iostream>   //引入头文件 - 头部文件
#include <windows.h>  //引入头文件 - windows.h
using namespace std;   //使用命名空间

int main()
{
    SetConsoleOutputCP(65001);    //调用API函数SetConsoleOutputCP(65001)
    cout << "Hello World" << endl;
    printf("如果有任何BUG可以到用户交流QQ群：904634489进行反馈~\n");
    printf("也可以一起分享编程知识，共同进步！");
}