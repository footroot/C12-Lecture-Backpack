import LinkedLists as LL
import time
import matplotlib.pyplot as plt

ll = LL.SinglyLinkedList()
arr = []

ll_times = []
arr_times = []

for i in range(10000):
    ll_start = time.time()
    ll.insert_at_beginning(i)
    ll_time = time.time() - ll_start
    ll_times.append(ll_time)

    arr_start = time.time()
    arr.insert(0, i)
    arr_time = time.time() - arr_start
    arr_times.append(arr_time)

plt.plot(ll_times, label = "Linked List")
plt.plot(arr_times, label = "Array")
    