通过countVector保存每一个链表的当前元素，维持最小队列，若指针为NULL，则为最大；

countVector的初始化通过STL中的sort(queue)完成。

每次取countVector的第一个元素加入答案链表，并将第一个元素所在链表的下一个元素加入到countVector中，由于countVector有序，可以直接依次比较（若采用二分查找则可以缩小时间复杂度为O(nlogn)。

在countVector第一个元素变为空指针时停止操作。

空间复杂度为O(n)，时间复杂度为O(n^2)。
